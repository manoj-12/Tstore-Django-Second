// toggle:-

$(document).ready(function () {
  $(".cross").hide();
  // $(".nav-bar").css("display","none")
  $(".toggle").click(function () {
      // $(".nav-bar").show();
      $(".nav-bar").css("display", "block")
      $(this).hide();
      $(".cross").show();
  })

  $(".cross").click(function () {
      // $(".nav-bar").hide();
      $(".nav-bar").css("display", "none");
      $(this).hide();
      $(".toggle").show();
  })
})


$('.owl-carousel-1').owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  autoplay: true,
  autoplayTimeout: 1500,
  responsive: {
    0: {
      items: 1
    }
  }
})

// whatsNewCarousel start here:-

$('.whatsNewCarousel').owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  autoplay: true,
  autoplayTimeout: 1000,
  dots:false,
  responsive: {
    0: {
      items: 1
    },
    400: {
      items: 1.5
    },
    500: {
      items: 2
    },
    600: {
      items: 2.5
    },
    700: {
      items: 2
    },
    900: {
      items: 3
    },
    1000: {
      items: 4
    },
    1150: {
      items: 6
    }
  }
})

// whatsNewCarousel End here:-




// $('.offer-slider').owlCarousel({
//   loop: true,
//   margin: 50,
//   nav: false,
//   dots: false,
//   // autoplay: true,  
//   autoplayTimeout: 1000,
//   responsive: {
//     0:{
//       items:1
//   },
//   400:{
//     items:3
// },

//   600:{
//       items:3
//   },
//   1000:{
//       items:4
//   }
//   }
// })



















$('.owl-carousel-1').owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  // autoplay: true,
  autoplayTimeout: 1500,
  responsive: {
    0: {
      items: 1
    }
  }
})



$(document).ready(function(){
  $(".filter-icon").click(function(){
    $(".filter-section").toggle();
    // $(".main-bodyfilter").toggle();
  })
});


$(document).ready(function(){
  $(".short-icon").click(function(){
    $(".short-section-row").toggle();
  })
});