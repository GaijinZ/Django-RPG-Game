import { getCookie } from '../utils.js'
import { showItems } from '../utils.js'


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


document.querySelector('#weapons').addEventListener('click', showItems('.weapon-items', '#weapons', '.close-weapon'));
document.querySelector('#armors').addEventListener('click', showItems('.armor-items', '#armors', '.close-armor'));
document.querySelector('#spells').addEventListener('click', showItems('.spell-items', '#spells', '.close-spell'));
document.querySelector('#potions').addEventListener('click', showItems('.potion-items', '#potions', '.close-potion'));
