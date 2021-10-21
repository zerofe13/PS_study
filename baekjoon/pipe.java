package baekjoon;
import java.util.*;
//17070
public class pipe {
    static int N;
    static int[][] map;
    static int[][] visit;     
    static int dx[] = {1,1,0}; //가로 세로 대각선 이동 
    static int dy[] = {0,1,1};    
    static int result = 0;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        map = new int[N][N];
        visit = new int[N][N];
        for (int i = 0 ; i<N;i++){
            for(int j = 0 ; j < N ; j++){
                map[i][j] = sc.nextInt();
            }
        }
        dfs(1,0,0,0);
        System.out.println(result);
    }
    public static void dfs(int x ,int y,int pip_state, int depth){
        if(x==N-1 && y==N-1){
            result +=1;
            return;
        }
        if (pip_state == 0){
            for (int i = 0 ; i<2; i++){
                int nx = x +dx[i];
                int ny = y +dy[i];
                if (i==0){
                    if (nx>=0 && nx <N && ny>=0 && ny <N && map[ny][nx] == 0 ){
                        dfs(nx,ny,0,depth+1);
                    }
                }
                if (i==1){
                    if (nx>=0 && nx <N && ny>=0 && ny <N && map[ny][nx] == 0 &&map[ny-1][nx] == 0 &&map[ny][nx-1] == 0){
                        dfs(nx,ny,1,depth+1);
                    }
                }
            }
        }if (pip_state == 1){
            for (int i = 0 ; i<3; i++){
                int nx = x +dx[i];
                int ny = y +dy[i];
                if (i==0){
                    if (nx>=0 && nx <N && ny>=0 && ny <N && map[ny][nx] == 0 ){
                        dfs(nx,ny,0,depth+1);
                    }
                }
                if (i==1){
                    if (nx>=0 && nx <N && ny>=0 && ny <N && map[ny][nx] == 0 &&map[ny-1][nx] == 0 &&map[ny][nx-1] == 0){
                        dfs(nx,ny,1,depth+1);
                    }
                }
                if (i==2){
                    if (nx>=0 && nx <N && ny>=0 && ny <N && map[ny][nx] == 0 ){
                        dfs(nx,ny,2,depth+1);
                    }
                }
            }
        }
        if (pip_state == 2){
            for (int i = 1 ; i<3; i++){
                int nx = x +dx[i];
                int ny = y +dy[i];
                if (i==1){
                    if (nx>=0 && nx <N && ny>=0 && ny <N && map[ny][nx] == 0 &&map[ny-1][nx] == 0 &&map[ny][nx-1] == 0){
                        dfs(nx,ny,1,depth+1);
                    }
                }
                if (i==2){
                    if (nx>=0 && nx <N && ny>=0 && ny <N && map[ny][nx] == 0 ){
                        dfs(nx,ny,2,depth+1);
                    }
                }
            }
        } 
    }
}
