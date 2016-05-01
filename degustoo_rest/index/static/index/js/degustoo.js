//$.noConflict();

$(document).ready(function(){
    ///////////////////////////////////////////////////////////
    /**
     * Event Listeners
     */

    $('#is_sub').change(function(){
        changeSubmenuValue();
    });

    $('#addItemButton').click(function(){
        //alert($('#addItemForm').html());
        $('#addItemForm').append('<input class="form-control">Vai Nessa Filho</input>')
    });

    /**
     * Functions
     */

    var is_sub = document.getElementById('is_sub');
    if(is_sub){
        function changeSubmenuValue(){
            if(is_sub.checked){
                $('#sub_card').attr('disabled', false);
            }else{
                $('#sub_card').attr('disabled', true);
            }
        }
        changeSubmenuValue();
    }

    /**
     * calling functions
     */

    ///////////////////////////////////////////////////////////

    ///////////////////////////////////////////////////////////

    $('.deg-menu > ul').children().first().css('border-radius', '5px 0 0 0');
    $('.deg-menu > ul').children().last().css('border-radius', '0 0 0 5px');

    $('.deg-menu li').hover(
        function(){
            $(this).css('background-color', '#505050');
            $(this).css('transform', 'scale(1.02)');
            /*$(this).css('background-color', '#990000');*/
            /*$(this).css('color', '#FFE275');*/
        },
        function(){
            $(this).css('background-color', '#3E3E3E');
            $(this).css('transform', 'scale(1.0)');
            /*$(this).css('color', '#FF7600');*/
        }
    );

    $('.deg-li-parent').hover(
        function(){
            $(this).children().slideDown();
        },
        function(){
            $(this).children().slideUp();
        }
    );

    $('.deg-index-menu-li-parent').hover(
        function(){
            $(this).children().slideDown();
        },
        function(){
            $(this).children().slideUp();
        }
    );

    /*$('#add-item').click(function(){
        $(this).preventDefault();
        $.post('/restaurante/cardapios/itens/novo-item', function(json){
            alert(json.mensagem);
        }, "json");
    });*/

    $('#item-form').submit(function(event){
        event.preventDefault();
        $.post($(this).attr('action'), $(this).serialize(), function(json){
            alert(json.mensagem);
        }, "json");
    });

    /**/
});

