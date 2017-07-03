$(document).ready(function(){
  $("#table").change(function() {
    var arr = [".contacts", ".donors", ".sponsors", ".students", ".volunteers", ".contributions"];
    var tbl = "." + $("#table").val();
    var options = [
    ["First Name", "Last Name", "E-mail", "Phone", "Address - Line 1", "Address - Line 2", "City", "Postal Code", "Province"],
    ["Organization Name", "Location", "Year Donated", "Amount Donated", "Primary Contact", "Secondary Contact"],
    ["Name", "Service Provided", "Primary Contact", "Secondary Contact"],
    ["First Name", "Last Name", "E-mail", "Phone", "Program City", "School", "Program Institution", "Year Attended", "Address - Line 1", "Address - Line 2", "City", "Province", "Postal Code", "Ref. First Name", "Ref. Last Name", "Ref. E-mail", "Ref. Addr - Line 1", "Ref. Addr - Line 2", "Ref. City", "Ref. Province"],
    ["First Name", "Last Name", "E-mail", "Phone", "Role", "Years Helped", "Address - Line 1", "Address - Line 2", "City", "Postal Code", "Province"],
    ["Year","Sponsor","Donor","Volunteer","Amount Contributed","Service Provided","Volunteer Hours"]];
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
