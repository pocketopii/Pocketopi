class Solution {
    public String solution(String s) {
        int length = s.length();
        if (length % 2 == 1) {
            // 홀수일 때, 중간 문자 반환
            return Character.toString(s.charAt(length / 2));
        } else {
            // 짝수일 때, 중간 두 문자 반환
            return s.substring(length / 2 - 1, length / 2 + 1);
        }
    }
}
