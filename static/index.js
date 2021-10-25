$(function(){
    $.get({
        url: "/api/materials",
        success: function(data){
            for(let m of data.materials){
                $("#materials").append(new Option(m.name, m.id));
            }
        },
        error: function(e){
            console.log(e);
        },
    });

    $("#materials").change(function(){
        const id = $(this).find(":selected").val();
        $.get({
            url: "/api/materials/"+id,
            success: function(data){
                $("img").attr("src", data.img);
                $("#name").text(data.name);
                $("#price").text(data.price?data.price:"N/A");
            },
            error: function(e){
                console.log(e);
            },
        })
    });

    $("#material-type").change(function(){
        const alignment = $(this).find(":selected").val();
        $("#materials").empty();
        $.get({
            url: "/api/materials?alignment="+alignment,
            success: function(data){
                for(let m of data.materials){
                    $("#materials").append(new Option(m.name, m.id));
                }
            },
            error: function(e){
                console.log(e);
            },
        });
    });
})