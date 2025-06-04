async function splitPDF() {
  let pagesInput = document.getElementById('pages').value;
let Pages = pagesInput
  .split(',')            
  .map(x => parseInt(x)) 
  .filter(x => !isNaN(x));

  console.log(Pages)



  const input = document.getElementById('fileInput');
  const file = input.files[0];

  if (!file) {
    console.log('No file selected.');
    const messages = document.querySelector('.messages');
    messages.innerHTML += `<div class="alert alert-danger alert-dismissible fade show" role="alert">
                   <strong>Split Failed!</strong> Please upload a valid PDF file to split.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>`
    return;
  }

  if (file.type !== "application/pdf") {
    const messages = document.querySelector('.messages');
    messages.innerHTML += `<div class="alert alert-danger alert-dismissible fade show" role="alert">
                   <strong>Split Failed!</strong> Please select a valid PDF file.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>`
    return;
  }

  const formData = new FormData();
  formData.append('pages', Pages);
  formData.append('file', file);




    const response = await fetch('http://127.0.0.1:5000/api/remove-pages', {
      method: 'POST',
      body: formData 
    });

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    console.log(`url ${url}`)
    a.download
    document.body.appendChild(a);
    a.click();
    a.remove();

    window.URL.revokeObjectURL(url);

  // } 


}

const submitbtn = document.getElementById('submit');

submitbtn.addEventListener('click', (e) => {
  // e.preventDefault();
  splitPDF();
});