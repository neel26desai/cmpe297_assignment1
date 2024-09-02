import java.util.Arrays;

public class OptimizedBubbleSort {
    public static void optimizedBubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            boolean swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j+1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            // If no swapping occurred, array is already sorted
            if (!swapped) {
                break;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        System.out.println("Original array: " + Arrays.toString(arr));
        
        int[] sortedArr = arr.clone();
        optimizedBubbleSort(sortedArr);
        System.out.println("Sorted array: " + Arrays.toString(sortedArr));

        // Test with an already sorted array to demonstrate early termination
        int[] alreadySortedArr = {1, 2, 3, 4, 5, 6, 7};
        System.out.println("\nAlready sorted array: " + Arrays.toString(alreadySortedArr));
        
        int[] result = alreadySortedArr.clone();
        optimizedBubbleSort(result);
        System.out.println("Result after optimized bubble sort: " + Arrays.toString(result));
    }
}