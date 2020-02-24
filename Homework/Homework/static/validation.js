$(document).ready(function(){
   
    function phone_validation(){
        // var contact = $(this).val();
        $('#valid').remove()
        var phone=$('#id_phone').val()
        $('#phone').remove()
        $.ajax({
        url: '/ajax/validate_phone/',
        data: {
        'phone': phone
        },
        dataType: 'json',
        success: function (data) {
        if (data.is_taken) {
            
        $('#id_phone').after("<span id='phone' class='text-danger'><img class='img-thumbnail' style='width: 40px' src='../static/error.png'/>User With This Phone Number Already Exists.</span></p> ")
        return false
        }else{
            $('#id_phone').after("<span id='phone' class='text-primary'><img class='img-thumbnail' style='width: 40px' src='../static/success.png'/>&nbsp;Availabel.</span></p> ")
            return true
            
        }
        }
        });
        
        }

    function contact_validation(){
         len=$('#id_phone').val()
         var con= /^[0-9]*$/
         $('#error_contact').remove()
         if(len.length>10 || len.length<10 ){
             $("#id_phone").after("<span style='color:red' id='error_contact'>* Contact Number Must Contains 10 digits NUmber !</span>")
             return false
         }else if(!con.test(len)){
            $("#id_phone").after("<span style='color:red' id='error_contact'>* Contact Number Must be digit not a character !</span>")
             return false
         }else{
             return true
         }
    }
    function email_validation()
    {
         len=$('#id_email').val()
         var con= /^[a-zA-Z_.0-9]+@[a-zA-Z]+[.]{1}[a-zA-Z]+$/
         $('#error_email').remove()
         if(!con.test(len)){
            $("#id_email").after("<span style='color:red' id='error_email'>* Please Enter Valid Email Address!</spna>")
             return false
         }else{
             return true
         }
    }
    function first_name_validation(){
        len=$('#id_first_name').val()
        var con= /^[a-zA-Z_]*$/
        $('#error_first_name').remove()
        if(!con.test(len)){
            $("#id_first_name").after("<span style='color:red' id='error_first_name'>*First Name Must be character or not a digit or special charecter !</span>")
            return false
        }else{
            return true
        }
    }
    function last_name_validation()
    {
        len=$('#id_last_name').val()
        var con= /^[a-zA-Z_]*$/
        $('#error_last_name').remove()
        if(!con.test(len)){
            $('#id_last_name').after("<span style='color:red' id='error_last_name'>*Last Name Must be character or not a digit or special charecter !</span>")
            return false
        }else{
            return true
        }
    }
    function password_validation()
    {
        pass1=$('#id_password1').val()
        pass2=$('#id_password2').val()
        $('#error_password2').remove()
        if(pass2.length<=0){
            $('#id_password2').after("<span style='color:red' id='error_password2'>* Confirm Password should not be blank !</span>") 
            return false
        }

        if(pass1!=pass2){
            $('#id_password2').after("<span style='color:red' id='error_last_name'>* Password not match with Confirm Password !</span>") 
            return false
        }else{
            return true
        }
    }
    //registration form validation
   

    // $('#id_phone').blur(function(){
        
    // });

    $('#id_phone').blur(function(){
        contact_validation()
        phone_validation()
    }); 

    $('#id_first_name').blur(function(){
       first_name_validation()
    }); 

    $('#id_last_name').blur(function(){
       last_name_validation()
    }); 

    $('#id_email').blur(function(){
        email_validation()
    });

    $('#id_password2').blur(function(){
       password_validation()
    });

    $('#singup').submit(function(e) {
        
        if(!(contact_validation() && !(phone_validation()) && first_name_validation() && last_name_validation() && email_validation() && password_validation())) 
        {
            e.preventDefault()
        } 
    });

    // book cleaner
    function city_validation()
    {
        cityval=$('#id_city').val()
        $("#error_city").remove() 
        if(cityval.length<=0){
             $("#id_city").after("<span style='color:red' id='error_city'>*  Select City !</span>")
             return false
         }else{
             return true
        }
    }
   
    function timeslot_validation()
    {
        timeslotval=$('#id_slot').val()
        $("#error_timeslot").remove() 
        if(timeslotval== 0){
            $("#id_slot").after("<span style='color:red' id='error_city'>*  Select Time Slot !</span>") 
            return false
        }else{
            return true
        }
    }

    function date_validation()
    {
        dateval=$('#id_date').val()
        select_date=new Date(dateval) //selected date
        syear=select_date.getFullYear()
        smonth=select_date.getMonth()
        sdate=select_date.getDate()
        today_date=new Date() // today date
        tyear=today_date.getFullYear()
        tmonth=today_date.getMonth()
        tdate=today_date.getDate()
        $("#error_date").remove()
        if(syear>tyear){
            return true;
        }else if(syear==tyear){
            if(smonth>tmonth){
                return true;
            }else if(smonth==tmonth){
                if(sdate>tdate){
                    return true;
                }else if(sdate==tdate){
                    return true;
                }else{
                    $("#id_date").after("<span style='color:red' id='error_date'>*Selected Date Must Be Future Date. !</span>");
                    return false;
                }
            }
        }else{
            $("#id_date").after("<span style='color:red' id='error_date'>*Selected Date Must Be Future Date.!</span>"); 
            return false;
        }
    }

    $('#id_city').change(function(){
        city_validation()
    });
 
    $('#id_slot').change(function(){
        timeslot_validation()
    });
 
    $('#id_date').change(function(){
        date_validation()
    });

    $("#searchform").submit(function(e){
        if(!(city_validation() && timeslot_validation() && date_validation()))
        {
            e.preventDefault()
        }
    });
    
});

$("#id_phone").change(function () {
    console.log( $(this).val() );
  });

//Login Validators
function login_contact_validation(){
    len=$('#id_phone').val()
    var con= /^[0-9]*$/
    $('#error_contact').remove()
    if(len.length>10 || len.length<10 ){
        $("#id_phone").after("<span style='color:red' id='error_contact'>* Contact Number Must Contains 10 digits NUmber !</span>")
        return false
    }else if(!con.test(len)){
       $("#id_phone").after("<span style='color:red' id='error_contact'>* Contact Number Must be digit not a character !</span>")
        return false
    }else{
        return true
    }
}
function pass_validation(){
    len=$('id_password').val()
    $('#error_password').remove()
    if(len.length<=5){
        $('id_password').after("<span style='color:red' id='error_contact'>*Password not less then 5 Digits!</span>")
        return false
    }
    else{
    return true
    }
}
$('#id_phone').blur(function(){
login_contact_validation()
});

$('#id_password').blur(function(){
    pass_validation()
    });
    
$('#login').submit(function(e) {
    
if(!(Login_contact_validation() && pass_validation())) 
{
    e.preventDefault()
} 
});
