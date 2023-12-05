// Replace any negative array values with 'Mert'.
function change_array(arr){
    for(i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr[i] = "Mert"
        }
    }
    console.log(arr);
    return arr
}

change_array([-1,1,-1,1,-1])

