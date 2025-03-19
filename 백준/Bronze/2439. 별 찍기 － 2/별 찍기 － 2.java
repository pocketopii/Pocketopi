import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		//입력받기
		int num = scanner.nextInt();
		//층
		for(int i = 1; i <= num; i++) {
			for(int j = num; j > i; j--) { //' '출력
				System.out.print(' ');
			}
			for(int m = 1; m <= i; m++) { // '*' 출력
				System.out.print('*');
			}
			System.out.println();
		}
	}
}
