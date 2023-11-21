function Fire() {
   
    alert("bid has been placed")
}


document.addEventListener('DOMContentLoaded', () => {
    
    let buttons = document.querySelectorAll('.A')
    buttons.forEach(elemtn => {
        elemtn.addEventListener(click , () => {
            
            elemtn.className = "d"
        })
    })



     CloseActionElement = document.querySelector(".hidden")
     ClosedActionElement = document.getElementById("closeAction")
    
    bidButtonElement = document.querySelector('.bidButtonAlert')
    if (bidButtonElement) {
    bidButtonElement.addEventListener('click', Fire);
    }

    ClosedActionElement.addEventListener('click', ()  => {
        
        CloseActionElement.className = "gg"


        alert("Closed")
    });
});