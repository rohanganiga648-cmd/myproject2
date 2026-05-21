function go(id){
    document.getElementById(id).scrollIntoView({behavior:"smooth"});
}

async function check(){
    let resultBox = document.getElementById("result");
    resultBox.innerHTML = "Scanning...";

    // Dummy features (replace with real extraction)
    let features = [1,0,1,0,1];

    let res = await fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({features})
    });

    let data = await res.json();

    if(data.result === 1){
        resultBox.innerHTML = `⚠️ Phishing Detected (${data.confidence}%)`;
        resultBox.style.color = "red";
    } else {
        resultBox.innerHTML = `✅ Safe (${data.confidence}%)`;
        resultBox.style.color = "green";
    }
}