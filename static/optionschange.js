$(document).ready(function(){
  $("#table").change(function() {
    var arr = [".contacts", ".donors", ".sponsors", ".students", ".volunteers"];
    var tbl = "." + $("#table").val();
    var options = [
    ["First Name", "Last Name", "Email", "Phone", "Address Line 1", "Address Line 2", "City", "Postal Code", "Province"],
    ["Org Name", "Location", "Year Donated", "Amount Donated", "Primary Contact ID", "Secondary Contact ID"],
    ["Name", "Service Provided", "Primary Contact ID", "Secondary Contact ID"],
    ["First Name", "Last Name", "Email", "Phone Number", "Program City", "School", "Program Institution", "Year Attended", "Address Line 1", "Address Line 2", "City", "Province", "Postal Code", "Ref. First Name", "Ref. Last Name", "Ref. Email", "Ref. Address Line 1", "Ref. Address Line 2", "Ref. City", "Ref. Province"],
    ["First Name", "Last Name", "Email", "Phone", "Role", "Years Helped", "Address Line 1", "Address Line 2", "City", "Postal Code", "Province"]];
    for (var i = 0; i < arr.length; i++) {
      if (tbl == arr[i]) {
        $("#field").empty();
        $("#field").append($("<option></option>").attr("value", "all").text("Anything"));
        for (var j=0; j<options[i].length;j++) {
          $("#field").append($("<option></option>").attr("value", options[i][j]).text(options[i][j]));
        }
      }
    }

  })

})
