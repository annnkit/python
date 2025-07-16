document.addEventListener("DOMContentLoaded", () => {
  loadTasks();
});

function addTask() {
  const input = document.getElementById("input");
  const taskText = input.value.trim();
  if (taskText === "") {
    alert("Please enter a task");
    return;
  }

  const task = {
    id: Date.now(),
    text: taskText,
    completed: false,

  }

  saveTask(task);

  renderTask(task);

  taskInput.value = ``;
}

function renderTask(task) {
    const taskList = document.getElementById("taskList");
    const li = document.createElement("li");
    li.dataset.id = task.id;

    li.innerHTML = `
    <span class="${task.completed ? 'completed' : ''}">${task.text}</span> 
    <div class = "task-actions">

    <button onclick = "toggleTask(${task.id})">
    ${task.completed ? `undo` : `completed`}
    </button>

    <button onclick = "deleteTask(${task.id})">
    Delete
    </button>

    </div>
    `;
    taskList.appendChild(li); 

}

function saveTask(task){
  let tasks = getTasks();
  tasks.push(task);
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

function loadTasks() {
  const taskList = document.getElementById("taskList");
  const tasks = getTasks();
  tasks.forEach(task => renderTask(task));
}

function toggleTask(id){
  let tasks = getTasks();
  tasks = tasks.map(task => {
    if (task.id == id) {
      task.completed = !task.completed;
    }
    return task;
  });
  localStorage.setItem(`tasks`, JSON.stringify(tasks));
}

function getTasks() {
  return JSON.parse(localStorage.getItem(`tasks`)) || [];
}

function refreshTaskList() {
  const taskList = document.getElementById('taskList');
  taskList.innerHtml = '';
  LoadTask();
}