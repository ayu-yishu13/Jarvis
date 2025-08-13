$(document).ready(function () {

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    //siri-configuration
    var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    amplitude: "2",
    speed: "0.30",
    autostart: true
    });

    //siri-message
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    //playsound mic buttton
    $("#MicBtn").click(function () { 
        eel.playAssistentsound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()

        
    });

     //function doc_keyUp(e) {

        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time
        //if (e.key === ctrlKey && shiftKey && spaceKey) {
            //eel.playAssistantSound()
            //$("#Oval").attr("hidden", true);
            //$("#SiriWave").attr("hidden", false);
            //eel.allCommands()()
       // }
    //}
    //document.addEventListener('keyup', doc_keyUp, false);


    function doc_keyUp(e) {
    if (e.ctrlKey && e.shiftKey && e.code === 'Space') {
        eel.playAssistantSound();
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands();
    }
}
document.addEventListener('keyup', doc_keyUp, false);
});
