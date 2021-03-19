+++
type = "question"
title = "isakmp.ispi as a display filter"
description = '''I am attempting to apply a display filter based on the ISAKMP Intiator SPI, which is f64e30753a4a41b6. I have used the filter builder (expression) and as soon as I paste in either f6 4e 30 75 3a 4a 41 b6 or f64e30753a4a41b6 then the filter is shown as being invalid. I have tried &quot;f64e30753a4a41b6&quot; a...'''
date = "2017-07-03T15:58:00Z"
lastmod = "2017-08-18T14:00:00Z"
weight = 62485
keywords = [ "spi", "isakmp.ispi", "isakmp" ]
aliases = [ "/questions/62485" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [isakmp.ispi as a display filter](/questions/62485/isakmpispi-as-a-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62485-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62485-score" class="post-score" title="current number of votes">0</div><span id="post-62485-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am attempting to apply a display filter based on the ISAKMP Intiator SPI, which is f64e30753a4a41b6.</p><p>I have used the filter builder (expression) and as soon as I paste in either f6 4e 30 75 3a 4a 41 b6 or f64e30753a4a41b6 then the filter is shown as being invalid.</p><p>I have tried "f64e30753a4a41b6" and "f6 4e 30 75 3a 4a 41 b6" which works for the filter checker, but does not output any data even though I can see packets with ISAMP SPI set to f64e30753a4a41b6.</p><p>Any ideas?</p><p>Thanks,</p><p>Pat</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-spi" rel="tag" title="see questions tagged &#39;spi&#39;">spi</span> <span class="post-tag tag-link-isakmp.ispi" rel="tag" title="see questions tagged &#39;isakmp.ispi&#39;">isakmp.ispi</span> <span class="post-tag tag-link-isakmp" rel="tag" title="see questions tagged &#39;isakmp&#39;">isakmp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '17, 15:58</strong></p><img src="https://secure.gravatar.com/avatar/08a54f74f365f2309cf9460433cf01b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="patgrogan_act_au&#39;s gravatar image" /><p><span>patgrogan_ac...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="patgrogan_act_au has no accepted answers">0%</span></p></div></div><div id="comments-container-62485" class="comments-container"></div><div id="comment-tools-62485" class="comment-tools"></div><div class="clear"></div><div id="comment-62485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62488"></span>

<div id="answer-container-62488" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62488-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62488-score" class="post-score" title="current number of votes">1</div><span id="post-62488-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have you tried <code>isakmp.ispi == f6:4e:30:75:3a:4a:41:b6</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '17, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Jul '17, 12:15</strong> </span></p></div></div><div id="comments-container-62488" class="comments-container"><span id="63487"></span><div id="comment-63487" class="comment"><div id="post-63487-score" class="comment-score"></div><div class="comment-text"><p>This worked fine. Thanks for the information. Pat</p></div><div id="comment-63487-info" class="comment-info"><span class="comment-age">(18 Aug '17, 13:45)</span> <span class="comment-user userinfo">patgrogan_ac...</span></div></div><span id="63488"></span><div id="comment-63488" class="comment"><div id="post-63488-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-63488-info" class="comment-info"><span class="comment-age">(18 Aug '17, 14:00)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-62488" class="comment-tools"></div><div class="clear"></div><div id="comment-62488-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

