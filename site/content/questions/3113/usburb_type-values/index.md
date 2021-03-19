+++
type = "question"
title = "usb.urb_type values?"
description = '''The usb.urb_type is described as &quot;URB type&quot; &quot;String&quot; in the manual http://www.wireshark.org/docs/dfref/u/usb.html. This is very helpful. But now, I want to see only host-do-device requests. usb.urb_type == URB_SUBMIT blocks everything.'''
date = "2011-03-25T04:50:00Z"
lastmod = "2011-08-03T10:08:00Z"
weight = 3113
keywords = [ "filtering" ]
aliases = [ "/questions/3113" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [usb.urb\_type values?](/questions/3113/usburb_type-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3113-score" class="post-score" title="current number of votes">0</div><span id="post-3113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The usb.urb_type is described as "URB type" "String" in the manual http://www.wireshark.org/docs/dfref/u/usb.html. This is very helpful. But now, I want to see only host-do-device requests. usb.urb_type == URB_SUBMIT blocks everything.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filtering" rel="tag" title="see questions tagged &#39;filtering&#39;">filtering</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '11, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/867c6bf0fb8fcddd7e73bd6b6498543d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="valentin&#39;s gravatar image" /><p><span>valentin</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="valentin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Mar '11, 05:00</strong> </span></p></div></div><div id="comments-container-3113" class="comments-container"></div><div id="comment-tools-3113" class="comment-tools"></div><div class="clear"></div><div id="comment-3113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="3121"></span>

<div id="answer-container-3121" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3121-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3121-score" class="post-score" title="current number of votes">0</div><span id="post-3121-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="valentin has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try: <code>usb.urb_type contains "S"</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3121" class="comments-container"></div><div id="comment-tools-3121" class="comment-tools"></div><div class="clear"></div><div id="comment-3121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3128"></span>

<div id="answer-container-3128" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3128-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3128-score" class="post-score" title="current number of votes">0</div><span id="post-3128-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have changed the format of this field from a "String" to an "Unsigned 8-bit integer", so starting with Wireshark 1.5.1, you will be able to filter using <code>usb.urb_type == 83</code> or <code>usb.urb_type == 0x53</code> or by using <code>usb.urb_type == URB_SUBMIT</code> as you tried to do before. This will also apply to any of the <a href="http://www.wireshark.org/download/automated/">automated builds</a>, r36331 or later. Until then, you can use <code>usb.urb_type contains "S"</code>, as I mentioned earlier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '11, 12:02</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3128" class="comments-container"></div><div id="comment-tools-3128" class="comment-tools"></div><div class="clear"></div><div id="comment-3128-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5452"></span>

<div id="answer-container-5452" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5452-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5452-score" class="post-score" title="current number of votes">0</div><span id="post-5452-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you can also usb[8] == 53</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Aug '11, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/18e5c82b31b3648c5f4ca6e4b5d20e9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="terxx&#39;s gravatar image" /><p><span>terxx</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="terxx has no accepted answers">0%</span></p></div></div><div id="comments-container-5452" class="comments-container"></div><div id="comment-tools-5452" class="comment-tools"></div><div class="clear"></div><div id="comment-5452-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

