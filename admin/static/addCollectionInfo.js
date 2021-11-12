function loadCollectorOptions(){
    $.get({
        url: "/api/collectors",
        success: function(data){
            for(let c of data){
                $("#collector-select").append(new Option(c.name, c.id));
            }
            $("#collector-select").change();
        },
        error: function(e){console.log(e);},
    });
};

function loadCollectionOptions(collectorId){
    $.get({
        url: "/api/collections?collectorId="+collectorId,
        success: function(data){
            $("#collection-select").find("option").remove();
            for(let c of data){
                $("#collection-select").append(new Option(c.name, c.id));
            }
            $("#collection-select").change();
        },
        error: function(e){console.log(e);},
    });
};

function loadArtefactOptions(){
    $.get({
        url: "/api/artefacts?sort=name",
        success: function(data){
            for(let a of data){
                $("[id^=artefact-select-]").append(new Option(a.name, a.id));
            }
        },
        error: function(e){console.log(e);},
    });
};

function loadRewardOptions(){
    $.get({
        url: "/api/rewards",
        success: function(data){
            for(let r of data){
                $("select[id^=reward-select-]").append(new Option(r.name, r.id));
                $("select[id^=completion-select-]").append(new Option(r.name, r.id));
                $("#completion-select-1").val(49430).change(); //set to "Chronotes"
            }
        },
        error: function(e){console.log(e);},
    });
};

function copyToClipboard(text) {
    var $txt = $('<textarea />');    
    $txt.val(text).css({ width: "1px", height: "1px" }).appendTo('body');
    $txt.select();    
    if (document.execCommand('copy')) {
        $txt.remove();
    }
};

$(function(){
    loadCollectorOptions();
    loadArtefactOptions();
    loadRewardOptions();

    $("#collector-select").change(function(){
        const collectorId = $(this).find(":selected").val();
        $.get({
            url: "/api/collectors/"+collectorId,
            success: function(data){
                $("#collector-img").attr("src", data.img);
            },
            error: function(e){
                console.log(e);
            },
        });

        loadCollectionOptions(collectorId);
    });
    
    $("#collection-select").change(function(){
        const url = "https://runescape.wiki/w/"+$(this).find(":selected").text().replace(" ","_");
        copyToClipboard(url);
    });

    $("#submit").click(function(){
        var formData = new FormData();

        formData.append("collectionId", $("#collection-select").val());

        var artefactRewards = new Array();
        $("select[id^=artefact-select]").each(function(idx){
            if($(this).find(":selected").val()>0){
                let artefactReward = {};
                artefactReward.artefactId = $(this).find(":selected").val();
                artefactReward.rewardId = $("#reward-"+this.id.slice(9)).val();
                artefactReward.rewardAmt = $("#reward-"+this.id.slice(9)+"-amount").val();
                
                if(artefactReward.rewardAmt>0){
                    artefactRewards.push(artefactReward);
                }
            }
        });
        formData.append("artefactRewards", JSON.stringify(artefactRewards));
        
        var collectionRewards = new Array();
        $("select[id^=completion-select]").each(function(idx){
            if($(this).find(":selected").val()>0){
                let collectionReward = {};
                collectionReward.rewardId = $(this).find(":selected").val();
                collectionReward.rewardAmt = $("#completion-"+this.id.slice(11)+"-amount").val();
                
                if(collectionReward.rewardAmt>0){
                    collectionRewards.push(collectionReward);
                }
            }
        });
        formData.append("collectionRewards", JSON.stringify(collectionRewards));
        console.log(collectionRewards);

        $.post({
            url: '/admin/add/collection-info',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data){
                if(data.success){
                    $("#response").text(data.msg);
                    $("select[id^=artefact-select]").val(-1).change();
                    $("select[id^=completion-select]").val(-1).change();
                    $("#completion-select-1").val(49430).change(); //set to "Chronotes"
                }else{
                    console.log(data.error);
                    $("#response").text(data.error);
                }
            },
            error: function(e){console.log(e);},
        });
    });

})