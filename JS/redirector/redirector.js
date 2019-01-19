const websites = ['https://www.youtube.com/watch?v=-7jjo8UICjQ','https://www.youtube.com/watch?v=uaMcMi03QTQ','https://www.youtube.com/watch?v=BxENSZ6wXkA','https://www.youtube.com/watch?v=-yCQraOX4Bw'];
const randomSite = document.querySelector('#random-site');

randomSite.addEventListener('click', function(){
    
    window.location = websites[Math.floor(Math.random() * websites.length)]
})


