$(document).ready(function () {
  $("#delete").on("click", function() {
    var tags = []
    $("input:checkbox[name=deletebox]:checked").each(function(){
        tags.push($(this).val());
    });
    for (var i = 0; i < tags.length; i++) {
      console.log(tags[i]);
    }
  })
})
