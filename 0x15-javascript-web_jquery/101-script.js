const item = '<li>Item</li>';
$(document).ready(function () {
  $('#add_item').click(() => $('.my_list').append(item));
  $('#remove_item').click(() => $('.my_list').children().last().remove());
  $('#clear_list').click(() => $('.my_list').children().remove());
});
