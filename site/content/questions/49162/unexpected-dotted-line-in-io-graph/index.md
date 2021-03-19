+++
type = "question"
title = "unexpected dotted line in I/O Graph"
description = '''Hi, i just wanted to analyse IGMP behavior with I/O Graph with Version 2.0.1. What I got is beside the expected dots for a IGMP event, a dotted line at 0. I tried to change IGMP to 224/8 and changes in Style (Diamant, Block etc) and got always a similar line. Does anybody has an idea how to remove t...'''
date = "2016-01-13T04:27:00Z"
lastmod = "2016-01-20T05:54:00Z"
weight = 49162
keywords = [ "iograph" ]
aliases = [ "/questions/49162" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [unexpected dotted line in I/O Graph](/questions/49162/unexpected-dotted-line-in-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49162-score" class="post-score" title="current number of votes">0</div><span id="post-49162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i just wanted to analyse IGMP behavior with I/O Graph with Version 2.0.1. What I got is beside the expected dots for a IGMP event, a dotted line at 0. I tried to change IGMP to 224/8 and changes in Style (Diamant, Block etc) and got always a similar line.</p><p>Does anybody has an idea how to remove that "line"?</p><p>Thanks</p><p>Sorry, I am not allowed to attach a picture.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iograph" rel="tag" title="see questions tagged &#39;iograph&#39;">iograph</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '16, 04:27</strong></p><img src="https://secure.gravatar.com/avatar/15649b981f6bb7e84eacf9c178094fdb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="oilman44&#39;s gravatar image" /><p><span>oilman44</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="oilman44 has no accepted answers">0%</span></p></div></div><div id="comments-container-49162" class="comments-container"><span id="49376"></span><div id="comment-49376" class="comment"><div id="post-49376-score" class="comment-score"></div><div class="comment-text"><p>can you please upload the image somewhere else (google drive, dropbox) and post the link here?</p></div><div id="comment-49376-info" class="comment-info"><span class="comment-age">(19 Jan '16, 07:44)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="49400"></span><div id="comment-49400" class="comment"><div id="post-49400-score" class="comment-score"></div><div class="comment-text"><p>Yes, of course, I hope that works.</p><p><a href="http://www.fotos-hochladen.net/view/wiresharkiogranscr0e5tp2.jpg">http://www.fotos-hochladen.net/view/wiresharkiogranscr0e5tp2.jpg</a></p></div><div id="comment-49400-info" class="comment-info"><span class="comment-age">(20 Jan '16, 05:33)</span> <span class="comment-user userinfo">oilman44</span></div></div></div><div id="comment-tools-49162" class="comment-tools"></div><div class="clear"></div><div id="comment-49162-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49401"></span>

<div id="answer-container-49401" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49401-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49401-score" class="post-score" title="current number of votes">1</div><span id="post-49401-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Y values of your graph are "packets/s". Subsequently, for those "time intervals" or "ticks" (whose duration can be chosen in logarithmic steps from 0.001 s to 10 min. or so) where there wasn't any packet matching the filter rule, the corresponding Y value of "packets/s" is 0.</p><p>You can see that the fat red line at Y=0 becomes narrower at time ticks where Y value differs from 0 and so the dot for that interval is placed elsewhere. In your case, it is best visible shortly after 120 s time where you had two intervals with Y = 1 packet/s in two cases.</p><p>You may like the picture more if you change the graph style from "Dot" to "Impulse" for this kind of packets which occur only now and then.</p><p>I don't know, however, any setting which would allow you to specify that zero Y-values should not be drawn if Dot, Diamond or any other "discrete" style is used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jan '16, 05:54</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jan '16, 15:32</strong> </span></p></div></div><div id="comments-container-49401" class="comments-container"></div><div id="comment-tools-49401" class="comment-tools"></div><div class="clear"></div><div id="comment-49401-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

