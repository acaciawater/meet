var bounds = null;

function htmlEncode(value) {
    return $('<div/>').text(value).html();
} 

function fetchPoints(url,options) {
    $.ajax({
	    url: url,

	    contentType: 'application/json',
	    
    	beforeSend: function (xhr) {
//    	    xhr.setRequestHeader ("Authorization", "Basic " + btoa(username + ":" + password));
    	},
	    
		success: function(data) {
			bounds = new google.maps.LatLngBounds();
			var infowindow = new google.maps.InfoWindow();
			var count = 0;
			data.forEach(function(point) {
				++count;
		   		var marker = new google.maps.Marker({
		   			position: new google.maps.LatLng(point.fields.latitude,point.fields.longitude),
		   			map: options.map,
					icon: {
		  			      path: google.maps.SymbolPath.CIRCLE,
		  			      scale: 5,
		  			      fillColor: 'red',
		  			      fillOpacity: 0.8,
		  			      strokeColor: 'white',
		  			      strokeWeight: 2
		  			}
		   		});
		   		

	   			options.list.insertAdjacentHTML('beforeend','<a href="" class="list-group-item">'+point.fields.sensor+' ('+ point.pk+')</a>');
	   			options.badge.innerHTML = count;
		   		
		   		google.maps.event.addListener(marker, 'click', (function(marker) {
		   	        return function() {
						var html = '<h3>Meting '+point.pk+'</h3>'+
						'<table class="table table-striped"><tr><td>Sensor</td><td>'+point.fields.sensor+'</td></tr>'+
						'<tr><td>Tijdstip</td><td>'+point.fields.date+'</td></tr>'+
						'<tr><td>'+point.entity+'</td><td>'+point.fields.value+'&nbsp;'+htmlEncode(point.fields.unit)+'</td></tr>'+
						'</table>';
						infowindow.setContent(html);
						infowindow.open(options.map, marker);
		   	        }
		   		})(marker));

		   		bounds.extend(marker.position);
			});
			
			map.fitBounds(bounds);
	    },

	    error: function(hdr,status,errorThrown) {
	    	//alert("Fout tijdens laden van punten: " + errorThrown);
	    },

	    complete: function(hdr, status) {
	    }
    });
}
