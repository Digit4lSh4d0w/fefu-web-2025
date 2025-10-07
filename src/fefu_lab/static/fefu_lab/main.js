function toggleForm(id) {
    var el = document.getElementById(id);
    if (el.classList.contains("hidden")) {
        el.classList.remove("hidden");
        el.classList.add("visible");
    } else {
        el.classList.remove("visible");
        el.classList.add("hidden");
    }
}
