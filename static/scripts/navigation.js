const sidebar = document.querySelector(".sidebar");
const navigation = document.getElementById("main-images");
const close = document.getElementById("close");

navigation.addEventListener("click", function(){
    sidebar.classList.toggle("show-sidebar");
})

close.addEventListener("click", function(){
    sidebar.classList.toggle("show-sidebar");
})