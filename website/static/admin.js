const select_img = document.getElementById("select_img")
const bnt_archive = document.getElementById("btn_archive")
const text_archive = document.getElementById("text_archive")
const file_archive = document.getElementById("file_archive")
const a_arch = document.getElementById("a_arch")

$(document).ready(function () {
    $(bnt_archive).click(function () { 

      let text = text_archive.value
      let nom_file = file_archive.files[0].name
      let file = new FormData();
      nom_file=nom_file.replace(" ","_");
      nom_file=nom_file.replace("(","");
      nom_file=nom_file.replace(")","");
      nom_file=nom_file.replace("é","e");
      nom_file=nom_file.replace("è","e");
      file.append('file' , $(file_archive)[0].files[0]);
      console.log(nom_file);
      

    
      $.ajax({
        type: "POST",
        url: "/arch_img",
        data: file,
        contentType: false,
        cache: false,
        processData: false,
      
       
      });
      $.ajax({
        type: "POST",
        url: '/arch_txt',
        data: {text:text , nom_file:nom_file},
        success: function () {
          location.reload()
      }
    
    });
  
      // e.preventDefault();

    });
  })


$(document).ready(function () {
    $(select_img).change(function () { 
      let pute = new FormData();
      pute.append('file' , $(select_img)[0].files[0]);
     
      $.ajax({
        type: "POST",
        url: "/data",
        data: pute,
        contentType: false,
        cache: false,
        processData: false,
        
       
      });
  
  
      // e.preventDefault();
      
    });
  })
  
  function auto_height(elem) {  /* javascript */
    elem.style.height = "1px";
    elem.style.height = (elem.scrollHeight)+"px";
}


function htmlEntities(str) {
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function del_arch(element,list){
let arch_del = element.parentElement;
let arch_link

if(list=='list_arch'){
   arch_link= arch_del.firstChild.getAttribute('href');
}
if(list=="qui_sommes_nous"){
  arch_link='rientamere'
}

if(list=="philo_semaine"){
  arch_link=arch_del.children[0].children[2].getAttribute('src');
}
else{
   arch_link= arch_del.children[0].children[0].getAttribute('src')
}
console.log(list);
console.log(arch_link);
arch_link = arch_link.replace(" ","_");
arch_link = arch_link.replace("(","");
arch_link = arch_link.replace(")","");
arch_del=arch_del.innerHTML.replace('<i onclick="del_arch(this,\''+list+'\')" id="trash_i" class="fa fa-trash" aria-hidden="true"></i>', '');
$.ajax({
  type: "POST",
  url: '/del_arch_txt',
  data: {arch:arch_del , arch_link:arch_link,list:list},
   success: function () {
     
}

});

}

const btn_elec=document.getElementById("btn_elec")
const elec_img = document.getElementById("elec_img")
const text_elec=document.getElementById("text_elec")
const choix_elec = document.getElementById("choix_elec")

$(document).ready(function () {
  $(btn_elec).click(function () { 
    let choix = choix_elec.value
    let text = text_elec.value
    let nom_file = elec_img.files[0].name
    let file = new FormData();
    nom_file=nom_file.replaceAll(" ","_");
      nom_file=nom_file.replaceAll("(","");
      nom_file=nom_file.replaceAll(")","");
      nom_file=nom_file.replaceAll("é","e");
      nom_file=nom_file.replaceAll("è","e");
    file.append('file' , $(elec_img)[0].files[0]);
    console.log(nom_file);
    
     
  
    $.ajax({
      type: "POST",
      url: "/elec_img",
      data: file,
      contentType: false,
      cache: false,
      processData: false,
      
     
    });
    $.ajax({
      type: "POST",
      url: '/elec_txt',
      data: {text:text , nom_file:nom_file,choix:choix},
      success: function () {
        location.reload()
    }
    
  
  });

    // e.preventDefault();

  });
})



$(function() {

  const section=document.getElementsByTagName('section')

 
   for (var i = 0; i<section.length; i++) {
    
     if (undefined == section[i].children[1]){
     section[i].style.display="none"
   }
   }

})


const btn_qui_somme = document.getElementById("btn_quisommes")
const txt_face = document.getElementById("txt_face")
const ifram_face = document.getElementById("if_face")

$(document).ready(function () {
  $(btn_qui_somme).click(function () { 

    let text = txt_face.value
    let ifram = ifram_face.value
  
    $.ajax({
      type: "POST",
      url: '/fac_txt',
      data: {text:text , ifram:ifram},
      success: function () {
        location.reload()
    }
  
  });

    // e.preventDefault();

  });
})


const file_philo=document.getElementById("file_philo")
const nom_philo=document.getElementById("nom_phil")
const para_phil=document.getElementById("para_phil")
const btn_phil=document.getElementById("btn_phil")

$(document).ready(function () {
  $(btn_phil).click(function () { 

    let text = para_phil.value
    let nom_file = file_philo.files[0].name
    let nom_phil = nom_philo.value
    let file = new FormData();
    nom_file=nom_file.replace(" ","_");
    nom_file=nom_file.replace("(","");
    nom_file=nom_file.replace(")","");
    nom_file=nom_file.replace("é","e");
    nom_file=nom_file.replace("è","e");
    file.append('file' , $(file_philo)[0].files[0]);
    console.log(nom_file);
    

  
    $.ajax({
      type: "POST",
      url: "/data",
      data: file,
      contentType: false,
      cache: false,
      processData: false,
    
     
    });
    $.ajax({
      type: "POST",
      url: '/phil_txt',
      data: {text:text , nom_file:nom_file,nom_phil:nom_phil},
      success: function () {
       
    }
  
  });

    // e.preventDefault();

  });
})