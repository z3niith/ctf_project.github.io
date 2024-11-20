function submitFlag() {
    const flag = document.getElementById("flag-input").value;
    const resultElement = document.getElementById("result");

    // Send the flag to the Flask server
    fetch("/submit_flag", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ flag: flag })
    })
    .then(response => response.json())
    .then(data => {
        resultElement.textContent = data.message;
        resultElement.style.color = data.message === "Correct! Flag is valid!" ? 'green' : 'red';
    })
    .catch(error => {
        resultElement.textContent = "An error occurred. Please try again.";
        resultElement.style.color = 'red';
    });
}
