window.addEventListener('scroll',function(){document.getElementById('nav').classList.toggle('scrolled',window.scrollY>50)});
var h=document.getElementById('hamburger');if(h){h.addEventListener('click',function(){var n=document.getElementById('navLinks');n.style.display=n.style.display==='flex'?'none':'flex'});}
