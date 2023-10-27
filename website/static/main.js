// main.js
function deleteStudent(id) {
    $.ajax({
        url: '/delete_student/' + id,
        type: 'POST',
        success: function(response) {
            // Handle the response from the server
            // For example, you might remove the row for the deleted student from the table
            $('#' + id).closest('tr').remove();
        }
    });
}

// main.js
function deleteCourse(course) {
    $.ajax({
        url: '/delete_course/' + course,
        type: 'POST',
        success: function(response) {
            // Handle the response from the server
            // For example, you might remove the row for the deleted student from the table
            $('#' + course).closest('tr').remove();
        }
    });
}