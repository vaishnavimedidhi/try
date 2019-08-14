DisableScrolling();
$('#our-mission div.container div.row').hide();

//////////////////////// DOCUMENT READY

$(document).ready(function () {
	
	$('#spotlight').show('fade', 2000, function () {
		ReinstateScrolling();
	});
	
	window.addEventListener('scroll', function(event) {
		
		let top = ($(window).scrollTop() || $("body").scrollTop());
		console.log(top);
		
		if (top >= 200)
		{
			$('#our-mission div.container div.row').fadeIn('slow');
		}
		
	});
	
});

//////////////////////// FUNCTIONS

function ReinstateScrolling()
{
	window.removeEventListener('scroll', NoScroll);
}

function DisableScrolling()
{
	window.addEventListener('scroll', NoScroll);
}

function NoScroll()
{
  window.scrollTo( 0, 0 );
}