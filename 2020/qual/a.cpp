#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <stdlib.h>
#include <algorithm>

using namespace std;

int B, L, D;
vector<int> bookSc;
vector<int> N, T, M;
vector<vector<int>> libBList;
unordered_set<int> bVis;

typedef long long ll;

ll scoreL(int startD, int lib, vector<int> &bList) {
    ll sc = 0, remainD = D - (startD + T[lib]);
    if (remainD > 0) {
        ll maxShipN = remainD * M[lib];
        for (int i = 0; i < min(maxShipN, (ll)bList.size()); i++) {
            int bid = bList[i];
            if (!bVis.count(bid)) {
                sc += bookSc[bid];
                bVis.insert(bid);
            }
        }
    }
    return sc;
}

ll score(vector<pair<int, vector<int>>> &ofList) {
    bVis.clear();

    ll sc = 0, currD = 0;
    for (auto &libAndBList: ofList) {
        int lib = libAndBList.first;
        vector<int> &bList = libAndBList.second;
        sc += scoreL(currD, lib, bList);
        currD += T[lib];
    }
    return sc;
}

int main() {

    vector<string> fileList = {
        "dataSet/a_example.txt",
        "dataSet/b_read_on.txt",
        "dataSet/c_incunabula.txt",
        "dataSet/d_tough_choices.txt",
        "dataSet/e_so_many_books.txt",
        "dataSet/f_libraries_of_the_world.txt",
    };


    ll totalSc = 0;
    for (string &fileIn: fileList) {
        ifstream fin(fileIn);

        fin >> B >> L >> D;

        bookSc = vector<int>(B);
        for (int i = 0; i < B; i++) {
            fin >> bookSc[i];
        }

        N = T = M = vector<int>(L);
        libBList = vector<vector<int>>(L);
        int bid;
        for (int lib = 0; lib < L; lib++) {
            fin >> N[lib] >> T[lib] >> M[lib];
            for (int i = 0; i < N[lib]; i++) {
                fin >> bid;
                libBList[lib].push_back(bid);;
            }
        }

        fin.close();

        vector<pair<int, vector<int>>> ofList;

#if 1
        vector<pair<int, int>> libSort;
        for (int lib = 0; lib < L; lib++) {
            libSort.push_back(make_pair(T[lib], lib));
        }
        sort(libSort.begin(), libSort.end());
        vector<int> libSortOrder;
        for (auto libPair: libSort) {
            libSortOrder.push_back(libPair.second);
        }
#endif
#if 0
        for (auto lib: libSortOrder) {
            int lib = libPair.second;
            ofList.push_back(make_pair(lib, libBList[lib]));
        }
#endif
#if 1
        vector<int> bCount(B, 0);
        for (int lib = 0; lib < L; lib ++) {
            for (int bid: libBList[lib]) {
                bCount[bid]++;
            }
        }

        vector<vector<double>> preSum(L, vector<double>(D, 0));
        vector<double> allSc(D, 0);
        for (int lib = 0; lib < L; lib++) {
            vector<pair<double, int>> scBList;
            for (int i = 0; i < N[lib]; i++) {
                int bid = libBList[lib][i];
                // scBList.push_back(make_pair((double)bookSc[bid] / bCount[bid], bid));
                scBList.push_back(make_pair((double)bookSc[bid], bid));
            }
            sort(scBList.rbegin(), scBList.rend());

            for (int i = 0; i < N[lib]; i++) {
                libBList[lib][i] = scBList[i].second;
            }
            
#if 0
            continue;
#endif

            for (int i = T[lib]; i < D; i++) {
                double scOfDay = 0;
                int shipDay = i - T[lib];
                for (int j = shipDay * M[lib]; j < (shipDay + 1) * M[lib]; j++) {
                    if (j >=scBList.size()) {
                        break;
                    }
                    scOfDay += scBList[j].first;
                }
                preSum[lib][i] = preSum[lib][i - 1] + scOfDay;
                allSc[i] += preSum[lib][i];
            }

            // out << lib << ": ";
            // for (int i = 0; i < D; i++) {
            //     cout << preSum[lib][i] << " ";
            // }
            // cout << endl;
        }
        // cout << "total: ";
        // for (int i = 0; i < D; i++) {
        //     cout << allSc[i] << " ";
        // }
        // cout << endl;

        int rD = D;
        unordered_set<int> libVis, bShip;
        int curLib = 0;
        while (rD > 0) {
            int maxLib = -1;
#if 0
            if (curLib < L) {
                maxLib = libSortOrder[curLib++];
            }
#endif
#if 1
            double maxCredit = 0;

            for (int lib = 0; lib < L; lib++) {
                if (libVis.count(lib)) {
                    continue;
                }
                double credit = 0;
                int r = rD - 1, l = rD - T[lib] - 1;
                if (l < 0) {
                    continue;
                }
                // credit = preSum[lib][r] -
                //          allSc[r] + allSc[l] +
                //          preSum[lib][r] - preSum[lib][l];
                // credit /= T[lib];
                credit = preSum[lib][r] / T[lib];
                if (maxLib < 0 || credit > maxCredit) {
                    maxCredit = credit;
                    maxLib = lib;
                }
            }
#endif
            if (maxLib < 0) {
                break;
            }
            libVis.insert(maxLib);
            rD -= T[maxLib];

            vector<int> shipList;
            int bookCnt = 0, maxBookCnt = rD * M[maxLib];
            for (int bid: libBList[maxLib]) {
                if (!bShip.count(bid)) {
                    shipList.push_back(bid);
                    bShip.insert(bid);
                    bookCnt++;
                }
                if (bookCnt == maxBookCnt) {
                    break;
                }
            }
            ofList.push_back(make_pair(maxLib, shipList));
        }
#endif

        // construct ofList
        // vector<pair<int, vector<int>>> ofList;
        // for (int lib = 0; lib < L; lib++) {
        //     ofList.push_back(make_pair(lib, libBList[lib]));
        // }

        ll t = score(ofList);
        totalSc += t;
        cout << "(" << t << ", " << totalSc << ")" << endl;
    }

    cout << totalSc << endl;
    return 0;
}
