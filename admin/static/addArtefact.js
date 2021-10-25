function copyToClipboard(text) {
    var $txt = $('<textarea />');    
    $txt.val(text).css({ width: "1px", height: "1px" }).appendTo('body');
    $txt.select();    
    if (document.execCommand('copy')) {
        $txt.remove();
    }
};

function clearForm(){
    $("#artefact-id,#artefact-name").val("");
}


$(function(){
    $("#submit").click(function(){
        $.ajax({
            type: "POST",
            data: {
                id: $("#artefact-id").val(),
                name: $("#artefact-name").val(),
                alignment: $("#artefact-alignment").find(":selected").val(),
                levelRequired: $("#level-required").val(),
                xp: $("#xp-gained").val(),
            },
            success: function(data){
                if(data["success"]){
                    clearForm();
                    $("#artefact-name").val(data["next"]);
                    copyToClipboard(data["next"]+" rs3 item id");
                    window.open("https://runescape.wiki/w/"+data["next"].replace(" ","_")+"#Artefact_info");
                    // window.open("https://www.google.com/search?q="+data["next"].replace(" ","+")+"+rs3+item+id");
                }else{
                    console.log(data["error"]);
                }
            },
            error: function(e){
                console.log(e);
            },
        });
    })
})