$(document).ready(function(event){
  event.preventDefault ? event.preventDefault() : (event.returnValue = false);
  $(".myTransactions").click(function(){
    $(".userTransaction").css("display","inline");
    $(".userProfile").css("display","none");
    $(".editProfile").css("display","none");
    $(".changePassword").css("display","none");
  });
  $(".profileEdit").click(function(){
    $(".editProfile").css("display","inline");
    $(".userTransaction").css("display","none");
    $(".userProfile").css("display","none");
    $(".changePassword").css("display","none");
  });
  $(".passwordChange").click(function(){
    $(".editProfile").css("display","none");
    $(".userTransaction").css("display","none");
    $(".userProfile").css("display","none");
    $(".changePassword").css("display","inline");
  });
  $(".myProfile").click(function(){
    $(".editProfile").css("display","none");
    $(".userTransaction").css("display","none");
    $(".userProfile").css("display","inline");
    $(".changePassword").css("display","none");
  });

});
