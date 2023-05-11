  const fileInput = document.getElementById('file');
  const uploadStatus = document.getElementById('upload_status');
  const placeholder = document.getElementById('frame')

// Upload progress event listener
  fileInput.addEventListener('change', () => {
    uploadStatus.innerHTML = 'Uploading...';
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload', true);
    xhr.upload.onprogress = (event) => {
      const percent = (event.loaded / event.total) * 100;
      uploadStatus.innerHTML = `Uploading... ${percent.toFixed(2)}%`;
      placeholder.classList.add('animate-pulse');
    };
    xhr.onload = () => {
      uploadStatus.innerHTML = '&#10003; Uploaded';
      placeholder.classList.toggle('animate-pulse');
    };
    const formData = new FormData();
    formData.append('video_file', fileInput.files[0]);
    xhr.send(formData);
  });