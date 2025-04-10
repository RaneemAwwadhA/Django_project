// Function to confirm product deletion
const deleteitem = (id) =>
{
  Swal.fire({
    title: 'Are you sure?',
    text: "You will not be able to retrieve this item after deletion!",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#d33',
    cancelButtonColor: '#3085d6',
    confirmButtonText: 'Yes, delete!',
    cancelButtonText: 'Cancel'
  }).then((result) => {

    if (result.isConfirmed) {
      $.ajax({
        url: '/prod/delete/' + id,  
        type: 'GET',

        success: function(result) {
        
        alert('Product deleted successfully!');
        location.reload();  // Refresh the page to correctly sort the numbers
          
        },
        error: function() {
          alert('Error deleting product');  // In case of an error
        }
      });
    }
  });
}



// Function to close messages when pressing the X mark
document.querySelectorAll('.close-btn').forEach(function(button) {
  button.addEventListener('click', function() {
      const message = button.parentElement; 
      message.style.display = 'none'; 
  });
});


// A function to confirm whether or not to save changes to the product
document.addEventListener("DOMContentLoaded", function () {
  const saveBtn = document.getElementById("confirmSaveBtn");

  if (saveBtn) {
    saveBtn.addEventListener("click", function (e) {
      e.preventDefault(); // يمنع الفورم من الإرسال الفوري

      Swal.fire({
        title: "Do you want to save the changes?",
        showDenyButton: true,
        showCancelButton: true,
        confirmButtonText: "Yes, save it",
        denyButtonText: "Don't save",
        cancelButtonText: "Cancel"
      }).then((result) => {
        if (result.isConfirmed) {
          document.querySelector("form").submit();
        } else if (result.isDenied) {
          Swal.fire("Changes were not saved", "", "info");
        }
      });
    });
  }
});
 /////













