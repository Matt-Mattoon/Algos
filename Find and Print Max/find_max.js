// Function that finds the max value in an array and returns that value
function find_max(arr){
    console.log("find_max(",arr,")")
    let max = arr[0]
    // Edge case
    if(arr.length==0){
        console.log("array is empty")
        return
    }
    for(i=0;i<arr.length;i++){
        if(arr[i]>max){
            max = arr[i]
        }
    }
    console.log("find_max returned", max)
    return max
}

find_max([-3,0,6,3])
find_max([6])
find_max([])