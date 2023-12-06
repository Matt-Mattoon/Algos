// Analyze an array’s values and print the average.
function get_avg(arr){
    let total = 0;
    console.log('get_avg');
    for(i=0;i<arr.length;i++){
        total+=arr[i];
    }
    let avg = total/arr.length;
    console.log('returned', avg);
    return avg;
}

get_avg([8,8,5,7]);