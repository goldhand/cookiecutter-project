  definegrid = function() {
    var browserWidth = $(window).width(); 
    pageUnits = 'px';
    colUnits = '%';
    gutUnits = 'px';
    pageMarUnits = 'px';
    columnwidth = 5.76923075;
    gutterwidth = 30;
    columns = 12;
    pagetopmargin = 0;
    rowheight = 6;
    gridonload = 'off';


    // screen-lg
    if (browserWidth >= 1200) 
    {
        pagewidth = 1170;
        columnwidth = 5.92105263;
        makehugrid();
    }
    // screen-md
    if (browserWidth <= 1199 && browserWidth >= 992) 
    {
        pagewidth = 970;
        columnwidth = 5.24;
        makehugrid();
    }
    // screen-sm
    if (browserWidth <= 991 && browserWidth >= 768) 
    {
        pagewidth = 720;
        columnwidth = 4.51388889;
        makehugrid();
    }
    // screen-xs
    if (browserWidth <= 767) 
    {
        pageUnits = '%';
        pagewidth = 100;
        makehugrid();
    }

  }
  $(document).ready(function() {
    definegrid();
    setgridonload();
  });    

  $(window).resize(function() {
    definegrid();
    setgridonresize();
  });