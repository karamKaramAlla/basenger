$.ajax({
    type: "post",
    url: url_for("signup"),
    data: {
        username:"",
        password:"",
        email:""
    },
    success: function (response) {
        console.log("sended")
    }
});