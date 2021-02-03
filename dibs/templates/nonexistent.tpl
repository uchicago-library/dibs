<!DOCTYPE html>
<html lang="en">
  %include('static/banner.html')
  <head>
    <title>No such item</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
  </head>
  
  <body>
    <div class="container-fluid">
      <div class="alert alert-danger my-3" role="alert">
        <h4 class="alert-heading">No such item</h4>
        %if barcode == 'None':
          <p id="without-barcode">This item does not exist.</p>
        %else:
          <p id="with-barcode">An item with barcode {{barcode}} does not exist.</p>
        %end
      </div>
    </div
  </body>
</html>
