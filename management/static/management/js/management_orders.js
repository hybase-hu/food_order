
older_data = []
first_run = true
const _list = document.getElementById('list')
console.log(_list)
function callNewsOrder() {
    $.ajax({
        type:'GET',
        url: '/management/orders/json/',
        success:function(response) {
            if (older_data.length != response.length && first_run == true) {
                older_data = response
                if (first_run) {
                    first_run = false
                }

                if (first_run == false) {
                    alert("new order received")
                    first_run = true
                }
            }
        },
        error:function(error) {
            console.log(error.message)
        }
    })
}

setInterval(callNewsOrder,1000 * 5);

