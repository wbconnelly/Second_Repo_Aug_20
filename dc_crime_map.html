<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">

 <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.5/leaflet.css" />
 <script src="https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.5/leaflet.js"></script>
<script src="https://maps.googleapis.com/maps/api/js"></script>
<script src="dc_crime2.geojson" type="text/javascript"></script>
<script src="us_states.geojson" type="text/javascript"></script>
<script src="http://matchingnotes.com/javascripts/leaflet-google.js"></script>

<style> #mapid { height: 500px; }
input[type=select], select{
    width: 25%;
	height: 38px;
	margin-top: 1%;
    border: 1px solid #ccc;
    border-radius: 2px;}</style>
</head>
<body>
<div id="mapid" class = "col-md-10 col-md-offset-1" style="border: solid darkgrey; border-radius: 10px; margin-top: 30px; height: 750px"></div>
<select id= "crime_category" class ="col-md-10 col-md-offset-1" style="border: solid darkgrey; border-radius: 10px; margin-bottom: 50px;">
    <option value ="MOTO_TH_15">MOTOR VEHICLE THEFT</option>
    <option value ="SX_AB_15">SEX ABUSE</option>
    <option value ="ARSON_15">ARSON</option>
    <option value ="HOM_2015">HOMICIDE</option>
    <option value ="">BURGLARY</option>
    <option value ="ASDW_15">ASSAULT W/DANGEROUS WEAPON</option>
    <option value ="THEFT_AUTO_15_THFT_AU_15">THEFT F/AUTO</option>
    <option value ="THFT_OT_15">THEFT/OTHER</option>
    <option value ="ROBBERY_15">ROBBERY</option>

</body>
<script>

$(function() {

var center = [38.9, -77.0]
var mymap = L.map('mapid').setView(center, 12);
var crime_category = $('#crime_category').val()

var sex_abuse_icon = L.icon({
    iconUrl: 'http://crime-security.org/material/029.png',
    iconSize: [20,20]
});
var arson_icon = L.icon({
    iconUrl: 'https://www.iconexperience.com/_img/g_collection_png/standard/256x256/fire.png',
    iconSize: [20,20]
});
var homicide_icon = L.icon({
    iconUrl: 'http://crime-security.org/material/034.png',
    iconSize: [20,20]
});
var burglary_icon = L.icon({
    iconUrl: 'http://crime-security.org/material/003.png',
    iconSize: [20,20]
});
var assault_dng_icon = L.icon({
    iconUrl: 'http://crime-security.org/material/071.png',
    iconSize: [20,20]
});
var theft_auto_icon = L.icon({
    iconUrl: 'http://crime-security.org/material/055.png',
    iconSize: [20,20]
});
var moto_theft_icon = L.icon({
    iconUrl: 'http://crime-security.org/material/033.png',
    iconSize: [20,20]
});
var theft_other_icon = L.icon({
    iconUrl: 'http://crime-security.org/material/065.png',
    iconSize: [20,20]
});
var marker_icon = L.icon({
    iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-icon-2x.png',
    iconSize: [20,20]
});
var robbery_icon = L.icon({
    iconUrl: 'http://crime-security.org/material/101.png',
    iconSize: [20,20]
});

function get_icon(d) {
	return d ==  'SEX ABUSE' ? sex_abuse_icon:
			d == 'ARSON' ? arson_icon:
			d == 'HOMICIDE' ? homicide_icon:
			d == 'BURGLARY' ? burglary_icon:
			d == 'ASSAULT W/DANGEROUS WEAPON' ? assault_dng_icon:
			d == 'THEFT F/AUTO' ? theft_auto_icon:
			d == 'MOTOR VEHICLE THEFT' ? moto_theft_icon:
			d == 'THEFT/OTHER' ? theft_other_icon:
			d == 'ROBBERY' ? robbery_icon:
				marker_icon;
}

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + 'pk.eyJ1Ijoid2Jjb25uZWxseSIsImEiOiJjaW1pN2w2MncwMDYydXlrdTNyMHR6aWdwIn0.E-vP5rCL3l6lOLyfU0FyIA', {
    id: 'mapbox.emerald'
}).addTo(mymap);

$('#crime_category').change(function() {
var crime_category = $('#crime_category').val()

function total_inc(category){
    var total = 0
    for(var i = 0; i < dc_psa.features.length; i++) {
    total = total + Number(dc_psa.features[i].properties[crime_category]);
}
    var avg = total/i
    var q1 = (avg*2)/5;
    var q2 = q1 *2;
    var q3 = q1 *3;
    var q4 = q1 *4;
    var q5 = q1 *5;
return {total:total, 
        num:i, 
        average: avg,
        q1 : q1,
        q2: q2,
        q3: q3,
        q4: q4,
        q5: q5};}

console.log(total_inc(crime_category).q1, total_inc(crime_category).q2, total_inc(crime_category).q3, total_inc(crime_category).q4, total_inc(crime_category).q5 );

function getColor(d) {
     return d > total_inc(crime_category).q5 ? '#800000' :
           d > total_inc(crime_category).q4 ? '#FF0000' :
           d > total_inc(crime_category).q3  ? '#FF8000' :
           d > total_inc(crime_category).q2  ? '#FFCC66' :
           d > total_inc(crime_category).q1   ? '#FFFF66' :
                      '#FFEDA0';
};
console.log(getColor(dc_psa.features[0].properties[crime_category]));
console.log(dc_psa.features[0].properties[crime_category]);
var style = function(feature) {
    return {
        fillColor: getColor(feature.properties[crime_category]),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}


L.geoJson(dc_psa, {style: style}).addTo(mymap);



//var category = "ROBBERY_15"

var crime_data = $.getJSON('https://dc.demo.socrata.com/resource/mk4t-ueny.json?$limit=100000', function(data) { try{
$.each(data, function(i, item) {
    
    var latlng = [item.location.coordinates[1], item.location.coordinates[0]];
    var incident = L.marker(latlng,{icon: get_icon(item.offense)}).bindPopup(item.offense).addTo(mymap);
//console.log(item.offense);

});} 
catch(err) {console.log(err);}

console.log(data);});

});

console.log(dc_psa);

});



</script>
</html>
