async function mergePDF() {
  const input = document.getElementById('fileInput');
  const pdfFile = input.files[0];
  let watermarkValue = document.getElementById('watermark_input').value;


  if (!pdfFile) {
    alert("Please select a PDF file.");
    return;
  }


  // if ((input.files).length < 2) {
  //   console.log('No files selected.');
  //   const messages = document.querySelector('.messages');
  //   messages.innerHTML += `<div class="alert alert-danger alert-dismissible fade show" role="alert">
  //                  <strong>Merge Failed!</strong> Please upload multiple PDF files to merge.
  //                   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  //               </div>`
  //   return;
  // }


  // if (file.type !== "application/pdf") {
  //   const messages = document.querySelector('.messages');
  //   messages.innerHTML += `<div class="alert alert-danger alert-dismissible fade show" role="alert">
  //                  <strong>Split Failed!</strong> Please select a valid PDF file.
  //                   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  //               </div>`
  //   return;
  // }

  const formData = new FormData();
  formData.append('PDF', pdfFile);
  formData.append('watermark', watermarkValue);



  // try {
  const response = await fetch('http://127.0.0.1:5000/api/watermark', {
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
  mergePDF();
});