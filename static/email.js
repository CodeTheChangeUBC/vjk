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
      $("#emailButton").attr("data-clipboard-text", str)

      copyToClipboard();
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

function copyToClipboard() {

    $('#emailButton').tooltip({
      trigger: 'click',
      placement: 'right'
    });

    var clipboard = new Clipboard('#emailButton')
    
    // Click the button
    $("#emailButton").trigger('click');

    clipboard.on('success', function(e) {
      setTooltip(e.trigger, 'Copied!');
      hideTooltip(e.trigger);
    });

    clipboard.on('error', function(e) {
      setTooltip(e.trigger, 'Failed!');
      hideTooltip(e.trigger);
    });
}

function setTooltip(btn, message) {
  $(btn).tooltip('hide')
    .attr('data-original-title', message)
    .tooltip('show');
}

function hideTooltip(btn) {
  setTimeout(function() {
    $(btn).tooltip('hide');
  }, 1000);
}
