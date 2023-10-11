function clock(url, textBtn, autoRedirect = false) {
    num = parseInt(document.getElementById("clockNum").innerText)
    if (num < 1) {
        clearInterval(interval)
        if (autoRedirect) {
            document.getElementById("containerURL").innerHTML = "<p>Redirigiendo...</p>";
            window.location.href = url;
        } else {
            aElement = document.createElement("a");
            aElement.href = url;
            // aElement.target = "_blank";
            aElement.innerHTML = textBtn;
            aElement.classList.add("btn", "btn-success", "btn-lg", "w-50");
            document.getElementById("containerURL").innerHTML = "";
            document.getElementById("containerURL").appendChild(aElement);
        }
    } else {
        num--;
        document.getElementById("clockNum").innerText = num
    }
}

