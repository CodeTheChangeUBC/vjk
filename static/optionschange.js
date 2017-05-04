$(document).ready(function(){
  $("#table").change(function() {
    var arr = [".contacts", ".donors", ".sponsors", ".students", ".volunteers"];
    var tbl = "." + $("#table").val();
    var options = [
    ["First Name", "Last Name", "Email", "Phone", "Donor", "Sponsor", "Student", "Volunteer"],
    ["Org Name", "Location", "Year donation", "Amount Donated", "Primary Contact ID", "Secondary Contact ID"],
    ["Name", "Service Provided"],
    ["First Name", "Last Name", "Email", "Location", "School", "Year Attended", "Ref. First Name", "Ref. Last Name", "Ref. Email"],
    ["First Name", "Last Name", "Email", "Phone", "Role", "Years Helped"]];
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
