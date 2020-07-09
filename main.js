window.addEventListener("load", () => {
    let text = document.querySelector('#hoseStatus').innerText;
    if (text === "Open") {
        document.querySelector('#hoseOn').style.display = 'none';
        document.querySelector('#hoseOff').style.display = 'block';
    } else {
        document.querySelector('#hoseOff').style.display = 'none';
        document.querySelector('#hoseOn').style.display = 'block';
    }
});

function editLabel(e) {
    document.querySelector('').style.display = 'none'; //hide the label
    document.querySelector('').style.display = 'block'; //show the input field
    
    //fill the input field with current label
    document.querySelector('').placeholder = document.querySelector('').innerText;
}
    