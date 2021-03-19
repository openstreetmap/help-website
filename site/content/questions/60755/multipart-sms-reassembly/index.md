+++
type = "question"
title = "Multipart SMS reassembly"
description = '''in multipart SMS, if all parts are existed then wireshark is reassembeld them. is it possible to reassembeling a multipart SMS even though one part is not existed ? for example in a 3 part SMS if parts 1 and 2 are existed and part 3 is not existed,then wireshark reassembled parts 1 and 2.'''
date = "2017-04-11T22:37:00Z"
lastmod = "2017-04-12T01:00:00Z"
weight = 60755
keywords = [ "gsmsms", "reassembely", "gsm_sms" ]
aliases = [ "/questions/60755" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Multipart SMS reassembly](/questions/60755/multipart-sms-reassembly)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60755-score" class="post-score" title="current number of votes">0</div><span id="post-60755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>in multipart SMS, if all parts are existed then wireshark is reassembeld them. is it possible to reassembeling a multipart SMS even though one part is not existed ? for example in a 3 part SMS if parts 1 and 2 are existed and part 3 is not existed,then wireshark reassembled parts 1 and 2.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gsmsms" rel="tag" title="see questions tagged &#39;gsmsms&#39;">gsmsms</span> <span class="post-tag tag-link-reassembely" rel="tag" title="see questions tagged &#39;reassembely&#39;">reassembely</span> <span class="post-tag tag-link-gsm_sms" rel="tag" title="see questions tagged &#39;gsm_sms&#39;">gsm_sms</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '17, 22:37</strong></p><img src="https://secure.gravatar.com/avatar/28d5dc133c31193058a99892f00a0213?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ghader&#39;s gravatar image" /><p><span>ghader</span><br />
<span class="score" title="61 reputation points">61</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ghader has no accepted answers">0%</span></p></div></div><div id="comments-container-60755" class="comments-container"></div><div id="comment-tools-60755" class="comment-tools"></div><div class="clear"></div><div id="comment-60755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60758"></span>

<div id="answer-container-60758" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60758-score" class="post-score" title="current number of votes">1</div><span id="post-60758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Reassemble to what? A partial PDU? And how to indicate where the break is happening? And what if multiple parts are missing? Does the space needs to be filled in to make the size match? Filled in with what?</p><p>As you can see, there are many options, and it is hard to satisfy everyone. While in practice such incomplete PDU is dropped, so the relevance is limited anyway. Therefore the investment is not made, unless the application calls for it, the example being RTP media playback. And ever there the issues listed above are hard to implement in a way to satisfy all.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '17, 01:00</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-60758" class="comments-container"></div><div id="comment-tools-60758" class="comment-tools"></div><div class="clear"></div><div id="comment-60758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

