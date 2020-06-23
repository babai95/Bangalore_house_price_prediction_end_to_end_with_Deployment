  function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms) {
      if(uiBathrooms[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function getBalconyValue() {
    var uiBalcony = document.getElementsByName("uiBalcony");
    for(var i in uiBalcony) {
      if(uiBalcony[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }

  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
      if(uiBHK[i].checked) {
          return parseInt(i)+1;
      }
    }
    return -1; // Invalid Value
  }
  
  function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var area_type = document.getElementById("uiAreatype");
    var location = document.getElementById("uiLocations");
    var sqft = document.getElementById("uiSqft");
    var bhk = getBHKValue();
    var bathrooms = getBathValue();
    var balcony = getBalconyValue();
    var estPrice = document.getElementById("uiEstimatedPrice");
  
    $.post(url_for('predict_house_price'), {
        area_type:area_type.value,
        location:location.value,
        bhk:bhk,
        total_sqft: parseFloat(sqft.value),
        bath: bathrooms,
        balcony: balcony
    },function(data, status) {
        console.log(data.estimated_house_price);
        estPrice.innerHTML = "<h2>" + data.estimated_house_price.toString() + " Lakh</h2>";
        console.log(status);
    });
  }
  
  function onPageLoad() {
    console.log( "document loaded" );
    $.get(url_for('get_locations'),function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    });

    $.get(url_for('get_area_types'),function(data, status) {
        console.log("got response for get_area_types request");
        if(data) {
            var area_types = data.area_types;
            var uiAreatype = document.getElementById("uiAreatype");
            $('#uiAreatype').empty();
            for(var i in area_types) {
                var opt = new Option(area_types[i]);
                $('#uiAreatype').append(opt);
            }
        }
    });

  }
  
  window.onload = onPageLoad;