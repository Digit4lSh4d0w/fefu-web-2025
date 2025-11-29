const userTypeRadios = document.querySelectorAll('input[name="role"]');
const studentFields = document.getElementById("student-fields");
const teacherFields = document.getElementById("teacher-fields");

userTypeRadios.forEach((radio) => {
  radio.addEventListener("change", function () {
    if (this.value === "student") {
      studentFields.style.display = "block";
      teacherFields.style.display = "none";
    } else if (this.value === "teacher") {
      studentFields.style.display = "none";
      teacherFields.style.display = "block";
    }
  });
});
