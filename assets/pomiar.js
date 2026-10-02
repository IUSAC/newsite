/* Pomiar zdarzeń kontaktu (PKW Adwokaci). Zbiera: klik telefon, e-mail, WhatsApp, wysłanie formularza.
   Zdarzenia trafiają do window.dataLayer (Google Tag Manager / GA4) i do gtag(), jeśli jest załadowany.
   Bez identyfikatora GA4 nic nie wychodzi na zewnątrz – podpięcie to jeden tag w <head>. */
(function(){
  window.dataLayer=window.dataLayer||[];
  function send(name,params){
    var p=Object.assign({event:name,page:location.pathname},params||{});
    window.dataLayer.push(p);
    if(typeof window.gtag==='function'){window.gtag('event',name,params||{})}
  }
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;
    var h=a.getAttribute('href')||'',where=a.closest('.mbar')?'pasek':(a.closest('footer')?'stopka':(a.closest('#kontakt')?'kontakt':'tresc'));
    if(h.indexOf('tel:')===0)send('kontakt_telefon',{miejsce:where,numer:h.slice(4)});
    else if(h.indexOf('mailto:')===0)send('kontakt_email',{miejsce:where});
    else if(h.indexOf('wa.me')>-1||h.indexOf('whatsapp')>-1)send('kontakt_whatsapp',{miejsce:where});
  },{passive:true});
  document.addEventListener('submit',function(e){
    var f=e.target;if(!f||f.tagName!=='FORM')return;
    send('formularz_wyslany',{formularz:f.id||'bez-id'});
  },true);
  window.pkwPomiar=send;
})();
