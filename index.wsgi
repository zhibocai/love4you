# coding:utf8
import sae
import web
        
urls = (
    '/', 'Index'
)

class Index:        
    def GET(self):
        html = u"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xml:lang="en" xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<title>Love</title>
	    <meta http-equiv="content-type" content="text/html; charset=utf-8">
        <link type="text/css" rel="stylesheet" href="/static/css/default.css"/ >
		<script type="text/javascript" src="/static/js/jquery.min.js"></script>
		<script type="text/javascript" src="/static/js/jscex.min.js"></script>
		<script type="text/javascript" src="/static/js/jscex-parser.js"></script>
		<script type="text/javascript" src="/static/js/jscex-jit.js"></script>
		<script type="text/javascript" src="/static/js/jscex-builderbase.min.js"></script>
		<script type="text/javascript" src="/static/js/jscex-async.min.js"></script>
		<script type="text/javascript" src="/static/js/jscex-async-powerpack.min.js"></script>
		<script type="text/javascript" src="/static/js/functions.js" charset="utf-8"></script>
		<script type="text/javascript" src="/static/js/love.js" charset="utf-8"></script>
	</head>
    <body>
        <div id="main">
            <div id="error">亲，您使用的浏览器无法支持即将显示的内容，请换成谷歌(<a href="http://www.google.cn/chrome/intl/zh-CN/landing_chrome.html?hl=zh-CN&brand=CHMI">Chrome</a>)或者火狐(<a href="http://firefox.com.cn/download/">Firefox</a>)浏览器哟~</div>
            <div id="wrap">
                <div id="text">
			        <div id="code">
			        	<span class="say">...做我女朋友...好吗?</span><br />
                        <span class="say">...嘿嘿，看我心情咯~</span><br />
			        	<span class="say">答应我吧~</span><br />
                        <span class="say">那好咧，勉强同意你了~不过要看你的表现啦~</span><br />
			        	<span class="say">要什么表现...</span><br />
			        	<span class="say">你自己看着办~</span><br />
			        	<span class="say">我觉得我压力好大</span><br />
			        	<span class="say">有鸭梨才有动力~</span><br />
			        	<span class="say">告诉我呗~</span><br />
			        	<span class="say">你还是考察期咧</span><br />
			        	<span class="say">考察期? 多久转正啊?</span><br />
			        	<span class="say">看你咧~ {笑}</span><br />
                        <span class="say">...</span><br/><br/><br/>
                        <span class="say">谢谢你走进我的世界，也让我走入你的世界。</span><br/>
                        <span class="say"><span class="space"></span> -- 永远爱你的菠菜。{羞}</span>
			        </div>
                </div>
                <div id="clock-box">
                    @菠菜 与 @Angel 相恋的
                    <div id="clock"></div>
                </div>
                <canvas id="canvas"></canvas>
            </div>
            <!--
            Angel说要听我唱, 这里注释掉 <(￣︶￣)>
            <audio src="" autoplay="autoplay"></audio>
            -->
        </div>
    </body>
    <script>
    </script>

    <script>
    (function(){
        var canvas = $('#canvas');

        if (!canvas[0].getContext) {
            $("#error").show();
            return false;
        }

        var width = canvas.width();
        var height = canvas.height();
        
        canvas.attr("width", width);
        canvas.attr("height", height);

        var opts = {
            seed: {
                x: width / 2 - 20,
                color: "rgb(190, 26, 37)",
                scale: 2
            },
            branch: [
                [535, 680, 570, 250, 500, 200, 30, 100, [
                    [540, 500, 455, 417, 340, 400, 13, 100, [
                        [450, 435, 434, 430, 394, 395, 2, 40]
                    ]],
                    [550, 445, 600, 356, 680, 345, 12, 100, [
                        [578, 400, 648, 409, 661, 426, 3, 80]
                    ]],
                    [539, 281, 537, 248, 534, 217, 3, 40],
                    [546, 397, 413, 247, 328, 244, 9, 80, [
                        [427, 286, 383, 253, 371, 205, 2, 40],
                        [498, 345, 435, 315, 395, 330, 4, 60]
                    ]],
                    [546, 357, 608, 252, 678, 221, 6, 100, [
                        [590, 293, 646, 277, 648, 271, 2, 80]
                    ]]
                ]] 
            ],
            bloom: {
                num: 700,
                width: 1080,
                height: 650,
            },
            footer: {
                width: 1200,
                height: 5,
                speed: 10,
            }
        }

        var tree = new Tree(canvas[0], width, height, opts);
        var seed = tree.seed;
        var foot = tree.footer;
        var hold = 1;

        canvas.click(function(e) {
            var offset = canvas.offset(), x, y;
            x = e.pageX - offset.left;
            y = e.pageY - offset.top;
            if (seed.hover(x, y)) {
                hold = 0; 
                canvas.unbind("click");
                canvas.unbind("mousemove");
                canvas.removeClass('hand');
            }
        }).mousemove(function(e){
            var offset = canvas.offset(), x, y;
            x = e.pageX - offset.left;
            y = e.pageY - offset.top;
            canvas.toggleClass('hand', seed.hover(x, y));
        });

        var seedAnimate = eval(Jscex.compile("async", function () {
            seed.draw();
            while (hold) {
                $await(Jscex.Async.sleep(10));
            }
            while (seed.canScale()) {
                seed.scale(0.95);
                $await(Jscex.Async.sleep(10));
            }
            while (seed.canMove()) {
                seed.move(0, 2);
                foot.draw();
                $await(Jscex.Async.sleep(10));
            }
        }));

        var growAnimate = eval(Jscex.compile("async", function () {
            do {
    	        tree.grow();
                $await(Jscex.Async.sleep(10));
            } while (tree.canGrow());
        }));

        var flowAnimate = eval(Jscex.compile("async", function () {
            do {
    	        tree.flower(2);
                $await(Jscex.Async.sleep(10));
            } while (tree.canFlower());
        }));

        var moveAnimate = eval(Jscex.compile("async", function () {
            tree.snapshot("p1", 240, 0, 610, 680);
            while (tree.move("p1", 500, 0)) {
                foot.draw();
                $await(Jscex.Async.sleep(10));
            }
            foot.draw();
            tree.snapshot("p2", 500, 0, 610, 680);

            // 会有闪烁不得意这样做, (＞﹏＜)
            canvas.parent().css("background", "url(" + tree.toDataURL('image/png') + ")");
            canvas.css("background", "#ffe");
            $await(Jscex.Async.sleep(300));
            canvas.css("background", "none");
        }));

        var jumpAnimate = eval(Jscex.compile("async", function () {
            var ctx = tree.ctx;
            while (true) {
                tree.ctx.clearRect(0, 0, width, height);
                tree.jump();
                foot.draw();
                $await(Jscex.Async.sleep(25));
            }
        }));

        var textAnimate = eval(Jscex.compile("async", function () {
            // 2011-06-03 21:20:00
		    var together = new Date();
		    together.setFullYear(2011, 5, 3);
		    together.setHours(21);
		    together.setMinutes(20);
		    together.setSeconds(0);
		    together.setMilliseconds(0);

		    $("#code").show().typewriter();
            $("#clock-box").fadeIn(500);
            while (true) {
                timeElapse(together);
                $await(Jscex.Async.sleep(1000));
            }
        }));

        var runAsync = eval(Jscex.compile("async", function () {
            $await(seedAnimate());
            $await(growAnimate());
            $await(flowAnimate());
            $await(moveAnimate());

            textAnimate().start();

            $await(jumpAnimate());
        }));

        runAsync().start();
    })();
    </script>

<!--

  /~ .~\    /~  ~\   
 '      `\/'      *
(               . *)
 \            . *./
  `\ .      . .*/'
    `\ * .*. */'
      `\ * */'
        `\/'

感谢饭团的同学们, 没有你们的帮助我和Angel, 不会那么快走到一起~ 哼(ˉ(∞)ˉ)唧

某日在Google里搜索"程序员的浪漫", 找到了hackerzhou做的http://love.hackerzhou.me, 
这也给了我启发, 所以我打算为我和Angel也做个类似的网页. 从2月7日开始, 从零开始学习HTML5, 
终于赶在2月14日前完成了这个版本. 时间仓促, 借鉴了很多代码, 最后也写得很烂, 见笑了. 

PS:能看到这里的朋友, 如果想拿代码泡MM或者学习的, 尽管拿去改, 就不用问作者啦. :)
-->
</html>
"""
        web.header('Content-Type', 'text/html')
        return html

app = web.application(urls, globals()).wsgifunc()
application = sae.create_wsgi_app(app)
