var locations = [
	{
		name: 'Hamburgisches Architekturarchiv',
		lat: 53.5455053,
		long: 10.0014884
	},
	{
		name: 'Colon',
		lat: 53.5575982,
		long: 9.9901161
	},
	{
		name: 'Hamburger Rathaus',
		lat: 53.5499061,
		long:  9.9926535
	},
    {
        name: 'Hamburg Central Station',
        lat: 53.5528,
        long: 10.0070
    },
    {
        name: 'Zentralbibliothek',
        lat: 53.5496805,
        long: 10.0081401
    }
];

var map;
var foursquareClientID;
var foursquareClientSecret;


function generateURL(self) {
    var foursquareURL = 'https://api.foursquare.com/v2/venues/search?ll=' + self.lat + ',' + self.long + '&client_id='
        + foursquareClientID + '&client_secret=' + foursquareClientSecret + '&v=20160118' + '&query=' + self.name;
    return foursquareURL;
}

function query(foursquareURL, self) {
    $.getJSON(foursquareURL).done(function (data) {
        var results = data.response.venues[0];
        self.street = results.location.formattedAddress[0];
        self.city = results.location.formattedAddress[1];
    }).fail(function () {
        alert("Error : API requests");
    });
}

function getContentString(self) {
    return '<div class="info-window-content"><div class="title"><b>' + self.name + "</b></div>" +
        '<div class="content">' + self.street + "</div>" +
        '<div class="content">' + self.city + "</div></div>";
}

var Location = function(location) {
	var self = this;
	this.name = location.name;
	this.lat = location.lat;
	this.long = location.long;
	this.street = "";
	this.city = "";
	this.visible = ko.observable(true);

    var foursquareURL = generateURL(self);
    query(foursquareURL, self);

    this.contentString = getContentString(self);
	this.infoWindow = new google.maps.InfoWindow({content: self.contentString});
	this.marker = new google.maps.Marker({
			position: new google.maps.LatLng(location.lat, location.long),
			map: map,
			title: location.name
	});

	this.showMarker = ko.computed(function() {
		if(this.visible() === true) {
			this.marker.setMap(map);
		} else {
			this.marker.setMap(null);
		}
		return true;
	}, this);

	this.marker.addListener('click', function () {
        self.contentString = getContentString(self);
        self.infoWindow.setContent(self.contentString);
        self.infoWindow.open(map, this);
        self.marker.setAnimation(google.maps.Animation.BOUNCE);
        setTimeout(function() {
            self.marker.setAnimation(null);
        }, 2100);
    });

	this.bounce = function(place) {
		google.maps.event.trigger(self.marker, 'click');
	};
};

function getFilteredLocations(self, filter) {
    return ko.utils.arrayFilter(self.locationList(), function (locationItem) {
        var string = locationItem.name.toLowerCase();
        var result = (string.search(filter) >= 0);
        locationItem.visible(result);
        return result;
    });
}

function showAllLocations(self) {
    self.locationList().forEach(function (locationItem) {
        locationItem.visible(true);
    });
    return self.locationList();
}

function AppViewModel() {
	var self = this;

	this.searchTerm = ko.observable("");

	this.locationList = ko.observableArray([]);

	map = new google.maps.Map(document.getElementById('map'), {
			zoom: 15,
			center: {lat: 53.546, lng: 10.001}
	});

	locations.forEach(function(locationItem){
		self.locationList.push( new Location(locationItem));
	});

	this.filteredList = ko.computed( function() {
		var filter = self.searchTerm().toLowerCase();
		if (!filter) {
            return showAllLocations(self);
        } else {
			return getFilteredLocations(self, filter);
		}
	}, self);

	this.mapElem = document.getElementById('map');
	this.mapElem.style.height = window.innerHeight;
}

function startApp() {

    foursquareClientID = "<foursquare client id>";
    foursquareClientSecret = "<foursquare client secret>";

	ko.applyBindings(new AppViewModel());
}

function errorHandling() {
	alert("Please check your internet.");
}
