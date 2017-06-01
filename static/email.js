$(document).ready(function(){
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
        $(this).prop("checked", sourceStatus);
      });
    } else if (sourceID == "selectAllStudents") {
      $(".checkboxStudent").each(function() {
        $(this).prop("checked", sourceStatus);
      });
    } else if (sourceID == "selectAllVolunteers") {
      $(".checkboxVolunteer").each(function() {
        $(this).prop("checked", sourceStatus);
      });
    } else {

    }
  }

});

function copyToClipboard(text) {
    window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
}
