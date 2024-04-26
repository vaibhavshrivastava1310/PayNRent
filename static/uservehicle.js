$(document).ready(function(){
    $.getJSON('/api/displayvehicleforuser',{param:'all'},function(data){
        var htm=`
        <div class="box">
            <div>
                <img src="/static/Subscription.png" style="height: 100%;width: 100%;"/>
            </div>
        </div>`
        data.map((item)=>{
            htm+=`<a href='http://localhost:8000/api/displayselectedvehicle/?vehicle=${JSON.stringify(item)}' style="text-decoration:none;pointer:'cursor';color:#000000">
            <div class="box">
            <div class="imagebox">
                <img class="image" src="/${item.picture}"/>
            </div>
            <div class="company">
               ${item.companyname}
            </div>
            <div class="carname">
                ${item.subcategoryname}
            </div>
            <div class="information">
                <div>
                    <img src="/static/iconPetrol.svg"/>
                    ${item.fueltype}
                </div>
                <div>
                    <img src="/static/iconTransmission.svg"/>
                    ${item.transmissiontype}
                </div>
                <div>
                    <img src="/static/iconSeat.svg"/>
                    ${item.noofseats} Seater
                </div>
            </div>
            <div class="bookprice">
                <div>
                    <span class="ruppee">&#8377;</span>
                    <span class="amount">${item.price}</span>
                </div>
                <div id="btn" class="button_style">
                    Book
                    <ion-icon name="chevron-forward-outline" style="font-weight: bold;"></ion-icon>
                </div>
            </div>
            <div class="rate">
                189 kms | Prices &nbsp; <b>exclude</b> &nbsp; fuel cost
            </div>
            </a>
        </div> `
        })
        $('#listvehicle').html(htm)
    })



//    ************************** on load ****************************************



function searching(value){
    $.getJSON('/api/displayvehicleforuser',{param:value},function(data){
        var htm=`
        <div class="box">
            <div>
                <img src="/static/Subscription.png" style="height: 100%;width: 100%;"/>
            </div>
        </div>`
        data.map((item)=>{
            htm+=`<a href='http://localhost:8000/api/displayselectedvehicle/?vehicle=${JSON.stringify(item)}' style="text-decoration:none;pointer:'cursor';color:#000000">
            <div class="box">
            <div class="imagebox">
                <img class="image" src="/${item.picture}"/>
            </div>
            <div class="company">
               ${item.companyname}
            </div>
            <div class="carname">
                ${item.subcategoryname}
            </div>
            <div class="information">
                <div>
                    <img src="/static/iconPetrol.svg"/>
                    ${item.fueltype}
                </div>
                <div>
                    <img src="/static/iconTransmission.svg"/>
                    ${item.transmissiontype}
                </div>
                <div>
                    <img src="/static/iconSeat.svg"/>
                    ${item.noofseats} Seater
                </div>
            </div>
            <div class="bookprice">
                <div>
                    <span class="ruppee">&#8377;</span>
                    <span class="amount">${item.price}</span>
                </div>
                <div id="btn" class="button_style">
                    Book
                    <ion-icon name="chevron-forward-outline" style="font-weight: bold;"></ion-icon>
                </div>
            </div>
            <div class="rate">
                189 kms | Prices &nbsp; <b>exclude</b> &nbsp; fuel cost
            </div>
            </a>
        </div> `
        })
        $('#listvehicle').html(htm)
    })
}
$(".brand").click(function(){
    var sb=''
    $(".brand").map(function(i,item){
        if($(this).prop("checked"))
        {
            sb+="'"+$(this).val()+"',"
        }
    })
    sb=sb.substring(0,sb.length-1)
    if(sb==''){
        searching('all')
    }
    else{
        searching(sb)
    }
  })
$(".fuel").click(function(){
    var sf=''
    $(".fuel").map(function(i,item){
        if($(this).prop("checked"))
        {
            sf+="'"+$(this).val()+"',"
        }
    })
    sf=sf.substring(0,sf.length-1)
    if(sf==''){
        searching('all')
    }
    else{
        searching(sf)
    }
})
$(".transmission").click(function(){
    var st=''
    $(".transmission").map(function(i,item){
        if($(this).prop("checked"))
        {
            st+="'"+$(this).val()+"',"
        }
    })
    st=st.substring(0,st.length-1)
    if(st==''){
        searching('all')
    }
    else{
        searching(st)
    }
})
$(".category").click(function(){
    var sc=''
    $(".category").map(function(i,item){
        if($(this).prop("checked"))
        {
            sc+="'"+$(this).val()+"',"
        }
    })
    sc=sc.substring(0,sc.length-1)
    if(sc==''){
        searching('all')
    }
    else{
        searching(sc)
    }
})
$(".seat").click(function(){
    var ss=''
    $(".seat").map(function(i,item){
        if($(this).prop("checked"))
        {
            ss+="'"+$(this).val()+"',"
        }
    })
    ss=ss.substring(0,ss.length-1)
    if(ss==''){
        searching('all')
    }
    else{
        searching(ss)
    }
})
})