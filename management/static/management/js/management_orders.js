
older_data = []
const _list = document.getElementById('list')
console.log(_list)
function callNewsOrder() {
    $.ajax({
        type:'GET',
        url: '/management/orders/json/',
        success:function(response) {
            if (older_data.length != response.length) {
                older_data = response
                response.forEach(object => {
                    console.log(object['pk'] + " " + object.fields)
                    cardview_list.innerHTML += `
                        <div class="_cardview _mt-5">
                        <img src="{{item.food_pictures.url}}" alt="{{item.food}} pictures" class="_cardview__sm_image">
                        <div class="_cardview__container ">
                            <div class="_cardview__title"><b><a href="{% url 'management:management_food_update' pk=item.pk %}" class="_link">{{item.food_code|upper}}: </b>{{item.food_name|upper}}</a></div>
                            <div class=" _mt-5">{{item.food_price}} FT</div>
                            <div class="_cardview__body _mt-5 ">{{item.food_description | truncatewords:10}}</div>
                        </div>
                    </div>
                    `
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

