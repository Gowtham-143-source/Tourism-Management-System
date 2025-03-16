let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');
let formBtn = document.querySelector('#login-btn');
let loginForm = document.querySelector('.login-form-container');
let formClose = document.querySelector('#form-close');
let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');
let videoBtn = document.querySelectorAll('.vid-btn');
// const carousel = document.querySelector('.carousel');
// const Wrapper = document.querySelector('.Wrapper');

// const arrowBtns = document.querySelectorAll('.Wrapping i');
// const firstCardWidth = carousel.querySelector('.card').offsetWidth;

// const carouselChildrens =[...carousel.children];
// s
// let isDragging = false, startX, startScrollLeft, timeoutId;

// let cardPerView = Math.round(carousel.offsetWidth / firstCardWidth);

// carouselChildrens.slice(-cardPerView).reverse().forEach( card => {
//     carousel.insertAdjacentHTML('afterbegin',card.outerHTML);

// });

// carouselChildrens.slice(-cardPerView).reverse().forEach( card => {
//     carousel.insertAdjacentHTML('beforeend',card.outerHTML);

// });

// arrowBtns.forEach(btn => {
//     btn.addEventListener('click', () => {
//         console.log(btn.id);
//         carousel.scrollLeft += btn.id === 'left' ? -firstCardWidth : firstCardWidth;
//     })

// });

// const dragStart = (e) =>{
//     isDragging = true;
//     carousel.classList.add("dragging");
//     // record the initial cursor an scroll position of the carousel
//     startX = e.pageX;
//     startScrollLeft =carousel.scrollLeft;
    
// }

// const dragging = (e) => {
//     if(!isDragging) return; //if isDragging is false return from here
//     carousel .scrollLeft = startScrollLeft- (e.pageX - startX);
// }

// const dragStop = () =>{
//     isDragging = true;
//     carousel.classList.remove("dragging");

// }

// const autoPlay = () => {
//     if(window,innerWidth < 800) return;

//     timeoutId = setTimeout(() => carousel.scrollLeft += firstCardWidth, 2500);
// }
// autoPlay();


// const infiniteScroll = () => {
//     if(carousel.scrollLeft ===0) {
//         carousel.classList.add('no-transition');
//         carousel.scrollLeft = carousel.scrollWidth -(2 * carousel.offsetWidth);
//         carousel.classList.remove('no-transition');
//     }else if(carousel.clientLeft(scrollLeft) === carousel.scrollWidth - carousel.offsetWidth){
//         carousel.classList.add('no-transition');
//         carousel.scrollLeft = carousel.offsetWidth;
//         carousel.classList.remove('no-transition');
//     }
// }

// clearTimeout(timeoutId);
// if(!Wrapper.matches(":hover")) autoPlay();

// carousel.addEventListener("mousedown", dragStart);
// carousel.addEventListener("mousemove", dragging);
// document.addEventListener("mouseup", dragStop);
// carousel.addEventListener("scroll", infiniteScroll);


window.onscroll = () =>{
    searchBtn.classList.remove('fa-times');
    searchBar.classList.remove('active');
    menu.classList.remove('fa-times');
    navbar.classList.remove('active');
    loginForm.classList.remove('active');

}

menu.addEventListener('click',() =>{
    menu.classList.toggle('fa-times');
    navbar.classList.toggle('active');
});

searchBtn.addEventListener('click',() =>{
    searchBtn.classList.toggle('fa-times');
    searchBar.classList.toggle('active');
});

formBtn.addEventListener('click',() =>{
    loginForm.classList.add('active');
});

formClose.addEventListener('click',() =>{
    loginForm.classList.remove('active');
});


videoBtn.forEach(btn =>{
    btn.addEventListener('click', () =>{
        document.querySelector('.controls .active').classList.remove('active');
        btn.classList.add('active');
        let src =btn.getAttribute('data-src');
        document.querySelector('#video-slider').src =src;
    });
});
