+++
type = "question"
title = "Suspected Retransmissions"
description = '''Hello All We use a few different packet analysis suites - Wireshark being one of the main ones. One of the biggest problems I have is Wireshark&#x27;s often incorrect assumption about retransmitted packets. I know that NG and OpNet follow an entire TCP stream before assessing the number of retransmission...'''
date = "2010-09-29T10:31:00Z"
lastmod = "2010-09-30T07:21:00Z"
weight = 354
keywords = [ "retransmissions" ]
aliases = [ "/questions/354" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Suspected Retransmissions](/questions/354/suspected-retransmissions)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-354-score" class="post-score" title="current number of votes">1</div><span id="post-354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All</p><p>We use a few different packet analysis suites - Wireshark being one of the main ones. One of the biggest problems I have is Wireshark's often incorrect assumption about retransmitted packets. I know that NG and OpNet follow an entire TCP stream before assessing the number of retransmissions - but I'm not sure how WireShark handles it. Another issue we're having right now is a few of our probes are tapped into fiber uplinks - and as of a recent code change the packets aren't always being written onto disk in the correct order (maybe off just a few ms) - and this has thrown WS for a loop. I expected the number of OOS packets to go up, which it did, but the number of suspected retransmissions has gone through the roof. Is there a way to avoid this?<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-retransmissions" rel="tag" title="see questions tagged &#39;retransmissions&#39;">retransmissions</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Sep '10, 10:31</strong></p><img src="https://secure.gravatar.com/avatar/9e493496d59bb4ce33c37cd6e7a26a4d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GeonJay&#39;s gravatar image" /><p><span>GeonJay</span><br />
<span class="score" title="470 reputation points">470</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GeonJay has 2 accepted answers">5%</span> </br></p></div></div><div id="comments-container-354" class="comments-container"><span id="367"></span><div id="comment-367" class="comment"><div id="post-367-score" class="comment-score"></div><div class="comment-text"><p>Hi, you're saying you've "tapped into fiber uplinks" - how exactly do you do that? Are you using a full duplex fiber tap with 2 downlinks that are captured on two separate interfaces and then merged? Or do you use SPAN ports, or even link aggregation taps?</p></div><div id="comment-367-info" class="comment-info"><span class="comment-age">(29 Sep '10, 15:46)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="373"></span><div id="comment-373" class="comment"><div id="post-373-score" class="comment-score"></div><div class="comment-text"><p>These are full duplex taps. To be honest they're one of my favorite desktop conversation items. I've cracked one open and it's literally a small mirror sitting at what I assume to be a 45 degree angle. We only trust TAPs at our core-to-dist border because of the high throughput (we have 10G bowties). So, two switches and two headend routers meshed gives you 4 connections, each consisting of two fibers for a total of 8 fibers - so we have 8 TAPs that feed a monstrous probe. The probe then aggregates all 8 interfaces into a single virtual interface from which we can grab captures.</p></div><div id="comment-373-info" class="comment-info"><span class="comment-age">(30 Sep '10, 05:38)</span> <span class="comment-user userinfo">GeonJay</span></div></div><span id="374"></span><div id="comment-374" class="comment"><div id="post-374-score" class="comment-score"></div><div class="comment-text"><p>I like FDX Taps to, especially the optical ones. I don't like aggregation taps as they sometimes introduce errors either to the production connection or in the connection to the capture device.</p><p>Problem with full duplex captures is that sometimes the single interfaces have difficulties "delivering" the packets to the merge process in time and get delayed because the other cards have higher priority or just "better luck" with IRQs etc. Then the merge reorders packets and you have stuff like for example a "200 OK" appearing before the "GET" request is issued. It throws Wireshark off, too.</p></div><div id="comment-374-info" class="comment-info"><span class="comment-age">(30 Sep '10, 05:53)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="375"></span><div id="comment-375" class="comment"><div id="post-375-score" class="comment-score"></div><div class="comment-text"><p>This is our current problem. We use one of the well known probe manufacturers (rhymes with petsnout). As of the last two code releases we have major issues with aggregate interfaces in high volume network segments writing the packets to the disk out of order AND the AGG interfaces have started dropping segments. This is a code issue for sure - it didn't happen until the last 2 updates. That's the code change I mentioned in my earlier post - those OOO packets are part of our incorrectly reported retrans. Lately we've been unAGGing the interfaces and grabbing individual captures :(</p></div><div id="comment-375-info" class="comment-info"><span class="comment-age">(30 Sep '10, 06:45)</span> <span class="comment-user userinfo">GeonJay</span></div></div><span id="376"></span><div id="comment-376" class="comment"><div id="post-376-score" class="comment-score"></div><div class="comment-text"><p>Ouch, that's no fun, but unfortunately I think you'll have to get the code guys to fix things so that the automatic aggregations do work correctly again. There's not much that you can do to avoid OoO packets otherwise, and probably no way to fix things within Wireshark either. It will keep displaying suspected retransmissions messages since it sees a lower sequence number appearing after a higher sequence number in the packet before the current one.</p></div><div id="comment-376-info" class="comment-info"><span class="comment-age">(30 Sep '10, 07:21)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-354" class="comment-tools"></div><div class="clear"></div><div id="comment-354-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="369"></span>

<div id="answer-container-369" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-369-score" class="post-score" title="current number of votes">2</div><span id="post-369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="GeonJay has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can read the code at http://anonsvn.wireshark.org/viewvc/trunk-1.4/epan/dissectors/packet-tcp.c?revision=33861&amp;view=markup (that's the location for verion 1.4.0) - search for:</p><pre><code>/* RETRANSMISSION/FAST RETRANSMISSION/OUT-OF-ORDER</code></pre><p>That section explains how the decision to mark a packet as a retransmission/fast_retransmission/out-of-order is made.</p><p>You could turn off TCP Preferences Analyze Sequence Numbers, but then you'd miss so much interpretation of TCP issues...</p><p>Hope this helps.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Sep '10, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lchappell has 6 accepted answers">8%</span></p></div></div><div id="comments-container-369" class="comments-container"></div><div id="comment-tools-369" class="comment-tools"></div><div class="clear"></div><div id="comment-369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

