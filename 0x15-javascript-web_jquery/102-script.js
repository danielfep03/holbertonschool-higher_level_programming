const apiUrl = 'https://www.fourtonfish.com/hellosalut/';

$(document).ready(function () {
  $('#btn_translate').click(() => {
    const lang = $('#language_code').val();
    const url = apiUrl + '?lang=' + lang;

    $.get(url, ({ hello }) => $('#hello').html(hello));
  });
});
