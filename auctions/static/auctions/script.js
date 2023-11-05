


function Fire() {
    alert("bid has been placed")
}

document.addEventListener('DOMContentLoaded', () => {
    bidButtonElement = document.querySelector('.bidButtonAlert')
    if (bidButtonElement) {
    bidButtonElement.addEventListener('click', Fire);
    }
});