//******
// Detecting mobile devices
var isMobile = {
    Android: function() { return navigator.userAgent.match(/Android/i); },
    BlackBerry: function() { return navigator.userAgent.match(/BlackBerry/i); },
    iOS: function() { return navigator.userAgent.match(/iPhone|iPad|iPod/i); },
    Opera: function() { return navigator.userAgent.match(/Opera Mini/i); },
    Windows: function() { return navigator.userAgent.match(/IEMobile/i); },
    any: function() { return (isMobile.Android() || isMobile.BlackBerry() || isMobile.iOS() || isMobile.Opera() || isMobile.Windows()); }
};
// as found on http://www.abeautifulsite.net/detecting-mobile-devices-with-javascript/
//******

if ( isMobile.any() ) {
    var filery,
        galleries,
        thumbnails,
        overlays;

    galleries = document.getElementsByClassName('fancy-filery');

    for( var i = galleries.length-1; i >= 0; i-- ){
        filery = galleries[i]
        thumbnails = filery.getElementsByClassName('fancy-thumbnail');
        overlays = filery.getElementsByClassName('fancy-overlay');

        for( var j = thumbnails.length-1; j >= 0; j--){
            filery.removeChild(thumbnails[j])
        }

        for( var j = overlays.length-1; j >= 0; j--){
            filery.removeChild(overlays[j])
        }
    }

}


