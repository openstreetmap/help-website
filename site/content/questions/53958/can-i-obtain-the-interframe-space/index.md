+++
type = "question"
title = "can I obtain the interframe space?"
description = '''Is it possible for Wireshark to obtain the interframe space? I Like know the time between packets, the time between the last bit of a packet and the first bit of the next packet'''
date = "2016-07-09T15:06:00Z"
lastmod = "2016-07-09T15:17:00Z"
weight = 53958
keywords = [ "timestamps", "interframe" ]
aliases = [ "/questions/53958" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can I obtain the interframe space?](/questions/53958/can-i-obtain-the-interframe-space)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53958-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53958-score" class="post-score" title="current number of votes">0</div><span id="post-53958-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is it possible for Wireshark to obtain the interframe space? I Like know the time between packets, the time between the last bit of a packet and the first bit of the next packet</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamps" rel="tag" title="see questions tagged &#39;timestamps&#39;">timestamps</span> <span class="post-tag tag-link-interframe" rel="tag" title="see questions tagged &#39;interframe&#39;">interframe</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jul '16, 15:06</strong></p><img src="https://secure.gravatar.com/avatar/848b625956ca61e6b7c0fe04897dac94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="higiniofac&#39;s gravatar image" /><p><span>higiniofac</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="higiniofac has no accepted answers">0%</span></p></div></div><div id="comments-container-53958" class="comments-container"></div><div id="comment-tools-53958" class="comment-tools"></div><div class="clear"></div><div id="comment-53958-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53959"></span>

<div id="answer-container-53959" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53959-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53959-score" class="post-score" title="current number of votes">0</div><span id="post-53959-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, that cannot be captured with normal hardware. You can only capture frames that the network card already "carved" from the bitstream on the physical medium, not the interframe gap between them.</p><p>The only way I know to capture this kind of thing is with a professional capture device using fiber links and full duplex TAPs, at least Network General S6000 devices could do that. No idea if it's still possible today. I guess it goes into the realm of cable diagnostic devices, e.g. Fluke.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jul '16, 15:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-53959" class="comments-container"></div><div id="comment-tools-53959" class="comment-tools"></div><div class="clear"></div><div id="comment-53959-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

