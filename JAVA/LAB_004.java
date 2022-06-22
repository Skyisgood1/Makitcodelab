
public class LAB_004 {
	//Global Variable
	
	public static int n = 100;
	
	// Constant
	public static final int NUMBER_OF_SPACES = 10;
	public static void main(String[] args) {
		/*
		//n = Local Variable
		int n = 10;
		for (int i = 1; i <= n; i++) {
			System.out.print(i + "번째: ");
			System.out.print("Start");
			whiteSpaces(i, '*');
			System.out.print("end");
			System.out.println();
		}
		*/
		
		drawBox(10,5);
		drawBox(); 
		double result = add(3,4);
		System.out.println(result);
		
		System.out.println(Math.max(10, 5));
		System.out.println(Math.sqrt(27));
		
		// Type casting 
		int answer = (int) Math.sqrt(6);
		System.out.println(answer);
		
	}
	public static void writeChars(int n,char c) {
		//n = parameter
		for (int i = 1; i <= n; i++) {
			System.out.print(c);
		}
	}
	
	public static void drawBox(int w, int h) {
		writeChars(w, '*');
		System.out.println();
		for (int i = 1; i <= h-2; i++) {
			System.out.print('*');
			writeChars(w-2,' ');
			System.out.print('*');
			System.out.println();
		}
		writeChars(w,'*');
	}
	//Method Overloading 
	public static void drawBox() {
		System.out.println("새로운 매소드");
	}
	
	public static double add(int a, int b) {
		return a + b;
		
		// Unreachable Code
		// System.out.println("이 문장은 출력될까요?");
	}
	
}
