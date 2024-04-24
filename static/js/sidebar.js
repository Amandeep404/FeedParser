const sidebar = document.getElementById("sidebar");
const sidebarToggle = document.getElementById("sidebar-toggle");
const sidebarContent = document.getElementById("sidebar-content");
const username = document.getElementById("user-name");
const mainContent = document.getElementById("main-content");
const toggleIcon = document.getElementById("toggle-icon");

sidebarToggle.addEventListener("click", function () {
  if (sidebar.classList.contains("w-1/6")) {
    // Expanded
    sidebar.classList.replace("w-1/6", "w-12"); // Collapse
    sidebarContent.classList.add("hidden"); // Hide content
    username.classList.add("hidden"); // Hide content
    toggleIcon.src = "/static/images/sidebar_close.png"; // Change to collapse icon
    mainContent.classList.add("pl-12"); // Adjust for collapsed sidebar
  } else {
    // Collapsed
    sidebar.classList.replace("w-12", "w-1/6"); // Expand
    sidebarContent.classList.remove("hidden"); // Show content
    username.classList.remove("hidden"); // Show content
    toggleIcon.src = "/static/images/sidebar_open.png"; // Change to open icon
    mainContent.classList.remove("pl-12"); // Adjust for expanded sidebar
  }
});

const dropUp = document.getElementById("drop-up-menu");

function toggleDropUp() {
  // Toggle between showing and hiding the drop-up menu
  dropUp.classList.toggle("hidden");

}

sidebarToggle.addEventListener("click", function () {
  dropUp.classList.toggle("hidden");
  if (sidebar.classList.contains("w-12")) {
    // Expanded
    dropUp.style.display = 'none';
  }
  else {
    dropUp.style.display = '';
  }
});
