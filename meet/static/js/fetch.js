var bounds = null;

function htmlEncode(value) {
    return $('<div/>').text(value).html();
} 
function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

  
function clearMarkers() {
    setMapOnAll(null);
}

function fetchPoints(url,options) {
    $.ajax({
	    url: url,

	    contentType: 'application/json',
	    
    	beforeSend: function (xhr) {
//    	    xhr.setRequestHeader ("Authorization", "Basic " + btoa(username + ":" + password));
    	},
	    
		success: function(data) {
			clearMarkers();
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
		   		markers.push(marker);
		   		
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
			
		    if (bounds.getNorthEast().equals(bounds.getSouthWest())) {
		        var extendPoint1 = new google.maps.LatLng(bounds.getNorthEast().lat() + 0.1, bounds.getNorthEast().lng() + 0.1);
		        var extendPoint2 = new google.maps.LatLng(bounds.getNorthEast().lat() - 0.1, bounds.getNorthEast().lng() - 0.1);
		        bounds.extend(extendPoint1);
		        bounds.extend(extendPoint2);
		     }
			
			map.fitBounds(bounds);

	    },

	    error: function(hdr,status,errorThrown) {
	    	//alert("Fout tijdens laden van punten: " + errorThrown);
	    },

	    complete: function(hdr, status) {
	    }
    });
}


function pressLink(pk) {
	var url = '/getseries?user='+pk;
    fetchPoints(url, {
    	map:map, 
    });
//    fillTable('/getusers', {
//    	list:document.getElementById('list'),
//    	badge:document.getElementById('badge')
//    });
}


function fillTable(url, options){
	
    $.ajax({
	    url: url,

	    contentType: 'application/json',
	    
    	beforeSend: function (xhr) {
//    	    xhr.setRequestHeader ("Authorization", "Basic " + btoa(username + ":" + password));
    	},
	    
		success: function(data) {
			var count = 0;
			console.log(data[1])
			var nr_of_measurements = data[1]
			data[0].forEach(function(object) {
				++count;
				options.list.insertAdjacentHTML('beforeend','<a href="javascript:pressLink('+object.pk+')" class="list-group-item">'+object.fields.username+'<span id="badge" class="badge">'+nr_of_measurements[object.fields.username]+'</a>');
	   			options.badge.innerHTML = count;
			});
	    },

	    error: function(hdr,status,errorThrown) {
	    	//alert("Fout tijdens laden van de tabel: " + errorThrown);
	    },

	    complete: function(hdr, status) {
	    }
    });
}
