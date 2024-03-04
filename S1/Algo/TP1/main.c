#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void printArray(int [], int );
void insertionSort(int [], int );
void bubbleSort(int [], int );
void swap(int*, int*);
void mergeSort( int [], int, int);
void merge( int [] ,int, int, int);
int partition(int [], int, int );
void quickSort(int [], int , int );
void heapify(int [], int , int );
void heapSort(int [], int );
void testSortedTable(int);
void testUnsortedTable(int);
void testReversedSortTable(int);
int *initSortedTable(int);
int *initUnsortedTable(int);
int *initReversedSortedTable(int);

int main() {
    int arr[] = { 12, 11, 13, 5, 6 };
    int n = sizeof(arr) / sizeof(arr[0]);
 
    // --------------- Pour tester sur les tableaux tries 
    // parametre N: la taille du tableau
    // testSortedTable(5);


    // --------------- Pour tester sur les tableaux tries en ordre invers 
    // parametre N: la taille du tableau
    // testReversedSortTable(5);

    // --------------- Pour tester sur les tableaux tries en ordre invers 
    // parametre N: la taille du tableau
    testUnsortedTable(50);
    
    // ------------------ les appels des fontions de trie
    // ------------------ arr : le tableaux;  n= la taille du tableau;  
    //insertionSort(arr, n);
    // bubbleSort(arr, n);
    //mergeSort(arr, 0, n);
    //quickSort(arr, 0, n);
    //heapSort(arr, n);

    return 0;
}

int *initSortedTable(int n){
    int *arr = malloc(sizeof(int)*n);
    for(int i=0; i<n; i++){
        arr[i]=i;
    }
    return arr;
}

int *initReversedSortedTable(int n){
    int *arr = malloc(sizeof(int)*n);
    for(int i=n; i>0; i--){
        arr[i]=i;
    }
    return arr;
}

int *initUnsortedTable(int n){
    srand(time(0));
    int *arr = malloc(sizeof(int)*n);
    for(int i=n; i>0; i--){
        arr[i]=rand();
    }
    return arr;

}

void testSortedTable(int n){
    int *arr = initSortedTable(n);
    printArray(arr, n);
    clock_t t;
    double time_taken;

    t = clock();
    printf("Trie Par iserstion:\n");
    printArray(arr, n);
    insertionSort(arr, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("isertion pris %f seconds pour s'executer \n\n", time_taken);

    t = clock();
    printf("Trie a bulle:\n");
    printArray(arr, n);
    bubbleSort(arr, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("bulle pris %f seconds pour s'executer \n\n", time_taken);


    t = clock();
    printf("Trie a fusion:\n");
    printArray(arr, n);
    mergeSort(arr,0, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("fusion pris %f seconds pour s'executer \n\n", time_taken);


    t = clock();
    printf("Trie a rapide:\n");
    printArray(arr, n);
    quickSort(arr,0, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("rapide pris %f seconds pour s'executer \n\n", time_taken);


    t = clock();
    printf("Trie a Tas:\n");
    printArray(arr, n);
    heapSort(arr, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("Tas pris %f seconds pour s'executer \n\n", time_taken);


}

void testReversedSortTable(int n){
    int *arr = initReversedSortedTable(n);
    clock_t t;
    double time_taken;

    t = clock();
    printf("Trie Par iserstion:\n");
    printArray(arr, n);
    insertionSort(arr, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("isertion pris %f seconds pour s'executer \n\n", time_taken);

    arr = initReversedSortedTable(n);
    t = clock();
    printf("Trie a bulle:\n");
    printArray(arr, n);
    bubbleSort(arr, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("bulle pris %f seconds pour s'executer \n\n", time_taken);


    arr = initReversedSortedTable(n);
    t = clock();
    printf("Trie a fusion:\n");
    printArray(arr, n);
    mergeSort(arr,0, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("fusion pris %f seconds pour s'executer \n\n", time_taken);


    arr = initReversedSortedTable(n);
    t = clock();
    printf("Trie a rapide:\n");
    printArray(arr, n);
    quickSort(arr,0, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("rapide pris %f seconds pour s'executer \n\n", time_taken);


    arr = initReversedSortedTable(n);
    t = clock();
    printf("Trie a Tas:\n");
    printArray(arr, n);
    heapSort(arr, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("Tas pris %f seconds pour s'executer \n\n", time_taken);
 
}

void testUnsortedTable(int n){
    int *arr = initUnsortedTable(n);
    clock_t t;
    double time_taken;

    t = clock();
    printf("Trie Par iserstion:\n");
    printArray(arr, n);
    insertionSort(arr, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("isertion pris %f seconds pour s'executer \n\n", time_taken);

    arr = initUnsortedTable(n);
    t = clock();
    printf("Trie a bulle:\n");
    printArray(arr, n);
    bubbleSort(arr, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("bulle pris %f seconds pour s'executer \n\n", time_taken);


    arr = initUnsortedTable(n);
    t = clock();
    printf("Trie a fusion:\n");
    printArray(arr, n);
    mergeSort(arr,0, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("fusion pris %f seconds pour s'executer \n\n", time_taken);


    arr = initUnsortedTable(n);
    t = clock();
    printf("Trie a rapide:\n");
    printArray(arr, n);
    quickSort(arr,0, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("rapide pris %f seconds pour s'executer \n\n", time_taken);


    arr = initUnsortedTable(n);
    t = clock();
    printf("Trie a Tas:\n");
    printArray(arr, n);
    heapSort(arr, n);
    printArray(arr, n);
    t = clock() - t;
    time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds
    printf("Tas pris %f seconds pour s'executer \n\n", time_taken);
}


void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
 
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int n) {
	for (int i=0; i < n; i++)
		printf("%d ", arr[i]);
	printf("\n");
}

void swap(int* xp, int* yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
 
void bubbleSort(int arr[], int n) {
    int i, j;   
    for (i = 0; i < n - 1; i++)
        for (j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(&arr[j], &arr[j + 1]);
}

//r => right element
// l => left element
// mid => mid of the array
void merge(int arr[], int l, int mid, int r) {
    int i, j, k;
    int n1 = mid - l + 1;
    int n2 = r - mid;
 
    /* create temp arrays */
    int L[n1], R[n2];
 
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
 
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    /* Copy the remaining elements of L[], if there
    are any */
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    /* Copy the remaining elements of R[], if there
    are any */
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
 
/* l is for left index and r is right index of the
sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        // Same as (l+r)/2, but avoids overflow for
        // large l and h
        int mid = l + (r - l) / 2;
 
        // Sort first and second halves
        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);
 
        merge(arr, l, mid, r);
    }
}

int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // pivot
    int i = (low - 1); // Index of smaller element
  
    for (int j = low; j <= high - 1; j++) {
        // If current element is smaller than the pivot
        if (arr[j] < pivot) {
            i++; // increment index of smaller element
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        /* pi is partitioning index, arr[p] is now
        at right place */
        int pi = partition(arr, low, high);
  
        // Separately sort elements before
        // partition and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void heapify(int arr[], int N, int i){
    // Find largest among root, left child and right child
 
    // Initialize largest as root
    int largest = i;
 
    // left = 2*i + 1
    int left = 2 * i + 1;
 
    // right = 2*i + 2
    int right = 2 * i + 2;
 
    // If left child is larger than root
    if (left < N && arr[left] > arr[largest])
 
        largest = left;
 
    // If right child is larger than largest
    // so far
    if (right < N && arr[right] > arr[largest])
 
        largest = right;
 
    // Swap and continue heapifying if root is not largest
    // If largest is not root
    if (largest != i) {
 
        swap(&arr[i], &arr[largest]);
 
        // Recursively heapify the affected
        // sub-tree
        heapify(arr, N, largest);
    }
}
 
// Main function to do heap sort
void heapSort(int arr[], int N){
 
    // Build max heap
    for (int i = N / 2 - 1; i >= 0; i--)
 
        heapify(arr, N, i);
 
    // Heap sort
    for (int i = N - 1; i >= 0; i--) {
 
        swap(&arr[0], &arr[i]);
 
        // Heapify root element to get highest element at
        // root again
        heapify(arr, i, 0);
    }
} 