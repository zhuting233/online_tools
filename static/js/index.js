


Vue.component('Inavbar', {
    template: `
		<div class="navbar row">
			<a class="navbar-brand" href="/">
				<img src="/static/image/logo.png" id="logo">
			</a>
            <a class="navbar-brand" href="/"><span id="logotext">在线工具箱</span> </a>
			<ul class="nav navbar-nav navbar-right collapse navbar-collapse" id="example-navbar-collapse">
				<li class="active">
					<a href="/">主页</a>
				</li>
				<li>
					<a href="#">关于</a>
				</li>
				<li>
					<button type="button" class="btn btn-large btn-block btn-info login">登录/注册</button>
				</li>
			</ul>
		</div>
    `
})

Vue.component('Iblock', {
    template: `
    <a :href="iconurl" target="_blank" class="block">
        <!-- <i class="icon iconfont icon-erweima"></i> -->
        <div :class="iconclass">                          
        </div>
        <span class="text">
        <span class="text-content">{{title}}</span>
        
    </a>`,
    props: ['title', 'iconclass', 'iconurl']
})




new Vue({
    el: '#app',
    data: {
        brand: '在线工具箱',
        bannerstring: '君欲善其事，必先利其器',
        description: '在线工具箱 帮您更方便的处理事情',
        footer: '©2020 ',
        beian: '皖ICP备19023504号-1'
    }
})