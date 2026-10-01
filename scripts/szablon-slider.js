/* Slider z bloga: strzałki, pasek postępu, przeciąganie myszą */
(function(){
  var t=document.getElementById('bs-track');if(!t)return;
  var sec=t.closest('.bs'),prev=sec.querySelector('[data-dir="-1"]'),next=sec.querySelector('[data-dir="1"]'),bar=sec.querySelector('.bs-bar i');
  function step(){var li=t.querySelector('li');if(!li)return t.clientWidth;var gap=parseFloat(getComputedStyle(t).columnGap)||0;var per=Math.max(1,Math.floor((t.clientWidth+gap)/(li.offsetWidth+gap)));return per*(li.offsetWidth+gap)}
  function upd(){var max=t.scrollWidth-t.clientWidth,x=t.scrollLeft;prev.disabled=x<=4;next.disabled=x>=max-4;
    var w=Math.min(1,t.clientWidth/t.scrollWidth);bar.style.width=(w*100)+'%';bar.style.transform='translateX('+(max>0?(x/max)*(1/w-1)*100:0)+'%)';
    sec.querySelector('.bs-bar').style.visibility=max>4?'visible':'hidden'}
  [prev,next].forEach(function(b){b.addEventListener('click',function(){t.scrollBy({left:step()*+b.dataset.dir})})});
  t.addEventListener('scroll',upd,{passive:true});addEventListener('resize',upd);upd();
  /* przeciąganie myszą (na dotyku działa natywny swipe) */
  var down=false,sx=0,sl=0,moved=false;
  t.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse'||e.button!==0)return;down=true;moved=false;sx=e.clientX;sl=t.scrollLeft});
  addEventListener('pointermove',function(e){if(!down)return;var dx=e.clientX-sx;if(!moved&&Math.abs(dx)>6){moved=true;t.classList.add('is-drag')}if(moved)t.scrollLeft=sl-dx});
  addEventListener('pointerup',function(){if(!down)return;down=false;if(moved){var li=t.querySelector('li'),gap=parseFloat(getComputedStyle(t).columnGap)||0,u=li.offsetWidth+gap,target=Math.round(t.scrollLeft/u)*u;
    t.classList.remove('is-drag');t.scrollTo({left:target});setTimeout(function(){moved=false},0)}});
  t.addEventListener('click',function(e){if(moved){e.preventDefault();e.stopPropagation()}},true);
  t.addEventListener('dragstart',function(e){e.preventDefault()});
})();
