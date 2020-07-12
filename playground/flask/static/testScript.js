function myFunction() {
  document.getElementById('demo').innerHTML = Date();
  $.ajax({
    type: 'GET',
    url:'/data/',
    success: function (response) {
      console.log(response);
    }
  })
}
