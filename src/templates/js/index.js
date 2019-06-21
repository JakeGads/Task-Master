function main() {
    let newUserBttn = document.getElementById("new_user");
    let newUserModel = document.getElementById("new_user_popup");
    let newEventBttn = document.getElementById("new_event");
    let newEventModel = document.getElementById("new_event_popup");

    let span = document.getElementsByClassName("close")[0];
    let span0 = document.getElementsByClassName("close")[1];


    newUserBttn.onclick = function() {
        newUserModel.style.display = "block";
    }

    newEventBttn.onclick = function() {
        newEventModel.style.display = "block";
    }

    span.onclick = function() {
        newUserModel.style.display = "none";
    }

    span0.onclick = function() {
        newEventModel.style.display = "none"
    }

}

main()