function resultButton() {


    //
    var data = {day_of_week:document.getElementById("Weekdays").value, 
                    time_of_day:document.getElementById("ToD").value,
                    police_district:document.getElementById("District").value,
                    crime_category:document.getElementById("Category").value,
                    zip_code:document.getElementById("ZipCode").value};

    var jsonData = JSON.stringify(data)
    console.log(jsonData)
    console.log(data)             
    //jquery post to url and pass in json object 
    jQuery.post('/formpost/<data>', jsonData)
      
  }

  jQuery.post('/formpost/<data>', {day_of_week:document.getElementById("Weekdays").value, 
  time_of_day:document.getElementById("ToD").value,
  police_district:document.getElementById("District").value,
  crime_category:document.getElementById("Category").value,
  zip_code:document.getElementById("ZipCode").value})


  onclick="resultButton(Weekdays, ToD, District, Category, ZipCode)"