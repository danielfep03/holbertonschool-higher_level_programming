const apiUrl = 'https://www.fourtonfish.com/hellosalut/';
const translate = ({ charCode }) => {
  const lang = $('#language_code').val();
  const url = apiUrl + '?lang=' + lang;
  if (!charCode || charCode === 13)
    $.get(url, ({ hello }) => $('#hello').html(hello));
};

$(document).ready(function () {
  $('#btn_translate').click(translate);
  $('#language_code').keypress(translate);
});
