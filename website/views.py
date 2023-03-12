from flask import Blueprint , render_template,url_for,json,request
import os 



views = Blueprint('views', __name__)







def save_liste(link,list):
    file=open('./save/'+link+'.txt','w')
    for item in list:
        file.write(item+"\n")
    file.close
    

def get_list(link):
    list=[]
    file = open('./save/'+link+'.txt','r')
    for line in file:
        
        x = line[:-1]
        list.append(x)

    return list




elec_aff_socio=get_list("elec_aff_socio")
elec_coo_g=get_list("elec_coo_g")
elec_aff_int=get_list("elec_aff_int")
elec_aff_ext=get_list("elec_aff_ext")
elec_secré=get_list("elec_secré")
elec_comm=get_list("elec_comm")
elec_tresor=get_list("elec_tresor")
elec_aff_poli=get_list("elec_aff_poli")
elec_aff_peda=get_list("elec_aff_peda")



qui_sommes_nous=get_list("qui_sommes_nous")

@views.route('/elec_txt', methods=['POST'])
def elec_txt():
    choix= request.form["choix"]
    nom_file = request.form["nom_file"]
    text = request.form["text"]
    element = f'<div class="elec_par"> <img src="/static/img_elec/{nom_file}"><p>{text}</p> </div>'
    element=element.strip('""')
    if choix == "affaires_socio":
        elec_aff_socio.append(element)
        save_liste("elec_aff_socio",elec_aff_socio)
        return elec_aff_socio
    if choix == "coo_gene":
        elec_coo_g.append(element)
        save_liste("elec_coo_g",elec_coo_g)
        return elec_coo_g
    if choix == "affaire_inter":
        elec_aff_int.append(element)
        save_liste("elec_aff_int",elec_aff_int)
        return elec_aff_int
    if choix == "affare_ext":
        elec_aff_ext.append(element)
        save_liste("elec_aff_ext",elec_aff_ext)
        return elec_aff_ext
    if choix == "secreta":
        elec_secré.append(element)
        save_liste("elec_secré",elec_secré)
        return elec_secré
    if choix == "comm":
        elec_comm.append(element)
        save_liste("elec_comm",elec_comm)
        return elec_comm
    if choix == "tresorie":
        elec_tresor.append(element)
        save_liste("elec_tresor",elec_tresor)
        return elec_tresor
    if choix == "affaire_poli":
        elec_aff_poli.append(element)
        save_liste("elec_aff_poli",elec_aff_poli)
        return elec_aff_poli
    if choix == "affaire_peda":
        elec_aff_peda.append(element)
        save_liste("elec_aff_peda",elec_aff_peda)
        return elec_aff_peda
    
    
    

    list_arch.append(element)
    save_liste("list_arch",list_arch)
    
    return list_arch

def image_im():
    list_img_dossier=[]
    files = os.listdir("./website/static/test/")
    for name in files:
        element=f"<img class='image_po' src='/static/test/{name}'>"
        element=element.strip('""')
        list_img_dossier.append(element)
        
    return list_img_dossier

list_arch=get_list("list_arch")



@views.route('/arch_txt', methods=['POST'])
def signUpUser():
    nom_file = request.form["nom_file"]
    text = request.form["text"]
    element = f'<a id="a_arch" href="/static/file_archive/{nom_file}" download="">{text}</a>'
    element=element.strip('""')
    list_arch.append(element)
    save_liste("list_arch",list_arch)
    return list_arch

@views.route('/fac_txt', methods=['POST'])
def fac_txt():
    ifram = request.form["ifram"]
    text = request.form["text"]
    element = f' <div class="divquisomme "><h3>{text}</h3>{ifram}</div>'
    element=element.strip('""')
    qui_sommes_nous.append(element)
    save_liste("qui_sommes_nous",qui_sommes_nous)
    return qui_sommes_nous


@views.route('/del_arch_txt', methods=['POST'])
def del_arch():
    arch = request.form["arch"]
    link = request.form["arch_link"]
    list_del = request.form["list"]
    print(arch)

    def check(n_list,lien):
        if list_del == lien:
            if lien == "qui_sommes_nous":
                 n_list.remove(arch)
                 save_liste(lien,n_list)
                 return n_list
            n_list.remove(arch)
            save_liste(lien,n_list)
            os.remove("./website"+link)
    
    check(list_arch,"list_arch")
    check(elec_aff_socio,"elec_aff_socio")
    check(elec_coo_g,"elec_coo_g")
    check(elec_aff_int,"elec_aff_int")
    check(elec_aff_ext,"elec_aff_ext")
    check(elec_secré,"elec_secré")
    check(elec_comm,"elec_comm")
    check(elec_tresor,"elec_tresor")
    check(elec_aff_poli,"elec_aff_poli")
    check(elec_aff_peda,"elec_aff_peda")
    check(qui_sommes_nous,"qui_sommes_nous")

    return arch
   
    
   


@views.route('/')
def home():
    return render_template("index.html",np=str(nom_phil),pnp=str(para_philo),img=str(image),l_img=''.join(image_im()),arch_agg=''.join(list_arch),aff_ext=''.join(elec_aff_ext)
    ,aff_in=''.join(elec_aff_int),aff_peda=''.join(elec_aff_peda) ,aff_poli=''.join(elec_aff_poli) ,aff_socio=''.join(elec_aff_socio) ,comm=''.join(elec_comm) ,coo=''.join(elec_coo_g)
    ,secre=''.join(elec_secré),tresor=''.join(elec_tresor),qui_somme=''.join(qui_sommes_nous)  )





def rgb_to_hex(r, g, b):
    
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

couleur_t=''
couleur_b='' 





# def change_tcolor(img):
#     global couleur_t
#     image = Image.open ( f"./website/static/{img}")
#     image = image.convert("RGB")
#     coordonee_t = x,y = 0 , 0
#     rt,gt,bt=image.getpixel(coordonee_t)
#     couleur_t=rgb_to_hex(rt,gt,bt)



# def change_bcolor(img):
#     global couleur_b
#     image = Image.open ( f"./website/static/{img}")
#     image = image.convert("RGB")
#     coordonee_b = x,y = image.height *-1 , 0
#     rb,gb,bb= image.getpixel (coordonee_b)  #Je recupere la couleur du pixel
#     couleur_b=rgb_to_hex(rb,gb,bb)




   #J'affiche le resultat








from apscheduler.schedulers.background import BackgroundScheduler


#Nom de philosophe afficher 
nom=["aristote" , "platon " , "hegel" , "jean paul sartre " ]
#Paragraphe afficher (il faut qu'il sois ou meme endrois que le philosophe en question) ex aristote element 0 donc son par doit etre element 0 de la liste 
para=["""
Aristote (384-322 av. J.-C.) est un philosophe et polymathe grec de l'Antiquité. Il est avec Platon, dont il a été le disciple à l'Académie, l'un des penseurs les plus influents que le monde occidental ait connu. Il est aussi l'un des rares à avoir abordé presque tous les domaines de connaissance de son temps : biologie, physique, métaphysique, logique, poétique, politique, rhétorique, éthique et de façon ponctuelle l'économie. Chez Aristote, la philosophie, à l’origine « amour de la sagesse », est comprise dans un sens plus large comme recherche du savoir pour lui-même, interrogation sur le monde et science des sciences.
 
Pour lui, la science comprend trois grands domaines : la science théorique, la science pratique et la science productive ou poïétique (appliquée). La science théorique constitue la meilleure utilisation que l'homme puisse faire de son temps libre. Elle est composée de la « philosophie première » ou métaphysique, de la mathématique et de la physique, appelée aussi philosophie naturelle. La science pratique tournée vers l'action (praxis) est le domaine de la politique et de l'éthique. La science productive couvre le domaine de la technique et de la production de quelque chose d'extérieur à l'homme. Entrent dans son champ l'agriculture, mais aussi la poésie, la rhétorique et, de façon générale, tout ce qui est fait par l'homme. La logique, quant à elle, n'est pas considérée par Aristote comme une science, mais comme l'instrument qui permet de faire progresser les sciences. Exposée dans un ouvrage intitulé Organon, elle repose sur deux concepts centraux : le syllogisme, qui marquera fortement la scolastique, et les catégories."""
, """
Platon (en grec ancien Πλάτων / Plátôn /plá.tɔːn/1), né en 428 / 427 av. J.-C. et mort en 348 / 347 av. J.-C. à Athènes, est un philosophe antique de la Grèce classique, contemporain de la démocratie athénienne et des sophistes qu'il critiqua vigoureusement. Il reprit le travail philosophique de certains de ses prédécesseurs, notamment Socrate dont il fut l'élève, ainsi que Parménide, Héraclite et Pythagore, afin d'élaborer sa propre pensée. Celle-ci explore la plupart des champs importants, c'est-à-dire la métaphysique, l'éthique, l'esthétique et la politique.
 
Son œuvre, composée presque exclusivement de dialogues, produit les premières formulations classiques des problèmes majeurs de l'histoire de la philosophie occidentale2. Chaque dialogue de Platon est l'occasion d'interroger un sujet donné, par exemple le beau ou le courage. Il y développe une méthode qu'il appelle dialectique ou maïeutique. Il voua la majeure partie de son activité à la philosophie première, mais il se consacra aussi aux apparences et aborda l'histoire naturelle dans laquelle il voulut établir deux principes :
""" , """
Georg Wilhelm Friedrich Hegel (/ˈɡeːɔɐ̯k ˈvɪlhɛlm ˈfʁiːdʁɪç ˈheːɡl̩/N 1), né le 27 août 1770 à Stuttgart et mort le 14 novembre 1831 à Berlin, est un philosophe allemand.

Son œuvre, postérieure à celle de Emmanuel Kant, appartient à l'idéalisme allemand et a eu une influence décisive sur l'ensemble de la philosophie contemporaine.

Hegel enseigne la philosophie sous la forme d'un système unissant tous les savoirs suivant une logique dialectique. Le système est présenté comme une « phénoménologie de l'esprit » puis comme une « encyclopédie des sciences philosophiques », titres de deux de ses ouvrages, et englobe l'ensemble des domaines philosophiques, dont la métaphysique et l'ontologie, la philosophie de l'art et de la religion, la philosophie de la nature, la philosophie de l'histoire, la philosophie morale et politique ou la philosophie du droit.
""" , """
Jean-Paul Charles Aymard Sartre [ ʒãpol saχtχ]n 1, né le 21 juin 1905 dans le 16e arrondissement de Paris et mort le 15 avril 1980 dans le 14e arrondissement, est un philosophe et écrivain français, représentant du courant existentialiste, dont l'œuvre et la personnalité ont marqué la vie intellectuelle et politique de la France de 1945 à la fin des années 1970.
 
Écrivain prolifique, fondateur et directeur de la revue Les Temps modernes (1945), il est connu aussi bien pour son œuvre philosophique et littéraire qu'en raison de ses engagements politiquesn 2, d'abord en liaison avec le Parti communiste, puis avec des courants gauchistes, au sens léniniste2 du terme, plus particulièrement maoïstes, dans les années 1970.

Intransigeant et fidèle à ses idées, il a toujours rejeté tant les honneurs que toute forme de censure ; il a notamment refusé le prix Nobel de littérature en 1964. Exception notable, il a cependant accepté le titre de docteur honoris causa de l'Université de Jérusalem en 1976. Il refusa de diriger une série d'émissions télévisées qu'on lui proposait, parce qu'on y mettait comme condition la réalisation d'une maquette préalable, et expliqua : « Je n'ai plus l'âge de passer des examens. » Il contribua à la création du journal Libération, allant jusqu'à le vendre lui-même dans les rues pour donner plus de publicité à son lancement.
"""]

img_list=["aristote.png","platon.jpeg","hegel.jpg","jp.jpg"]

nom_phil="husserl.jpg"
nb_liste =0
para_philo =0
image="husserl.jpg"


# change_tcolor(image)
# change_bcolor(image)
def change():
    global nb_liste
    global nom_phil
    global image
    global para_philo
    if nb_liste >= len(nom) :
        nb_liste=0
        print("la liste s'est remis à zeros")
    nom_phil=nom[nb_liste]
    image=img_list[nb_liste]
    # change_tcolor(image)
    # change_bcolor(image)
    para_philo=para[nb_liste]
    print(f"le philosophe à changer nous somme au {nb_liste} element de la liste .")
    nb_liste +=1
change()

scheduler = BackgroundScheduler()
scheduler.add_job(func=change, trigger="interval", seconds=20)
scheduler.start()

data = 0
