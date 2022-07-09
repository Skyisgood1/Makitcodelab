import java.util.*;
public class iuguyituthg {
	
	public static void main(String[] args) {
		/*
		Scanner sc = new Scanner(System.in);
		System.out.print("Type a number: ");
		
		if (sc.hasNextInt()) {
			int number = sc.nextInt();
			System.out.println("You types the integer" + number);
		} else if (sc.hasNextDouble()) {
			double number = sc.nextDouble();
			System.out.println("You type the real number " + number);
		}
		
		
			//#22
		Scanner console = new Scanner(System.in);
		System.out.print("Type ur age: ");
		int age = console.nextInt();
		
		while (age <= 0) {
			System.out.print("Type your age: ");
			age = console.nextInt();
		}
		
		System.out.print("Type your GPA: ");
		double gpa = console.nextDouble();
		
		while (gpa < 0.0 || gpa > 4.0) {
			System.out.print("Type your GPA: ");
			gpa = console.nextDouble();
		}
		
		
		Scanner sc = new Scanner(System.in);
		System.out.print("Typr a number (or - 1 to stop): ");
		int num = sc.nextInt();
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		int cnt = 0;
		boolean flag = false;
		
		while (num != - 1) {
			flag = true;
			if (max < num) {
				max = num;
			}
			if (min > num) {
				min = num;
			}
			System.out.print("Type a numer (or -1 to stop) :");
			num = sc.nextInt();
		}
		
		if (flag) {
			System.out.println("Max was " + max);
			System.out.println("Min was " + min);
			
		}
		
		String s  = "Rabbit";
		printLetters(s);
		
		
		Scanner sc = new Scanner(System.in);
		int x = sc.nextInt();
			#07
		Random random = new Random();
		int a = random.nextInt(50) + 50;
		while (a % 2 == 0) {
			a = random.nextInt(50) + 50;
		}
		System.out.println(a);
		
		
		// do - while문
		do {
			System.out.println(x);
			x = sc.nextInt();
		} while (x != 0);
		
		// while문
		while (x != 0) {
			System.out.println(x);
			x = sc.nextInt();
		}
		
		System.out.println("0을 입력해여 끝납니다.");
		*/
		
		
		int i = 1;
		while (i <= 2) {
			int j = 1;
			while (j <= 3) {
				int k = 1;
				while (k <= 4) {
					System.out.print("*");
					k++;
				}
				System.out.print("!");
				j++;
			}
			i++;
		}
		
		
		int number = 4;
		int count = 1;
		while (count <= number) {
			System.out.println(number);
			number = number / 2;
			count++;
			
		
		}	
		
	}
	
	public static void printLetters(String text) {
		for (int i = 0; i < text.length(); i++) {
			// print (text[i] + "-", end = ' ')
			if (i < text.length()-1) {
				System.out.print(text.charAt(i) + "-");
			} else {
				System.out.print(text.charAt(i));
			}
		}
		System.out.println();
		*/
	}

}
