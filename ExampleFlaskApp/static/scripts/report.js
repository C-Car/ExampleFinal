var initial_amount = {
    "ham": 14,
    "bread": 18,
    "cheese": 24
  };
$(document).ready(function() {
    // report button click event handler
    $(".reportbtn").click(function() {
      // send an AJAX request to the server to get the sandwich resources information
      $.ajax({
        url: "/resource",
        type: "GET",
        dataType: "json",
        success: function(data) {
          // initialize a string variable to hold the resource information
          var resourcesInfo = "";
          // loop through each resource object in the data list
          for (var i = 0; i < data.length; i++) {
            // extract the "item" and "amount" properties from the resource object
            var item = data[i].item;
            var amount = data[i].amount;
            // append the resource information to the string variable
            resourcesInfo += item + ": " + amount + ", ";
          }
          // update the messages area with the sandwich resources information
          $("#p1").text(resourcesInfo);
        },
        error: function(jqXHR, textStatus, errorThrown) {
          console.log(textStatus, errorThrown);
        }
      });
    });
    $(".smallbtn").click(function() {
        // send an AJAX request to the server to make a medium sandwich
        $.ajax({
            url: "/makesmall",
            type: "POST",
            dataType: "json",
            success: function(data) {
              // update the messages area with the success message
              $("#p1").text(data.message);
            },
            error: function(jqXHR, textStatus, errorThrown) {
              console.log(textStatus, errorThrown);
            }
          });
        });
    $(".mediumbtn").click(function() {
        // send an AJAX request to the server to make a medium sandwich
        $.ajax({
          url: "/makemedium",
          type: "POST",
          dataType: "json",
          success: function(data) {
            // update the messages area with the success message
            $("#p1").text(data.message);
          },
          error: function(jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
          }
        });
      });
      $(".largebtn").click(function() {
        // send an AJAX request to the server to make a medium sandwich
        $.ajax({
          url: "/makelarge",
          type: "POST",
          dataType: "json",
          success: function(data) {
            // update the messages area with the success message
            $("#p1").text(data.message);
          },
          error: function(jqXHR, textStatus, errorThrown) {
            console.log(textStatus, errorThrown);
          }
        });
      });
      $(".offbtn").click(function() {
        // send an AJAX request to the server to reset the sandwich resources to their initial values
        $.ajax({
            url: "/reset",
            type: "POST",
            dataType: "json",
            success: function(data) {
              // display a success message in the messages area
              $("#p1").text("Resources reset!");
            },
            error: function(jqXHR, textStatus, errorThrown) {
              console.log(textStatus, errorThrown);
            }
          });
        });
});

  