document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("madlib-form");

    if (form) {
        form.addEventListener("submit", function (event) {
            let valid = true;

            document.querySelectorAll("input[type='text']").forEach(input => {
                if (input.value.trim().length < 3) {
                    valid = false;
                    alert("Each response should be at least 3 characters long!");
                    input.focus();
                }
            });
            if (!valid) event.preventDefault();
        });
    }
});