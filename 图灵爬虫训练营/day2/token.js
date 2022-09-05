var iJ = function (je) {
    var jd = [];
    // 获取键进行排序a-z
    var ck = Object.keys(je).sort();
    ck.forEach(function (jf, bx) {
        if (jf !== _$_543c[136] && jf !== _$_543c[137]) {
            jd.push(jf + _$_543c[122] + je[jf])
        }
    });
    jd = jd.join(_$_543c[121]);
    // 生成jd=>由jx处理后生成
    // iI处理jd,生成拼接请求参数（排序过的）
    return iI(jd)
}

var iI = function (jc) {
    // JSON.stringify() js对象转换成字符串
    // 压缩方式：二进制压缩 十六进制压缩
    // zip rar 文件压缩方式
    jc = cD.deflate(JSON.stringify(jc));
    jc = iD(jc);
    return jc
}

var iP = {
    rId: Rohr_Opt.Flag,
    ver: _$_543c[138],
    // 生成2个相同的时间戳
    ts: new Date().getTime(),
    cts: new Date().getTime(),
    brVD: iN(),
    brR: iM(),
    bI: iL(),
    mT: [],
    kT: [],
    aT: [],
    tT: [],
    aM: iK()
}


iP.reload = function (jv) {  // jv  拼接的请求url+请求参数（不带token）
    var jw;
    var jx = {};
    //  判断生成jx
    if (typeof jv === _$_543c[91]) {
        jx = iO.parse(jv.split(_$_543c[146])[1])
    } else {
        if (typeof jv === _$_543c[2]) {
            jx = jv
        }
    }
    // iJ  处理jx
    // jx=>拼接的请求参数转变为键值对的格式
    ;iP.sign = iJ(jx);  // 第一次加密
    // 生成时间戳 覆盖前面生成的时间戳，产生不同的时间戳
    iP.cts = new Date().getTime();
    // iI处理ip，js生成的参数
    jw = iI(iP);  // 第二次加密
    // 判断
    if (Rohr_Opt.LogVal && typeof (window) !== _$_543c[0]) {
        window[Rohr_Opt.LogVal] = encodeURIComponent(jw)
    }
    ;
    return jw
}