var time = document.querySelector('.time');

var updateClock = function() {
    var now = new Date();
    var remaining = new Date(now.getFullYear(), now.getMonth(), now.getDay(), 16 - now.getHours(), 60 - now.getMinutes(), 60 - now.getSeconds());
    
    var hours = remaining.getHours();
    var minutes = remaining.getMinutes();
    var seconds = remaining.getSeconds();

    // format
    if (now.getHours() > 16)
    {
        time.innerHTML = 'Times up!';
    }
    else
    {

        minutes = minutes < 10 ? '0' + minutes : minutes;
        seconds = seconds < 10 ? '0' + seconds : seconds;
        time.innerHTML = hours + ':' + minutes + ':' + seconds;
    }

    // display
    
}

document.querySelector("form").addEventListener('submit', e => {
    e.preventDefault();
    logWater();
})

var waterConsumed = 0;
var lastWater = 24;

function logWater() 
{
    const waterInput = document.querySelector("form input");
    waterNow = Number(waterInput.value);
    if (waterNow==NaN || waterNow==undefined)
        return;
    if (waterNow > lastWater)
    {
        waterConsumed = waterConsumed + lastWater;
        lastWater = 24;
    }
    
    waterConsumed = waterConsumed + (lastWater - waterNow);
    
    lastWater = waterNow;
    var progress = document.querySelector('.progress');
    progress.innerHTML = 75 - waterConsumed + " ounces remaining.";
    
}