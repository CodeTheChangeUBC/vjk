$(document).ready(function() {
  $("#table").change(function() {
    var tbl = $("#table").val()+"-div";
    var tables = ["contacts-div","donors-div","sponsors-div","students-div","volunteers-div","contributions-div"]
    for (var i = 0; i < tables.length; i++) {
      var path = "."+tables[i];
      if (tables[i] == tbl) {
        $(path).show();
      } else {
        $(path).hide();
      }
    }
  })
})
