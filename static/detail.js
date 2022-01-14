const $editButton = $('#edit-button')
const $deleteButton = $('#delete-button')
const $cancelButton = $('#cancel-button')
const $saveButton = $('#save-button')
const $editForm = $('#edit-form')

$editForm.hide();

function editUser(evt) {
    $editForm.is(":visible") ? $editForm.hide() : $editForm.show();
    $deleteButton.is(":visible") ? $deleteButton.hide() : $deleteButton.show();
    $editButton.text() === "Edit" ? $editButton.text('^ Close Form ^') : $editButton.text("Edit");
    
}

// function cancelEdit(evt) {
//     // evt.preventDefault();
//     $editForm.is(":visible") ? $editForm.hide() : $editForm.show()
// }

$editButton.on('click', editUser)
// $cancelButton.on('click', cancelEdit)