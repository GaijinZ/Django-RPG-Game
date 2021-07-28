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

function shop(itemToBuy) {
    $.ajax({
        type: 'POST',
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        data: {
            action: itemToBuy.attr('name'),
            id: itemToBuy.attr('value'),
        },
        success: function(response) {
            alert('You have purchased the ' + response.name)
            location.reload();
        }
    });
}

$(document).ready(function() {
    $(".weapon-items").on('click', '#buy_weapon', function(e) {
        e.preventDefault();
        shop($(this));
    });
    $(".armor-items").on('click', '#buy_armor', function(e) {
        e.preventDefault();
        shop($(this));
    });
    $(".spell-items").on('click', '#buy_spell', function(e) {
        e.preventDefault();
        shop($(this));
    });
    $(".potion-items").on('click', '#buy_potion', function(e) {
        e.preventDefault();
        shop($(this));
    });
});

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
