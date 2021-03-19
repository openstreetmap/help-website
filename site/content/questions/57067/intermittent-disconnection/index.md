+++
type = "question"
title = "intermittent disconnection"
description = '''can somebody please explain the below packet capture output.I am not good with packet captures. Client:192.168.1.3 Server:121.11.12.241 This Packet capture has been taken from client end. 625: 16:29:35.800892 802.1Q vlan#412 P0 192.168.1.3.62597 &amp;gt; 121.11.12.241.443: S 3810026419:3810026419(0) win...'''
date = "2016-11-07T08:50:00Z"
lastmod = "2016-11-07T13:55:00Z"
weight = 57067
keywords = [ "capture", "window", "tcpdump", "packet", "tcpwindowsize" ]
aliases = [ "/questions/57067" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [intermittent disconnection](/questions/57067/intermittent-disconnection)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57067-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>can somebody please explain the below packet capture output.I am not good with packet captures.</p><p>Client:192.168.1.3<br />
Server:121.11.12.241<br />
This Packet capture has been taken from client end.</p><pre><code>625: 16:29:35.800892 802.1Q vlan#412 P0 192.168.1.3.62597 &gt; 121.11.12.241.443: S 3810026419:3810026419(0) win 8192 &lt; mss 1460,nop,wscale 8,nop,nop,sackOK&gt;  
626: 16:29:35.816730 802.1Q vlan#412 P0 121.11.12.241.443 &gt; 192.168.1.3.62597: S 2188766603:2188766603(0) ack 3810026420 win 4140 &lt; mss 1380,sackOK,eol&gt; 
627: 16:29:35.817386 802.1Q vlan#412 P0 192.168.1.3.62597 &gt; 121.11.12.241.443: . ack 2188766604 win 64860 
628: 16:29:35.819354 802.1Q vlan#412 P0 192.168.1.3.62597 &gt; 121.11.12.241.443: R 3810026420:3810026420(0) ack 2188766604 win 0</code></pre><p>Thanks in advance</p></div><div id="question-tags" class="tags-container tags">capture window tcpdump packet tcpwindowsize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '16, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/5abe0fecf3868ada8e06d9e2a8eabbe8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jith1010&#39;s gravatar image" /><p>Jith1010<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jith1010 has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Nov '16, 09:45</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-57067" class="comments-container"></div><div id="comment-tools-57067" class="comment-tools"></div><div class="clear"></div><div id="comment-57067-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57099"></span>

<div id="answer-container-57099" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57099-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>tcpdump's way of displaying TCP is, well, compact. Wireshark is aimed to render you the same information in much more user-friendly form, so if you cannot install Wireshark on the platform where you've taken that capture, just run <code>tcpdump</code> the same way you did but add <code>-s 0 -w some/file/name</code> to its command line parameters. Then, copy some/file/name to a machine on which you can run Wireshark and open it there.</p><p>In your case:</p><p>625 - the client sends a SYN packet, indicating that it supports window scaling and sack, and the MSS value</p><p>626 - the server responds with a SYN,ACK packet, indicating that it does <strong>not</strong> support window scaling by not placing the <code>wscale</code> option to that packet, the MSS value, and making the option list shorter by using an EOL option.</p><p>627 - the client confirms reception of the server's SYN,ACK packet by sending its own ACK</p><p>628 - the client terminates the session in emergency mode by sending a RST packet, <strong>possibly</strong> because it didn't like that the server doesn't support window scaling, or because it didn't like something else about the server's response.</p><p>The actual reason can not be found using tcpdump or Wireshark. Network analyzers tell you <strong>what</strong> has happened, but very rarely the protocols carry detailed information about <strong>why</strong> it has happened.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '16, 13:55</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Nov '16, 13:56</p></div></div><div id="comments-container-57099" class="comments-container"><span id="57117"></span><div id="comment-57117" class="comment"><div id="post-57117-score" class="comment-score"></div><div class="comment-text"><p>So in your opinion which side has more chance to have the issue ,client side or server side?</p></div><div id="comment-57117-info" class="comment-info"><span class="comment-age">(07 Nov '16, 22:40)</span> Jith1010</div></div><span id="57126"></span><div id="comment-57126" class="comment"><div id="post-57126-score" class="comment-score"></div><div class="comment-text"><p>The initiative to terminate connection was client's.</p><p>As the client tears down the session at such an early stage, you may try to connect to other two https servers, one which does support window size scaling and another one which doesn't. If the client doesn't reset the connection to the first one at the same stage as in this capture and does reset at the same stage the connection to the second one, it is very likely that it doesn't like this particular feature (or the absence of it).</p></div><div id="comment-57126-info" class="comment-info"><span class="comment-age">(08 Nov '16, 00:51)</span> sindy</div></div></div><div id="comment-tools-57099" class="comment-tools"></div><div class="clear"></div><div id="comment-57099-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

