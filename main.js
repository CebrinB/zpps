window.addEventListener("load", () => {
    let text = document.querySelector('#hoseStatus').innerText;
    if (text === "Open") {
        document.querySelector('#hoseOn').style.display = 'none';
        document.querySelector('#hoseOff').style.display = 'block';
    } else {
        document.querySelector('#hoseOff').style.display = 'none';
        document.querySelector('#hoseOn').style.display = 'block';
    }

    const pencils = Array.from(document.querySelectorAll('#edit'));
    pencils.forEach(pencil => {
      pencil.addEventListener('touchend', e => {
        editLabel(e.currentTarget);
        
      });
    });
});

function editLabel(a) {
  debugger;
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
    