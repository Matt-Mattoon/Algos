// Print all odd integers from 1 to 255.
function print_odds(){
    console.log("print_odds");
    for(i=1;i<256;i++){
        if(i%2!=0){
            console.log(i);
        }
    }
    return
}

print_odds();