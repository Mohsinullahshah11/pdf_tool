async function mergePDF() {
  const input = document.getElementById('fileInput');
  if ((input.files).length < 2) {
    console.log('No files selected.');
    const messages = document.querySelector('.messages');
    messages.innerHTML += `<div class="alert alert-danger alert-dismissible fade show" role="alert">
                   <strong>Merge Failed!</strong> Please upload multiple image files to create pdf.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>`
    return;
  }

  const formData = new FormData();
  for (let i = 0; i < input.files.length; i++) {
    formData.append('files', input.files[i]);
  }

  // try {
    const response = await fetch('http://127.0.0.1:5000/api/images-to-pdf', {
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