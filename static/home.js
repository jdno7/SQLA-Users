const $addButton = $('#add-button')
const $createButton = $('#create-button')

const $addUserForm = $('#add-user-form')

$addUserForm.hide();

function addUser(evt) {
    $addUserForm.is(":visible") ? $addUserForm.hide() : $addUserForm.show();
    // $deleteButton.is(":visible") ? $deleteButton.hide() : $deleteButton.show();
    $addButton.text() === "Add User" ? $addButton.text('^ Close Form ^') : $addButton.text("Add User");
    
}

// function cancelEdit(evt) {
//     // evt.preventDefault();
//     $editForm.is(":visible") ? $editForm.hide() : $editForm.show()
// }

$addButton.on('click', addUser)
// $cancelButton.on('click', cancelEdit)