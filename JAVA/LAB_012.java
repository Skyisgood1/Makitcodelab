import java.util.*;

public class LAB_012 {

	public static void main(String[] args) {
		int[] original1 = {1,2,3,4};
		int[] original2 = {2,3,4,5};
		
		System.out.println(allLess(original1,original2));
		
		/*
		Random random = new Random();
		int length = random.nextInt(1,20);
		int[] arr = new int[length];
		
		for (int i = 0; i < length; i++) {
			arr[i] = random.nextInt(0,100);
			System.out.print(arr[i] + " ");
		}
		System.out.println();
		System.out.println(max(arr));
	
	}
	
	public static int max(int[] arr) {
		int max1 = arr[0];
		
		for (int i = 0; i < arr.length; i++) {
			if (max1 < arr[i]) {
				max1 = arr[i];
			}
		}
		
		return max1;
			*/
	}
	/*
	public static double average(int[] copy) {
		double sum = 0;	
		for (int i = 0; i <copy.length;i++) {
			sum += copy[i];
		}
		return sum/copy.length;
		
	}
	
	
	public static void printBackwards(int[] array) {
		for (int i = array.length-1; i >= 0; i--) {
			System.out.println(array[i]);
		}
	}
	*/
	public static boolean allLess(int[] arr1, int[] arr2) {
		if (arr1.length != arr2.length) {
			return false;
		} 
		
		for (int i = 0; i < arr1.length; i++) {
			if (arr1[i] > arr2[i]) {
				return false;
			}
		}
		return true;
	}
}
