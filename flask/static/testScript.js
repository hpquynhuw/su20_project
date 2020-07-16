function myFunction() {
  $.ajax({
         method: 'GET',
         url: '/home',
         });
  document.getElementById('list').innerHTML = "";
  document.getElementById('list').innerHTML = Date();

}

function ajaxCall() {
  $.ajax({
        method: 'GET',
        url: '/seattle',
        });
}
