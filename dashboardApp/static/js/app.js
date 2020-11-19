function resultButton() {


    var data = {day_of_week:document.getElementById("Weekdays").value, 
                    time_of_day:document.getElementById("ToD").value,
                    police_district:document.getElementById("District").value,
                    crime_category:document.getElementById("Category").value,
                    zip_code:document.getElementById("ZipCode").value};

    var day_of_week = document.getElementById("Weekdays").value
    var time_of_day = document.getElementById("ToD").value
    var police_district = document.getElementById("District").value
    var crime_category = document.getElementById("Category").value
    var zip_code = document.getElementById("ZipCode").value



    var jsonData = JSON.stringify({'day_of_week':day_of_week, 'time_of_day':time_of_day, 'police_district':police_district, 'crime_category':crime_category, 'zip_code':zip_code})

    console.log(jsonData)
    console.log(data)             
    
    
    $.ajax({
        url:'/formpost',
        type: 'POST',
        async: true,
        data:jsonData,
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        success: function (results_dict) {

            modal_message = "Crime Category : "+results_dict["Crime Category"]
            + "\nDay of Week : "+results_dict["Day of Week"]
            + "\nPolice District : "+results_dict["Police District"]
            + "\nTime of Day : "+results_dict["Time of Day"]
            + "\nZip Code : "+results_dict["Zip Code"]
            + "\n\n"+results_dict["outcome"]

            document.getElementById("modalResult").innerText = modal_message            
        }
        
  })

}



