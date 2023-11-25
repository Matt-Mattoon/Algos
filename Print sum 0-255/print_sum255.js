// A function, with a parameter int, that will print the consecutive sum of 0 to int and return the sum
function consecutive_sum(int){
    let sum = 0;
    for(i=0;i<=int;i++){
        sum+=i;
        console.log("+", i, "=", sum);
    }
    console.log("consecutive_sum returned", sum);
    return sum;
}

consecutive_sum(255);