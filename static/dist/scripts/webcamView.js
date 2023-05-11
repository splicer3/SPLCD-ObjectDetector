// Init webcam
Webcam.set({
    width: 640,
    height: 480,
    dest_width: 640,
    dest_height: 480,
    image_format: 'jpeg',
    jpeg_quality: 90,
    force_flash: false,
    flip_horiz: true,
    fps: 45,
    upload_name: 'video_file',
})

// Selecting webcam div
const webcamElement = document.getElementById('webcam')
// Attach webcam to webcam div
Webcam.attach('#webcam')
// Remove inline style and add classes to webcam video element (child of webcam div)
webcamElement.children[1].removeAttribute('style')
webcamElement.children[1].classList.add('self-center', 'object-contain', 'w-auto', 'h-auto')

const fileInput = document.getElementById('file');
const frame = document.getElementById('frame')

// Upload progress event listener
fileInput.addEventListener('click', () => {
    Webcam.snap((data_uri) => {
        fetch('/webcamdetection', {
            method: 'POST',
            body: JSON.stringify({ 'data_uri': data_uri }),
            headers: { 'Content-Type': 'application/json' }
        })
        .then(response => frame.src = "/detection")
        .then(data => console.log(data))
        .catch(error => console.error(error));
        frame.removeAttribute('style');
    });
});