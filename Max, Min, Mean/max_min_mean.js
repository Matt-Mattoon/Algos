// Given an array, print the max, min and average values for that array.
function mmm(arr){
    let max = arr[0];
    let min = arr[0];
    let total = arr[0];
    let avg = 0;
    for(i=1; i<arr.length; i++){
        total += arr[i];
        if(arr[i]>max){
            max = arr[i];
        }
        if(arr[i]<min){
            min = arr[i];
        }
    }
    avg = total/arr.length
    console.log("max", max, "min", min, "avg", avg);
    return max, min, avg;
}

mmm([-5,-5,3,4,1,2,5,5])