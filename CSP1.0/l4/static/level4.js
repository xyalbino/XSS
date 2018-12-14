function startTimer(seconds) {
        seconds = parseInt(seconds) || 3;
        setTimeout(function() {
          window.confirm("Time is up!");
          window.history.back();
        }, seconds * 1000);
      }
      function GetQueryString(name){
    var reg = new RegExp("(^|&)"+ name +"=([^&]*)(&|$)");
    var r = window.location.search.substr(1).match(reg);
           if(r!=null)return  unescape(r[2]); return null;}

      document.getElementById('gif').addEventListener('load',startTimer(GetQueryString('timer')));