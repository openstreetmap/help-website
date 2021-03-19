+++
type = "question"
title = "TCP loss display in column field"
description = '''Hi. In wireshark, Is possible to show in a column field a number (eg. 1) everytime it detects a packet loss?. I want to export the full capture to do some analysis. In addition, The filter BADTCP implies a loss of data? Thank you. Alvaro.'''
date = "2014-10-18T16:37:00Z"
lastmod = "2014-10-20T03:18:00Z"
weight = 37154
keywords = [ "wireshark", "tcp", "packetloss" ]
aliases = [ "/questions/37154" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP loss display in column field](/questions/37154/tcp-loss-display-in-column-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37154-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37154-score" class="post-score" title="current number of votes">0</div><span id="post-37154-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. In wireshark, Is possible to show in a column field a number (eg. 1) everytime it detects a packet loss?. I want to export the full capture to do some analysis. In addition, The filter BADTCP implies a loss of data?</p><p>Thank you.</p><p>Alvaro.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Oct '14, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/0f4ce7483f297f00bfbcab3fe35f77dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alvarmemo&#39;s gravatar image" /><p><span>alvarmemo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alvarmemo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Oct '14, 16:38</strong> </span></p></div></div><div id="comments-container-37154" class="comments-container"></div><div id="comment-tools-37154" class="comment-tools"></div><div class="clear"></div><div id="comment-37154-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37178"></span>

<div id="answer-container-37178" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37178-score" class="post-score" title="current number of votes">0</div><span id="post-37178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think what you're asking is possible.</p><p>It is possible to filter for when TCP misses a frame (<code>tcp.analysis.lost_segment</code>) but this is an Expert Info which can't be applied as a column.</p><p>I'm not familiar with the filter <code>BADTCP</code>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Oct '14, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-37178" class="comments-container"></div><div id="comment-tools-37178" class="comment-tools"></div><div class="clear"></div><div id="comment-37178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

