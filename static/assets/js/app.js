 // Force to scroll top 
 history.scrollRestoration = "manual"
 window.addEventListener('beforeunload', function (event) {
     window.scrollTo(0, 0);
 });


 //  Back to top 
 let btpbutton = document.getElementById('btpbutton')
 window.addEventListener('scroll', (function () {
     if ($(window).scrollTop() > 300) {
         btpbutton.classList.add('show');
     } else {
         btpbutton.classList.remove('show');
     }
 }))

 btpbutton.addEventListener('click', function (e) {
     window.scrollTo(0, 0);
 });

 //  Sub menu collapse
 const expandBtn = document.querySelectorAll(".expand-btn");
 expandBtn.forEach((btn) => {
     btn.addEventListener("click", () => {
         btn.classList.toggle("open");
     });
 });

 //  hamburger menu 
 let hamMenu = document.getElementById('hamburger')
 let navMenu = document.getElementById('nav-menu')
 hamMenu.addEventListener('click', function () {
     hamMenu.classList.toggle('active')
     navMenu.classList.toggle('active')
 })

 //  Download collapse 
 $(".downloadbtn").click(function (e) {
     $(this).children('.expand-icon').toggleClass('active');
     $(this).next(".dropdown").slideToggle();
     e.stopPropagation();
 });

 $(document).ready(function () {
     $(".dropdown .toogle-dropdown-sub").click(function (e) {
         $(this).children('.expand-icon').toggleClass('active');
         dropSub = $(this).next('.dropdown-sub')
         dropSub.slideToggle()
         dropSub.closest('li').siblings('li').children('.dropdown-sub').slideUp()
         dropSub.closest('li').siblings('li').children('.toogle-dropdown-sub').children('.expand-icon').removeClass('active')
         e.stopPropagation();
     });
 });

 // Watch modal
 $('#openwatch').on('click', function () {
     $('body').css('overflow', 'hidden')
     $('#watchModal').css({
         'display': 'flex',
     })
 })
 $('#closeModal').on('click', function () {
     $('#watchModal').hide()
     $('body').css('overflow', 'visible')
 })

 // Search Content
 $('.search-icon').on('click', function () {
     $('.nav').toggleClass('search_open')
     $('#id_search').focus()
     if ($('.searched-content li').css('opacity') && $('.searched-content').css('display') != 'none') {
         $('body').css('overflow', 'hidden')
     } else {
         $('body').css('overflow', 'visible')
     }
 })



 descript = document.querySelector('.descript')
 descriptCol = document.querySelector('.descript .col-12')
 seeMoreBtn = document.querySelector('.see-more-btn')

 function isOverflown(element) {
     return element.scrollHeight > element.clientHeight;
 }

 // checkOverflow()
 if (descriptCol) {
     if (isOverflown(descriptCol)) {
         descript.classList.add('hidden')
     }
 }
 if (seeMoreBtn)
     seeMoreBtn.addEventListener('click', () => {
         descript.classList.toggle('expand')
     })






 // Splide slider
 let width = window.innerWidth;
 let perLoadCount = 0
 let carousels = document.querySelectorAll('.slider__content');
 let heroslider_content = document.getElementById('heroslider_content');
 let topslider__content = document.getElementById('topslider__content');
 let primaryslider__content = document.getElementById('primary-slider');
 let secondaryslider__content = document.getElementById('secondary-slider');

 if (width > 768)
     perLoadCount = 1

 if (typeof (heroslider_content) != 'undefined' && heroslider_content != null) {
     new Splide(heroslider_content, {
         type: 'fade',
         perMove: 1,
         preloadPages: perLoadCount,
         interval: 5000,
         rewind: true,
         autoplay: true,
         cover: true,
         lazyLoad: 'nearby',
     }).mount();
 }

 if (typeof (topslider__content) != 'undefined' && topslider__content != null) {
     new Splide(topslider__content, {
         perPage: 5,
         perMove: 1,
         preloadPages: perLoadCount,
         cover: true,
         pagination: false,
         interval: 4000,
         autoplay: true,
         lazyLoad: 'nearby',
         breakpoints: {
             '1920': {
                 perPage: 6,
             },
             '1550': {
                 perPage: 5,
             },
             '1280': {
                 perPage: 4,
             },
             '768': {
                 perPage: 3,
             },
             '480': {
                 perPage: 2,
             },
         }
     }).mount();
     topslider__content.classList.add('splide_active')
 }

 // episode splider
 // episodes slider must be top of other carosals for fixing offsetTop problem 
 if ((typeof (secondaryslider__content) != 'undefined' && secondaryslider__content != null) && (typeof (primaryslider__content) != 'undefined' && primaryslider__content != null)) {
     let secondarySlider = new Splide(secondaryslider__content, {
         gap: 20,
         cover: true,
         isNavigation: true,
         focus: 1,
         arrows: false,
         pagination: false,
         breakpoints: {
             '1920': {
                 perPage: 6,
                 gap: '1.5rem',
             },

             '1312': {
                 perPage: 5,
                 gap: '1rem',
             },
             '992': {
                 perPage: 4,
                 gap: '1rem',
             },
             '688': {
                 perPage: 3,
                 gap: '1rem',
             },
             '480': {
                 perPage: 2,
                 gap: '1rem',
             },
         }
     }).mount();
     let primarySlider = new Splide(primaryslider__content, {
         type: 'slide',
         heightRatio: 0.5,
         pagination: false,
         arrows: false,
         cover: true,
     }); // do not call mount() here.

     primarySlider.sync(secondarySlider).mount();


     //  localStorage.clear()
     let episodeWatchStatus = localStorage.episodeWatchStatus

     if (episodeWatchStatus) {
         episodeWatchStatus = JSON.parse(episodeWatchStatus)
     } else {
         episodeWatchStatus = {}
     }
     seasonID = document.querySelector('.episode-main').dataset.seasonId
     primarySlider.go(episodeWatchStatus[seasonID] ? episodeWatchStatus[seasonID] : 0)

     secondarySlider.on('click', function () {
         episodeWatchStatus[seasonID] = secondarySlider.index
         console.log(JSON.stringify(episodeWatchStatus))
         localStorage.setItem('episodeWatchStatus', JSON.stringify(episodeWatchStatus))
     });

 }

 carousels.forEach(carousel => {
     //if in Viewport
     if (isInViewport(carousel, -100) && !carousel.classList.contains('splide_active')) {
         new Splide(carousel, {
             perPage: 5,
             perMove: 1,
             preloadPages: perLoadCount,
             cover: true,
             pagination: false,
             lazyLoad: 'nearby',
             breakpoints: {
                 '1920': {
                     perPage: 6,
                     gap: '1rem',
                 },
                 '1550': {
                     perPage: 5,
                     gap: '1rem',
                 },
                 '1280': {
                     perPage: 4,
                     gap: '1rem',
                 },
                 '768': {
                     perPage: 3,
                     gap: '1rem',
                 },
                 '480': {
                     perPage: 2,
                     gap: '1rem',
                 },
             }
         }).mount()
         carousel.classList.add('splide_active')
     }
 })

 document.addEventListener("DOMContentLoaded", function (event) {
     //  add event on scroll
     window.addEventListener('scroll', function (event) {
         carousels.forEach(carousel => {
             //if in Viewport
             if (isInViewport(carousel, -100) && !carousel.classList.contains('splide_active')) {
                 new Splide(carousel, {
                     perPage: 5,
                     perMove: 1,
                     preloadPages: perLoadCount,
                     cover: true,
                     pagination: false,
                     lazyLoad: 'nearby',
                     breakpoints: {
                         '1920': {
                             perPage: 6,
                             gap: '1rem',
                         },
                         '1550': {
                             perPage: 5,
                             gap: '1rem',
                         },
                         '1280': {
                             perPage: 4,
                             gap: '1rem',
                         },
                         '768': {
                             perPage: 3,
                             gap: '1rem',
                         },
                         '480': {
                             perPage: 2,
                             gap: '1rem',
                         },
                     }
                 }).mount()
                 carousel.classList.add('splide_active')
             }
         });
     }, false);

     // Search Content Api
     searchedOutput = ''
     $("#id_search").on('keyup', function () {
         let title = $(this).val();
         if (title.length >= 2) {
             dataDict = {
                 'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val(),
                 'title': title
             }
             $.ajax({
                 type: 'GET',
                 url: '/api/get_search_content',
                 data: dataDict,
                 success: function (data) {
                     if (data.status == 1) {
                         data.movieobjs.forEach(CreateSearchedOutputMovie)
                         data.seriseobjs.forEach(CreateSearchedOutputSeries)
                         data.softgameobjs.forEach(CreateSearchedOutputSoftsGames)
                         $('.searched-content > ul').html(searchedOutput)
                         searchedOutput = ''
                     } else {
                         $('.searched-content > ul').html(
                             `<li><a style='justify-content: center'>No Content Found !!!</a></li>`
                         )
                     }
                     if ($('.searched-content li').css('opacity')) {
                         $('body').css('overflow', 'hidden')
                     } else {
                         $('body').css('overflow', 'visible')
                     }
                     $(".searched-content li").delay(50).each(function (
                         i) {
                         $(this).delay(50 * i).queue(function () {
                             $(this).addClass("show");
                         })
                     })
                 }
             });
         } else {
             $('body').css('overflow', 'visible')
             $('.searched-content > ul').html('')
         }
     });
 });