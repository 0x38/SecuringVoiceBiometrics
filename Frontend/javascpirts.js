var send = true
var count = 0
navigator.mediaDevices.getUserMedia({
    audio: true
}, initializeRecorder);
var sampleRate;
​
function initializeRecorder(stream) {
    audio_context = new AudioContext;
    sampleRate = audio_context.sampleRate;
    var audioInput = audio_context.createMediaStreamSource(stream);
​    console.log("Created media stream.");
​    var bufferSize = 4096;
    var recorder = audio_context.createScriptProcessor(bufferSize, 1, 1); // record only 1 channel
    recorder.onaudioprocess = recorderProcess; // specify the processing function
    audioInput.connect(recorder); // connect stream to our recorder
    recorder.connect(audio_context.destination); // connect our recorder to the previous destination
}
​
var ws = new WebSocket('ws://127.0.1.1:8888/ws');
​
ws.onopen = function(evt) {
    console.log('Connected to websocket.');
    navigator.getUserMedia({
        audio: true,
        video: false
    }, initializeRecorder, function(e) {
        console.log('No live audio input: ' + e);
    });
}
​
function recorderProcess(e) {
    if (send) {
        var left = e.inputBuffer.getChannelData(0);
        ws.send(Float32ToInt16(left));
        console.log(count);
        if (count++ >= 100) {
            ws.send("terminate");
            send = false;
        }
    }
}
​
function Float32ToInt16(buffer) {
    l = buffer.length;
    buf = new Int16Array(l);
    while (l--) {
        buf[l] = Math.min(1, buffer[l]) * 0x7FFF;
    }
    return buf.buffer;
}
