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
});

function copyToClipboard(text) {
    window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
}
