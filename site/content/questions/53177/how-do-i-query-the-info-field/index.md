+++
type = "question"
title = "How do I query the &#x27;info&#x27; field?"
description = '''How do I query the &#x27;info&#x27; field? The following: info contains &quot;mysql&quot; produces error that it&#x27;s not a field or protocol name. But &#x27;info&#x27; is a field. It&#x27;s the last field in the display on the right. I&#x27;ve tried uppercase and lowercase.'''
date = "2016-06-03T07:19:00Z"
lastmod = "2016-06-03T18:00:00Z"
weight = 53177
keywords = [ "filter", "display-filter" ]
aliases = [ "/questions/53177" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I query the 'info' field?](/questions/53177/how-do-i-query-the-info-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53177-score" class="post-score" title="current number of votes">0</div><span id="post-53177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How do I query the 'info' field?</p><p>The following: <code>info contains "mysql"</code> produces error that it's not a field or protocol name. But 'info' is a field. It's the last field in the display on the right. I've tried uppercase and lowercase.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-display-filter" rel="tag" title="see questions tagged &#39;display-filter&#39;">display-filter</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '16, 07:19</strong></p><img src="https://secure.gravatar.com/avatar/caefc8177fd93e6be4a46eb2e45b2312?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jtl&#39;s gravatar image" /><p><span>jtl</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jtl has no accepted answers">0%</span></p></div></div><div id="comments-container-53177" class="comments-container"></div><div id="comment-tools-53177" class="comment-tools"></div><div class="clear"></div><div id="comment-53177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53178"></span>

<div id="answer-container-53178" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53178-score" class="post-score" title="current number of votes">1</div><span id="post-53178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jtl has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>'info' is a column, therefore not a field. The term field is restricted to dissected parts of the frame, or generated thereof. Columns can be filled based on these fields, or from other sources. Therefore you cannot use a display filter on the info column.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '16, 07:49</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53178" class="comments-container"><span id="53191"></span><div id="comment-53191" class="comment"><div id="post-53191-score" class="comment-score"></div><div class="comment-text"><p>On the other hand, the Info column <em>can</em> be queried using <code>tshark</code> and some external tools such as <code>findstr</code> or <code>grep</code>. As an example, see my answer to <a href="https://ask.wireshark.org/questions/52182/filtering-out-specific-lines-that-contain-specific-information-in-the-information-column">this</a> question.</p></div><div id="comment-53191-info" class="comment-info"><span class="comment-age">(03 Jun '16, 18:00)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-53178" class="comment-tools"></div><div class="clear"></div><div id="comment-53178-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

