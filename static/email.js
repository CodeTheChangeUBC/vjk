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
  })

  $("#selectAllContacts").on("click", function() {
    var checkedStatus = this.checked;
    $('#contacts-div').find('td:first :checkbox').each(function() {
      $(this).prop('checked', checkedStatus);
    });
  })
  $("#selectAllStudents").on("click", function() {
    var checkedStatus = this.checked;
    $('#students-div').find('td:first :checkbox').each(function() {
      $(this).prop('checked', checkedStatus);
    });
  })
  $("#selectAllVoluteers").on("click", function() {
    var checkedStatus = this.checked;
    $('#volunteers-div').find('input:checkbox[name=]').each(function() {
      $(this).prop('checked', checkedStatus);
    });
  })
});

function copyToClipboard(text) {
    window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
}
