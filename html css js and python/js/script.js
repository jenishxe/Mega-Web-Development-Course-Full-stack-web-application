function showReview(){
    // document.querySelector(".review-container").style.opacity="100%";
    // document.querySelector(".product-image").style.filter = 'brightness(.4)'
    document.querySelector(".review-container").classList.add("hover-review");
    document.querySelector(".product-image").classList.add("hover-image");
}

function hideReview(){
    // document.querySelector(".review-container").style.opacity="0%";
    // document.querySelector(".product-image").style.filter = 'brightness(1)'

    document.querySelector(".review-container").classList.remove("hover-review");
    document.querySelector(".product-image").classList.remove("hover-image")
}


// function videoEnded(){
//     console.log("Video Ended!")
// }

var video = document.querySelector("video");
video.addEventListener("ended", function(){console.log("Video Ended!")});

var productImg = document.querySelector(".product-image");
productImg.addEventListener("mouseover", showReview);
productImg.addEventListener("mouseout", hideReview);




var sun = document.getElementById("sun-icon");
var moon = document.getElementById("moon-icon");
var body = document.getElementsByTagName("body")[0];

function darkMode(){
    sun.style.display="none";
    moon.style.display="inline-block";
    body.classList.toggle("body-dark");
};

function lightMode(){
    sun.style.display="inline-block";
    moon.style.display="none";
    body.classList.toggle("body-dark");
};

// video control using js


document.addEventListener("keydown", function(e){
    currentTime = video.currentTime
    // console.log(e)
    switch(e.keyCode){
        case 37:
            // 37 for leftkey
            newtime = currentTime - 5
            if (newtime <=0){
                video.currentTime = 0;
            }
            else{
                video.currentTime = newtime
            }
            break
        case 39:
            // for right key
            newtime = currentTime + 5
            if (newtime >=video.duration){
                video.currentTime = video.duration;
            }
            else{
                video.currentTime = newtime
            }
            break
        case 37:
            //for space
            togglePLayePause();
            break
    }
})







// function sum(n1,n2){
//     console.log(n1+n2)
// }

// function second(p1,p2, fun){
//     fun(p1,p2)
// }








// javascript beginer and intermediate practice


// var listNum = [13,23,12,45,22,48,66,100,2,400,444,829,3,820]

// function findEven(list){
    
//     for(var i = 0; i<=list.length; i++ ){
//         if(list[i]%2==0){
//             console.log(list[i])
//         }
//     }
// }

// findEven(listNum);





// var breakTime = [];
// var round = 1;

// function addBreakTime(x){
//     while(round<=x){    
//         if(round%4==0){
//             breakTime.push(15);
//         }
//         else{
//             breakTime.push(5);
//         }
//         round++
//     }
//     console.log(breakTime)
    
// }













// // function addBreakTime(){
// //     if ( round %4==0 ){
// //         breakTime.push(15)
// //     }
// //     else{
// //         breakTime.push(5)
// //     };
// //     // round = round+1
// //     round++
// //     console.log(breakTime)
// // }