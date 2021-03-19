+++
type = "question"
title = "Capture length is always 94 byte"
description = '''Hi, I was looking at the TCPdump from one of the system, I am seeing the capture length is always 94 byte even if Frame length is more than that. What does it mean?  I see lot of retransmissions is it because of this? Frame Length: 1392 bytes (11136 bits) Capture Length: 94 bytes (752 bits) Frame Le...'''
date = "2015-05-26T13:08:00Z"
lastmod = "2015-05-26T13:53:00Z"
weight = 42672
keywords = [ "capture-length" ]
aliases = [ "/questions/42672" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capture length is always 94 byte](/questions/42672/capture-length-is-always-94-byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42672-score" class="post-score" title="current number of votes">0</div><span id="post-42672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I was looking at the TCPdump from one of the system, I am seeing the capture length is always 94 byte even if Frame length is more than that. What does it mean?</p><p>I see lot of retransmissions is it because of this?</p><p>Frame Length: 1392 bytes (11136 bits) Capture Length: 94 bytes (752 bits)</p><p>Frame Length: 142 bytes (1136 bits) Capture Length: 94 bytes (752 bits)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-length" rel="tag" title="see questions tagged &#39;capture-length&#39;">capture-length</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 May '15, 13:08</strong></p><img src="https://secure.gravatar.com/avatar/57f5bc5e6ed301add098a9ddc4aeeb6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sudarshan&#39;s gravatar image" /><p><span>Sudarshan</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sudarshan has no accepted answers">0%</span></p></div></div><div id="comments-container-42672" class="comments-container"></div><div id="comment-tools-42672" class="comment-tools"></div><div class="clear"></div><div id="comment-42672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42673"></span>

<div id="answer-container-42673" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42673-score" class="post-score" title="current number of votes">0</div><span id="post-42673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I am seeing the capture length is always 94 byte even if Frame length is more than that. What does it mean?</p></blockquote><p>It means that the system which created the capture file, limited the frame size to 94 bytes, for whatever reason (option -s for tcpdump, dumpcap and tshark, "Limit each packet to" in the Wireshark GUI: Capture -&gt; Options. Double-click an interface), or that somebody has used a pcap anonymizer tool which truncated the frames in the capture file.</p><blockquote><p>I see lot of retransmissions is it because of this?</p></blockquote><p>No.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 May '15, 13:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-42673" class="comments-container"></div><div id="comment-tools-42673" class="comment-tools"></div><div class="clear"></div><div id="comment-42673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

