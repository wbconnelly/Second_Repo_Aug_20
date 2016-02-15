jQuery(function($){$('#btn4').click( function initMap() {
  var state_filter_fac = $('#state_fac_select').val()
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: new google.maps.LatLng(39.8524, -93.80046)
  });

 //var state_filter = 'New York';
  $('.table_row_fac').remove();
$.ajax({
	type: 'GET',
	url: 'https://opendata.socrata.com/resource/mv3y-eras.json?state_name='+ state_filter_fac,
	success: function(data) {$.each(data, function(i, item) {
		 var marker = new google.maps.Marker({
							position: new google.maps.LatLng(item.location_1.latitude, item.location_1.longitude),
							map: map});
							
				$('#first_facility_row').after('<tr class = "table_row_fac"><td>' + item.facility +'</td><td>' + item.city_name +'</td><td>' + item.measure_category +'</td><td>' + item._2010 +'</td><td>' + item._2011 + '</td><td>' + item._2012 + '</td><td>' + item._2013 + '</td><td>' + item._2014 + '</td></tr>' );
		
				   var info_window = new google.maps.InfoWindow({
					content: '<div>Facility:' + item.facility +'</div>' +
						'<div> City:' +item.city_name +'</div>'
				});
            google.maps.event.addListener(marker, 'click', function() {
              info_window.open(map, marker);
            });
		});
	console.log(data);
	}
});
}  );});








