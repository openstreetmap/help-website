+++
type = "question"
title = "TCP packets being combined on the way to a server"
description = '''Hi there! I have the following scenario: Client &amp;lt;-&amp;gt; Tunnel &amp;lt;-&amp;gt; VPN Server &amp;lt;-&amp;gt; FileServer The client is requesting a file on a fileserver on the internet (ubuntu hosted in windows azure cloud) through a VPN that is terminated the VPN server (hosted in Germany at a different provider...'''
date = "2014-05-28T14:17:00Z"
lastmod = "2014-05-29T02:26:00Z"
weight = 33143
keywords = [ "jumboframes", "tcp" ]
aliases = [ "/questions/33143" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP packets being combined on the way to a server](/questions/33143/tcp-packets-being-combined-on-the-way-to-a-server)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33143-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there!</p><p>I have the following scenario:</p><p>Client &lt;-&gt; Tunnel &lt;-&gt; VPN Server &lt;-&gt; FileServer</p><p>The client is requesting a file on a fileserver on the internet (ubuntu hosted in windows azure cloud) through a VPN that is terminated the VPN server (hosted in Germany at a different provider).</p><p>Now when performing this download I have a very strange effect: on the client and on the file server packets are only being sent with max packet length 1390 which is fine.</p><p>Nonetheless, when performing TCPDUMP traces on the VPN server I suddenly see occasional jumbo frames that exceed the allowed packet length of 1390. Suddenly there are TCP packets that have a length of twice the allowed packet size and the TCP segments are also combined accordingly. This is causing a coughup on the VPN server causing the connection to drop. But I cant see the fileserver sending those jumbo frames.</p><p>I assume that those jumbo frames were not transmitted over the internet, so the ubuntu fileserver on windows azure probably didnt sent them out, but maybe a loadbalancing/optimizing element in the datacenter of the VPN server? is that actually possible? Would an intermediate network element be able to combine multiple TCP packets that were originally sent from a location to a single jumbo framed packet?</p><p>This is the capture on the VPN server: <img src="https://osqa-ask.wireshark.org/upfiles/VPNServer_Jumbo_1.png" alt="alt text" /></p><p>And this is the capture on the file server: <img src="https://osqa-ask.wireshark.org/upfiles/FileServer_NonJumbo.png" alt="alt text" /></p><p>I can also upload the packet traces if required.</p><p>Thanks &amp; Best Regards Qiong Wu</p></div><div id="question-tags" class="tags-container tags">jumboframes tcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 May '14, 14:17</strong></p><img src="https://secure.gravatar.com/avatar/5e801ed65b6f99fcad45fc7e61a5ffde?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Freundschaft&#39;s gravatar image" /><p>Freundschaft<br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Freundschaft has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 28 May '14, 14:18</p></div></div><div id="comments-container-33143" class="comments-container"></div><div id="comment-tools-33143" class="comment-tools"></div><div class="clear"></div><div id="comment-33143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33157"></span>

<div id="answer-container-33157" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33157-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>This may be a problem of where and how you are capturing the packets. I wrote a new blog post recently that explains some of those effects you mention here:</p><p><a href="http://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">http://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '14, 02:26</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div></div><div id="comments-container-33157" class="comments-container"><span id="33171"></span><div id="comment-33171" class="comment"><div id="post-33171-score" class="comment-score"></div><div class="comment-text"><p>good point, but is there actually any way of verifying whether this is connected with TCP optimization done on the local system or actual data on the line being too large? As far as I get it from your post, the only thing I can do is connect a TAP and check whats REALLY going over the line. Thanks for the input!</p></div><div id="comment-33171-info" class="comment-info"><span class="comment-age">(29 May '14, 08:18)</span> Freundschaft</div></div><span id="33172"></span><div id="comment-33172" class="comment"><div id="post-33172-score" class="comment-score"></div><div class="comment-text"><p>well, if you did capture locally on a system that gives you strange results (like oversized packets) it is a safe bet that this is the reason.</p><p>A dead giveaway of TCP optimization is if the TCP checksum is 0. Everything else is hard to say.</p></div><div id="comment-33172-info" class="comment-info"><span class="comment-age">(29 May '14, 08:39)</span> Jasper ♦♦</div></div><span id="33196"></span><div id="comment-33196" class="comment"><div id="post-33196-score" class="comment-score"></div><div class="comment-text"><p>thanks a lot for the help! I'll mark the answer as correct answer.</p></div><div id="comment-33196-info" class="comment-info"><span class="comment-age">(30 May '14, 04:34)</span> Freundschaft</div></div><span id="33259"></span><div id="comment-33259" class="comment"><div id="post-33259-score" class="comment-score"></div><div class="comment-text"><p>by the way: I have another question, if I use a virtual TAP device to mirror the traffic on the network interface that I want to monitor and capture on that interface, would I also produce these side effects?</p></div><div id="comment-33259-info" class="comment-info"><span class="comment-age">(02 Jun '14, 01:56)</span> Freundschaft</div></div></div><div id="comment-tools-33157" class="comment-tools"></div><div class="clear"></div><div id="comment-33157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

