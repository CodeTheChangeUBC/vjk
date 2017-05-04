$(document).ready(function(){
  $("#submit").on("click", function(){
    initiateSearch();
  })
  $("#input").on('keyup', function (e) {
    if (e.keyCode == 13) {
        initiateSearch();
    }
  });
  function initiateSearch() {
    var tbl = $("#table").val();
    var inpt = $("#input").val();
    var fild = $("#field").val();
    if (inpt != "") {
      if (fild=="all") {
        searchAll(tbl, inpt)
      } else {
        searchByFilter(tbl, inpt, fild)
      }
    } else {
      $("#"+tbl+" tr").each(function(){
        $(this).show();
      })
    }
  }
  function searchByFilter(table, input, field) {
    // 0 is a temporary number and should be replaced.
    var column_num;
    var index = 0;
    $("#"+table+" tr").each(function() {
      if (index == 0) {
        var lgth = $(this).find("th").length;
        for (var i=0; i<lgth;i++) {
          var column = $(this).find("th").eq(i).html();
          if (column == field) {
            column_num = i;
            break;
          }
        }
        index++;
      } else {
        var val = $(this).find("td").eq(column_num).html();
        console.log(val);
        console.log(input);
        if (val == input) {
          $(this).show();
        } else {
          $(this).hide();
        }
      }

    })
  }
  function searchAll(table, input) {
    var table = "#"+table;
    var index = 0;
    $(table+" tr").each(function() {
      if (index != 0) {
        var lgth = $(this).find("td").length;
        var bool = false;
        for (var i=1; i < lgth; i++) {
          var val = $(this).find("td").eq(i).html();
          if (val == input) { bool = true; }
        }
        if (bool) { $(this).show(); }
        else { $(this).hide(); }
      }
      index++;
    })
  }
});
