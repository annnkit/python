// const firstTask = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         console.log("Async Task Completed.")
//         resolve();
//     }, 2000);
// });

// firstTask.then(() => console.log(`First task resolved`))

// const userTask = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve({
//             student: `sai` , enrollment: `32421423`
//         });
//     }, 1000);
// });

// userTask.then((user) => console.log(user));


// console.log("start");

// const authTask = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         const hasError = false;
//         if(!hasError) {
//             resolve({
//                 username: `coder`, password: `secure123` 
//             });
//         }else {
//             reject(`ERROR: Autentication failed`);
//         }
//     }, 1000);
// })

// authTask
// .then((user) => {
//     console.log(user);
//     return user.username;
// })
// .then((username) => console.log(username))
// .catch((error) => console.log(error))
// .finally(() => console.log(`Auth task completed`));  // This will run regardless of the outcome of the promise.  // This will

// async function processAuthTask() {
//     try{
//         const result = await authTask;
//         console.log(result);
//     } catch (error) {
//         console.log(error);
//     }
// }

// processAuthTask();

// console.log("end");

async function fetchUser() {
    try {
        const response = await fetch(`https://api.github.com/users/ShivanshMehtaa`);
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log(`Error:`, error);
    }
}

fetchUser();