+++
type = "question"
title = "[RST , ACK] after [FIN , ACK] by client: is it normal?"
description = '''Sorry my question, I&#x27;m studying my TCP/IP connection with wireshark (first time) This is log packets:   No. Time Source Destination Protocol Length Info  404 10.145072000 192.168.1.2 173.194.112.111 TCP 54 aker-cdp &amp;gt; https [ACK] Seq=682 Ack=76019 Win=65536 Len=0  405 10.350617000 192.168.1.2 173....'''
date = "2015-12-24T10:37:00Z"
lastmod = "2015-12-24T11:06:00Z"
weight = 48702
keywords = [ "rst+ack" ]
aliases = [ "/questions/48702" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[RST , ACK\] after \[FIN , ACK\] by client: is it normal?](/questions/48702/rst-ack-after-fin-ack-by-client-is-it-normal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48702-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Sorry my question, I'm studying my TCP/IP connection with wireshark (first time) This is log packets:</p><p><code> No.     Time           Source                Destination           Protocol Length Info     404 10.145072000   192.168.1.2           173.194.112.111       TCP      54     aker-cdp &gt; https [ACK] Seq=682 Ack=76019 Win=65536 Len=0     405 10.350617000   192.168.1.2           173.194.112.104       TCP      54     qadmifevent &gt; https [FIN, ACK] Seq=357 Ack=4604 Win=65266 Len=0     406 10.350661000   192.168.1.2           173.194.112.104       TCP      54     qadmifevent &gt; https [RST, ACK] Seq=358 Ack=4604 Win=0 Len=0     407 10.350857000   192.168.1.2           173.194.112.111       TCP      54     lsi-raid-mgmt &gt; https [FIN, ACK] Seq=357 Ack=3828 Win=65266 Len=0     408 10.350876000   192.168.1.2           173.194.112.111       TCP      54     lsi-raid-mgmt &gt; https [RST, ACK] Seq=358 Ack=3828 Win=0 Len=0     409 10.351015000   192.168.1.2           173.194.112.119       TCP      54     seaodbc &gt; https [FIN, ACK] Seq=357 Ack=3828 Win=64568 Len=0     410 10.351033000   192.168.1.2           173.194.112.119       TCP      54     seaodbc &gt; https [RST, ACK] Seq=358 Ack=3828 Win=0 Len=0     411 10.385748000   173.194.112.104       192.168.1.2           TCP      60     https &gt; qadmifevent [FIN, ACK] Seq=4604 Ack=358 Win=45056 Len=0     412 10.388933000   173.194.112.111       192.168.1.2           TCP      60     https &gt; lsi-raid-mgmt [FIN, ACK] Seq=3828 Ack=358 Win=45056 Len=0</code></p></div><div id="question-tags" class="tags-container tags">rst+ack</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '15, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/8103ff29e1cf838f3c5ca71bb9634223?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wjll&#39;s gravatar image" /><p>wjll<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wjll has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Dec '15, 14:01</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48702" class="comments-container"></div><div id="comment-tools-48702" class="comment-tools"></div><div class="clear"></div><div id="comment-48702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48703"></span>

<div id="answer-container-48703" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48703-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Let me format your log for you (Kindly try to give packets in formatted form)</p><pre><code>192.168.1.2 173.194.112.111 TCP 54 aker-cdp &gt; https [ACK] Seq=682 Ack=76019 Win=65536 Len=0 
192.168.1.2 173.194.112.104 TCP 54 qadmifevent &gt; https [FIN, ACK] Seq=357 Ack=4604 Win=65266 Len=0 
192.168.1.2 173.194.112.104 TCP 54 qadmifevent &gt; https [RST, ACK] Seq=358 Ack=4604 Win=0 Len=0 
192.168.1.2 173.194.112.111 TCP 54 lsi-raid-mgmt &gt; https [FIN, ACK] Seq=357 Ack=3828 Win=65266 Len=0 
192.168.1.2 173.194.112.111 TCP 54 lsi-raid-mgmt &gt; https [RST, ACK] Seq=358 Ack=3828 Win=0 Len=0 
192.168.1.2 173.194.112.119 TCP 54 seaodbc &gt; https [FIN, ACK] Seq=357 Ack=3828 Win=64568 Len=0 
192.168.1.2 173.194.112.119 TCP 54 seaodbc &gt; https [RST, ACK] Seq=358 Ack=3828 Win=0 Len=0 
173.194.112.104 192.168.1.2 TCP 60 https &gt; qadmifevent [FIN, ACK] Seq=4604 Ack=358 Win=45056 Len=0
173.194.112.111 192.168.1.2 TCP 60 https &gt; lsi-raid-mgmt [FIN, ACK] Seq=3828 Ack=358 Win=45056 Len=0</code></pre><p>This behavior is not RFC compliant but seems that google.com(Dst IPs belong to google) is not willing to terminate connection gracefully, may be because of excessive load on its servers. This behavior is tolerable</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '15, 11:06</strong></p><img src="https://secure.gravatar.com/avatar/0032ac169dfa9b4487cca759adaf8097?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Muhammad%20Irshad&#39;s gravatar image" /><p>Muhammad Irshad<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Muhammad Irshad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Dec '15, 14:01</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-48703" class="comments-container"><span id="48705"></span><div id="comment-48705" class="comment"><div id="post-48705-score" class="comment-score"></div><div class="comment-text"><p>Thanks so much and sorry for my format. I noticed this behavior with Facebook Ip Dst.</p></div><div id="comment-48705-info" class="comment-info"><span class="comment-age">(24 Dec '15, 11:45)</span> wjll</div></div><span id="48708"></span><div id="comment-48708" class="comment"><div id="post-48708-score" class="comment-score"></div><div class="comment-text"><p>To use a fix width format for code or packet dump, either use the code button on the toolbar, add &lt; code&gt;,&lt; /code&gt; tags or indent by 4 spaces.</p></div><div id="comment-48708-info" class="comment-info"><span class="comment-age">(24 Dec '15, 14:03)</span> grahamb ♦</div></div></div><div id="comment-tools-48703" class="comment-tools"></div><div class="clear"></div><div id="comment-48703-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

