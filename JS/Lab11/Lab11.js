new Vue({

    el:'#vue-app',
    data:{
        name:'Charlie',
        job: 'Charlsing',
        website: 'https://github.com/charlie2265?tab=repositories',
        websiteTag:'<a href="https://github.com/charlie2265?tab=repositories">My Github</a>'
    },

    methods:{
        greet: function(time){
            return 'Good' +  time +  ' '  + this.name;
        }
    }
});
    methods:{
        
    }