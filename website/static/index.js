const ag = document.getElementById("ag");
const fag = document.getElementById("fag");
const ac = document.getElementById("ac");
const fac = document.getElementById("fac");
const boutton_m = document.getElementById("boutton_m");
const b_bar = document.getElementById("b_bar");
const philo = document.getElementById("philosophe_de_la_semaine");
const menu = document.getElementById("menu");
const header = document.getElementById("header");
const img1 = document.getElementById("img1");
const img2 = document.getElementById("img2");
const img3 = document.getElementById("img3");
const img4 = document.getElementById("img4");
const img5 = document.getElementById("img5");
const img6 = document.getElementById("img6");
const img7 = document.getElementById("img7");
const img8 = document.getElementById("img8");
const img9 = document.getElementById("img9");
const img10 = document.getElementById("img10");
const img11 = document.getElementById("img11");
let nimg = 1;
let etat_bar = 0;

boutton_m.addEventListener("mouseup", () => {
  if (etat_bar == 0) {
    console.log(etat_bar);
    menu.style.marginLeft = "70%";
    menu.style.opacity = "1";
    etat_bar = 1;
  } else {
    menu.style.marginLeft = "100%";
    menu.style.opacity = "0";
    etat_bar = 0;
  }
});

let b1 = header.getBoundingClientRect();
let b2 = menu.getBoundingClientRect();

document.addEventListener("mouseup", function (event) {
  if (!menu.contains(event.target) && !boutton_m.contains(event.target)) {
    menu.style.marginLeft = "100%";
    menu.style.opacity = "0";
    etat_bar = 0;
  }
});

function startTime() {
  var today = new Date();
  var h = today.getHours();
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById("time").innerHTML = h + ":" + m + ":" + s;
  var t = setTimeout(startTime, 500);
}
function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}

startTime();

function aghover() {
  ag.style.color = "#E50313";
  fag.style.color = "#E50313";
}

function achover() {
  ac.style.color = "#E50313";
  fac.style.color = "#E50313";
}

ag.addEventListener("mouseover", () => {
  aghover();
});
ac.addEventListener("mouseover", () => {
  achover();
});
ag.addEventListener("mouseout", () => {
  ag.style.color = "#edf4f8";
  fag.style.color = "#edf4f8";
});
ac.addEventListener("mouseout", () => {
  ac.style.color = "#edf4f8";
  fac.style.color = "#edf4f8";
});

// ***********************************Slider*****************************************

const precedent = document.getElementById("precedent");
const suivant = document.getElementById("suivant");

function precedentc() {
  nimg -= 1;
  if (nimg <= 0) {
    nimg = 11;
  }

  window.location.href = "#img" + nimg;
}

function suivantc() {
  nimg += 1;
  if (nimg >= 12) {
    nimg = 0;
  }

  window.location.href = "#img" + nimg;
  $.ajax({
    type: "POST",
    url: "/data",
    data: {
      oui: "oui",
    },
  });
}

const ivideo = document.getElementById("video");
let list_video = [
  "2j87vUSadHg",
  "D9s4ub2tjLA",
  "pe5HpgZKQjs",
  "xlI779nolHo&amp",
  "8FkoMm1hs1g",
  "tipv_s2EnlU",
  "5XCnGuK8CVc",
];

let list_video2 = [];

function video_ale() {
  const randomElement =
    list_video[Math.floor(Math.random() * list_video.length)];
  ivideo.src = `https://www.youtube.com/embed/${randomElement}?&autoplay=1&mute=1&playsinline=1&playlist=${randomElement}&loop=1&amp;controls=0&amp;showinfo=0 `;
}

video_ale();

// ********************************Admin*********************************************

const select_img = document.getElementById("select_img");
const inputFile = document.getElementById("file");
const connection = document.getElementById("Connexion");
const mdp = document.getElementById("mdp");

let con_v = false;
connection.addEventListener("click", () => {
  if (con_v == false) {
    mdp.style.width = "30%";
    mdp.style.opacity = "1";
    con_v = true;
  } else {
    mdp.style.width = "0%";
    mdp.style.opacity = "0";
    con_v = false;
  }
});

$(document).ready(function () {
  var clicked;
  $(mdp).change(function () {
    clicked = mdp.value;
    $.ajax({
      type: "POST",
      url: "/scan",
      data: { id: clicked },
      success: function () {
        window.location.href = "/admin";
      },
    });
  });
});

// ********************aggeep*************
const btn_election = document.getElementById("btn_election");
const btn_archive = document.getElementById("btn_archive");

const election = document.getElementById("election");
const archive = document.getElementById("archive");
const ag_div = document.getElementById("quinous");

let list_agge = [election, archive, ag_div];
let v_election = false;
let v_archive = false;



function slide(e) {
  
  const element = document.getElementById(e);
  if (element.style.height > "0vh") {
    element.style.height = "0vh";
  }

   else {
    list_agge.forEach((element) => {
      element.style.height = "0vh";
    });

    element.style.height = "100vh";
    if (e == "election"){
      slide_elec('Affaire_interne',document.getElementById("first"))
    }
  }
}

const section_elec = document.getElementById("section_elec");
const flex_elec = document.getElementById("flex_elec");
console.log(flex_elec);

function slide_elec(e, ele) {
  const element = document.getElementById(e);


    for (const child of section_elec.children) {
      child.style.height = "0vh";
    

    for (const child of flex_elec.children) {
      child.style.color = "#edf4f8";
      child.style.borderColor = "#edf4f8";
    }
    ele.style.color = "#272727";
    ele.style.borderColor = "#272727";
    element.style.height = "auto";
  }
}

slide_elec("affaires_socioculturelles");

document.getElementById("postfb").style.background = "white";
