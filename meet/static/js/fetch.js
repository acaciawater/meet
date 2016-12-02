var bounds = null;

function fetchPoints(url,map) {
    $.ajax({
	    url: url,

	    datatype: "json",

	    // TODO: Authentication
	    
	    beforeSend: function(hdr) {
	    	return true;
	    },
	    
		success: function(data) {
			if (data.meta.offset == 0) {
				// first batch of points: clear bounds
				bounds = new google.maps.LatLngBounds();
			}
			data.objects.forEach(function(point) {
		   		var marker = new google.maps.Marker({
		   			position: new google.maps.LatLng(point.latitude,point.longitude),
					icon: {
					      path: google.maps.SymbolPath.CIRCLE,
					      scale: 4,
					      fillColor: 'red',
					      fillOpacity: 0.8,
					      strokeColor: 'white',
					      strokeWeight: 1
					},
		   			map: map
		   		});
				bounds.extend(marker.position);
			});
			
			if (data.meta.next) {
				// fetch next batch of points
				fetchPoints(data.meta.next, map);
			}
			else {
				// no more points: fit map bounds
				if (bounds)
					map.fitBounds(bounds);
			}
	    },

	    error: function(hdr,status,errorThrown) {
	    	//alert("Fout tijdens laden van punten: " + errorThrown);
	    },

	    complete: function(hdr, status) {
	    }
    });
}
