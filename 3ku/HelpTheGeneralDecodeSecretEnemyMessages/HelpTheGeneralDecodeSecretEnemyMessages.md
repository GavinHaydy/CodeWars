# url
 [HelpTheGeneralDecodeSecretEnemyMessages](https://www.codewars.com/kata/52cf02cd825aef67070008fa)
 # Chinese
 ``` shell
帕特隆将军面临着一个问题，他的情报截获了一些来自敌人的秘密信息，但它们都被加密了。 这些信息对于抓住敌人并赢得战争至关重要。幸运的是，智能也捕获了一个编码设备。 然而，即使是最聪明的程序员也无法破解它。所以将军问你，他最奇怪但最聪明的程序员。

您可以像这样调用编码器。

encode("Hello World!")
我们的加密分析师一直在研究它，并发现了一些有趣的模式。

print(
encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(
encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(encode("!@#$%^&*()_+-"))
a,b,c = "", "", ""
for w in "abcdefghijklmnopqrstuvwxyz":
    a += encode(  "" + w)[0]
    b += encode( "_" + w)[1]
    c += encode("__" + w)[2]
print(a)
print(b)
print(c)
我们认为，如果你继续沿着这条路走下去，你应该能够破解密码！ 您需要填写

decode
功能。 祝你好运！一般赞助人指望你！


 ```

 # English
 ``` shell
General Patron is faced with a problem , his intelligence has intercepted some secret messages from the enemy but they are all encrypted. Those messages are crucial to getting the jump on the enemy and winning the war. Luckily intelligence also captured an encoding device as well. However even the smartest programmers weren't able to crack it though. So the general is asking you , his most odd but brilliant programmer.

You can call the encoder like this.

encode("Hello World!")
Our cryptoanalysts kept poking at it and found some interesting patterns.

print(
encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(
encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
print(encode("!@#$%^&*()_+-"))
a,b,c = "", "", ""
for w in "abcdefghijklmnopqrstuvwxyz":
    a += encode(  "" + w)[0]
    b += encode( "_" + w)[1]
    c += encode("__" + w)[2]
print(a)
print(b)
print(c)
We think if you keep on this trail you should be able to crack the code! You are expected to fill in the

decode
function. Good luck ! General Patron is counting on you!
 ```
