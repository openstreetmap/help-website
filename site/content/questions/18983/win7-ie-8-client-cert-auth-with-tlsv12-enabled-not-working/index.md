+++
type = "question"
title = "Win7, IE 8, Client Cert Auth with TLSv1.2 enabled NOT WORKING"
description = '''Hi All, I am troubleshooting the not working scenario in which we have sucessful client cert authentication from Win7, IE8 and TLS1.0 enabled - but as soon as in Advanced tab of Internet Options TLS v1.2 is also selected the communication if failing. Client&#x27;s machine has client certificate installed...'''
date = "2013-02-28T08:52:00Z"
lastmod = "2013-03-01T03:15:00Z"
weight = 18983
keywords = [ "ie8", "cert", "tlsv1.2", "win7", "client" ]
aliases = [ "/questions/18983" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Win7, IE 8, Client Cert Auth with TLSv1.2 enabled NOT WORKING](/questions/18983/win7-ie-8-client-cert-auth-with-tlsv12-enabled-not-working)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18983-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I am troubleshooting the not working scenario in which we have sucessful client cert authentication from Win7, IE8 and TLS1.0 enabled - but as soon as in Advanced tab of Internet Options TLS v1.2 is also selected the communication if failing.</p><p>Client's machine has client certificate installed, and also the root CA is installed in Trusted Root store</p><p>The process is as follows (with TLS 1.2 enabled)</p><ol><li><p>Client connects to the SSL server - the initial handshake works fine , and in the ServerHello we can see certificate request all right.</p></li><li><p>On the client side - there is a pop up with the list of client certs - user selects his cert and confirms OK</p></li><li><p>At this stage user getting "Page canot be displayed" message on IE . At the same time, looking into the trace and the communication being done from the client - the very starange thing is that there is no "ClientHello" being sent by the client (10.4.103.130).</p></li></ol><p>The initial TCP handshake looks ok, bu then client is finishing the connection, instead of staring SSL handshake by sending ClientHello....</p><pre><code>10.4.103.130    TCP 110     x.15.226.18   49984 &gt; https [SYN] Seq=2509215337 Win=32768 Len=0 MSS=1460 WS=1 TSval=4016368077 TSecr=0 SACK_PERM=1
x.15.226.18     TCP 92      10.4.103.130   https &gt; 49984 [SYN, ACK] Seq=2329522121 Ack=2509215338 Win=8190 Len=0 MSS=1460
10.4.103.130    TCP 86      x.15.226.18   49984 &gt; https [ACK] Seq=2509215338 Ack=2329522122 Win=33580 Len=0
10.4.103.130    TCP 86      x.15.226.18   49984 &gt; https [**FIN, ACK**] Seq=2509215338 Ack=2329522122 Win=33580 Len=0
x.15.226.18     TCP 92      10.4.103.130   https &gt; 49984 [FIN, ACK] Seq=2329522122 Ack=2509215339 Win=35688 Len=0
10.4.103.130    TCP 86      x.15.226.18   49984 &gt; https [ACK] Seq=2509215339 Ack=2329522123 Win=33579 Len=0</code></pre><ul><li>this has been checked on known working user cert and the situation is the same ....</li></ul><p>HAve anyone seen such a behaviour ?</p><p>What I am thinkg of is that TLS1.2 is not really enabled on the client machine.</p><p>Would this still apply ?: <a href="http://support.microsoft.com/kb/245030">http://support.microsoft.com/kb/245030</a></p><p><a href="http://derek858.blogspot.co.uk/2010/06/enable-tls-12-aes-256-and-sha-256-in.html">http://derek858.blogspot.co.uk/2010/06/enable-tls-12-aes-256-and-sha-256-in.html</a></p><p>Thanks for your input.</p><p>Andrzej</p></div><div id="question-tags" class="tags-container tags">ie8 cert tlsv1.2 win7 client</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 08:52</strong></p><img src="https://secure.gravatar.com/avatar/89941aca50bd896f00def88cf664f9de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrus&#39;s gravatar image" /><p>andrus<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Feb '13, 15:49</p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-18983" class="comments-container"></div><div id="comment-tools-18983" class="comment-tools"></div><div class="clear"></div><div id="comment-18983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19023"></span>

<div id="answer-container-19023" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19023-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This has been solved now</p><p>Combination of SSLv2 + SSLv3 + TLS1.0 + TLS1.1 - works OK</p><p>Combination of <strong>SSLv2</strong> + SSLv3 + TLS1.0 + TLS1.1 +<strong>TLS1.2</strong> - does NOT WORK</p><p>if want to have TLS1.2 enabled you need to disable SSLv2!</p><p>it appears to be some sort of IE8 bug .....</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Mar '13, 03:15</strong></p><img src="https://secure.gravatar.com/avatar/89941aca50bd896f00def88cf664f9de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andrus&#39;s gravatar image" /><p>andrus<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andrus has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Mar '13, 03:17</p></div></div><div id="comments-container-19023" class="comments-container"></div><div id="comment-tools-19023" class="comment-tools"></div><div class="clear"></div><div id="comment-19023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

