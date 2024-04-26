$(document).ready(function(){
    $.getJSON('/api/displaycategoryjson',function(data){
        $('#categoryid').append($('<option>').text('Select Category'))
        data.map((item)=>{
            $('#categoryid').append($('<option>').text(item.categoryname).val(item.id))
        })
    })
    $('#categoryid').change(function(){
        $.getJSON('/api/displaysubcategoryjson/',{'cid':$('#categoryid').val()},function(data){
            $('#subcategoryid').empty()
            $('#subcategoryid').append($('<option>').text('Select SubCategory'))
            data.map((item)=>{
                $('#subcategoryid').append($('<option>').text(item.subcategoryname).val(item.id))
            })
        })
    })
})