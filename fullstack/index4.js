const button1 = document.getElementById('button1');

const callit = () => {
    console.log('executed after 4 seconds');
}

const settime = setTimeout(callit, 4000);

button1.addEventListener(`click`, () => {
    clearTimeout(settime);
})

let timoutId = setTimeout(() => {
    console.log("this is a one time message afer 3 seconds.");
}, 3000);

let count=0;
let intervalId = setInterval(() => {
    console.log(`interval count: ${++count}`);
}, 1000);


setTimeout(() => {
    clearTimeout(timeoutId);
    console.log("timrout canceled");
}, 2000);


setTimeout(() => {
    clearInterval(intercalId);
    console.log("Interval stopped");
}, 5000);