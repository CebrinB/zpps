window.addEventListener("load", () => {
    let text = document.querySelector('#hoseStatus').innerText;
    if (text === "Open") {
        document.querySelector('#hoseOn').style.display = 'none';
        document.querySelector('#hoseOff').style.display = 'block';
    } else {
        document.querySelector('#hoseOff').style.display = 'none';
        document.querySelector('#hoseOn').style.display = 'block';
    }

    if (localStorage.hasOwnProperty('labels')) {
        let labels = JSON.parse(localStorage.getItem('labels'));
    } else {
        let labels = {"Sensor 1", "Sensor 2", "Sensor 3", "Sensor 4"};
    }
    let i = 0;
    let elems = Array.from(document.querySelectorAll('.label'));
    elems.forEach(elem => {
        elem.innerText = labels[i];
    });
    
    let pencil = document.querySelector('#edit');
    pencil.addEventListener('touchend', e => {
        editLabel(e.currentTarget);
    });
    
    pencil = document.querySelector('#save');
    pencil.addEventListener('touchend', e => {
        saveLabel();
    });
});

function editLabel(a) {
    a.style.display = 'none';                     //hide the edit button
    a.nextElementSibling.style.display = 'block'; //show the save button

    //hide old labels
    const labels = Array.from(document.querySelectorAll('.label'));
    labels.forEach(label => {
      label.style.display = 'none';
    });

    //show input fields and fill with current label
    const inputs = Array.from(document.querySelectorAll('input'));
    inputs.forEach(input => {
      input.parentElement.style.display = 'block';
      input.value = input.parentElement.previousElementSibling.innerText; 
    });   
}

function saveLabel() {
    const inputs = Array.from(document.querySelectorAll('input'));
    const labels = Array.from(document.querySelectorAll('.label'));
    let temp = []
    let i = 0;
    labels.forEach(label => {
        label.innerText = inputs[i].value;
        temp.push(inputs[i].value);
        i++;
    });
    
    localStorage.setItem('labels', JSON.stringify(temp));
    window.location.href = "/";
}
    