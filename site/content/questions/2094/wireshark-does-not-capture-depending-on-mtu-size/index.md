+++
type = "question"
title = "Wireshark does not capture depending on MTU size"
description = '''Hello! I have set the MTU to 1400 on computer &quot;A&quot;. From computer &quot;B&quot; I ping computer &quot;A&quot; by sending a 2000 bytes large ICMP packets: ping -s 2000 192.168.0.10 I don&#x27;t get any replies from computer &quot;A&quot;.  Wireshark detects fragmented IP packets with the info &quot;proto=ICMP 0x01, off=1480&quot;, but no ICMP pa...'''
date = "2011-02-02T01:31:00Z"
lastmod = "2011-02-02T13:51:00Z"
weight = 2094
keywords = [ "icmp", "mtu" ]
aliases = [ "/questions/2094" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark does not capture depending on MTU size](/questions/2094/wireshark-does-not-capture-depending-on-mtu-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2094-score" class="post-score" title="current number of votes">0</div><span id="post-2094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I have set the MTU to 1400 on computer "A".</p><p>From computer "B" I ping computer "A" by sending a 2000 bytes large ICMP packets:</p><p>ping -s 2000 192.168.0.10</p><p>I don't get any replies from computer "A". Wireshark detects fragmented IP packets with the info "proto=ICMP 0x01, off=1480", but no ICMP packets.</p><p>If I change the MTU to 1500 on computer "A", then packets of any size are sent over from computer "B" to computer "A" and are fragmented.</p><p>Why does it work with MTU=1500 but not with MTU=1400?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span> <span class="post-tag tag-link-mtu" rel="tag" title="see questions tagged &#39;mtu&#39;">mtu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Feb '11, 01:31</strong></p><img src="https://secure.gravatar.com/avatar/b40d415d5a5ed5142e38ad841b2e176a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rox&#39;s gravatar image" /><p><span>Rox</span><br />
<span class="score" title="21 reputation points">21</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rox has no accepted answers">0%</span></p></div></div><div id="comments-container-2094" class="comments-container"></div><div id="comment-tools-2094" class="comment-tools"></div><div class="clear"></div><div id="comment-2094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2111"></span>

<div id="answer-container-2111" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-2111-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-2111-score" class="post-score" title="current number of votes">3</div><span id="post-2111-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Computer B will send IP datagrams of up to 1480 bytes (assuming the IP header is 20 bytes). The rest of the ICMP packet (with a payload of 2000 bytes) will be sent in a second fragment. This can be verified by the fact that you see "proto=ICMP 0x01, <strong>off=1480</strong>".</p><p>The first IP fragment is 1500 bytes on the wire. However, Computer A was told it can only send/receive packets of up to 1400 bytes. Therefor it drops the first IP fragment of this IP datagram and only receives the second fragment with the offset of 1480.</p><p>When you change the MTU size on a system, you need to change it for all directly connected systems on the network.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Feb '11, 10:52</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Feb '11, 14:20</strong> </span></p></div></div><div id="comments-container-2111" class="comments-container"><span id="2116"></span><div id="comment-2116" class="comment"><div id="post-2116-score" class="comment-score"></div><div class="comment-text"><p>SYNbit is dead on. Your machine is not most likely not sending packets that are greater than 1500 bytes. Add the -f to your ping command to set the df bit.</p><p>C:Documents and Settingspaul&gt;ping -f -n 2 -l 2000 192.168.0.1</p><p>Pinging 192.168.0.1 with 2000 bytes of data:</p><p>Packet needs to be fragmented but DF set.</p><p>Packet needs to be fragmented but DF set.</p><p>Ping statistics for 192.168.0.1: Packets: Sent = 4, Received = 0, Lost = 2 (100% loss),</p><p>In this example, the message above is coming from the local stack, not a router.</p></div><div id="comment-2116-info" class="comment-info"><span class="comment-age">(02 Feb '11, 13:51)</span> <span class="comment-user userinfo">Paul Stewart</span></div></div></div><div id="comment-tools-2111" class="comment-tools"></div><div class="clear"></div><div id="comment-2111-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

