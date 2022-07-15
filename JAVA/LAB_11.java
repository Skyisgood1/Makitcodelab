import java.util.Random;

public class LAB_11 {

	public static void main(String[] args) {
		int min = -66;
		int max = 3838;
		
		int data[] = new int[(max - min) / 2];
		
		int index = 0;
		
		for (int i = min; i <= max; i++) {
			if (i % 2 != 0) {
				data[index] = i;
				index++;
			}
		}
		
		// arr[내가 배열에 값을 넣고 싶은 위치] = 내가 배열에 넣고 싶은 값;
		// arr[0] = 0;
		// arr[1] = 10;
	
		// 배열에 최종 저장된 값 출력하 
		for (int i = 0; i < data.length; i++) {
			System.out.print(data[i] + " ");
		}
		
		/* 3번 
		int data[] = {27, 51, 33, -1, 101};
		*/
		
		/* 2번 
		Random random = new Random();
		int length = random.nextInt(10, 100);
		
		// 배열을 생성하는 방법
		int[] arr = new int[length];
		
		// 배열을 초기화 하는 방법이자 배열에 값을 저장하는 방법 
		for (int i = 0; i < length; i++) {
			arr[i] = random.nextInt(1, 100);
			System.out.print(arr[i] + " ");
		}
		System.out.println();
		
		System.out.println("arr 배열의 길이는 : " + arr.length);
		
		// 배열의 첫번째 요소에 접근하는 방법
		System.out.println(arr[0]);
		// 배열의 10번째 요소에 접근하는 방법
		System.out.println(arr[9]);
		// 배열의 마지막 요소에 접근하는 방법
		System.out.println(arr[arr.length - 1]);
		*/
	}

}
