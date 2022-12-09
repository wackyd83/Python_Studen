u.default.encryptToken(u.default.encrypt())
// 主体函数或者方法  参数（需要被处理的内容）
// u.default.encrypt()参数其实也是一个方法
// encryptToken 主体加密方法
// default

// 生成参数的方法
 {
    key: "encrypt",
    value: function() {
        var t = this.getTokenStr()
          , n = this.getQtTime((0,  // 获取一个时间戳
        s.default)(this.dencryptCode(this.qtTime)))
          , r = n % 2;  // 取模（取余）
        return this.encryptFunction()[r](t + n)
    }
}

// 主体加密方法
{
    key: "encryptToken",
    value: function(t) {
        return (0,
        f.default)(t).toString()
    }
}

// 获取一个字符串（前端的HTML返回的  id选择器来获取） encrypt=>t  cookie QN48
{
    key: "getTokenStr",
    value: function() {
        var t = this.dencryptCode(this.tokenStr);
        var n = document.getElementById(t).innerHTML;
        return n ? n : (0,
        s.default)(this.dencryptCode(this.cookieToken))
    }
}

 {
    key: "encryptFunction",
    value: function() {
        return [function(e) {
            var t = (0,
            u.default)(e).toString();
            return (0,
            f.default)(t).toString()
        }
        , function(e) {
            var t = (0,
            f.default)(e).toString();
            return (0,
            u.default)(t).toString()
        }
        ]
    }
}
