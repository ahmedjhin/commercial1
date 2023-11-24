function Fire() {
   
    alert("bid has been placed")
}


document.addEventListener('DOMContentLoaded', () => {
    
    let buttons = document.querySelectorAll(".A")
    function amongs() {
        this.classList.add('bg-white', 'inline-block', 'border-l', 'border-t', 'border-r', 'rounded-t', 'py-2', 'px-4', 'text-blue-700', 'font-semibold')
    };
    buttons.forEach(elemtn => {
        elemtn.addEventListener('click' , amongs )
    });



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