'''JS代码，描述内容加密的参数和过程
          , f = d.a.enc.Utf8.parse("jo8j9wGw%6HbxfFn")
          , m = d.a.enc.Utf8.parse("0123456789ABCDEF");
function h(t)
{
    var e = d.a.enc.Hex.parse(t)
    , n = d.a.enc.Base64.stringify(e)
    , a = d.a.AES.decrypt(n, f, {
    iv: m,
    mode: d.a.mode.CBC,
    padding: d.a.pad.Pkcs7
}) \,
    r = a.toString(d.a.enc.Utf8);
return r.toString()
'''
import json
import requests
from Crypto.Cipher import AES

data = '95780ba0943730051dccb5fe3918f9fe1b6f2130681f99d5620c5497aa480f13068063ac378e2b22caa5bb9dfd753cdfc5e3e7970c1c42cd2a329175a20ff189d767bbb15783ec2788514321fbd15912c2605cb412f9da2effa938b6e965697dd4eb0c3dd446fa74f442a555e8113669869e0c74d3ea1ebc64d57474386bc4f95148a1ebb3241b420d1e19c674c9299644724a15d1b6add7d11944e08810b676f5e6cd39b45e63f0a7ae0a7219221e3828702fe3fab6a2d6f71d599b15c1d32e2dc217f901d0a3444ffbd2d4bd9652d49e7d152c4b4e8b993046bb33af2e81f01434394d3c56e01297fa8dd8ddedc1ff066c112f8a9717056c220f619bdbb3887cd13ccd2d68a9eda6f53008189b82ccc47b61ea18ed634c0f29973c4de8a2645edef20d3a031bc1e54fb8814b49d3a102d72f42d5596158a00226be2654fe7bcb054dbeb6dfc91c3337e16da02195a5ac6d6253371a1a4e5ecbfbe7914b659202ac13aad7f63a21d58d48dc287e78fc84b47f8d6f517bc27e071811636d8b2a650d5b2251e883b1d66f3269c91c1b6909f94a5178488b0950dd35e83bef491bd56b7d8c44364c86d833f3dd14f73bdd144a05d82e2ae093fbea7c52050dfb3498b1ed06dfda465afbc5b9f21a3b80dca4d56c9ab808928005e768c3d0242e966bc4eec6f0fec84fe29510ea48695a0af1f62922f514d20f93221a90389d8d1e3235adeab4efcbf1b3895e5fb54424ef802794f15ca5d70cf06421062645cd43ee72d4d7cc1e0bae2b739cbee45333bafd6c85f94e0702ab900d22da356194bbcdc9d179d84d5e712983b3c06a3d500eb220109e5f23a9cf6c585a4f65f6dfe4edf2f02fc800e39a458c220df89ccee7abdb8d009d4825da5c47bdd1b4663f8444afee856a0ec3ecae968cb48e9b16ddb2c43a2360f0d556d84b29b6f2ea834f79783929cceb01db888338e68f6581d87e2c066aa9ca94caf6aeeac081de22734bbc8ebea96c59fb10c6f498f22c1efcc89f10320d788f11e62214ba365ace067e71caf7c39da639a9ad6178c79f4b89aabf19307a2b66f3f32550680eba70f162f4142b30fd31bb3b826afe83e8cf107629b927b858f7dfc8645d09f6c75d6b98dbd8b5fb957d59a63a3108573e06e4818989f08663c3fa91e84b40980808ad36111d180a68bea09bf78c6226488f9e292a5a45ba19c9a2d6b0d5638690e43aa10b11946d3214bec92945d000e6c79beeb1d2c5fd56736cfd36dfd0cf4ceff88552658006da7753f6b6fdc20c6586ce2380a05896d4e95c5b619c1eef39b694c3506cf0b7bb4df0a355a874485c556cbf433772347ac37a177d9ce8b6bcae2ac34f9dc1e127e4eb913c5e8495f45c9653ca11dab69022587b1497308e3c15a61ccba765f11aec4f7921004e7286ab54ce846c6a36532bb0faf28e7d2db52c5474a61da1d6afff979f57fb7d681cfc9ce8a842b4a14b5f480d0463ce9dfba6871371a2740d13364ef4a035556b69f0a1b7e404624cde8675b8774ed99916bb75756bdeaeadd18453662e07a164a2e91cd04c12c8ea2f77c66f88b79e33fec73953b56eb7e8b37194e5e527f11faeabb4054096657155dbde1d08ca4a014c22560e4937500d9f1c87cd335533e3bafdea41a1c9c6b58170a65a4b53b01def2cb8f180a581f8cbb5dcbff39781cb083aa23e8a12fb3a7648119932f55e270b46f7ed8735fa9349fb99e4bdccb9ddc30d6a2e341aa353f69e41161e663cd5752fb09c90b9759d01d7a16f58870c411e6326503ec4dc967b5cff6e6f45fa7f001da2604312bae5e4f380e31a14feb52c093a73dd8bd674a31c08212974c7a7fafdbbdd5c582059919667c967efd2354638652ff77d7bfc29523c15baffa0b262b2399085294e56e058918fac07e411a9045c0e97975eaddf0ecf7a7dbf507636c009fdbfeefed927e0fe9b97dcbc6d002b2844f09f72090ec9c62fbf8c50f3ffce331d1ccb20f98f865effd34eecd1633cdf0f5396c966cb1f1c3efe1d38e5bdd8c1bacf565e9047bd36c95e1e18313a7de4584915132951c20e77d3e12beaef333d2bcb18a7b7eb91d07b9fe51f7f355e97d13078bde19dea3b0e52f7e17154a896bab9c2ed98fc9887ad4deb37ba5bb4069a4a4794b09b4ab381b35e38d084fe18aea4fb347de0945c2b6046c56fc63eb06ce2c39717f392ce3c3fd5dbf18a17b014e4bc79cb1cc04a93e8f6c9d9a74e513de0b5811f4994618e70038ee5913c444803ff6b860284c8f03bed82ff803b84bdead0e9307ab313a98ff47b320358ed8dac0bd7a49c9d9881bcf869c2c9a84840b52319015d1fc968f13d128b07bddf0a456c39f61fd431e996759525ee732d293c20b2f980edb80929f38398ff4a0013148bc7627cafe0c07488a60c4f5b89bfbc3253b7deaf0b9f2438c96748fda05f4b6e32ec66594e5684b6d4d45a2169696ae85bc9d198b138946e48f07229e6336b23af30f64a4312c29572eeac11ab7bcd87f1c019a7c39aee3ce0fc4ba27b217e9258812b9bc925966cec99b3887ec38c3523864d332decac2d6c9cc8c7a81422c3a6577b8877ee7ed90fff1f6689f13f24061b63ecf6cc81cdcca907c57d4390f72a2b10413ddfb139dd926db077f95f6e41183d32e4f17c54f326077c16c20c80f19fe9a5448531d0e0f4f1be60fb4504ef54a6b55d2dc125f12006aecb3abdcd49d68e74367a1de8d22bc9396f4431ad3875a99b5834c69cc9d0d2b7fb65ec92e49d7203153b50f4d8b310efe6508dcb047f958f2174ce2d82193ec21adcb5b03ae13e0d57e41f0fcd953983359c666c129dee80b4f90298e864352bf64aff790223ec9e65e7d4537a2060bfc2799293fe70c6ba6fda8a6f3126bef87a5931668d10be6dc18342b51eb23c17dfa60e4d2fb50bc06a04d8749f04c75f6906be07d0bda7e0950b25a0788e43357b4f808be37122ebd3204664860a145eb36a35963a06168596e6d2b4a52eeccd05f47fee5a7772989d35f23a730bc974b9cc9f31cd8282ff31b15225946def949677596097ea8689d60c2980563804e822450deb939b683857596d78a8716d19b135517935af3e0dc92c53933daf61ef6865e80c5c17e514c211b243c6322ae75e2f944a17a29700b274c26b5bc10bf0d704105d81be5f6dddea5664d6e37b5e0d68629b4266485bbdfc624c6a461dc512c37c44758ae721c50f6cbca1b5a2195fdaed4fb6449fcb500445bb7d92e78300c2959fc4626837d31c427f1b2c00ac39047c514c2426fd4d13c92f40b508eea2c16a0334354b13ecc06090eb1711b9778ee7fb6dc4ec5a371cb864a668c447667d66fbee2090b175a38dea40095128d786885897365c84e4e6b1a3266a5f392cb4a5dfdc734d1fe484a253a657d4c65edc3674c985bef597c0b99cba913828f22226518b9d8d53ce6cac51c6ac843182c9615eec6399b14a21b5c2d0c1ecc3e041351b34ec9faf495366074febf287c93f82abc80d9c5d18430cff0c54ef3f5d0e216673642cb52a475e926281e6237c42932da78478f8fd046ae2df5fd899aad63722129c6a55bde2dfd17b171be8756d2b84b253adbc0d52b44a195351a0c758d858541a8d6d9a5604d2fed14b8d6ac03d834a3568f74a4ba12df13aa3825483a8c4a0d3122ae55ec5725b3343f72e1420756c166782ba91fb4866d2830f65f757830e824cb59950293b2cbe30d339708166e6da57c6f9b9ca04e13ceaddb25b2692b1c92477cfaa724e70829fb5ff5d6699dd87ac73ddab6f59cc9c54675f0311dd90b6a11b4ede5a17bbaf9570eff8e7e86b4cbf506362ff42beb55b71ba3452de851655cb0fe0349805bdd4f5896b7763a89fe5e62c9fb3461a52cc626b3b99b48a016b54ab7789f81eedb1b26832bb72ab4d82314cd9c11c186d9ae00abd796317186346bb01d3565d5912587712794cf3c1aef24c20d3f371b69f019cfd0582e585eb13fbe39700bd4ecb084a68be6f1933c5dd9cf565dd14eb28982249932a30e4d280edc704a5d21e0e5cacfd5551a174033e4511fa579ab9f98dafba2639c8c85a7dbddd1550cc273c3c0b4f4b6cf1624089351712d2e5b26fb659cfba498de08a0cafc03c5a3e1ad73a8fc74cef34d26878ca069d9ccbe461f0f9c85490601a0d8cb09447d049ff06f51ef7a4324d8137736d212b9b21a49632da1b20768c2d1ab7eb2b7a40e3b7b243e3e4317ca3486c803aad9e8aafcbbc6372115ea8fd0a97caa66db9a253e29f97f17196202c1416d79ee69dba5b3dfc4f03cfb2fce30443fcd77512496a788fe480c714208c8624a826cb5d2c2ce0330872770f450f4044ea18f1f842d94aa6320f7c840f6d1143edc4be6b338b204c00476444f2ab0940347457df4c2e95dd3ba6b30ffe2ab0ed7195ebee61993d1de2f1eda2ea044e31b0ef1be50e80e1074a592a93e0bed0d3c7964e4737100d355c5db4fd38b4a6715bd16ab91468906884fea78e21d90cf278c5f76edc03675bb511549614014efe876cd0d6b0a6dfa43360aff05f5b172590e4abddb74bff42d1bdf5188fabd9c88b7be9680ad883bacb705a89361e00431978a83b19a60be5a643ac521ca11bd9b52dd1ca691d92fd715ff18590adecb621be00bfe73ee17478fff5df6dade2b007bf6e1738e3b610396ddebc442525334256f12badd8b638adf872173f6c117c91bee372d5ac3b6e84aff275831c43faa4f86ee6bf5f021d01e4df08552462003521bd93154b0046194d7ef24cf6afab23dae94711dcd6618ddf73f338ddf2ccb1e73e9c9237bdea9c439109a178e52b3dc9ecec1de34cb329dc4b21055882a746b56625caa192b9b16f68075aeeea17e9c3d9bd7ad4a687369873ed6ad3d14161174bf9edca666a2202c495c784e03a1ec1157e9fce3febe8096d4d77c3f53f6434eeb897cdc46d070c8ca8ec494b8d433e0a779f1c28efb6ed645447ce3ddaae68ed2f19f5930103ff45bccec3897b5f414971ab5ea63758f7b59be6024c1affd03d96f501861b42a798d9bf322bd33cec3254673fcfd7e2b852d41b9737518bb6dec0e2ce549223ca54ca18c7634ac174c875b7b63af89cb6ee5227fecea1d4816939e1e8fe788fea6273f318787f5c6b4e46961dd6561f5d78c7b22096b8ddb87493fe9ec8b259bd741dc2dafd7c9fda3fb822289a14124caec67bc08b580214f6f63d54bd80264510d1aab1d7ece574387b0d9d79799975e1ae85a1ac6fcffc31a68d6f8a9d167e719c5631a987f6ef34cf4c2c9925497b3b8c8aa78c5c28ea9629b37b7ff0cfc5068da4ecca018c452de821aebf1ff8a1af364d25849470ec3284ba276a37381c0baeba2c30f906f8cc8bb1c7ddcf5cbfa59031263100e609deb29be26508e746c1eaa61cbc540423e695344f94bcaaea588270ea7750ef1b0c9878162d7ea1324514619ed34dcff83bcc7b7789a5d36bbf598aea7f5bb48c6b0794e3338d1c2c9a9ce8c8f0a5133cf0b873602a24591c7ec687f91465c3f1f9b0b3dfb4b8b4817e9b693c3dafe5940b8666e6bbb26faca187dd4e37897e0743143c7c46a7bacf3f5fd5aedce02dbcc261e5d11622b76d6b364e01b7e8e2cba60c5228c75de346fa2192b63c7656c107183801404e2d17cd6086781b20b2358fc315851eedb3adf7adcb7aaefbe82b2112b3b1055ad6c760083424393c9f633ae9b2901530c5fe5e2bfa589532510593de8309e2dc60d3a0e2b2c1882b3303fd6b14419240dbf296d876280dc160ab44bae55f8ab5055b2b2a4520b906406e6560d2accf6b9368bd7b3196cff2cee84988c7749d3a0bc9e13b0641ad681afb5f9e3c25c33287b7abff7547b5ce47b2a22169fd513c91dd45438fa3c4ef0c1c82e48afe87158407e70c9365ed737bda8927af7a45b81c648a1b03854cca7e25368f974dc97c88d47ba026061d8d2066734bd78a31a9988cb8cb92e6e474e65a3949e2b8b8ea40a5541633d88224208018e300e668f8e4d6439a9eda429431c257856c49e043769744aceb0025f219fd148b435a6511c114306ba0064c1e91eb2c081687ef148483c4ba410f48ea925028092311265c110fb84c2fdc805fbd58da269752bf09e90d635e6498da89510128a62a1ef46c01a518a13863ba9201ea06850beb4a6408d72358331a3d24e73cd9479f3ad031278c9425106a6dee78e9c82ac2404a54e30ed9b61909d915c0c779c92df8badf2585bf689dcc42a0421f1cdc05142347aa268cbaee4b809460877ab75dd19e6c888e03ddb7cc41655ad2d0db86d8d4cb64b19f775943ad53c2f1f2a14dfb7bb8ba02fe144c5a90affb8b934dad4be957ec0c17b5f763e38a538137683f94d75281ebbfe305e965bc7504dfb4ade0693c00dc36a4799394a40d149d0043631dc5c5145ce01fe19d65cd0fbb61b5804fbf063622385b3b462050f5af71ec578f3b04efd6f65c141363d66660a4c9cdb623d92ac28cf7d73e6bea33ffffd95045ec88e77c00260d8e288b77a2ee3a08511bb52d432ba7bbcc16073bb9bc11126f1258bad4d487147a588a929fd8d6972549b40988000fdb2711f3aaa1c4b39798ee5343'

url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg=0&pgsz=15&total=0'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
}

response = requests.get(url, headers=headers).text
f = 'jo8j9wGw%6HbxfFn'  #  密钥
m = '0123456789ABCDEF'  #  偏移量

# 使用UTF-8进行转码
f = bytes(f, encoding='utf-8')
m = bytes(m, encoding='utf-8')

f1 = b'jo8j9wGw%6HbxfFn'
m1 = b'0123456789ABCDEF'

# 创建一个AES加密算法对象
cipher=AES.new(f,AES.MODE_CBC,m)  #  f:密钥key，AES.MODE_CBC:模式，m:偏移量

# # 解密  gbk编程 转utf-8编码  128  192?
decrypt_content=cipher.decrypt(bytes.fromhex(response))
result1=str(decrypt_content,encoding='utf-8')

# PKCS7填充JavaScript
length=len(result1)  #  字符串长度
unpadding=ord(result1[length-1])  #  得到最后一个字符串的ASCII
result2 = result1[0:length - unpadding]

result3 = json.loads(result2)['data']['list'] # dupms json.dumps()  dict  格式 json的

for i in result3:
    print(i)
