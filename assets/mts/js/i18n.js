(function() {
    'use strict';

    var lang = localStorage.getItem('mts-lang') || 'en';
    var translations = {};

    function tr(key) {
        if (translations[key] !== undefined) return translations[key];
        return key.split('.').reduce(function(o, p) { return o && o[p] !== undefined ? o[p] : undefined; }, translations);
    }

    function loadTranslations(callback) {
        try {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', 'lang/' + lang + '.json', false);
            xhr.send();
            if (xhr.status === 200) {
                translations = JSON.parse(xhr.responseText);
            }
        } catch(e) {
            console.error('i18n load error', e);
        }
        if (callback) callback();
    }

    function applyTranslations() {
        document.documentElement.lang = lang;

        document.querySelectorAll('[data-i18n]').forEach(function(el) {
            var key = el.getAttribute('data-i18n');
            var val = tr(key);
            if (!val) return;

            if (el.classList.contains('rts-text-anime-style-1')) {
                var textSpan = el.querySelector('span:not(:has(img))');
                if (textSpan && !el.querySelector('img')) {
                    el.innerHTML = '<span>' + val + '</span>';
                } else if (textSpan) {
                    textSpan.textContent = val;
                } else {
                    var firstChild = el.firstChild;
                    if (firstChild && firstChild.nodeType === 3) {
                        firstChild.textContent = val;
                    } else {
                        el.textContent = val;
                    }
                }
            } else {
                el.innerHTML = val;
            }
        });

        document.querySelectorAll('[data-i18n-placeholder]').forEach(function(el) {
            var key = el.getAttribute('data-i18n-placeholder');
            var val = tr(key);
            if (val) {
                el.placeholder = val;
            }
        });

        document.querySelectorAll('[data-i18n-alt]').forEach(function(el) {
            var key = el.getAttribute('data-i18n-alt');
            var val = tr(key);
            if (val) {
                el.alt = val;
            }
        });

        document.querySelectorAll('meta[data-i18n]').forEach(function(el) {
            var key = el.getAttribute('data-i18n');
            var val = tr(key);
            if (val) {
                el.setAttribute('content', val);
            }
        });

        var metaTitle = tr('meta.title');
        if (metaTitle) {
            document.title = metaTitle;
        }

        if (window.updateMapPopups) {
            window.updateMapPopups(translations, tr);
        }

        document.querySelectorAll('.lang-switcher .lang-btn').forEach(function(btn) {
            btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
        });
    }

    function reSplitAnimatedHeadings() {
        if (typeof SplitText === 'undefined') return;
        document.querySelectorAll('.rts-text-anime-style-1[data-i18n]').forEach(function(el) {
            if (el.split) {
                el.split.revert();
            }
            el.split = new SplitText(el, {
                type: 'lines,words,chars',
                linesClass: 'split-line'
            });
            if (el.animation) {
                el.animation.progress(1).kill();
            }
            gsap.set(el, { perspective: 400 });
            gsap.set(el.split.chars, { opacity: 0, x: '50' });
            el.animation = gsap.to(el.split.chars, {
                scrollTrigger: { trigger: el, start: 'top 95%' },
                x: '0', y: '0', rotateX: '0', opacity: 1,
                duration: 1, ease: Back.easeOut, stagger: 0.02
            });
        });
    }

    window.MTS = {
        lang: lang,
        t: function(key) { return tr(key) || key; },
        switchLang: function(newLang) {
            lang = newLang;
            localStorage.setItem('mts-lang', newLang);
            loadTranslations(function() {
                applyTranslations();
                reSplitAnimatedHeadings();
            });
        },
        init: function() {
            loadTranslations(applyTranslations);
        }
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() { MTS.init(); });
    } else {
        MTS.init();
    }
})();
