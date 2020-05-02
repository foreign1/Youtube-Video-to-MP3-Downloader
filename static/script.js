const items = document.querySelectorAll("li");
const underline = document.querySelector(".underline");

// Set initial size of the bar
underline.style.width = items[0].offsetWidth + "px";

for (let i = 0; i < items.length; i++) {
    const li = items[parseInt(i, 10)];

    li.addEventListener("click", () => {
        document.querySelector(".active").classList.remove("active");
        li.classList.add("active");

        // Move the bar dynamically
        let sizeToMove = 0;
        for (let j = 0; j < 1; j++) {
            sizeToMove += items[parseInt(j, 10)].offsetWidth;
        }
        underline.style.left = sizeToMove + "px";
        underline.style.width = li.offsetWidth + "px";
    });
}