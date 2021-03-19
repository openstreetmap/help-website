+++
type = "question"
title = "TCP Delay packet"
description = '''Hi , Good day.. May i know the reason for delay below... Thanks &amp;amp; appreciate it... Client ( 192.168.19.175 : NAT IP 192.168.30.134 ) -----------&amp;gt; Server 192.168.5.34 PORT 9491 - Delay 11 sec ( Client )  PORT 9491 - Delay 11 sec ( Server )  - Why no POST at server like normal ?   =============...'''
date = "2016-11-10T16:01:00Z"
lastmod = "2016-11-11T03:49:00Z"
weight = 57286
keywords = [ "delay" ]
aliases = [ "/questions/57286" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TCP Delay packet](/questions/57286/tcp-delay-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57286-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>Good day.. May i know the reason for delay below... Thanks &amp; appreciate it...</p><p>Client ( 192.168.19.175 : NAT IP 192.168.30.134 ) -----------&gt; Server 192.168.5.34</p><p>PORT 9491 - Delay 11 sec ( Client ) <img src="https://osqa-ask.wireshark.org/upfiles/Client_11sec_-_Port_9491.jpg" alt="alt text" /></p><p>PORT 9491 - Delay 11 sec ( Server ) - Why no POST at server like normal ? <img src="https://osqa-ask.wireshark.org/upfiles/Server_11sec_-_Port_9491.jpg" alt="alt text" /></p><p>======================================================================================</p><p>PORT 9522 - Delay 7 sec ( Client )</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Client_7_sec_-_Port_9522.jpg" alt="alt text" /></p><p>PORT 9522 - Delay 7 sec ( Server )</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Server_7_sec_-_Port_9522.jpg" alt="alt text" /></p><p>===============================================================================================</p><p>PORT 9470 - normal ( Client )</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Client_-_Port_9470_-_normal.jpg" alt="alt text" /></p><p>PORT 9470 - normal ( Server )</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Server_-_Port_9470_-_normal.jpg" alt="alt text" /></p><p>====================================================================================</p></div><div id="question-tags" class="tags-container tags">delay</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '16, 16:01</strong></p><img src="https://secure.gravatar.com/avatar/b8cbaa9ee7d5bf40e4c8f703e3197880?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="suarez123&#39;s gravatar image" /><p>suarez123<br />
<span class="score" title="1 reputation points">1</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="suarez123 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-57286" class="comments-container"><span id="57288"></span><div id="comment-57288" class="comment"><div id="post-57288-score" class="comment-score"></div><div class="comment-text"><p>Investigating a problem from a mere screenshot is a pain, not having the full power of Wireshark available. Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-57288-info" class="comment-info"><span class="comment-age">(10 Nov '16, 22:08)</span> Jaap ♦</div></div></div><div id="comment-tools-57286" class="comment-tools"></div><div class="clear"></div><div id="comment-57286-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57304"></span>

<div id="answer-container-57304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57304-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Based on a quick view of the screenshots it looks like packetloss resulting in retransmission timeouts are the culprit, but without proper analysis of the TCP SEQ and ACK values this could be a faulty assumption. So please do supply the tracefiles as Jaap mentioned.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '16, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></img></div></div><div id="comments-container-57304" class="comments-container"><span id="57349"></span><div id="comment-57349" class="comment"><div id="post-57349-score" class="comment-score"></div><div class="comment-text"><p>Thanks Syn-bit .. i unable to share since it related to confidential data.... May i knwo how to check the TCP SEQand ACK... thanks</p></div><div id="comment-57349-info" class="comment-info"><span class="comment-age">(12 Nov '16, 19:54)</span> suarez123</div></div><span id="57352"></span><div id="comment-57352" class="comment"><div id="post-57352-score" class="comment-score"></div><div class="comment-text"><p>Have a look at <a href="https://www.tracewrangler.com">TraceWrangler</a>, specifically made for this situation.</p></div><div id="comment-57352-info" class="comment-info"><span class="comment-age">(13 Nov '16, 01:36)</span> Jaap ♦</div></div><span id="57367"></span><div id="comment-57367" class="comment"><div id="post-57367-score" class="comment-score"></div><div class="comment-text"><p>Just wrote this tutorial to help:</p><p><a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/</a></p></div><div id="comment-57367-info" class="comment-info"><span class="comment-age">(13 Nov '16, 12:58)</span> Jasper ♦♦</div></div><span id="57368"></span><div id="comment-57368" class="comment"><div id="post-57368-score" class="comment-score">1</div><div class="comment-text"><p>@jasper yes, this will be helpful.</p></div><div id="comment-57368-info" class="comment-info"><span class="comment-age">(13 Nov '16, 13:54)</span> Christian_R</div></div></div><div id="comment-tools-57304" class="comment-tools"></div><div class="clear"></div><div id="comment-57304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

