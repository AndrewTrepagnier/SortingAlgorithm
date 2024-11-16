// Sorting Algorithm takes a random array of numbers and orders them from smallest to largest, works on any array of integers of any size
//By. Andrew Trepagnier

public class sorting_algorithm {
    // All functions and variables defined within the public class 'sorting_algorithm'

    public static void main(String[] args) {


        double[] R = {191, 7, 109, 91, 5, -7, 18};
        // manually make a copy using loop
        double[] S = new double[R.length];


        // for(where does i start; where does i end(usually based off of some array index); i++ to increment 1){
        for (int i = 0; i < R.length; i++) {
            S[i] = R[i];
            //System.out.println(S[i]);
        }
        //S and R are now the same, this will be our initial settings

        int n = R.length;

        // now begin sorting

        for (int j = n; j > 1; j--) {
            for (int i = 0; i < j - 1; i++) {
                //This way will let you see what the for loops are doing to the increment
                //within the given set of elements in R(ex. [1], [2], [3]) make an if statement that says if the first one in the
                //set, [1], is greater than the next one in the set, [1]+1, then swap their order

                if (S[i] > S[i + 1]) {
                    double tmp = S[i];
                    S[i] = S[i + 1];
                    S[i + 1] = tmp;
                }
            }

            }
        //after for sorting is done, just print each element in S in the order from smallest to largest
        for (int i = 0; i < S.length; i++) {
            System.out.println(S[i]);
        }


    }
}