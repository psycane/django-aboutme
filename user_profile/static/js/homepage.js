$(document).ready(function() {
	$(document).on('mouseenter', '#error_icon', function(e) {
		e.preventDefault();
		$(this).next().css('display', 'inline-block').stop(true, true).fadeIn(500);
	});
	$(document).on('mouseleave', '#error_icon', function(e) {
		e.preventDefault();
		$(this).next().stop(true, true).fadeOut(500);
	});
});
