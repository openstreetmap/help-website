+++
type = "question"
title = "Why can I no longer decode SSL traffic with Wireshark?"
description = '''I used to export decrypted SSL keys in txt format and store them on my C drive under the root directoryssl keys. I then went into Wireshark and added the path to the key under &quot;RSA Keys List&quot; - Example: 10.10.10.10,443,https,c:sslkeyswww-key.txt For some reason that no longer works and the only diff...'''
date = "2011-08-29T13:48:00Z"
lastmod = "2012-02-20T14:37:00Z"
weight = 5926
keywords = [ "decode", "ssl" ]
aliases = [ "/questions/5926" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why can I no longer decode SSL traffic with Wireshark?](/questions/5926/why-can-i-no-longer-decode-ssl-traffic-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5926-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5926-score" class="post-score" title="current number of votes">0</div><span id="post-5926-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I used to export decrypted SSL keys in txt format and store them on my C drive under the root directoryssl keys. I then went into Wireshark and added the path to the key under "RSA Keys List" - Example: 10.10.10.10,443,https,c:sslkeyswww-key.txt</p><p>For some reason that no longer works and the only difference I see is a slighty different way of entering that info with Wireshark 1.6.1...and the ability to include passwords (for encrypted keys maybe???). Has there been changes in how this is accomplished that I need to be aware of?</p><p>Any ideas what I might be doing wrong. Thanks in advance for any assistance...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decode" rel="tag" title="see questions tagged &#39;decode&#39;">decode</span> <span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Aug '11, 13:48</strong></p><img src="https://secure.gravatar.com/avatar/b8808bf25e90d7c20bf7b262198b6bd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rathskeller&#39;s gravatar image" /><p><span>Rathskeller</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rathskeller has no accepted answers">0%</span></p></div></div><div id="comments-container-5926" class="comments-container"><span id="5967"></span><div id="comment-5967" class="comment"><div id="post-5967-score" class="comment-score"></div><div class="comment-text"><p>Now I've tried the same trace file using the same SSL key with 2 different versions of Wireshark, 1.6.1 and 1.4.3. The earlier version works....the current version does not.</p><p>I can't believe this is a bug or someone else would've said something by now. I have to think it's something I'm doing wrong with the new format for entering SSL keys. It looks pretty simple and straight forward. The biggest difference I see is a table to fill out instead of a string....and....in the table I can't put https for protocol, I had to use ssl.</p><p>Is ANYONE loading SSL keys into Wireshark and decoding SSL? If so.......is it any different than the older versions?</p><p>I hate to downgrade my version of Wireshark to make SSL decode work but I might have to if I can't find anyone making the newest version work.</p></div><div id="comment-5967-info" class="comment-info"><span class="comment-age">(30 Aug '11, 12:17)</span> <span class="comment-user userinfo">Rathskeller</span></div></div></div><div id="comment-tools-5926" class="comment-tools"></div><div class="clear"></div><div id="comment-5926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5968"></span>

<div id="answer-container-5968" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5968-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5968-score" class="post-score" title="current number of votes">2</div><span id="post-5968-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There were two related bugs reported, which have not been verified yet:</p><ul><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6032">6032</a> SSL/TLS decryption needs wireshark to be rebooted</li><li><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=6033">6033</a> SSL/TLS decryption needs a "SSL debug file" in order to work</li></ul><p>Can you confirm that configuring the SSL debug file and then restarting wireshark does indeed result in your wireshark 1.6.1 to decrypt the SSL traffic?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Aug '11, 12:50</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5968" class="comments-container"><span id="6021"></span><div id="comment-6021" class="comment"><div id="post-6021-score" class="comment-score"></div><div class="comment-text"><p>Thanks much for the response, sorry so slow to get back...DMZ meltdown.</p><p>I do have an SSL debug file..<em>nodding</em>..and I restarted Wireshark...no help. I also renamed the debug file to .bak and tried restarting so I'd have a clean file. When I look at the file it tells me that the ssl keys were successfully loaded. However, when I open my test trace I see messages about not finding its key??</p><p>Example from debug file:</p><p>ssl_init IPv4 addr '172.24.65.100' (172.24.65.100) port '443' filename 'c:sslkeysolb-prod.txt' password(only for p12 file) '' ssl_init private key file c:sslkeysolb-prod.txt successfully loaded.</p><p>Then in the "dissect_ssl" portion I see..........</p><p>ssl_find_private_key server 172.24.65.200:443 ssl_find_private_key can't find private key for this server!</p><p>I know the key is good because I verified it and re-copied it to make sure it was okay. I'm using the same key with an earlier version of Wireshark and it works??</p><p>I still think there's a slight chance I'm doing something wrong but I don't know what.</p><p>Dane</p></div><div id="comment-6021-info" class="comment-info"><span class="comment-age">(31 Aug '11, 11:38)</span> <span class="comment-user userinfo">Rathskeller</span></div></div><span id="6026"></span><div id="comment-6026" class="comment"><div id="post-6026-score" class="comment-score">2</div><div class="comment-text"><p>Please use "Add Comment" to respond to earlier answers, that's the way this site works best (see the FAQ for details).</p><p>I hate the one to say it, but have another look at the IP addresses in your reponse.... I think you will be fine now :-)</p></div><div id="comment-6026-info" class="comment-info"><span class="comment-age">(31 Aug '11, 12:42)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="6044"></span><div id="comment-6044" class="comment"><div id="post-6044-score" class="comment-score"></div><div class="comment-text"><p>Arggg...(and thanks)......<em>slinks off</em>....</p></div><div id="comment-6044-info" class="comment-info"><span class="comment-age">(01 Sep '11, 05:50)</span> <span class="comment-user userinfo">Rathskeller</span></div></div><span id="8033"></span><div id="comment-8033" class="comment"><div id="post-8033-score" class="comment-score"></div><div class="comment-text"><p>FYI bug 6033 still applies to Wireshark 1.6.4. A debug file fixed my problem.</p></div><div id="comment-8033-info" class="comment-info"><span class="comment-age">(18 Dec '11, 14:18)</span> <span class="comment-user userinfo">kcd</span></div></div></div><div id="comment-tools-5968" class="comment-tools"></div><div class="clear"></div><div id="comment-5968-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="9150"></span>

<div id="answer-container-9150" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9150-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9150-score" class="post-score" title="current number of votes">-1</div><span id="post-9150-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I dont have an ip conflict and cannot get the SSL traffic to decode</p><p>Here is the debug log:</p><pre><code>ssl_association_remove removing TCP 8443 - http handle 000000000470FB20
Private key imported: KeyID bc:43:14:85:bd:de:53:9a:67:10:1d:f3:26:9f:b1:42:...
ssl_init IPv4 addr &#39;**75.147.121.41**&#39; (75.147.121.41) port &#39;**8443**&#39; filename &#39;C:\users\brian\projects\JoxPlz\demo\BaseManagerWan_SecureRawHttpSend\res\tomcat75.pem&#39; password(only for p12 file) &#39;&#39;
ssl_init private key file **C:\users\brian\projects\JoxPlz\demo\BaseManagerWan_SecureRawHttpSend\res\tomcat75.pem successfully loaded.**
association_add TCP port 8443 protocol http handle 000000000470FB20

dissect_ssl enter frame #4 (first time)
ssl_session_init: initializing ptr 0000000005FE1D30 size 680
  conversation = 0000000005FE1880, ssl_session = 0000000005FE1D30
  record: offset = 0, reported_length_remaining = 103
packet_from_server: is from server - FALSE
**ssl_find_private_key server 75.147.41.121:8443**
**ssl_find_private_key can&#39;t find private key for this server!** Try it again with universal port 0
ssl_find_private_key can&#39;t find private key for this server (universal port)! Try it again with universal address 0.0.0.0
ssl_find_private_key can&#39;t find any private key!
client random len: 32 padded to 32
dissect_ssl2_hnd_client_hello found CLIENT RANDOM -&gt; state 0x01</code></pre><p>The key is good as it is used in the transfer and is in correct PEM format; no password needed.</p><p>No idea what is wrong. Reboots, restarts, re-entries of parameters all lead to the same thing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Feb '12, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/d85cfde395796ff8d2093974f53173b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gyannea&#39;s gravatar image" /><p><span>gyannea</span><br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gyannea has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Feb '12, 14:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-9150" class="comments-container"><span id="9152"></span><div id="comment-9152" class="comment"><div id="post-9152-score" class="comment-score">1</div><div class="comment-text"><p>This is not an answer to the question asked. Please note that this is not a forum, but a Q&amp;A site (read the FAQ for more details).</p><p>I was going to ask you to ask this question as a separate question, but the answer is just too obvious: 75.147.121.41 != 75.147.41.121.</p></div><div id="comment-9152-info" class="comment-info"><span class="comment-age">(20 Feb '12, 14:37)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="9153"></span><div id="comment-9153" class="comment"><div id="post-9153-score" class="comment-score"></div><div class="comment-text"><p>You should post a new question for your problem as a) it's not an answer to the original problem, and b) it's not really related to the original problem, unless you too have misconfigured the addresses.</p></div><div id="comment-9153-info" class="comment-info"><span class="comment-age">(20 Feb '12, 14:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-9150" class="comment-tools"></div><div class="clear"></div><div id="comment-9150-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

