+++
type = "question"
title = "NFS and TCP ACKed Unseen Segment"
description = '''Hi, Environment consists of VMware ESXi 5.0 (Patch 9) servers and NetApp NAS/Filer. Experiencing periodic drops of NFS exports from the ESXi hosts. The exports automatically reconnect after 3 minutes. Storage vendor has reviewed tcpdump captures from the VMware hosts and believes they indicate netwo...'''
date = "2014-12-17T13:09:00Z"
lastmod = "2014-12-17T16:34:00Z"
weight = 38611
keywords = [ "nfs", "tcp", "segment", "acked", "unseen" ]
aliases = [ "/questions/38611" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [NFS and TCP ACKed Unseen Segment](/questions/38611/nfs-and-tcp-acked-unseen-segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38611-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38611-score" class="post-score" title="current number of votes">0</div><span id="post-38611-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Environment consists of VMware ESXi 5.0 (Patch 9) servers and NetApp NAS/Filer.</p><p>Experiencing periodic drops of NFS exports from the ESXi hosts. The exports automatically reconnect after 3 minutes.</p><p>Storage vendor has reviewed tcpdump captures from the VMware hosts and believes they indicate network issues.</p><p>Seeing many "TCP ACKed unseen segment" and "TCP Previous Segment not captured" messages in Wireshark.</p><p>Captures uploaded to - <a href="https://www.cloudshark.org/captures/a0fdd8dbca3e">https://www.cloudshark.org/captures/a0fdd8dbca3e</a></p><p>tcpdump configuration used -</p><pre><code># tcpdump-uw -i vmk3 -s 1514 -C 1M -W 10 -w /vmfs/volumes/test.pcap
tcpdump-uw: WARNING: SIOCGIFINDEX: Invalid argument
tcpdump-uw: listening on vmk3, link-type EN10MB (Ethernet), capture size 1514 bytes
tcpdump-uw: pcap_loop: recvfrom: Interrupted system call
189449 packets captured
189449 packets received by filter
0 packets dropped by kernel</code></pre><p>Thanks for you assistance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nfs" rel="tag" title="see questions tagged &#39;nfs&#39;">nfs</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-segment" rel="tag" title="see questions tagged &#39;segment&#39;">segment</span> <span class="post-tag tag-link-acked" rel="tag" title="see questions tagged &#39;acked&#39;">acked</span> <span class="post-tag tag-link-unseen" rel="tag" title="see questions tagged &#39;unseen&#39;">unseen</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '14, 13:09</strong></p><img src="https://secure.gravatar.com/avatar/b9d5ee73c288d19ec56e93129084d399?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="LJM&#39;s gravatar image" /><p><span>LJM</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="LJM has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>17 Dec '14, 13:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-38611" class="comments-container"></div><div id="comment-tools-38611" class="comment-tools"></div><div class="clear"></div><div id="comment-38611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38613"></span>

<div id="answer-container-38613" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38613-score" class="post-score" title="current number of votes">1</div><span id="post-38613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What you have is massive packet loss, meaning, that your capture wasn't able to record all packets coming in. This comes as no surprise, because capturing intense storage traffic cannot be performed without this kind of loss with normal PCs. You'd need a special high performance appliance for this kind of thing.</p><p>There are many places where packet loss can occur, with the kernel being only one of them. So even if TCPdump says 0 packets dropped by kernel it doesn't mean there is no drop.</p><p>What you could do is reduce the amount of bytes per packet captured to 64 or 128 bytes, because in situations like this the payload doesn't matter. You want to look at TCP behavior, and for that 64 bytes are more than enough.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Dec '14, 16:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38613" class="comments-container"></div><div id="comment-tools-38613" class="comment-tools"></div><div class="clear"></div><div id="comment-38613-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

