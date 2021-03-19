+++
type = "question"
title = "Null Terminated String"
description = '''Is there an available function that finds bytes till null character? (&#x27;0&#x27;) Thanks, Dhanashree'''
date = "2011-04-18T12:44:00Z"
lastmod = "2011-04-19T08:01:00Z"
weight = 3580
keywords = [ "terminated", "null", "string" ]
aliases = [ "/questions/3580" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Null Terminated String](/questions/3580/null-terminated-string)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3580-score" class="post-score" title="current number of votes">0</div><span id="post-3580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there an available function that finds bytes till null character? ('0')</p><p>Thanks, Dhanashree</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-terminated" rel="tag" title="see questions tagged &#39;terminated&#39;">terminated</span> <span class="post-tag tag-link-null" rel="tag" title="see questions tagged &#39;null&#39;">null</span> <span class="post-tag tag-link-string" rel="tag" title="see questions tagged &#39;string&#39;">string</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/c33cba1d3fea69f74f6c8c0425c16c75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsprabhu4&#39;s gravatar image" /><p><span>dsprabhu4</span><br />
<span class="score" title="11 reputation points">11</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsprabhu4 has no accepted answers">0%</span></p></div></div><div id="comments-container-3580" class="comments-container"></div><div id="comment-tools-3580" class="comment-tools"></div><div class="clear"></div><div id="comment-3580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3581"></span>

<div id="answer-container-3581" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3581-score" class="post-score" title="current number of votes">1</div><span id="post-3581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Each of <code>tvb_get_stringz</code>, <code>tvb_get_ephemeral_stringz</code>, and <code>tvb_get_seasonal_stringz</code> extract a <code>NULL</code> terminated string from the TVB and return it as a <code>guint8 *</code>.</p><p>I would recommend that you check for the presence of the terminating <code>NULL</code> before calling any of these functions, however, as it is not guaranteed to be in the captured packet (erroneous transmission, fuzz-test, fragmentation, etc). You could use <code>tvb_find_guint8</code> to do this; a returned length of <code>-1</code> means that the <code>NULL</code> was not found before the end of the packet or <code>maxlength</code> (an argument to the call).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-3581" class="comments-container"><span id="3589"></span><div id="comment-3589" class="comment"><div id="post-3589-score" class="comment-score"></div><div class="comment-text"><p>I am using following function and then checking if it is -1 or not. / <em>check for null character</em> / null_offset = tvb_find_guint8(tvb, offset + 1, -1,0);</p><p>Thank You. It really helped me.</p></div><div id="comment-3589-info" class="comment-info"><span class="comment-age">(18 Apr '11, 14:17)</span> <span class="comment-user userinfo">dsprabhu4</span></div></div><span id="3591"></span><div id="comment-3591" class="comment"><div id="post-3591-score" class="comment-score">2</div><div class="comment-text"><p>Note that if the terminating NUL is not found, tvb_get_stringz(), tvb_get_ephemeral_stringz(), and tvb_get_seasonal_stringz() will throw an exception, so that the packet will be reported as either cut short by the snapshot length (if it hits the captured length before finding a NUL or hitting the end of the packet) or malformed (if it hits the end of the packet before finding a NUL and the captured length and packet length are the same). In most cases, this is what you'd want - no need for the tvb_find_guint8().</p></div><div id="comment-3591-info" class="comment-info"><span class="comment-age">(18 Apr '11, 18:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="3607"></span><div id="comment-3607" class="comment"><div id="post-3607-score" class="comment-score"></div><div class="comment-text"><p>Thanks to all. I was able to do what i wanted to do.</p></div><div id="comment-3607-info" class="comment-info"><span class="comment-age">(19 Apr '11, 06:13)</span> <span class="comment-user userinfo">dsprabhu4</span></div></div><span id="3611"></span><div id="comment-3611" class="comment"><div id="post-3611-score" class="comment-score"></div><div class="comment-text"><p>(please use the "accept" button (the checkmark next to an answer) to accept an answer, this will make sure the question is removed from the "Unanswered Questions" list)</p></div><div id="comment-3611-info" class="comment-info"><span class="comment-age">(19 Apr '11, 08:01)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-3581" class="comment-tools"></div><div class="clear"></div><div id="comment-3581-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

