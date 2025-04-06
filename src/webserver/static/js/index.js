const app = document.getElementById('app');
const msg = document.getElementById('msg');
const input = document.getElementById('file');

app.addEventListener('click', function (event) {
    if (event.target && event.target.id === "submit_vtt") {
        console.log("Button clicked!");
    }
});

input.addEventListener("input", updateValue);

function updateValue(e) {
    console.log(e.target.value);
}

