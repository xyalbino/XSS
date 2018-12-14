
   var defaultMessage = "Welcome!<br><br>This is your <i>personal</i>"
        + " stream. You can post anything you want here, especially "
        + "<span style='color: #f00ba7'>madness</span>.";

      var DB = new PostDB(defaultMessage);
       function escapeHTML (unsafe_str) {
    return unsafe_str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/\"/g, '&quot;')
      .replace(/\'/g, '&#39;')
      .replace(/\//g, '&#x2F;')
}


      function displayPosts() {
        var containerEl = document.getElementById("post-container");
        containerEl.innerHTML = "";

        var posts = DB.getPosts();
        //console.log(posts);


        for (var i=0; i<posts.length; i++) {
          var html = '<table class="message"> <tr> <td valign=top> '
            + '<img src="/static/level2_icon.png"> </td> <td valign=top '
            + ' class="message-container"> <div class="shim"></div>';

          html += '<b>You</b>';
          html += '<span class="date">' + new Date(posts[i].date) + '</span>';
          html += "<blockquote>" + posts[i].message + "</blockquote>";
          html += "</td></tr></table>";
          containerEl.innerHTML += html;
           /* var tb = document.createElement('table');
            tb.class = "message";
            var tr = document.createElement('tr');
            var td1 = document.createElement('td');
            td1.valign = "top";
            var img = document.createElement('img');
            img.src = "/static/level2_icon.png";
            td1.appendChild(img);
            tr.appendChild(td1);
            var td2 = document.createElement('td');
            td2.valign = "top";
            td2.class = "message-container";
            var div = document.createElement('div');
            div.class = "shim";
            td2.appendChild(div);
            var b = document.createElement('b');
            b.textContent = "You";
            td2.appendChild(b);
            var span = document.createElement('span');
            span.class = "date";
            span.textContent = new Date(posts[i].date);
            td2.appendChild(span);
            var bl = document.createElement('blockquote');
            if(i==0){
                var str = 'personal'
                str.italics();
                bl.value = "Welcome!/nThis is your" +str
        + " stream. You can post anything you want here, especially madness."
            }
            bl.textContent = posts[i].message;
            td2.appendChild(bl);
            tr.appendChild(td2);
            tb.appendChild(tr);
            containerEl.appendChild(tb);*/
        }
      }

      window.onload = function() {
        document.getElementById('clear-form').onsubmit = function() {
          DB.clear(function() { displayPosts() });
          return false;
        }

        document.getElementById('post-form').onsubmit = function() {
          var message = document.getElementById('post-content').value;
           message = escapeHTML(message);
          DB.save(message, function() { displayPosts() } );
          document.getElementById('post-content').value = "";
          return false;
        }

        displayPosts();
      }