#!/usr/bin/env python3

import face_recognition
import sys
import numpy as np
from flask import Flask, jsonify, request, redirect
from signal import signal, SIGPIPE, SIG_DFL
from flask_cors import CORS
import base64
import os
import pickle
import json
from criaDat import criadat

 
# criando servidor web Flask
app = Flask(__name__)
# o cors faz com que possa enviar e receber via post de destinos que não estejam atrás do mesmo dominio
CORS(app)

@app.route("/")
def index():
    return "<h1 style='color:blue;'>KowaBulver<h1>"

@app.route("/api/create/<nome>", methods=['POST','GET'])
def uploadFace(nome):
    if request.method == 'POST':
        file = request.files['file']
        #name = request.form['name']
        ret = request.query_string.decode("utf-8")
        print("ret ",ret)
        if ret != "":
            nome += "?" + ret
        name = nome
        known_image = face_recognition.load_image_file(file)

        if len(known_image) > 0:
#        if len(imagem_conhecida) > 0:
            faceEncodings = face_recognition.face_encodings(known_image)
            
         #   codificacaoDaFace = face_recognition.face_encodings(imagem_conhecida)

            if len(faceEncodings) > 0:
#            if len(codificacaoDaFace) > 0:
                knownImageEncoding = faceEncodings[0]

          #      codificacaoImagemConhecida = codificacaoDaFace[0]
                
                
                knownFaceEncodings.append(knownImageEncoding)
                knownFaceNames.append(name)
                i = 0
                while i < len(knownFaceEncodings):
                    all_face_encodings[knownFaceNames[i]] = knownFaceEncodings[i]
                    i += 1
                print(len(all_face_encodings))
                print("faces ",knownFaceNames)
                #aqui é onde deve guardar no banco o rosto recem upado
           #     codificacoesDeFaceConhecidas.append()    
           #     nomesDeFaceConhecidas.append(name)

               # salva 
                with open(arquivo_dat, 'wb') as f:
                    pickle.dump(all_face_encodings, f)

                return jsonify({"face_cadastrada": True,
                                    "nome cadastrado": name,
                                    "todos nomes cadastrados":knownFaceNames 
                              })
            else:
                return jsonify({"face_cadastrada": False})
        else:
            return jsonify({"face_encontrada": False})
    
    else:
     return '''
      <!doctype html>
      <title>Selfie</title>
	<center><h3>Para cadastrar o professor, selecione a foto e digite o nome dele no local indicado.</h3></center>
	<hr/>
      <form method="POST" enctype="multipart/form-data">
       Selecione a foto do Professor: 
	<input type="file" name="file">
        <br>
	<br>
        Digite o nome do Professor:
	<input type="text" name="name">
        <input type="submit" value="Upload">
      </form>
     '''

@app.route('/api/read', methods=['POST', 'GET'])
def detectFace():

    if request.method == 'POST':
        file = request.files['file']
        
        faceNames = []
        
        if (len(knownFaceNames) == 0):
            name = "sem cadastros" 
        else:
   #         

   #         image_base64 = request.form['fname']
   #         image_base64 = image_base64.replace("data:image/png;base64,","")
   #         image_base64 = image_base64.replace(" ","+")
   #         image = base64.b64decode(image_base64)
   #         with open('image.png', 'wb') as fh:
   #             fh.write(image)        
   # 
    
            capturePhoto = face_recognition.load_image_file(file)
    #
    #        capturePhoto = cv2.imread(fh)
    #        
    #         faceEncodings = face_recognition.face_encodings(capturePhoto)
            faceEncodings = face_recognition.face_encodings(capturePhoto)
    #        capturePhoto = face_recognition.load_image_file('./image.png')
    #        faceEncodings = face_recognition.face_encodings(image)
    #            
    #        
            name = "sem rostos detectados"

            for faceEncoding in faceEncodings:
                matches = face_recognition.compare_faces(knownFaceEncodings, faceEncoding)
                name = "Desconhecido"
                faceDistances = face_recognition.face_distance(knownFaceEncodings, faceEncoding)
                bestMatchIndex = np.argmin(faceDistances)
    #                
    #        
                if matches[bestMatchIndex]:
                    name = knownFaceNames[bestMatchIndex]
                
                faceNames.append(name)
    #
    #       
        if (len(faceNames) == 0):
            faceNames.append(name)
    #
        result = {"face_names": faceNames }
        return jsonify(result)
#        result = jsonify(result)
#        print(request.form['fname'])
#        return


    else:
        return '''

       <!doctype html>
       <title>Selfie</title>
       <h1>Foto para detectar</h1>
       <form method="POST" enctype="multipart/form-data">
         <input type="file" name="file">
         <input type="submit" value="Upload">
       </form>
       '''
    img = 0


if __name__ == '__main__':
    # Configura nome para o arquivo em que estão/serão gravados os nomes e as codificações das faces 
    arquivo_dat = "arquivo.dat" 

    retorno = criadat(arquivo_dat)
    
    nomesDeFaceConhecidas = retorno[0]
    codificacoesDeFaceConhecidas = retorno[1]
    
    print("Nome das faces carregadas do arquivo ",arquivo_dat)
    for face in nomesDeFaceConhecidas:
        print(face)
    print(nomesDeFaceConhecidas)
    
    knownFaceEncodings = codificacoesDeFaceConhecidas 
    knownFaceNames = nomesDeFaceConhecidas 
    all_face_encodings = {}
    signal(SIGPIPE, SIG_DFL)
    app.run(host='0.0.0.0', port=6000, debug=True, threaded=True)
