/*
*  Copyright (c) 2015 The WebRTC project authors. All Rights Reserved.
*
*  Use of this source code is governed by a BSD-style license
*  that can be found in the LICENSE file in the root of the source
*  tree.
 */

'use strict';

let recordedChunks;
var options = {mimeType: 'audio/webm'};
let recoder;
// Put variables in global scope to make them available to the browser console.
const audio = document.querySelector('audio');
const constraints = window.constraints = {
  audio: true,
  video: false
};

function handleSuccess(stream) {
  const audioTracks = stream.getAudioTracks();
  console.log('Got stream with constraints:', constraints);
  console.log('Using audio device: ' + audioTracks[0].label);
  stream.oninactive = function() {
    console.log('Stream ended');
  };
  window.stream = stream; // make variable available to browser console
  audio.srcObject = stream;
}

function handleError(error) {
  console.log('navigator.MediaDevices.getUserMedia error: ', error.message, error.name);
}

navigator.mediaDevices.getUserMedia(constraints).then(handleSuccess).catch(handleError);


function mediaplay(){
  recordedChunks = [];
  document.getElementById('gum-local').play();
  console.log("working");
  recoder = new MediaRecorder(window.stream, options);
  recoder.ondataavailable = handleDataAvailable;
  recoder.start();

  function handleDataAvailable(event) {
    if (event.data.size > 0) {
      recordedChunks.push(event.data);
      console.log("if condition working ")
    } else {
      console.log("else working ")

    }
  console.log("play");
  }
}
function mediastop(){
  document.getElementById('gum-local').pause();
  console.log("paused");
  recoder.stop();
  window.setTimeout(download,100);
}
function download()
{
  const blob = new Blob(recordedChunks, {type: 'audio/webm'});
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.style.display = 'none';
  a.href = url;
  a.download = 'test.mp3';
  document.body.appendChild(a);
  a.click();
  setTimeout(() => {
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  }, 100);
}
