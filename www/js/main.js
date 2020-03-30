/*  Criado por Ezekiel Bulver
 *  https://github.com/bulverismo
 *
 *  Foi utilizado partes dos códigos
 *  https://github.com/webrtc/samples/tree/gh-pages/src/content/getusermedia/gum
 *  https://github.com/mahenrique94/video-reconhecimento-facial-face-api
 * 
 */

'use strict';

const api_endpoint = process.env.API_ENDPOINT;
console.log(api_endpoint);
const cam = document.getElementById('cam')
const video = document.querySelector('video');
var canvas = document.getElementById('canvas');
const button = document.querySelector('button');
var botao = document.getElementById('botao');
var rosto = document.getElementById('rosto');
var contextRosto = rosto.getContext('2d');
let retorno = document.getElementById('retorno')
let cadastrar = document.getElementById('cadastrar')
let nome = document.getElementById('nome')

var tracker = new tracking.ObjectTracker('face');
var rectangule=""

rosto.style.display = "none"

const constraints = {
  audio: false,
  video: true
};

function handleSuccess(stream) {
  window.stream = stream;
  video.srcObject = stream;
}

function handleError(error) {
  console.log('navigator.MediaDevices.getUserMedia error: ', error.message, error.name);
}

navigator.mediaDevices.getUserMedia(constraints).then(handleSuccess).catch(handleError);

window.onload = function() {

  var tarefa = tracking.track(video, tracker, { camera: true });

  tracker.on('track', function(event) {
  rectangule= null
  event.data.forEach(function(rect) {
        
    rectangule=rect

    })
  })
}

botao.onclick = () => {

  if (rectangule) {
    
    retorno.innerHTML = "";
    rosto.style.display = "inline";
    contextRosto = rosto.getContext('2d');
    contextRosto.drawImage(video, 2*rectangule.x-45, 2*rectangule.y-30, 2*rectangule.width+40, 2*rectangule.height+40, 0, 0, 100, 100)
          
  } else {
    
    rosto.style.display = "none";
    retorno.innerHTML = "Por favor tente novamente";

  }
}

cadastrar.onclick = () => {
  // validar antes
  var dataUrl = rosto.toDataURL()
  let campoNome = nome.value

  if (campoNome !== "" && campoNome !== undefined && rosto.style.display !== "none" ) {
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      
      if (this.readyState == 4 && this.status == 200) {
        var myArr = JSON.parse(this.responseText);
        organizaArray(myArr);
      } else {
        rosto.style.display = "none";
        retorno.innerHTML ='\
           <div class="spinner-border"></div>\
        ';
      }
    }
    
    xhttp.open("POST", "http://localhost:5001/api/create", true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    let jsonObject = {"foto":dataUrl,"nome":campoNome}
    xhttp.send(JSON.stringify(jsonObject))
  }
}

function organizaArray(dados) {
  var status = dados.face_cadastrada;
  var nome = dados["nome cadastrado"]
  var cadastros = dados["todos nomes cadastrados"] 

  if (status) {
    rosto.style.display = "none";
    retorno.innerHTML ='\
      <div class="alert alert-success alert-dismissible fade show"> \
        <button type="button" class="close" data-dismiss="alert">&times;</button> \
        <strong>Successo!</strong> '+nome+' foi cadastrado. \
      </div> \
      ';
  }else{
    rosto.style.display = "none";
    retorno.innerHTML ='\
      <div class="alert alert-danger alert-dismissible fade show"> \
        <button type="button" class="close" data-dismiss="alert">&times;</button> \
        <strong>Erro!</strong> Tente novamente! \
      </div> \
      ';
  }
  
}
