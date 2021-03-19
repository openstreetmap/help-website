+++
type = "question"
title = "How to show ssl decrypted packet content"
description = '''I have tried: tshark n -o ssl.keylog_file:/tmp/master.txt -Y ip.src==xxx.yyy.nnn.mmm -d tcp.port==0-999999,ssl I see this Capturing on &#x27;eth0&#x27;   6540 56.156992382 xxx.yyy.nnn.mmm -&amp;gt; 192.168.1.2 TCP 74 7072 → 49188 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1380 WS=256 SACK_PERM=1 TSval=603635523 TS...'''
date = "2016-01-12T11:51:00Z"
lastmod = "2016-01-14T03:03:00Z"
weight = 49141
keywords = [ "ssl", "parameters", "tshark", "dump" ]
aliases = [ "/questions/49141" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to show ssl decrypted packet content](/questions/49141/how-to-show-ssl-decrypted-packet-content)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49141-score" class="post-score" title="current number of votes">0</div><span id="post-49141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried: tshark n -o ssl.keylog_file:/tmp/master.txt -Y ip.src==xxx.yyy.nnn.mmm -d tcp.port==0-999999,ssl I see this Capturing on 'eth0'<br />
</p><pre><code>6540 56.156992382 xxx.yyy.nnn.mmm -&gt; 192.168.1.2  TCP 74 7072 → 49188 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1380 WS=256 SACK_PERM=1 TSval=603635523 TSecr=10839353                                              
6546 56.291147285 xxx.yyy.nnn.mmm -&gt; 192.168.1.2  TCP 1434 [TCP segment of a reassembled PDU]              
6548 56.293045394 xxx.yyy.nnn.mmm -&gt; 192.168.1.2  TCP 1434 [TCP segment of a reassembled PDU]              
6550 56.294313103 xxx.yyy.nnn.mmm -&gt; 192.168.1.2  TLSv1 1300 Server Hello, Certificate, Server Hello Done  
6560 56.343469786 xxx.yyy.nnn.mmm -&gt; 192.168.1.2  TLSv1 125 Change Cipher Spec, Encrypted Handshake Message
6575 56.785954188 xxx.yyy.nnn.mmm -&gt; 192.168.1.2  TLSv1 231 Application Data</code></pre><p>How can I dump the packet content as "follow tcp streamm" in wireshark already does ?</p><p>Is it possible to use something like as described in <a href="https://isc.sans.edu/forums/diary/Psst+Your+Browser+Knows+All+Your+Secrets/16415/">https://isc.sans.edu/forums/diary/Psst+Your+Browser+Knows+All+Your+Secrets/16415/</a> in such a way as to have a file decrypted packets in real time ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-parameters" rel="tag" title="see questions tagged &#39;parameters&#39;">parameters</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-dump" rel="tag" title="see questions tagged &#39;dump&#39;">dump</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jan '16, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/306d7986d36750697c633864525d3775?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="famedoro&#39;s gravatar image" /><p><span>famedoro</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="famedoro has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jan '16, 00:01</strong> </span></p></div></div><div id="comments-container-49141" class="comments-container"><span id="49189"></span><div id="comment-49189" class="comment"><div id="post-49189-score" class="comment-score"></div><div class="comment-text"><p>Lacking your capture and the keys, I cannot answer you, I can only give a hint. I've tried with https sample capture, where you need to set a link to a file containing the RSA decryption key to get the payload decrypted, and I am not sure whether the keylog file is used the same way.</p><p>As the mappings between IP, port, payload protocol and RSA key file are not stored in the preferences file but in a separate one, they cannot (to my knowledge) be handed over to tshark using the <code>-o</code> parameter. But if you define these mappings using Wireshark, they get stored and tshark will use them too, without any options telling it to do so.</p><p>Now another point, the dissector to be used to the decrypted payload is not chosen automatically based on the tcp port of the encrypted packet; instead, you define it together with the mapping between ip,port, and rsa key. If you set it to "http", you'll have no single protocol field to output. So I'd recommend to set the payload "protocol" to <code>data</code>, and if you do so, you can use tshark options <code>-T fields -e data</code>. This way, you'll get the decrypted payload as hex stream without any separators. I.e. an <code>Abc</code> string in the decrypted payload will be output as <code>416263</code>.</p></div><div id="comment-49189-info" class="comment-info"><span class="comment-age">(13 Jan '16, 13:13)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="49200"></span><div id="comment-49200" class="comment"><div id="post-49200-score" class="comment-score"></div><div class="comment-text"><p><span>@sindy</span> I have already shark n -o ssl.keylog_file:/tmp/master.txt -Y ip.src==xxx.yyy.nnn.mmm -d tcp.port==0-999999,ssl -T fields -e data and in this case does not show any information. Is it possible to use something like as described in <a href="https://isc.sans.edu/forums/diary/Psst+Your+Browser+Knows+All+Your+Secrets/16415/">https://isc.sans.edu/forums/diary/Psst+Your+Browser+Knows+All+Your+Secrets/16415/</a> in such a way as to have a file decrypted packets in real time ?</p></div><div id="comment-49200-info" class="comment-info"><span class="comment-age">(14 Jan '16, 00:03)</span> <span class="comment-user userinfo">famedoro</span></div></div></div><div id="comment-tools-49141" class="comment-tools"></div><div class="clear"></div><div id="comment-49141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49193"></span>

<div id="answer-container-49193" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49193-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49193-score" class="post-score" title="current number of votes">0</div><span id="post-49193-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To decrypt, as mentioned by <span>@sindy</span>, you must enter the key info into the SSL RSA Keys list preference in Wireshark. This will create a ssl_keys file in your preferences directory. Once this has been set up tshark will decrypt the SSL data.</p><p>For example, using the <a href="https://wiki.wireshark.org/SampleCaptures#SSL_with_decryption_keys">snakeoil sample capture</a> you must enter the following into the SSL RSA Keys List preferences:</p><ul><li>IP address - 127.0.0.1</li><li>Port - 443</li><li>Protocol - http</li><li>Key File - path to rsasnakeoil2.key</li><li>Password - leave blank</li></ul><p>Loading the rsasnakeoil2.cap file into Wireshark should show the decrypted HTTP traffic. If successful, tshark can then be used to dump the stream using the <code>-z follow, ...</code> argument, e.g. to dump the hex and ascii of ssl stream 1:</p><pre><code>tshark -r -rsasnakeoil2.cap -q -z follow,ssl,hex,1

===================================================================          
Follow: ssl,hex                                                              
Filter: tcp.stream eq 1                                                      
Node 0: 127.0.0.1:38714                                                      
Node 1: 127.0.0.1:443                                                        
00000000  47 45 54 20 2f 69 63 6f  6e 73 2f 64 65 62 69 61  GET /ico ns/debia
00000010  6e 2f 6f 70 65 6e 6c 6f  67 6f 2d 32 35 2e 6a 70  n/openlo go-25.jp
...</code></pre><p>If you just want the raw hex without the offsets and ascii, use <code>raw</code> instead of <code>hex</code> in the <code>-z argument</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '16, 15:59</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-49193" class="comments-container"><span id="49199"></span><div id="comment-49199" class="comment"><div id="post-49199-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> Is it possible to use something like as described in <a href="https://isc.sans.edu/forums/diary/Psst+Your+Browser+Knows+All+Your+Secrets/16415/">https://isc.sans.edu/forums/diary/Psst+Your+Browser+Knows+All+Your+Secrets/16415/</a> in such a way as to have a file decrypted packets in real time ?</p></div><div id="comment-49199-info" class="comment-info"><span class="comment-age">(13 Jan '16, 23:59)</span> <span class="comment-user userinfo">famedoro</span></div></div><span id="49201"></span><div id="comment-49201" class="comment"><div id="post-49201-score" class="comment-score"></div><div class="comment-text"><p>Not easily as you need to somehow retrigger Wireshark that the contents of the SSL key log file has changed, and then select the appropriate ssl stream.</p></div><div id="comment-49201-info" class="comment-info"><span class="comment-age">(14 Jan '16, 00:30)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="49204"></span><div id="comment-49204" class="comment"><div id="post-49204-score" class="comment-score"></div><div class="comment-text"><p><span>@grahamb</span> Must I use wireshark ? Is it possible to have a decrypted real time data stream using only tshark ?</p></div><div id="comment-49204-info" class="comment-info"><span class="comment-age">(14 Jan '16, 01:02)</span> <span class="comment-user userinfo">famedoro</span></div></div><span id="49209"></span><div id="comment-49209" class="comment"><div id="post-49209-score" class="comment-score"></div><div class="comment-text"><p>The issue is not whether you use tshark or Wireshark, the issue is the dynamic nature of the session keys. *shark doesn't read the key log file each time it needs a value from it but only once when starting, that's why <span></span><span>@grahamb</span> wrote that you'd have to tell *shark that the contents of the file has changed (and choose the right tcp stream id).</p><p>As far as I know, there is currently no "input point for asynchronous events" allowing to tell a running *shark that it should do something, nor any "watch for changes" functionality of the *shark itself.</p><p>Normally you only need to decrypt ongoing communication in real time in order to take urgent measures based on its contents, and this is an activity which a typical *shark user doesn't perform too often. Those who need it usually work with an appropriate budget.</p></div><div id="comment-49209-info" class="comment-info"><span class="comment-age">(14 Jan '16, 03:03)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-49193" class="comment-tools"></div><div class="clear"></div><div id="comment-49193-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

