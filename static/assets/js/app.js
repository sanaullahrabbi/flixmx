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