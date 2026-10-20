'use strict';
document.documentElement.classList.add('js');
const toggle=document.querySelector('.menu-toggle'),nav=document.getElementById('main-nav');
function closeNav(returnFocus=false){nav.classList.remove('is-open');toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Open navigation');if(returnFocus)toggle.focus({preventScroll:true});}
toggle?.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';nav.classList.toggle('is-open',open);toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Close navigation':'Open navigation');});
document.addEventListener('keydown',event=>{if(event.key==='Escape')closeNav(true)});
document.addEventListener('click',event=>{if(!event.target.closest('.site-header'))closeNav()});
const search=document.getElementById('style-search');
search?.addEventListener('input',()=>{const q=search.value.trim().toLowerCase();let count=0;document.querySelectorAll('[data-style]').forEach(el=>{el.hidden=!el.dataset.search.includes(q);if(!el.hidden)count++});document.querySelectorAll('.gallery-group').forEach(el=>el.hidden=![...el.querySelectorAll('[data-style]')].some(x=>!x.hidden));document.getElementById('filter-count').textContent=`${count} illustrated ${count===1?'study':'studies'}`;document.getElementById('empty-search').hidden=count>0;});
const panels=[...document.querySelectorAll('[data-panel]')],chapterLinks=[...document.querySelectorAll('[data-chapter]')];
function showChapter(){if(!panels.length)return;const requested=location.hash.slice(1),id=panels.some(p=>p.id===requested)?requested:'overview';panels.forEach(p=>p.hidden=p.id!==id);chapterLinks.forEach(a=>{if(a.dataset.chapter===id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')});}
showChapter();window.addEventListener('hashchange',()=>{showChapter();if(panels.length){const current=panels.find(p=>!p.hidden);current?.scrollIntoView({block:'start'});}});
const compare=document.getElementById('compare-neutral'),image=document.getElementById('specimen');
const originalAlt=image?.alt;
compare?.addEventListener('click',()=>{const neutral=compare.getAttribute('aria-pressed')!=='true';compare.setAttribute('aria-pressed',String(neutral));image.src=neutral?image.dataset.neutral:image.dataset.styled;image.alt=neutral?'Neutral version of the same study content':originalAlt;compare.textContent=neutral?`Show ${image.dataset.styleName}`:'Compare with neutral';document.getElementById('specimen-caption').textContent=neutral?'Neutral comparison: similar content with restrained styling.':'Original study illustration, not an archival screenshot.';});
document.querySelectorAll('[data-external-image]').forEach(img=>{function unavailable(){const message=document.createElement('p');message.className='archive-unavailable';message.textContent='The archive image could not load here. Open its archive record below to view the reference.';img.parentElement.replaceChild(message,img);}img.addEventListener('error',unavailable,{once:true});if(img.complete&&img.naturalWidth===0)unavailable();});
