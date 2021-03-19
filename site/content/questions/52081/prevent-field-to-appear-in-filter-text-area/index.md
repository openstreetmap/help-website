+++
type = "question"
title = "Prevent field to appear in filter text area"
description = '''Im a writing a dissector with a lot of fields, but only some of them are worth filtering. Is there a way to prevent some fields to appear in the filter text area ? README.dissector tells tha &quot;The abbreviation is the identifier used in a display filter. If it is an empty string then the field will no...'''
date = "2016-04-29T09:10:00Z"
lastmod = "2016-04-30T01:30:00Z"
weight = 52081
keywords = [ "filter", "field", "abbrev" ]
aliases = [ "/questions/52081" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Prevent field to appear in filter text area](/questions/52081/prevent-field-to-appear-in-filter-text-area)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52081-score" class="post-score" title="current number of votes">0</div><span id="post-52081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Im a writing a dissector with a lot of fields, but only some of them are worth filtering.</p><p>Is there a way to prevent some fields to appear in the filter text area ?</p><p>README.dissector tells tha "The abbreviation is the identifier used in a display filter. If it is an empty string then the field will not be filterable.", but if I use an empty string (""), I get an exception when I start wireshark.</p><p>Do you know how to proceed ?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-field" rel="tag" title="see questions tagged &#39;field&#39;">field</span> <span class="post-tag tag-link-abbrev" rel="tag" title="see questions tagged &#39;abbrev&#39;">abbrev</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '16, 09:10</strong></p><img src="https://secure.gravatar.com/avatar/dfd728dcc858e4bb45f3ea8804fe9ba1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hpa&#39;s gravatar image" /><p><span>hpa</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hpa has no accepted answers">0%</span></p></div></div><div id="comments-container-52081" class="comments-container"></div><div id="comment-tools-52081" class="comment-tools"></div><div class="clear"></div><div id="comment-52081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52084"></span>

<div id="answer-container-52084" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52084-score" class="post-score" title="current number of votes">1</div><span id="post-52084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="hpa has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That version of the docs is out of date; the current master README.dissector says:</p><pre><code>The abbreviation is the identifier used in a display filter.  As such it
cannot be an empty string.</code></pre><p>In other words, Wireshark's goal/requirement is that all fields are filterable. We shouldn't presume to know what users may want to filter on.</p><p>A common example I give here is: yes, it <strong>is</strong> useful to be able to filter on spare bytes (which are supposed to always be zero): I've repeatedly had to do that myself to find broken implementations (that is, implementations that aren't setting the spares to 0 and other implementations that aren't ignoring those spares).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '16, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-52084" class="comments-container"><span id="52095"></span><div id="comment-52095" class="comment"><div id="post-52095-score" class="comment-score"></div><div class="comment-text"><blockquote><p>We shouldn't presume to know what users may want to filter on.</p></blockquote><p>And "we" includes <em>all</em> people writing dissectors.</p></div><div id="comment-52095-info" class="comment-info"><span class="comment-age">(30 Apr '16, 01:30)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-52084" class="comment-tools"></div><div class="clear"></div><div id="comment-52084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

