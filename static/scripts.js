function checkURL() {
    const url = document.getElementById("urlInput").value;
    const resultText = document.getElementById("result");

    resultText.innerHTML = "Checking...";
    
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: url })
    })
    .then(res => res.json())
    .then(data => {
        if (data.result === "Safe") {
            resultText.innerHTML = "Safe ✅";
            resultText.className = "safe";
        } else {
            resultText.innerHTML = "Phishing ⚠️";
            resultText.className = "phishing";
        }
    });
}