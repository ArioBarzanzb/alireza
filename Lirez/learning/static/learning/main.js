function toggleText(button, courseId) {
    var buttonText = button.textContent || button.innerText;
    if (buttonText === "Add to Dashboard") {
        button.textContent = "Remove from Dashboard";
        // Add the course to the dashboard
    } else {
        button.textContent = "Add to Dashboard";
        // Remove the course from the dashboard
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const themeToggleBtn = document.querySelector(".theme-toggle");
    const card = document.querySelector(".card");
    const themeToggleBtnM = document.querySelector(".mobile-nav__theme-toggle");
    //---------------
    const theme = localStorage.getItem("theme");
    
    theme && document.body.classList.add("light-mode");
    
    themeToggleBtn.addEventListener("click", () => {
      document.body.classList.toggle("light-mode");
      if (document.body.classList.contains("light-mode")) {
        localStorage.setItem("theme","light-mode");
      } else {
        localStorage.removeItem("theme");
      }
    });
    
    themeToggleBtnM.addEventListener("click", () => {
      document.body.classList.toggle("light-mode");
      if (document.body.classList.contains("light-mode")) {
        localStorage.setItem("theme", "light-mode");
      } else {
        localStorage.removeItem("theme");
      }
    });
    // ___________
    const mobileNav = document.querySelector(".mobile-nav");
    const headerBtn = document.querySelector(".header__bars");
    const mobileLinks = document.querySelectorAll(".mobile-nav__link")
    let isMobileNavOpen = false;
    headerBtn.addEventListener("click", () => {
      isMobileNavOpen = !isMobileNavOpen;
      if (isMobileNavOpen === true) {
        mobileNav.style.display = "flex";
        document.body.style.overflowY = "hidden";
      } else {
        mobileNav.style.display = "none";
        document.body.style.overflowY = "auto";
      }
    });
    
    mobileLinks.forEach(Link => {
     Link.addEventListener("click" ,() => {
        isMobileNavOpen = false;
        mobileNav.style.display = "none"
        document.body.style.overflowY = "auto";
     })
    })




    // My codes
    var userTypeSelect = document.getElementById("user_type");
    var teacherFields = document.getElementById("teacher-fields");
    
    userTypeSelect.addEventListener("change", function() {
        if (userTypeSelect.value === "teacher") {
            teacherFields.style.display = "block";
        } else {
            teacherFields.style.display = "none";
        }
    });
    document.getElementsByTagName('form')[0].addEventListener('submit', function(event) {
        var userType = document.querySelector('select[name="user_type"]').value;
    
        if (userType === "teacher") {
            var firstName = document.querySelector('input[name="first_name"]').value;
            var lastName = document.querySelector('input[name="last_name"]').value;
            var resume = document.querySelector('textarea[name="resume"]').value;
    
            if (firstName === "" || lastName === "" || resume === "") {
                alert("First name, last name and resume fields must be filled out for teachers");
                event.preventDefault();
                return false;
            }
        }
    });
})