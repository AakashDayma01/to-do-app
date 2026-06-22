
function askNewText(taskId, currentText) {
    let newText = prompt("Update your task:", currentText);
    
    if (newText !== null && newText.trim() !== "") {
        document.getElementById('input-' + taskId).value = newText;
        document.getElementById('form-' + taskId).submit();
    }
}