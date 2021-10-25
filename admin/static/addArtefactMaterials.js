function loadArtefactOptions(){
    $.get({
        url: "/api/artefacts",
        success: function(data){
            for(let a of data.artefacts){
                $("#artefact-select").append(new Option(a.name, a.id));
            }
        },
        error: function(e){
            console.log(e);
        }
    });
};

function loadMaterialOptions(){
    $.get({
        url: "/api/materials",
        success: function(data){
            for(let a of data.materials){
                $("[id^=material-select]").append(new Option(a.name, a.id));
            }
        },
        error: function(e){
            console.log(e);
        }
    });
}

function copyToClipboard(text) {
    var $txt = $('<textarea />');    
    $txt.val(text).css({ width: "1px", height: "1px" }).appendTo('body');
    $txt.select();    
    if (document.execCommand('copy')) {
        $txt.remove();
    }
};

$(function(){
    loadArtefactOptions();
    loadMaterialOptions();
    
    $("#artefact-select").change(function(){
        var url = "/api/artefacts/"+$(this).find(":selected").val();

        $.get({
            url: url,
            success: function(data){
                $("#artefact-img").attr("src", data.img);
            }
        })

        copyToClipboard($(this).find(":selected").text());

        // url = "https://runescape.wiki/w/"+$(this).find(":selected").text().replace(" ","_")+"#Restoration";
        // window.open(url);
        // $("#wiki").attr("href", url);
        // url = "https://www.runehq.com/item/"+$(this).find(":selected").text().replace(" ","-")+"-(damaged)";
        // $("iframe").attr("src", url);
    });

    $("#submit").click(function(){
        var formData = new FormData();

        formData.append("artefactId", $("#artefact-select").find(":selected").val());

        var materials = new Array();
        $("[id^=material-select]").each(function(idx){
            let amount = $("#"+this.id+"-amount").val();
            if(amount && $(this).val()>0){
                materials.push([$(this).find(":selected").val(), $("#"+this.id+"-amount").val()]);
            }
        });
        formData.append("materials", materials)

        $.post({
            url: '/admin/add/artefact-materials',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data){
                if(data.success){
                    $("#response").text(data.msg);
                    $("input [id^='material-select-']").val("")
                    // nextIdx = $("#artefact-select option:selected").index() + 1;
                    // $('#selectBox :nth-child('+nextIdx-1+')').prop('selected', false);
                    // $('#selectBox :nth-child('+nextIdx+')').prop('selected', true);
                }else{
                    console.log(data.error);
                    $("#response").text(data.error);
                }
            },
            error: function(e){
                console.log(e)
            }
        })
    })
})