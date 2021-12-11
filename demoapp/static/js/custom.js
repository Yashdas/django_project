 /*(jQuery);*/
jQuery(document).ready(function() {
    // ORIGINAL DEFAULT HEADER
    if($('header.default').length){
      var lowheight = $('header.default').outerHeight();
      $(window).on('scroll', function(){
        if($(window).scrollTop() > 10 ) {
          $('header.default').addClass('smaller')
              .css('height', lowheight);
        }
        else {
          $('header.default').removeClass('smaller')
                              .css('height', 'auto');
        }
      });
    }
 });

     /*profile page shine;*/

jQuery(document).ready(function($){
  var timelineBlocks = $('.cd-timeline-block'),
    offset = 0.8;

  //hide timeline blocks which are outside the viewport
  hideBlocks(timelineBlocks, offset);

  //on scolling, show/animate timeline blocks when enter the viewport
  $(window).on('scroll', function(){
    (!window.requestAnimationFrame) 
      ? setTimeout(function(){ showBlocks(timelineBlocks, offset); }, 100)
      : window.requestAnimationFrame(function(){ showBlocks(timelineBlocks, offset); });
  });

  function hideBlocks(blocks, offset) {
    blocks.each(function(){
      ( $(this).offset().top > $(window).scrollTop()+$(window).height()*offset ) && $(this).find('.cd-timeline-images, .cd-timeline-content').addClass('is-hidden');
    });
  }

  function showBlocks(blocks, offset) {
    blocks.each(function(){
      ( $(this).offset().top <= $(window).scrollTop()+$(window).height()*offset && $(this).find('.cd-timeline-images').hasClass('is-hidden') ) && $(this).find('.cd-timeline-images, .cd-timeline-content').removeClass('is-hidden').addClass('bounce-in');
    });
  }
});        
 
   jQuery(document).ready(function() {

      jQuery('.fadeInUp').addClass("hideAnimate").viewportChecker({
      classToAdd: 'animated fadeInUp', // Class to add to the elements when they are visible
      offset: 100   

      });  
      jQuery('.bounceRight').addClass("hideAnimate").viewportChecker({
      classToAdd: 'animated bounceInRight', // Class to add to the elements when they are visible
      offset: 100    
    }
                                                                  );
    
    jQuery('.bounceLeft').addClass("hideAnimate").viewportChecker({
      classToAdd: 'animated bounceInLeft', // Class to add to the elements when they are visible
      offset: 100    
    }
                                                                 );
    
    jQuery('.fadeInUp').addClass("hideAnimate").viewportChecker({
      classToAdd: 'animated fadeInUp', // Class to add to the elements when they are visible
      offset: 100    
    }
                                                               );
    jQuery('.fadeInLeft').addClass("hideAnimate").viewportChecker({
    classToAdd: 'showAnimate animated fadeInLeft', // Class to add to the elements when they are visible
    offset: 100    
    });  

    jQuery('.fadeInRight').addClass("hideAnimate").viewportChecker({
    classToAdd: 'showAnimate animated fadeInRight', // Class to add to the elements when they are visible
    offset: 100    
    }); 
  
  });  

$(document).ready(function(){
  $("#Testimonials").owlCarousel({
        autoPlay: false,
        items :1,
        itemsDesktop      : [1024,1],
        itemsDesktopSmall: [979,1],
        itemsTablet      : [768,1],
        itemsMobile      : [479,1],

  });
  
 
   wow = new WOW(
                      {
                      boxClass:     'wow',      // default
                      animateClass: 'animated', // default
                      offset:       0,          // default
                      mobile:       true,       // default
                      live:         true        // default
                    }
                    )
     wow.init();
});

