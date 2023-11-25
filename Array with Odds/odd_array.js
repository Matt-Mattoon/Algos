// Create an array with all the odd integers between 1 and int parameter (inclusive).
function odd_array(int){
    console.log("odd_array(",int,")");
    new_array = [];
    for(i=0;i<=int;i++){
        if(i%2!==0){
            new_array.push(i);
        }
    }
    console.log("odd_array returned", new_array);
    return new_array;
}

odd_array(255);