import java.io.*;
import java.util.*;

public class LAB_10 {
	public static void main(String[] args) throws FileNotFoundException {
		// 17번
		Scanner input = new Scanner(System.in);
		String fileName = input.next();
		
		Scanner output = new Scanner(new File(fileName));
		printEntireFile(output);
		
		/* 15번
		Scanner input = new Scanner(new File("brownfox.txt"));
		
		while (input.hasNext()) {
			String line = input.next();
			System.out.println(line);
		}
		*/
		
		/* 12번, 13번, 14번
		Scanner input = new Scanner(new File("readme.txt"));
		int count = 0;
		
		while (input.hasNextInt()) {
			System.out.println("input: " + input.nextInt());
			count++;
		}
		
		System.out.println(count + " total");
		*/
		
		/* 11번 
		Scanner sc = new Scanner(new File("data.txt"));
		countWords(sc);
		*/
	}
	
	public static void printEntireFile(Scanner output) {
		while (output.hasNextLine()) {
			String line = output.nextLine();
			System.out.println(line);
		}
	}
	
	public static void countWords(Scanner input) {
		int lineCount = 0;
		int wordCount = 0;
		
		while (input.hasNextLine()) {
			String line = input.nextLine();
			lineCount++;
			
			StringTokenizer tokenizer = new StringTokenizer(line);
			
			while (tokenizer.hasMoreTokens()) {
				String token = tokenizer.nextToken();
				wordCount++;
			}
		}
		
		System.out.println(lineCount + " " + wordCount);
	}
}
