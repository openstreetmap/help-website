+++
type = "question"
title = "Replay pcapng file via wireshark"
description = '''Hello, I have captured a .pcapng-file (protocol of the packets is UDP) with wireshark. Now, I want to replay it (so that it seems that the packets were sent just now and I will be able to receive them with a ros node) - how do I do that?  I am rather new to wireshark and have already searched a bit,...'''
date = "2015-12-01T03:40:00Z"
lastmod = "2015-12-01T04:48:00Z"
weight = 48122
keywords = [ "node", "udp", "playback", "replay" ]
aliases = [ "/questions/48122" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Replay pcapng file via wireshark](/questions/48122/replay-pcapng-file-via-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48122-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48122-score" class="post-score" title="current number of votes">0</div><span id="post-48122-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have captured a .pcapng-file (protocol of the packets is UDP) with wireshark. Now, I want to replay it (so that it seems that the packets were sent just now and I will be able to receive them with a ros node) - how do I do that? I am rather new to wireshark and have already searched a bit, but didn't found a case concerning a .pcapng-file.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-node" rel="tag" title="see questions tagged &#39;node&#39;">node</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-playback" rel="tag" title="see questions tagged &#39;playback&#39;">playback</span> <span class="post-tag tag-link-replay" rel="tag" title="see questions tagged &#39;replay&#39;">replay</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '15, 03:40</strong></p><img src="https://secure.gravatar.com/avatar/ae1863f554c9582645a612209b10c3e9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Victoria_W&#39;s gravatar image" /><p><span>Victoria_W</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Victoria_W has no accepted answers">0%</span></p></div></div><div id="comments-container-48122" class="comments-container"></div><div id="comment-tools-48122" class="comment-tools"></div><div class="clear"></div><div id="comment-48122-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48126"></span>

<div id="answer-container-48126" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48126-score" class="post-score" title="current number of votes">0</div><span id="post-48126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is passive, as in it does not provide replay functionality. Go have a look at <a href="https://wiki.wireshark.org/Tools#Traffic_generators">the traffic generator section</a> of the wiki for some tools that do that. Maybe you need to convert to pcap before you can use them though.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Dec '15, 04:48</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-48126" class="comments-container"></div><div id="comment-tools-48126" class="comment-tools"></div><div class="clear"></div><div id="comment-48126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

