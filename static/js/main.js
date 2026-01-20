function copyLink() {
    const input = document.getElementById("shortLink");
    const status = document.getElementById("copyStatus");

    input.select();
    input.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(input.value);

    status.classList.remove("d-none");
    setTimeout(() => status.classList.add("d-none"), 1500);
}
