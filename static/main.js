alert("hello");


document.addEventListener("DOMContentLoaded", function(){
    document.querySelector("#add").onclick = post;
}
);


function post(){
    let company = document.querySelector("#compamy").value;
    let role = document.querySelector("#role").value;
    alert(company + " for the role" + role);
}