$(document).ready(function(){
  $(".logo2").animate({opacity: '1'},1500);

});

$(document).ready(function(){
  $(".nav-link").hover(function(){
    $(this).css("color","#7EF9FF");
    $(this).css("text-shadow","0 0 5px #7EF9FF, 0 0 10px #7EF9FF, 0 0 15px #7EF9FF, 0 0 20px #7EF9FF, 0 0 30px #7EF9FF, 0 0 40px #7EF9FF, 0 0 55px #7EF9FF, 0 0 75px #7EF9FF, -5px 1px 18px #7EF9FF, -5px 1px 18px #7EF9FF");
  },
  function(){
    $(this).css("color","#7EF9FF");
    $(this).css("text-shadow","none");
  });
  $(".login").hover(function(){
    $(this).css("background-color","#7EF9FF");
  },
  function(){
    $(this).css("background-color","#141517");
  });


  $(".sedan").hover(function(){
    $(this).animate({padding: '270px'});
  },
  function(){
    $(this).animate({padding: '250px'});
  });

  $(".van").hover(function(){
    $(this).animate({padding: '270px'});
  },
  function(){
    $(this).animate({padding: '250px'});
  });

  $(".suv").hover(function(){
    $(this).animate({padding: '270px'});
  },
  function(){
    $(this).animate({padding: '250px'});
  });

  $("#name1").hover(function(){
    $("#name1img").animate({width: '175px',
  height: '175px'});
  },
  function(){
    $("#name1img").animate({width: '150px',
  height: '150px'});
  });

  $("#name2").hover(function(){
    $("#name2img").animate({width: '175px',
  height: '175px'});
  },
  function(){
    $("#name2img").animate({width: '150px',
  height: '150px'});
  });

  $("#name3").hover(function(){
    $("#name3img").animate({width: '175px',
  height: '175px'});
  },
  function(){
    $("#name3img").animate({width: '150px',
  height: '150px'});
});

  $("#name4").hover(function(){
    $("#name4img").animate({width: '175px',
  height: '175px'});
  },
  function(){
    $("#name4img").animate({width: '150px',
  height: '150px'});
  });
});
