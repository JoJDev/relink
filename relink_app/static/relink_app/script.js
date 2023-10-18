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
            aElement.classList.add("btn", "btn-success", "btn-lg");
            
            if (screen.width <= 425) {
                aElement.classList.add("w-100", "mt-4", "py-3");
            } else if (screen.width <= 768) {
                aElement.classList.add("w-75", "mt-4", "py-2");
            } else {
                aElement.classList.add("w-50", "my-4", "py-1");
            }
            
            document.getElementById("containerURL").innerHTML = "";
            document.getElementById("containerURL").appendChild(aElement);
        }
    } else {
        num--;
        document.getElementById("clockNum").innerText = num
    }
}

