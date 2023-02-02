function wait(ms){
    var start = new Date().getTime();
    var end = start;
    while(end < start + ms) {
      end = new Date().getTime();
    }
}
$(function() {
    wait(3000);
    $("#p1").html("Welcome to the Sandwich Maker Page");
});