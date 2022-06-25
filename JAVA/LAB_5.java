
public class LAB_5 {
	public static void main(String[] args) {
		/* 4번
		printOdds(3);
		printOdds(17 / 2);
		int x = 25;
		printOdds(37 - x + 1);
		*/
		
		/* 5번
		int number = 8;
		halfTheFun(11);
		halfTheFun(2 - 3 + 2 * 8);
		halfTheFun(number);
		System.out.println("number = " + number);
		*/
		
		/* 6번
		String one = "two";
		String two = "three";
		String three = "1";
		int number = 20;
		
		sentence(one, two, 3);
		sentence(two, three, 14);
		sentence(three, three, number + 1);
		sentence(three, two, 1);
		sentence("eight", three, number / 2);
		*/
		
		/* 7번
		String whom = "her";
		String who = "him";
		String it = "who";
		String he = "it";
		String she = "whom";
		
		sentence(he, she, it);
		sentence(she, he, who);
		sentence(who, she, who);
		sentence(it, "stu", "boo");
		sentence(it, whom, who);
		*/
		
		/* 13번
		System.out.println(Math.max(18 - 5, Math.ceil(4.6 * 3)));
		*/
	}
	/* 4번
	public static void printOdds(int n) {
		for (int i = 1; i <= n; i++) {
			int odd = 2 * i - 1;
			System.out.print(odd + " ");
		}
		System.out.println();
	}
	*/

	/* 5번
	public static void halfTheFun(int number) {
		number = number / 2;
		for (int count = 1; count <= number; count++) {
			System.out.print(count + " ");
		}
		System.out.println();
	}
	*/
	
	/* 6번
	public static void sentence(String three, String one, int number) {
		System.out.println(one + " times " + three + " = " + (number  * 2));
	}
	*/ 
	
	/* 7번
	public static void sentence(String she, String who, String whom) {
		System.out.println(who + " and " + whom + " like " + she);
	}
	*/
}
