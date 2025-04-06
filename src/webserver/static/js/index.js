const app = document.getElementById('app');
const msg = document.getElementById('msg');

app.addEventListener('click', function (event) {
    if (event.target && event.target.id === "submit_vtt") {
        console.log("Button clicked!");
    }
});