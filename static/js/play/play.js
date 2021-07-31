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

function attackMonster(attackType) {
    $.ajax({
        type: 'POST',
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        data: {
            action: attackType.attr('name'),
            id: attackType.attr('value'),
        },
        success: function(response) {
            if(response.status == 0){
                alert('You have died')
                window.location = response.url;
            }
            else{
                $(' #monster-health').html('Health: ' + response.monster_health);
                $(' #player-health').html('Health: ' + response.player_health);
                $(' #player-mana').html('Mana: ' + response.player_mana);
                $(' #player-exp').html('Experience: ' + response.player_exp);
                $(' #player-lvl').html('Level: ' + response.player_lvl);
                $(' #monster-name').html(response.monster_name);
                $(' #potion-amount').html(response.potion_amount + ' left');
                if(response.monster_health <= 0) {
                    alert('You have killed the monster');
                    location.reload();
                }
            }
        }
    });
};

$(document).ready(function() {
    $(".weapon").on('click', '#weapon-attack', function(e) {
        e.preventDefault();
        attackMonster($(this));
    });
    $(".use-spells").on('click', '#spell-attack', function(e) {
        e.preventDefault();
        attackMonster($(this));
    });
    $(".use-potions").on('click', '#use-potion-btn', function(e) {
        e.preventDefault();
        attackMonster($(this));
    });
});

function showAvailableItems(item, button, close) {
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

document.querySelector('#available-spells').addEventListener(
    'click', showAvailableItems('.use-spells', '#available-spells', '.close-spells'
));
document.querySelector('#available-potions').addEventListener(
    'click', showAvailableItems('.use-potions', '#available-potions', '.close-potions'
));
