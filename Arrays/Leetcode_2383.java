/*
    Minimum hours of training to win a competition

    You are entering a competition, and are given two positive integers 
    initialEnergy and initialExperience denoting your initial energy and initial 
    experience respectively.

    You are also given two 0-indexed integer arrays energy and experience, both 
    of length n.

    You will face n opponents in order. The energy and experience of the ith 
    opponent is denoted by energy[i] and experience[i] respectively. When you 
    face an opponent, you need to have both strictly greater experience and 
    energy to defeat them and move to the next opponent if available.

    Defeating the ith opponent increases your experience by experience[i], but 
    decreases your energy by energy[i].

    Before starting the competition, you can train for some number of hours. After
    each hour of training, you can either choose to increase your initial 
    experience by one, or increase your initial energy by one.

    Return the minimum number of training hours required to defeat all n 
    opponents.

    Example 1:

        Input: 
            initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], 
            experience = [2,6,3,1]

        Output: 8

        Explanation: 
        You can increase your energy to 11 after 6 hours of training, and your 
        experience to 5 after 2 hours of training.
        You face the opponents in the following order:
        - You have more energy and experience than the 0th opponent so you win.
        Your energy becomes 11 - 1 = 10, and your experience becomes 5 + 2 = 7.
        - You have more energy and experience than the 1st opponent so you win.
        Your energy becomes 10 - 4 = 6, and your experience becomes 7 + 6 = 13.
        - You have more energy and experience than the 2nd opponent so you win.
        Your energy becomes 6 - 3 = 3, and your experience becomes 13 + 3 = 16.
        - You have more energy and experience than the 3rd opponent so you win.
        Your energy becomes 3 - 2 = 1, and your experience becomes 16 + 1 = 17.
        You did a total of 6 + 2 = 8 hours of training before the competition, so we return 8.
        It can be proven that no smaller answer exists.
 */

public class Leetcode_2383 {
    public static void main(String[] args) {
        int initialEnergy = 5;
        int initialExperience = 3;
        int energy[] = { 1, 4, 3, 2 };
        int experience[] = { 2, 6, 3, 1 };

        int training = 0;

        for (int i = 0; i < energy.length; i++) {

            System.out.println(i + " ");

            if (initialEnergy <= energy[i]) {
                int temp = (energy[i] - initialEnergy) + 1;
                training += temp;
                initialEnergy += temp;
                System.out.println("training" + training);
            }
            if (initialExperience <= experience[i]) {
                int temp = (experience[i] - initialExperience) + 1;
                training += temp;
                initialExperience += temp;
                System.out.println("training" + training);
            }
            initialEnergy -= energy[i];
            initialExperience += experience[i];

            System.out.println("energy[i]" + energy[i]);
            System.out.println("experience[i]" + experience[i]);
            System.out.println("initial energy" + initialEnergy);
            System.out.println("initial Experience" + initialExperience);
            System.out.println("training" + training);
            System.out.println();
            System.out.println();
        }
    }

}
