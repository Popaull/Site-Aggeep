from flask import Blueprint , render_template

import os
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, abort, render_template, jsonify,json,url_for



ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
info = Blueprint('info', __name__)


def save_liste(link,list):
    file=open('./save/'+link+'.txt','w')
    for item in list:
        file.write(item+"\n")
    file.close
    
def get_ip_list(link):
    list=[]
    file = open('./save/'+link+'.txt','r')
    for line in file:
        
        x = line[:-1]
        list.append(x)

    return list

def get_list(link,nom_list):
    list=[]
    file = open('./save/'+link+'.txt','r')
    for line in file:
        x = line[:-1]
        list.append("<div>"+x+f'<i onclick="del_arch(this,\'{nom_list}\')" id="trash_i" class="fa fa-trash" aria-hidden="true"></i>'+"</div>")
    return list


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

list_adresse=get_ip_list("save_ip")
mdp="oui"
ip_addr = ""

elec_aff_socio=get_list("elec_aff_socio",'elec_aff_socio')
elec_coo_g=get_list("elec_coo_g",'elec_coo_g')
elec_aff_int=get_list("elec_aff_int",'elec_aff_int')
elec_aff_ext=get_list("elec_aff_ext",'elec_aff_ext')
elec_secré=get_list("elec_secré",'elec_secré')
elec_comm=get_list("elec_comm",'elec_comm')
elec_tresor=get_list("elec_tresor",'elec_tresor')
elec_aff_poli=get_list("elec_aff_poli",'elec_aff_poli')
elec_aff_peda=get_list("elec_aff_peda",'elec_aff_peda')

@info.route('/arch_img', methods = ['POST'])
def archive_image_post():
    files = request.files.getlist("file")
    errors = {}
    success = False
    for file in files:
        filename = secure_filename(file.filename)
        file.save(os.path.join('./website/static/file_archive',filename))
        success=True

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp =jsonify(errors)
        resp.status_code = 206
        return resp
    if success :
        resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp


@info.route('/elec_img', methods = ['POST'])
def elect_img():
    files = request.files.getlist("file")
    errors = {}
    success = False
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('./website/static/img_elec/',filename))
            success=True
        else:
            return print("fichier non comprensible")

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp =jsonify(errors)
        resp.status_code = 206
        return resp
    if success :
        resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp


@info.route('/data', methods = ['POST'])
def get_post_javascript_data():
    files = request.files.getlist("file")
    errors = {}
    success = False
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('./website/static/test',filename))
            success=True
        else:
            return print("fichier non comprensible")

    if success and errors:
        errors['message'] = 'File(s) successfully uploaded'
        resp =jsonify(errors)
        resp.status_code = 206
        return resp
    if success :
        resp = jsonify({'message' : 'Files successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

@info.route('/scan', methods=['POST'])
def signUpUser():
    global ip_addr
    ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    a = request.form["id"]
    if a == mdp:
        list_adresse.append(ip_addr)
        save_liste("save_ip",list_adresse)
        print(f"{a} est le bon mot de passe")
        return a
    else :
        print(f"mauvais mot de passe entrer de{ip_addr}")







@info.route('/admin')
def page_admin():
    if request.remote_addr not in list_adresse:
        abort(404)  # Not Found
    else:
        return render_template("admin_file.html",list_arch=''.join(get_list("list_arch",'list_arch')),aff_ext=''.join(get_list("elec_aff_ext",'elec_aff_ext'))
    ,aff_in=''.join( get_list("elec_aff_int",'elec_aff_int')),aff_peda=''.join( get_list("elec_aff_peda",'elec_aff_peda')) ,aff_poli=''.join( get_list("elec_aff_poli",'elec_aff_poli')) 
    ,aff_socio=''.join( get_list("elec_aff_socio",'elec_aff_socio')) ,comm=''.join( get_list("elec_comm",'elec_comm')) ,coo=''.join( get_list("elec_coo_g",'elec_coo_g'))
    ,secre=''.join( get_list("elec_secré",'elec_secré')),tresor=''.join( get_list("elec_tresor",'elec_tresor')))