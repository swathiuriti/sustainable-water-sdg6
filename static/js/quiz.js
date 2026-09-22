let selectedQuestions = [];

const container =
document.getElementById(
"quizContainer"
);

function shuffle(array){

for(let i=array.length-1;i>0;i--){

const j =
Math.floor(
Math.random()*(i+1)
);

[array[i],array[j]] =
[array[j],array[i]];

}

return array;

}

function loadQuiz(){

container.innerHTML = "";

const shuffledQuestions =
shuffle([...questionBank]);

selectedQuestions =
shuffledQuestions.slice(
0,
Math.min(10,
questionBank.length)
);

selectedQuestions.forEach(
(q,index)=>{

let options =
shuffle([...q.options]);

let html = `

<div class="card shadow p-3 mb-3">

<h5>
${index+1}. ${q.question}
</h5>

`;

options.forEach(option=>{

html += `

<div class="form-check">

<input
class="form-check-input"
type="radio"
name="q${index}"
value="${option}">

<label
class="form-check-label">

${option}

</label>

</div>

`;

});

html += `</div>`;

container.innerHTML += html;

});

}

function submitQuiz(){

let score = 0;

let reviewHTML = "";

selectedQuestions.forEach(
(q,index)=>{

let selected =

document.querySelector(
`input[name="q${index}"]:checked`
);

if(
selected &&
selected.value === q.answer
){

score++;

}
else{

reviewHTML += `

<div class="alert alert-warning">

<b>Question:</b>
${q.question}

<br>

<b>Your Answer:</b>
${selected ?
selected.value :
"Not Answered"}

<br>

<b>Correct Answer:</b>
${q.answer}

</div>

`;

}

});

let percentage =
(score/10)*100;

localStorage.setItem(
"quizScore",
Math.round(
(score/10)*25
)
);

document.getElementById(
"resultSection"
).style.display =
"block";

document.getElementById(
"scoreText"
).innerHTML =

`Score: ${score}/10 (${percentage.toFixed(1)}%)`;

let badge =
"📘 Learner";

let message =
"Keep learning.";

if(percentage>=90){

badge =
"🏆 Water Warrior";

message =
"Outstanding knowledge of SDG 6.";

}
else if(percentage>=75){

badge =
"🌱 Eco Guardian";

message =
"Very good performance.";

}
else if(percentage>=50){

badge =
"💧 Rain Hero";

message =
"Good attempt.";

}

document.getElementById(
"badgeText"
).innerHTML =
"Badge: " + badge;

document.getElementById(
"messageText"
).innerHTML =
message;

document.getElementById(
"reviewSection"
).innerHTML =
reviewHTML;

fetch(
"/save_quiz",
{
method:"POST",
headers:{
"Content-Type":
"application/x-www-form-urlencoded"
},
body:"score="+score
}
);

drawChart(
percentage
);

window.scrollTo(
0,
resultSection.offsetTop
);

document.getElementById(
"resultSection"
).scrollIntoView({

behavior:"smooth",
block:"start"

});

}

function drawChart(score){

const ctx =
document.getElementById(
"scoreChart"
);

new Chart(ctx,{

type:"doughnut",

data:{

labels:[
"Score",
"Remaining"
],

datasets:[{

data:[
score,
100-score
],

borderWidth:0

}]

},

options:{

responsive:false,

cutout:"85%",

plugins:{

legend:{
display:false
}

}

}

});

}

function resetQuiz(){

document.getElementById(
"resultSection"
).style.display =
"none";

loadQuiz();

window.scrollTo({

top:0,
behavior:"smooth"

});

}

loadQuiz();