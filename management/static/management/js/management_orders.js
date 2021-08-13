
older_data = []

function callNewsOrder() {
    $.ajax({
        type:'GET',
        url: '/management/orders/json/',
        success:function(response) {
            if (older_data.length != response.length) {
                older_data = response
                response.forEach(object => {
                    console.log(object['pk'] + " " + object.fields)
//
                })
            }
        },
        error:function(error) {
            console.log(error.message)
        }
    })
}

setInterval(callNewsOrder,1000 * 5);

