function Fire() {
    alert("bid has been placed")
}


document.addEventListener('DOMContentLoaded', () => {
    
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