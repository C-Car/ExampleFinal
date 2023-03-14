(() => {
    wallet = 0; 
    var enough = true; 
    var canMake = true; 
    var change = 0; 


    let resources = {"bread": 12,  
    "ham": 18,  
    "cheese": 24, };
    let small ={
        "ingredients": {
            "bread":2,
            "ham": 4,  
            "cheese": 4,  
        },
        "cost": 1.75,
    }
    let med ={
        "ingredients": {
            "bread": 4,  
            "ham": 6, 
            "cheese": 8, 
        },
        "cost": 3.25,
    }
    let large ={
        "ingredients": {
            "bread": 6,  
            "ham": 8,  
            "cheese": 12,  
        },
        "cost": 5.5,
    }
    function updWallet(coin){
        wallet = coin; 
        document.getElementById("wall").innerHTML = wallet;
    }


    function check_resources(){
        for(let key in this.resources){
            if(ingredients[key] > self.machine_resources[key]){
                this.enough = False
            }
            else{
                this.enough = True
            }
                
        }
    }
    function make_sandwhich(size){
        if(this.enough){
            for(let key in size[ingredients]){
                resources[key] = resources[key] - size["ingredients"][key]; 
            }
        }
        
    }
    function checkout(size){
        if(wallet< size["cost"]){
            canMake = false; 
            return false; 
        }
        else{
            canMake = true; 
            change = wallet - size["cost"];
        }
    }
    
       
    
       
  })()
function helloWorld(){
    display(); 
}
function change(){
    displayChange(); 
}
function display(){
    var iframe = document.getElementById('sample');
    var frame = iframe.contentDocument || iframe.contentWindow.document;
    frame.body.innerHTML = "<p style = 'color: #ff69b4 !important;'>Sample output</p>";
    
}
function displayChange(){
    var iframe = document.getElementById('change');
    var frame = iframe.contentDocument || iframe.contentWindow.document;
    frame.body.innerHTML = "<p style = 'color: #ff69b4 !important;'>:)</p>";

}
// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
      }, false)
    })
  })()