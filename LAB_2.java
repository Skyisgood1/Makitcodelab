
public class LAB_2 {
	/*
	public static void first() {
		System.out.println("1");
	}
	
	public static void second() {
		System.out.println("2");
		first();
	}
	
	public static void third() {
		System.out.println("3");
		first();
		second();
	}
	*/
	
	public static void main(String[] args) {		
		/* 2진수를 10진수로 바꾸기
		int result = Integer.parseInt("1001110", 2);
		System.out.println(result);
		*/
		
		/*
		System.out.println("\"Several slashes are sometimes seem.\"");
		System.out.println("Said Sally. \"I\'ve said so.\" See?");
		System.out.println("\\ / \\\\ // \\\\\\ ///");
		*/
		
		/*
		message1();
		message2();
		System.out.println("Done with main.");
		*/
		
		/*
		second();
		first();
		second();
		third();
		*/
		
		int sum = 0;
		
		for (int j = 1; j <= 5; j++) {
			for (int i = 1; i <= 10; i++)	{
				System.out.print("*");
			}
		System.out.println();
			
		}
		
		/*
		for (int i = 1; i <= 100; i++) {
			if (i % 2 == 0)	{
				System.out.println(i);
			}
		}
		*/
	}
	
	/*
	public static void message1() {
		System.out.println("This is message1.");
	}

	public static void message2() {
		System.out.println("This is message2.");
		message1();
		System.out.println("Done with message2.");
	}
	*/
}
