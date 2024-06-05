document.addEventListener("DOMContentLoaded", function() {
    // Add event listener to the sort button
    document.querySelector(".sort .navbutton").addEventListener("click", function() {
        document.querySelector(".dropdown-content").classList.toggle("show");
    });

    // Close the dropdown if the user clicks outside of it
    window.onclick = function(event) {
        if (!event.target.matches('.sort .navbutton')) {
            var dropdowns = document.getElementsByClassName("dropdown-content");
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    }
});
