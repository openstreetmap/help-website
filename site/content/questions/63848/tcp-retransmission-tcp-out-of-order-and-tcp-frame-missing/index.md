+++
type = "question"
title = "tcp retransmission &amp; tcp out of order and tcp frame missing"
description = '''Dear Gurus, Sorry if i sound stupid but i am very new to networking.My application work as ESME for the smsc and it seems that recently we observing huge delay in ack of submitted message or ack not coming at all.I can see in netstat output of linux send queue is increasing hugely.Taken a tcpdump in...'''
date = "2017-10-12T08:40:00Z"
lastmod = "2017-10-12T12:54:00Z"
weight = 63848
keywords = [ "dup-ack", "networking", "retransmission" ]
aliases = [ "/questions/63848" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tcp retransmission & tcp out of order and tcp frame missing](/questions/63848/tcp-retransmission-tcp-out-of-order-and-tcp-frame-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63848-score" class="post-score" title="current number of votes">0</div><span id="post-63848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Dear Gurus, Sorry if i sound stupid but i am very new to networking.My application work as ESME for the smsc and it seems that recently we observing huge delay in ack of submitted message or ack not coming at all.I can see in netstat output of linux send queue is increasing hugely.Taken a tcpdump in which i can see to much [TCP Dup ACK],[TCP Out-Of-Order],[TCP Retransmission]</p><p>Also i see in wireshark Smsc send mesg with</p><pre><code>seq:1 ACK:1 Len: 51 --&gt;&quot;213.132.40.140 -&gt; 192.168.40.8 SMPP SMPP Deliver_sm&quot;</code></pre><p>but we reply by</p><pre><code>192.168.40.8 -&gt; 213.132.40.140 TCP 42758 &gt; dynamid [ACK] Seq=4141 Ack=52 Win=128 Len=0</code></pre><p>That means are we losing frames.Pls help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-retransmission" rel="tag" title="see questions tagged &#39;retransmission&#39;">retransmission</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Oct '17, 08:40</strong></p><img src="https://secure.gravatar.com/avatar/fa1980828063294ccc18c39a018df15e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kaushalender&#39;s gravatar image" /><p><span>kaushalender</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kaushalender has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Oct '17, 09:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-63848" class="comments-container"><span id="63851"></span><div id="comment-63851" class="comment"><div id="post-63851-score" class="comment-score"></div><div class="comment-text"><p>can you upload a PCAP somewhere, e.g. Cloudshark? If you need to sanitze it first, read <a href="https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/">https://blog.packet-foo.com/2016/11/the-wireshark-qa-trace-file-sharing-tutorial/</a></p></div><div id="comment-63851-info" class="comment-info"><span class="comment-age">(12 Oct '17, 12:54)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-63848" class="comment-tools"></div><div class="clear"></div><div id="comment-63848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

