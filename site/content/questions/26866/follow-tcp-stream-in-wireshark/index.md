+++
type = "question"
title = "Follow TCP Stream in Wireshark."
description = '''when i filter the pcap file i seen one error which i never seen before ie: (Error creating filter for this stream. A transport or network layer header is needed) what does that mean could you please tel me.. And how can i rectify this for further assistance.. Thanks  '''
date = "2013-11-11T23:33:00Z"
lastmod = "2013-11-12T04:08:00Z"
weight = 26866
keywords = [ "wireshark" ]
aliases = [ "/questions/26866" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Follow TCP Stream in Wireshark.](/questions/26866/follow-tcp-stream-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26866-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26866-score" class="post-score" title="current number of votes">0</div><span id="post-26866-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when i filter the pcap file i seen one error which i never seen before ie: (Error creating filter for this stream. A transport or network layer header is needed) what does that mean could you please tel me.. And how can i rectify this for further assistance.. Thanks<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Nov '13, 23:33</strong></p><img src="https://secure.gravatar.com/avatar/e5fb768309758188648a9fb880d7bbfc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eva&#39;s gravatar image" /><p><span>eva</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eva has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Nov '13, 23:34</strong> </span></p></div></div><div id="comments-container-26866" class="comments-container"></div><div id="comment-tools-26866" class="comment-tools"></div><div class="clear"></div><div id="comment-26866-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26878"></span>

<div id="answer-container-26878" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-26878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-26878-score" class="post-score" title="current number of votes">0</div><span id="post-26878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Error creating filter for this stream. A transport or network layer header is needed)</p></blockquote><p>That error message will be shown if the <strong>TCP or UDP header was not fully captured</strong>. This could be due to size limitations during the capture process (Option -s, GUI: Capture -&gt; Options: Double click an interface -&gt; Limit each packet to).</p><p>I was able to generate the error message by capturing only 44 bytes of each frame. The resulting TCP header does contain the ports, but nothing else.</p><blockquote><p><a href="http://cloudshark.org/captures/7f20a6decb77">http://cloudshark.org/captures/7f20a6decb77</a><br />
</p></blockquote><p>If you try to follow a TCP Stream you will get that error messages.</p><p>You can check your capture file, to figure out if the full frame was captured or just the first n bytes. If you look at the frame in the details pane, you'll see the frame size <strong>and</strong> the captured size in the first 'line'.</p><blockquote><p>Frame 11: <strong>534 bytes on wire</strong> (4272 bits), <strong>44 bytes captured</strong> (352 bits)</p></blockquote><p>You can also look at the TCP/UDP header and check if there is something missing.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Nov '13, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-26878" class="comments-container"></div><div id="comment-tools-26878" class="comment-tools"></div><div class="clear"></div><div id="comment-26878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

