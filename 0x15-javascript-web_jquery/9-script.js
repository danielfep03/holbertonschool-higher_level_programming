$(document).ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', ({ hello }) => {
    $('#hello').html(`${hello}`);
  });
});
