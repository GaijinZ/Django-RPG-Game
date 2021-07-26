function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

function showItems(item, button, close) {
    let modal = document.querySelector(item);
    let trigger = document.querySelector(button);
    let closeButton = document.querySelector(close);

    function toggleModal() {
        modal.classList.toggle("show-items");
    }

    function windowOnClick(event) {
        if (event.target === modal) {
            toggleModal();
        }
    }

    trigger.addEventListener("click", toggleModal);
    closeButton.addEventListener("click", toggleModal);
    window.addEventListener("click", windowOnClick);
}

document.querySelector('#weapons').addEventListener('click', showItems('.weapon-items', '#weapons', '.close-weapon'));
document.querySelector('#armors').addEventListener('click', showItems('.armor-items', '#armors', '.close-armor'));
document.querySelector('#spells').addEventListener('click', showItems('.spell-items', '#spells', '.close-spell'));
document.querySelector('#potions').addEventListener('click', showItems('.potion-items', '#potions', '.close-potion'));
