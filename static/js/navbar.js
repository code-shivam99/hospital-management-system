const menuToggle = document.getElementById("menu-toggle");

const navLinks = document.getElementById("nav-links");

menuToggle.addEventListener("click", function () {
  navLinks.classList.toggle("active");
});

/* Active Navbar */

const sections = document.querySelectorAll("section");

const navItems = document.querySelectorAll(".nav-links a");

window.addEventListener("scroll", () => {
  let current = "";

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;

    if (pageYOffset >= sectionTop - 100) {
      current = section.getAttribute("id");
    }
  });

  navItems.forEach((a) => {
    a.classList.remove("active");

    if (a.getAttribute("href") === "#" + current) {
      a.classList.add("active");
    }
  });
});

/* HERO SLIDER */

/* TOGGLE MENU */

const menuToggle = document.getElementById("menu-toggle");

const navLinks = document.getElementById("nav-links");

menuToggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});


/* MOBILE DROPDOWN */

const dropdown = document.querySelector(".dropdown");

dropdown.addEventListener("click", () => {
  if (window.innerWidth <= 992) {
    dropdown.classList.toggle("active");
  }
});

/* HERO SLIDER */

const slides = document.querySelectorAll(".slide");

let currentSlide = 0;

function changeSlide() {
  slides.forEach((slide) => {
    slide.classList.remove("active");
  });

  currentSlide++;

  if (currentSlide >= slides.length) {
    currentSlide = 0;
  }

  slides[currentSlide].classList.add("active");
}

/* AUTO SLIDE */

setInterval(changeSlide, 3000);

const toggle = document.getElementById("menu-toggle");

const navLinks = document.getElementById("nav-links");

toggle.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

/* NAVBAR SCROLL */

window.addEventListener("scroll", () => {
  const navbar = document.querySelector(".navbar");

  navbar.classList.toggle("scrolled", window.scrollY > 50);
});

  