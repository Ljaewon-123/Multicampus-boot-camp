'''
        $(function(){
            $('#fish_sel').change(function(){
                fish_kind = $("#fish_sel option:selected").val()
                $.ajax({
                    url:'rank_fish/',
                    data: {'fish_kind':fish_kind,},
                    dataType: 'json',
                    success: function(msg){
                        //alert('asdf')
                        var lst = msg['fish']
                        for(var i =0; i<lst.length; i++){
	                        //console.log(lst[i])
	                        $('#total_container').append("<div class = 'container'>   \
                                                        <ul class='fish_rank'>  \
                                                        <li ><img src='{% static 'image/nunukang.jpeg' %}' alt=''></li>   \
                                                        <li><span>pro</span></li>   \
                                                        <li><span>"+lst[i]['myname']+"</span></li>  \
                                                        <li><span>"+lst[i]['length']+"</span></li>  \
                                                        <li><span>"+lst[i]['score']+"</span></li>     \
                                                    </ul>   \
                                                </div>");
                        }


                    }
                })
            })

        })

'''