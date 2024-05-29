let a = document.querySelector("nav")
let btn = document.createElement("button")
btn.innerText = "Mode"
a.append(btn)

document.body.style.backgroundColor = "black";
btn.style.backgroundColor = "black";
btn.style.padding = "0.1%";
btn.style.paddingLeft = "1%";
btn.style.paddingRight = "1%";
btn.style.color = "aqua";
btn.style.borderRadius = "10px";
btn.style.boxShadow = "0px 0px 5px 0px";



let mode = "dark";
btn.addEventListener("click", () => {
    if (mode == "dark") {
        document.body.style.backgroundColor = "White";
        let li = document.querySelectorAll("a")
        li.forEach(e => {
            e.style.color = "red";
            e.style.fontWeight = "bold";
        });

        let get = document.querySelector("button")
        get.innerText = "Mode:Light"
        mode = "light";

    } else {
        document.body.style.backgroundColor = "black";
        document.body.style.color = "white";
        let li = document.querySelectorAll("a")
        li.forEach(e => {
            e.style.color = "aqua";
        });

        let get = document.querySelector("button")
        get.innerText = "Mode:Dark"
        mode = "dark";

    }
});

let p = document.querySelectorAll("p")
p.forEach(e => {
    e.addEventListener("mouseover", () => {
        e.style.color = "gold";
        e.style.fontSize = "1.2rem"
    })
});