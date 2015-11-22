var ele = function (el){
    return [].slice.call(document.querySelectorAll(el));
};

window.addEventListener('resize', function(){
    checkFilery();
});

document.addEventListener("DOMContentLoaded", function() {
    checkFilery();
});

var FileryPage = function (filery, thumbs, id) {
    this.selector = document.createElement('div');
    this.filey = filery;
    this.thumbnails = thumbs;
    this.pageID = id;

    this.selector.classList.add('.filery-page-selector');
    this.selector.setAttribute('id', id);
    this.filey.appendChild(this.selector);

    FileryPage.prototype.hide = function () {
        var i;
        for ( i = this.thumbnails.length -1; i >= 0; i-- ){
            this.thumbnails[i].style.display = 'none';
        }
    };

    FileryPage.prototype.show = function () {
        var i;
        for ( i = this.thumbnails.length -1; i >= 0; i-- ){
            this.thumbnails[i].style.display = 'inline-block';
        }
    };

};


var checkFilery = function () {
    var i,
        filery,
        thumbnails,
        firstImg,
        secondImg,
        maxImages,
        availableSpace,
        marginLeft,
        marginRight,
        page,
        pages,
        fileryPage,
        fileryPages = [],
        first,
        last;

    filery = ele('.fancy-filery')[0];
    thumbnails = [].slice.call(filery.querySelectorAll('.fancy-thumbnail'));
    if ( thumbnails.length > 2 ) {
        firstImg = thumbnails[0];
        marginLeft = parseInt(getComputedStyle(firstImg).getPropertyValue('margin-left'), 10);
        secondImg = thumbnails[1];
        marginRight = parseInt(getComputedStyle(secondImg).getPropertyValue('margin-right'), 10);
        availableSpace = filery.clientWidth - marginLeft;
        imgSpace = secondImg.clientWidth + marginRight;

        maxImages = Math.floor(availableSpace / imgSpace);

        if (maxImages < thumbnails.length ){
            page = 0;
            pages = Math.ceil(thumbnails.length / maxImages);
            for ( i = pages-1; i >= 0; i-- ){
                first = page * maxImages;
                last = page+1 * maxImages;
                fileryPage = new FileryPage(filery, thumbnails.slice(first, last), page);
                fileryPages.push(fileryPage);
                if ( page > 0){
                    fileryPage.hide();
                } else {
                    fileryPage.show();
                }

                page++;
            }
        } else {
            for ( i = thumbnails.length -1; i >= 0; i-- ){
                thumbnails[i].style.display = 'inline-block';
            }
        }

    }
}