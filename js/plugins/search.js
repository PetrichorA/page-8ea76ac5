EPUBJS.reader.search={},EPUBJS.reader.search.SERVER="https://pacific-cliffs-3579.herokuapp.com",EPUBJS.reader.search.request=function(e,n){var r=$.ajax({dataType:"json",url:EPUBJS.reader.search.SERVER+"/search?q="+encodeURIComponent(e)});r.fail((function(e){console.error(e)})),r.done((function(e){n(e)}))},EPUBJS.reader.plugins.SearchController=function(e){var n,r=this,a=$("#searchBox"),i=$("#searchResults"),t=$("#searchView");return a.on("search",(function(e){if(""==a.val())return i.empty(),"Search"==r.SidebarController.getActivePanel()&&r.SidebarController.changePanelTo("Toc"),$(n).find("body").unhighlight(),void(n=!1);r.SidebarController.changePanelTo("Search"),e.preventDefault()})),{show:function(){(function(){var r=a.val();""!=r&&(i.empty(),i.append("<li><p>Searching...</p></li>"),EPUBJS.reader.search.request(r,(function(a){var t=a.results;i.empty(),n&&$(n).find("body").unhighlight(),0!=t.length?(n=$("#viewer iframe")[0].contentDocument,$(n).find("body").highlight(r,{element:"span"}),t.forEach((function(a){var t=$("<li></li>"),o=$("<a href='"+a.href+"' data-cfi='"+a.cfi+"'><span>"+a.title+"</span><p>"+a.highlight+"</p></a>");o.on("click",(function(a){var i=$(this).data("cfi");a.preventDefault(),e.gotoCfi(i+"/1:0"),e.on("renderer:chapterDisplayed",(function(){n=$("#viewer iframe")[0].contentDocument,$(n).find("body").highlight(r,{element:"span"})}))})),t.append(o),i.append(t)}))):i.append("<li><p>No Results Found</p></li>")})))})(),t.addClass("shown")},hide:function(){t.removeClass("shown")}}};