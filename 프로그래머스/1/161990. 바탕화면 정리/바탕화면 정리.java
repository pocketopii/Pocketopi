class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = new int[4];
        int length = wallpaper.length;
        int in_length = wallpaper[0].length();
        
        int max_row = 0;
        int max_col = 0;
        int min_row = length;
        int min_col = in_length;
        
        for (int i = 0; i < length ; i++) {
        	for (int j = 0 ; j < in_length ; j++) {
        		if(wallpaper[i].charAt(j) == '#') {
        			if(max_row < i) {
        				max_row = i;
        			}
        			if(max_col < j) {
        				max_col = j;
        			}
        			if(min_row > i) {
        				min_row = i;
        			}
        			if(min_col > j) {
        				min_col = j;
        			}
        		}
        	}
        }
        answer[0] = min_row;
        answer[1] = min_col;
        answer[2] = max_row+1;
        answer[3] = max_col+1;
        return answer;
    }
}