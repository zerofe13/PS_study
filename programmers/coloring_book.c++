#include <vector>
#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int> > picture) {

    int dx[] = {0,1,0,-1};
    int dy[] = {1,0,-1,0};
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    int check[m][n];
    queue<pair<int,int> > q;
    
    memset(check,0,sizeof(check));
    

    for(int i = 0; i<m; i++){
        for (int j =0; j<n; j++){
            if (picture[i][j] != 0 && check[i][j] ==0){
                int number_of_one_area = 0;

                check[i][j] = 1;
                number_of_area++;

                q.push(make_pair(i,j));
                while (q.empty() == false){

                    int y = q.front().first;
                    int x = q.front().second;
                    int nx = 0;
                    int ny = 0;

                    q.pop();
                    for(int d = 0; d<4; d++ ){
                        nx = x + dx[d];
                        ny = y + dy[d];
                        if (nx >= 0 && nx <n && ny >= 0 && ny < m && check[ny][nx] == 0 && picture[ny][nx] ==picture[y][x]){
                            q.push(make_pair(ny,nx));
                            check[ny][nx] =1;
                            number_of_one_area++;
                        }
                    }
                }
                max_size_of_one_area = max(number_of_one_area,max_size_of_one_area);
            }
        }
    }
   
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area+1;
    return answer;
}

int main(void){
    int m = 6;
    int n = 4;
    int temp[6][4] = {{1,1,1,0},{1,2,2,0},{1,0,0,1},{0,0,0,1},{0,0,0,3},{0,0,0,3}};
    vector <vector<int> > picture;
    for(int i = 0; i<m; i++){
        picture.push_back(vector<int>());
        for (int j = 0; j<m; j++){
            picture.at(i).push_back(temp[i][j]);
        }
    } 
    vector<int> a;
    a = solution(m,n,picture);
    cout<<a[0]<<" "<<a[1]<<endl;
}
