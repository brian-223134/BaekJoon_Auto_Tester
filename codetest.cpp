#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void dfs(vector<int> tree[], int node, bool leaf[])
{
    for (int i = 0; i < tree[node].size(); i++)
    {
        int num = tree[node][i];
        dfs(tree, num, leaf);
    }
    tree[node].clear();
    leaf[node] = true;
}

int main(int argc, char* argv[])
{
    istream* in = &cin;
    ostream* out = &cout;
    ifstream fin;
    ofstream fout;
    if (argc >= 3) {
        fin.open(argv[1]);
        fout.open(argv[2]);
        in = &fin;
        out = &fout;
    }
    ios_base::sync_with_stdio(false);
    (*in).tie(NULL);
    (*out).tie(NULL);

    int N;
    (*in) >> N;

    vector<int> tree[50];
    bool leaf[50] = {false};

    for (int i = 0; i < N; i++)
    {
        int p;
        (*in) >> p;
        if (p == -1)
            continue;
        else
        {
            tree[p].push_back(i);
        }
    }

    int node;
    (*in) >> node;

    dfs(tree, node, leaf);

    bool br = false;
    for (int i = 0; i < N; i++)
    {
        for (auto it = tree[i].begin(); it != tree[i].end(); it++)
        {
            if (*it == node)
            {
                tree[i].erase(it);
                br = true;
                break;
            }
        }
        if (br)
            break;
    }

    int answer = 0;

    for (int i = 0; i < N; i++)
    {
        if (!leaf[i] && tree[i].size() == 0)
            answer++;
    }

    (*out) << answer;

    return 0;
}