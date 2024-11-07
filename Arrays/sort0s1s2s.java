import java.util.*;

/*
    Given an array arr containing 0s, 1s and 2s. Sort the array in ascending order

    Examples:
        Input:
            arr[] = [0,1,2,0,1,2]
        Output:
            arr[] = [0,0,1,1,2,2]

    Constraints:
        1 <= arr.size() <=10^6
        0 <= arr[i] <= 2
 */

public class sort0s1s2s {
    public static void sort012(int arr[]) {
        int noOf0 = 0, noOf1 = 0, noOf2 = 0;
        int newarr[] = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0) {
                noOf0++;
            } else if (arr[i] == 1) {
                noOf1++;
            } else {
                noOf2++;
            }
        }

        // int index = 0;
        for (int i = 0; i < noOf0; i++) {
            System.out.print(0 + " ");
        }
        for (int i = 0; i < noOf1; i++) {
            System.out.print(1 + " ");
        }
        for (int i = 0; i < noOf2; i++) {
            System.out.print(2 + " ");
        }
    }

    public static void main(String[] args) {
        int arr[] = { 0, 1, 2, 0, 1, 2 };

        sort012(arr);
    }
}