$(document).ready(function(){
  $("#table").change(function() {
    var arr = [".contacts", ".donors", ".sponsors", ".students", ".volunteers"];
    var tbl = "." + $("#table").val();
    var options =
    [{
      "First Name": "first_name",
      "Last Name": "last_name",
      "Email":"email",
      "Phone":"phone",
      "Donor":"donor",
      "Sponsor":"sponsor",
      "Student":"student",
      "Volunteer":"volunteer"
    },
    {
      "Org Name":"org_name",
      "Location":"location",
      "Year donation":"year_donation",
      "Amount Donated":"amount_donation",
      "Primary Contact ID":"primary_contact_id",
      "secondary Contact ID":"secondary_contact_id"
    },
    {
      "Name": "name",
      "Service Provided": "service_provided"
    },
    {
      "First Name": "first_name",
      "Last Name": "last_name",
      "Email": "email",
      "Location": "location",
      "School": "year_attended",
      "Ref. First Name": "reference_fname",
      "Ref. Last Name": "reference_lname",
      "Ref. Email": "reference_email"
    },
    {
      "First Name": "first_name",
      "Last Name": "last_name",
      "Email": "email",
      "Phone": "phone",
      "Role": "role",
      "Years Helped": "years_helped"
    }];
    for (var i = 0; i < arr.length; i++) {
      if (tbl == arr[i]) {
        $("#field").empty();
        $("#field").append($("<option></option>").attr("value", "all").text("Anything"));
        var keys = Object.keys(options[i]);
        var vals = Object.values(options[i]);
        $.each(options, function(key,value) {
        $("#field").append($("<option></option>")
           .attr("id", keys[key]).text(keys[key]));
         });
      }
    }

  })

})
