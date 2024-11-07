import java.util.*;

/* 
    You are given an array arr of positive integers. Your task is to find all the 
    leaders in the array. An element is considered a leader if it is greater than
    or equal to all elements to its right. The rightmost element is always a 
    leader.

    Examples:
        Input:
            arr=[16,17,4,3,5,2]
        Output:
            [17,5,2]
        Explanation:
            Note that there is nothing greater on the right side of 17, 5 and 2
    
    Constraints:
        1 <= arr.size() <= 10^6
        0 <= arr[i] <= 10^6
 */

public class Leader {
    public static ArrayList<Integer> Lead(int arr[]) {
        ArrayList<Integer> answer = new ArrayList<>();
        int rightMost = arr[arr.length - 1];
        answer.add(rightMost);

        for (int i = arr.length - 2; i >= 0; i--) {
            if (rightMost <= arr[i]) {
                answer.add(arr[i]);
                rightMost = arr[i];
            }
        }

        Collections.reverse(answer);
        return answer;
    }

    public static void main(String[] args) {
        int arr[] = { 16, 17, 4, 3, 5, 2 };
        int arr0[] = { 10, 4, 2, 4, 1 };

        ArrayList<Integer> al = new ArrayList<>();
        al = Lead(arr);
        System.out.println(al);

        ArrayList<Integer> al1 = new ArrayList<>();
        al1 = Lead(arr0);
        System.out.println(al1);
    }
}
