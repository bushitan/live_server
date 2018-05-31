//tinyMCE.init({
//    mode : "textareas",
//    theme : "modern",
// plugins: [
// "advlist autolink lists link image charmap print preview hr anchor pagebreak",
// "searchreplace wordcount visualblocks visualchars code fullscreen",
// "insertdatetime media nonbreaking save table contextmenu directionality",
// "emoticons template paste textcolor"
// ],
// toolbar1: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image",
// toolbar2: "print preview media | forecolor backcolor emoticons",
// image_advtab: true,
// //visualblocks_default_state: true,
//    width: '700',
//    height: '400',
//    language:'zh_CN'
//});


tinyMCE.init({
    selector: 'textarea',
    theme : "modern",
    plugins: ["image"],
    image_advtab: true,
    paste_data_images:true,
    width: '700',
    height: '800',
    file_browser_callback: function(field_name, url, type, win) {
        if(type=='image'){
            $('#my_form input').click();
        }
    },
});
$( document ).ready(function() {
    h ='<iframe id="form_target" name="form_target" style="display:none"></iframe><form id="my_form" action="/live/xx_mgr/upload/image/" target="form_target" method="post" enctype="multipart/form-data" style="width:0px;height:0;overflow:hidden"><input name="img" type="file" onchange="$(\'#my_form\').submit();this.value=\'\';"></form>';

    $('body').append(h);
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
            }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    console.log(csrftoken);
    $('#my_form').append('<input type="hidden" name="csrfmiddlewaretoken" value='+csrftoken+' />');
});

// tinymce.init({
//        selector: "textarea",
//        plugins: [
//            "advlist autolink autosave link image lists charmap print preview hr anchor pagebreak spellchecker",
//            "searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking",
//            "table contextmenu directionality emoticons template textcolor paste fullpage textcolor"
//        ],
//
//        toolbar1: "undo redo | cut copy paste | bold italic underline strikethrough | alignleft aligncenter alignright alignjustify | styleselect formatselect fontselect fontsizeselect",
//        toolbar2: " searchreplace | bullist numlist | outdent indent blockquote | link unlink anchor image media code | inserttime preview | forecolor backcolor",
//        toolbar3: "table | hr removeformat | subscript superscript | charmap emoticons | print fullscreen | ltr rtl | spellchecker | visualchars visualblocks nonbreaking template pagebreak restoredraft",
//
//        menubar: false,
//        toolbar_items_size: 'small',
//
//        style_formats: [
//            {title: 'Bold text', inline: 'b'},
//            {title: 'Red text', inline: 'span', styles: {color: '#ff0000'}},
//            {title: 'Red header', block: 'h1', styles: {color: '#ff0000'}},
//            {title: 'Example 1', inline: 'span', classes: 'example1'},
//            {title: 'Example 2', inline: 'span', classes: 'example2'},
//            {title: 'Table styles'},
//            {title: 'Table row 1', selector: 'tr', classes: 'tablerow1'}
//        ],
//
//        templates: [
//            {title: 'Test template 1', content: 'Test 1'},
//            {title: 'Test template 2', content: 'Test 2'}
//        ],
//        language:'zh_CN'
//    });