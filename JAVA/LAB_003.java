
public class LAB_001 {

	public static void main(String[] args) {
		/*
		int x = 3;
		int y = 5;
		
		y = x-- + 5 + --x;
		System.out.println(y);
		*/
		
		int x = 3;
		int y = 0;
		y = x++;
		System.out.println(x);	//x=4
		System.out.println(y);	//y=3
		
		y = x - y;	//y=1
		System.out.println(-x);	//-4 Ãâ‹
		System.out.println(y = -y);	// -1 Ãâ
		
		x++;	// currently, x = 4 -> 5
		++y;	// currently, y = -1 -> 0
		System.out.println(x++);
		System.out.println(++y);
		System.out.println(x + " " + y);
	}

}
