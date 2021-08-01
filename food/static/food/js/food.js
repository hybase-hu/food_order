console.log("itt vagyok");
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

console.log(csrf)

function sendOrder(food_pk) {
    console.log("onclick")

    $('.ui.modal')
      .modal({
        blurring: true
      })
      .modal('show')
    ;

    $.ajax({
        type:'POST',
        url:"/orders/",
        data:{
            csrfmiddlewaretoken:csrf,
            pk:food_pk,
        },
        success:function(response) {
            console.log("SUCCESS",response.result)
        },
        error:function(error) {
            console.log("ERROR",error)
        }
    })
}