$(document).ready(function(){
  clipboard = new Clipboard('.btn')

  $("#download").on("click", function() {
      var arr = [];
      // Get checked email
      $("input:checkbox[name=checks]:checked").each(function(){
          arr.push($(this).val());
      });
      // Unique list of emails
      arr = jQuery.unique(arr);
      // Array to String
      var str = arr.toString();
      copyToClipboard(str);
  });
  var everythingStatus = false;
  $("#selectEverything").on("click", function() {
    everythingStatus = !everythingStatus;
    $(".checkboxContact").each(function() {
      $(this).prop("checked", everythingStatus);
    });
    $(".checkboxStudent").each(function() {
      $(this).prop("checked", everythingStatus);
    });
    $(".checkboxVolunteer").each(function() {
      $(this).prop("checked", everythingStatus);
    });
  })
  $("#selectAllContacts").on("click", function() {
    toggle(this);
  });
  $("#selectAllStudents").on("click", function() {
    toggle(this);
  });
  $("#selectAllVolunteers").on("click", function() {
    toggle(this);
  });
  function toggle(source) {
    var sourceStatus = source.checked;
    var sourceID = source.id;
    if (sourceID == "selectAllContacts") {
      $(".checkboxContact").each(function() {
        var row = "#"+this.id + "Row";
        if ( $(row).is(':visible') ) {
          $(this).prop("checked", sourceStatus);
        } else {
          $(this).prop("checked", false);
        }
      });
    } else if (sourceID == "selectAllStudents") {
      $(".checkboxStudent").each(function() {
        var row = "#" + this.id + "Row";
        if ( $(row).is(':visible') ) {
          $(this).prop("checked", sourceStatus);
        } else {
          $(this).prop("checked", false);
        }
      });
    } else if (sourceID == "selectAllVolunteers") {
      $(".checkboxVolunteer").each(function() {
        var row = "#" + this.id + "Row";
        if ( $(row).is(':visible') ) {
          $(this).prop("checked", sourceStatus);
        } else {
          $(this).prop("checked", false);
        }
      });
    } else {
      console.log("How did it get here?? You are a magician, Harry!");
    }
  }

});

function copyToClipboard(text) {
    window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
}
