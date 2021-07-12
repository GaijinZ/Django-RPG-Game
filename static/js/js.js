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

function attackMonster(attack_type) {
    $.ajax({
        type: 'POST',
        headers: {"X-CSRFToken": getCookie("csrftoken")},
        data: {
            action: attack_type.attr('name'),
            id: attack_type.attr('value'),
        },
        success: function(response) {
            if(response.status == 0){
                alert('You have died')
                window.location = response.url;
            }
            else{
                $(' #monster-id').html('ID: ' + response.monster_id);
                $(' #monster-health').html('Health: ' + response.monster_health);
                $(' #player-health').html('Health: ' + response.player_health);
                $(' #player-mana').html('Mana: ' + response.player_mana);
                $(' #player-exp').html('Experience: ' + response.player_exp);
                $(' #player-lvl').html('Level: ' + response.player_lvl);
                $(' #monster-type').html(response.monster_type);
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
    $(".spells").on('click', '#spell-attack', function(e) {
        e.preventDefault();
        attackMonster($(this));
    });
});


const modal = document.querySelector(".spells");
const trigger = document.querySelector("#trigger");
const closeButton = document.querySelector(".close-button");

function toggleModal() {
    modal.classList.toggle("show-spells");
}

function windowOnClick(event) {
    if (event.target === modal) {
        toggleModal();
    }
}

trigger.addEventListener("click", toggleModal);
closeButton.addEventListener("click", toggleModal);
window.addEventListener("click", windowOnClick);
