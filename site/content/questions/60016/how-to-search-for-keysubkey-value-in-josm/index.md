+++
type = "question"
title = "How to search for key:subkey = value in jOSM?"
description = '''I want to select all buildings which don&#x27;t have an address set. To find those, I want to seach for -addr:street=*, but this yields an unexpected token: &amp;lt;equals&amp;gt;. How can I seach for this?'''
date = "2017-10-08T18:58:00Z"
lastmod = "2017-10-08T20:18:00Z"
weight = 60016
keywords = [ "josm", "search", "searching" ]
aliases = [ "/questions/60016" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to search for key:subkey = value in jOSM?](/questions/60016/how-to-search-for-keysubkey-value-in-josm)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60016-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60016-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-60016-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to select all buildings which don't have an address set. To find those, I want to seach for <code>-addr:street=*</code>, but this yields an <code>unexpected token: &lt;equals&gt;</code>.</p>
<p>How can I seach for this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-searching" rel="tag" title="see questions tagged &#39;searching&#39;">searching</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Oct '17, 18:58</strong></p>
<img src="https://secure.gravatar.com/avatar/5aa76ca348911cce8f3ce7337f117d46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieter%20Vander%20Vennet&#39;s gravatar image" />
<p><span>Pieter Vande...</span><br />
<span class="score" title="241 reputation points">241</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieter Vander Vennet has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-60016" class="comments-container">
&#10;</div>
<div id="comment-tools-60016" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60016-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60017"></span>

<div id="answer-container-60017" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60017-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-60017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>By now, I've found the answer: put <code>key:subkey</code> in double quotes. The search query thus becomes</p>
<pre><code>    -&quot;addr:street&quot;=*</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Oct '17, 18:59</strong></p>
<img src="https://secure.gravatar.com/avatar/5aa76ca348911cce8f3ce7337f117d46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieter%20Vander%20Vennet&#39;s gravatar image" />
<p><span>Pieter Vande...</span><br />
<span class="score" title="241 reputation points">241</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieter Vander Vennet has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-60017" class="comments-container">
<span id="60020"></span>
<div id="comment-60020" class="comment">
<div id="post-60020-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Without the quotes it the colon is taken as the binary operator from the <em>key:valuefragment</em> syntax. (That syntax documented in the search dialog.)</p>
</div>
<div id="comment-60020-info" class="comment-info">
<span class="comment-age">(08 Oct '17, 20:18)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
</div>
<div id="comment-tools-60017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60017-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

