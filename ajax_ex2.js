jQuery(function($){$('#btn3').click(function replace_table() {
//var $table_row = $('.table_row')
var state_filter = $('#state_select').val()
var $first_row = $('#first_row')
$('.table_row').remove();

$.ajax({
	type: 'GET',
	url: 'https://opendata.socrata.com/resource/a6x9-fw3a.json?state_name='+ state_filter,
	success: function(data) {$.each(data, function(i, item) {
		//$('.table_row').remove();
		$first_row.after('<tr class = "table_row"><td>' + item.measure_category +'</td><td>' + item._2010 +'</td><td>' + item._2011 + '</td><td>' + item._2012 + '</td><td>' + item._2013 + '</td><td>' + item._2014 + '</td></tr>' );
		})
	console.log(data);
	}
});
});
});

