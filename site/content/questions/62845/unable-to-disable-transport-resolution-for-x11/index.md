+++
type = "question"
title = "Unable to disable transport resolution for X11"
description = '''Just installed the latest update and opened a capture. The port range in which I am working is 6001-6579 with much of it being labeled as X11, even though I have transport resolution disabled. I tried setting X11 to a different port range but it made no difference. The only name resolution I have en...'''
date = "2017-07-18T10:37:00Z"
lastmod = "2017-07-18T11:27:00Z"
weight = 62845
keywords = [ "nameresolution", "transport" ]
aliases = [ "/questions/62845" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Unable to disable transport resolution for X11](/questions/62845/unable-to-disable-transport-resolution-for-x11)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62845-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62845-score" class="post-score" title="current number of votes">0</div><span id="post-62845-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Just installed the latest update and opened a capture. The port range in which I am working is 6001-6579 with much of it being labeled as X11, even though I have transport resolution disabled. I tried setting X11 to a different port range but it made no difference.</p><p>The only name resolution I have enabled is MAC.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nameresolution" rel="tag" title="see questions tagged &#39;nameresolution&#39;">nameresolution</span> <span class="post-tag tag-link-transport" rel="tag" title="see questions tagged &#39;transport&#39;">transport</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Jul '17, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/2de4b9da4c2b5acc942c8325408149ec?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="raymos&#39;s gravatar image" /><p><span>raymos</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="raymos has no accepted answers">0%</span></p></div></div><div id="comments-container-62845" class="comments-container"></div><div id="comment-tools-62845" class="comment-tools"></div><div class="clear"></div><div id="comment-62845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62848"></span>

<div id="answer-container-62848" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62848-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62848-score" class="post-score" title="current number of votes">0</div><span id="post-62848-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think you meant to say 'I have Resolve transport names unchecked in the Name Resolution preferences pane'. That is something else than telling Wireshark not to dissect packets for these ports as X11 protocol packets. If you want that to happen then you'll have to go into the menu Analyse, Enabled Protocols... and look for X11 and uncheck that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Jul '17, 11:23</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-62848" class="comments-container"><span id="62849"></span><div id="comment-62849" class="comment"><div id="post-62849-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Never had to use that selection in the past to remove the protocol name(s).</p></div><div id="comment-62849-info" class="comment-info"><span class="comment-age">(18 Jul '17, 11:27)</span> <span class="comment-user userinfo">raymos</span></div></div></div><div id="comment-tools-62848" class="comment-tools"></div><div class="clear"></div><div id="comment-62848-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

