;(function ($) {
    $.fn.lSlide = function (options) {
        initLSlide(this, options);

    };
    function initLSlide(item,options) {
        var defaults = {
            nTop:-0.71
        };
        var opts = $.extend({},defaults,options);
        var _self = $(item);

        var timeId = -1;

        timeId = setInterval(function () {
            // 动画往上移动距离，单位为px
            _self.animate({top:opts.nTop + "px"},function () {
                // 查到第一个子元素
                var  item = _self.children('li')[0];
                // 获取第一个元素
                var  fChild =  $(item).prop('outerHTML');
               // 将第一个节点拼接到最后
                _self.append(fChild);
                // 将第一个节点删除
                $(item).remove();
            });
            _self.animate({top:0+ "px"},0);
        },1000);

        // 点击今日中奖名单停止轮播
        _self.on('touchstart',function () {
            clearInterval(timeId);
        })
    }
})(jQuery)