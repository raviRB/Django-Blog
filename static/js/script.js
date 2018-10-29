document.getElementById("id_profile_pic").className = " ";
function reply(pk){
    id = pk;
    console.log(id);
    var x = document.getElementById(id);
    if(x.style.display === "block")
    {
       x.style.display="none";
    }
    else{
        x.style.display="block";
    }

}