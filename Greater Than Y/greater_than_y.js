// Given an array and a value Y, count and print the number of array values greater than Y.
function greater_than_y(arr, y){
    let number_greater = 0;
    for(i=0;i<arr.length;i++){
        if(arr[i]>y){
            number_greater++;
        }
    }
    console.log("greater_than_y() returned", number_greater)
    return number_greater;
}

greater_than_y([0,-4,3,7,5,5,6,9,5,7],5)