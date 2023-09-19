document.addEventListener("DOMContentLoaded", () => {
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