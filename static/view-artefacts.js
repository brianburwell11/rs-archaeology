function loadArtefacts(){
    $("tbody").empty();
    const alignment = $("select").find(":selected").val();
    const url = "/api/artefacts?alignment="+alignment;

    $.get({
        url: url,
        success: function(data){
            console.log(data);
            for(let artefact of data.artefacts){
                $.get({
                    url: "/api/artefacts/"+artefact.id,
                    success: function(a){
                        var html = "<tr>" +
                                    "<th scope='row'>"+a.id+"</th>" +
                                    "<td scope='row'>"+a.name+"</td>" +
                                    "<td scope='row'>"+"<img src='"+a.img+"'>"+"</td>" +
                                    "<td scope='row'>"+"<img src='"+a.imgDamaged+"'>"+"</td>" +
                                    "<td scope='row'>"+a.alignment+"</td>" +
                                    "<td scope='row'>"+a.levelRequired+"</td>" +
                                    "<td scope='row'>"+a.xp.toLocaleString("en")+"</td>" +
                                    "</tr>";
                                    
                        $("tbody").append(html);
                    },
                    error: function(e){
                        console.log(e);
                    },
                });
            };
        },
        error: function(e){
            console.log(e);
        },
    })
};

$(function(){
    loadArtefacts();
    $("select").change(loadArtefacts);


});