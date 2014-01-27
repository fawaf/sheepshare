$(document).ready(function() {
	var change = false;

	$("#test").click(function() {
		change = ! change;
		if (change == true) {
			$("#container").css("background-color", "pink");
		} else {
			$("#container").css("background-color", "#E8C387");
		}
	});
	$("#addFile").click(function() {
		$("<p><input type=\"file\" name=\"file\" /></p>").appendTo($("#files"));
	});
});
