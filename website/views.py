from apscheduler.schedulers.background import BackgroundScheduler
from flask import Blueprint, render_template, url_for, json, request
import os


views = Blueprint('views', __name__)


def save_liste(link, list):
    file = open('./save/'+link+'.txt', 'w')
    for item in list:
        file.write(item+"\n")
    file.close


def get_list(link):
    list = []
    file = open('./save/'+link+'.txt', 'r')
    for line in file:

        x = line[:-1]
        list.append(x)

    return list


elec_aff_socio = get_list("elec_aff_socio")
elec_coo_g = get_list("elec_coo_g")
elec_aff_int = get_list("elec_aff_int")
elec_aff_ext = get_list("elec_aff_ext")
elec_secré = get_list("elec_secré")
elec_comm = get_list("elec_comm")
elec_tresor = get_list("elec_tresor")
elec_aff_poli = get_list("elec_aff_poli")
elec_aff_peda = get_list("elec_aff_peda")

philo_semaine = get_list("philo_semaine")

qui_sommes_nous = get_list("qui_sommes_nous")


@views.route('/elec_txt', methods=['POST'])
def elec_txt():
    choix = request.form["choix"]
    nom_file = request.form["nom_file"]
    text = request.form["text"]
    element = f'<div class="elec_par"> <img src="/static/img_elec/{nom_file}"><p>{text}</p> </div>'
    element = element.strip('""')
    if choix == "affaires_socio":
        elec_aff_socio.append(element)
        save_liste("elec_aff_socio", elec_aff_socio)
        return elec_aff_socio
    if choix == "coo_gene":
        elec_coo_g.append(element)
        save_liste("elec_coo_g", elec_coo_g)
        return elec_coo_g
    if choix == "affaire_inter":
        elec_aff_int.append(element)
        save_liste("elec_aff_int", elec_aff_int)
        return elec_aff_int
    if choix == "affare_ext":
        elec_aff_ext.append(element)
        save_liste("elec_aff_ext", elec_aff_ext)
        return elec_aff_ext
    if choix == "secreta":
        elec_secré.append(element)
        save_liste("elec_secré", elec_secré)
        return elec_secré
    if choix == "comm":
        elec_comm.append(element)
        save_liste("elec_comm", elec_comm)
        return elec_comm
    if choix == "tresorie":
        elec_tresor.append(element)
        save_liste("elec_tresor", elec_tresor)
        return elec_tresor
    if choix == "affaire_poli":
        elec_aff_poli.append(element)
        save_liste("elec_aff_poli", elec_aff_poli)
        return elec_aff_poli
    if choix == "affaire_peda":
        elec_aff_peda.append(element)
        save_liste("elec_aff_peda", elec_aff_peda)
        return elec_aff_peda

    list_arch.append(element)
    save_liste("list_arch", list_arch)

    return list_arch


def image_im():
    list_img_dossier = []
    files = os.listdir("./website/static/test/")
    for name in files:
        element = f"<img class='image_po' src='/static/test/{name}'>"
        element = element.strip('""')
        list_img_dossier.append(element)

    return list_img_dossier


list_arch = get_list("list_arch")


@views.route('/arch_txt', methods=['POST'])
def signUpUser():
    nom_file = request.form["nom_file"]
    text = request.form["text"]
    element = f'<a id="a_arch" href="/static/img_philo/{nom_file}" download="">{text}</a>'
    element = element.strip('""')
    list_arch.append(element)
    save_liste("list_arch", list_arch)
    return list_arch


@views.route('/phil_txt', methods=['POST'])
def philo():
    nom_file = request.form["nom_file"]
    text = request.form["text"]
    nom_phil = request.form["nom_phil"]
    element = f'<div><h2 class="nom_phil">{nom_phil}</h2><div class="contp"><p>{text}</p></div><img src="/static/img_philo/{nom_file}"></div>'
    element = element.strip('""')
    philo_semaine.append(element)
    save_liste("philo_semaine", philo_semaine)
    return philo_semaine


@views.route('/fac_txt', methods=['POST'])
def fac_txt():
    ifram = request.form["ifram"]
    text = request.form["text"]
    element = f' <div class="divquisomme "><h3>{text}</h3>{ifram}</div>'
    element = element.strip('""')
    qui_sommes_nous.append(element)
    save_liste("qui_sommes_nous", qui_sommes_nous)
    return qui_sommes_nous


@views.route('/del_arch_txt', methods=['POST'])
def del_arch():
    arch = request.form["arch"]
    link = request.form["arch_link"]
    list_del = request.form["list"]
    print(arch)

    def check(n_list, lien):
        if list_del == lien:
            if lien == "qui_sommes_nous":
                n_list.remove(arch)
                save_liste(lien, n_list)
                return n_list
            n_list.remove(arch)
            save_liste(lien, n_list)
            os.remove("./website"+link)
    check(philo_semaine,"philo_semaine")
    check(list_arch, "list_arch")
    check(elec_aff_socio, "elec_aff_socio")
    check(elec_coo_g, "elec_coo_g")
    check(elec_aff_int, "elec_aff_int")
    check(elec_aff_ext, "elec_aff_ext")
    check(elec_secré, "elec_secré")
    check(elec_comm, "elec_comm")
    check(elec_tresor, "elec_tresor")
    check(elec_aff_poli, "elec_aff_poli")
    check(elec_aff_peda, "elec_aff_peda")
    check(qui_sommes_nous, "qui_sommes_nous")

    return arch


@views.route('/')
def home():
    return render_template("index.html", philo=''.join(phil), l_img=''.join(image_im()), arch_agg=''.join(list_arch), aff_ext=''.join(elec_aff_ext), aff_in=''.join(elec_aff_int), aff_peda=''.join(elec_aff_peda), aff_poli=''.join(elec_aff_poli), aff_socio=''.join(elec_aff_socio), comm=''.join(elec_comm), coo=''.join(elec_coo_g), secre=''.join(elec_secré), tresor=''.join(elec_tresor), qui_somme=''.join(qui_sommes_nous))

nb_liste=0

def change():
    global nb_liste
    global phil
    if nb_liste >= len(philo_semaine):
        nb_liste = 0
        print("la liste s'est remis à zeros")
    phil = philo_semaine[nb_liste]
    print(
        f"le philosophe à changer nous somme au {nb_liste} element de la liste .")
    nb_liste += 1


change()

scheduler = BackgroundScheduler()
scheduler.add_job(func=change, trigger="interval", seconds=20)
scheduler.start()

data = 0
