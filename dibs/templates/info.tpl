<!DOCTYPE html>
<html lang="en">
  %include('common/banner.html')
  <head>
    %include('common/standard-inclusions.tpl')
    <title>Welcome to DIBS</title>
 </head>

  <body>
    <div class="page-content">
      %include('common/navbar.tpl')

      <div class="container main-container">
        <h1 class="mx-auto text-center pt-3 caltech-color">
          Controlled Digital Lending at UChicago
        </h1>
        <h2 class="mx-auto my-3 text-center text-info font-italic">
          The <strong>Di</strong>gital <strong>B</strong>orrowing <strong>S</strong>ystem
        </h2>
        <p class="my-3"><strong>Caltech DIBS</strong> is an implementation of <a target="_blank" href="https://controlleddigitallending.org">Controlled Digital Lending</a>.  For more information, please see <a target="_blank" href="https://www.lib.uchicago.edu/research/teaching/course-reserves-setup/">our course reserves setup page</a>.
	</p>
      </div>

      %include('common/footer.tpl')
    </div>
  </body>
</html>
