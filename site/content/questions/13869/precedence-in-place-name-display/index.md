+++
type = "question"
title = "Precedence in place name display"
description = '''Hi there, I&#x27;m wondering if it was possible to specify in an easy way which place name label should take precedence over others. Concretely, there are a bunch of place=city&#x27;s around where I live (http://www.openstreetmap.org/?mlat=-32.89&amp;amp;mlon=151.8&amp;amp;zoom=6&amp;amp;layers=M) but the &quot;wrong&quot; city la...'''
date = "2012-06-28T06:53:00Z"
lastmod = "2012-06-30T09:18:00Z"
weight = 13869
keywords = [ "rendering", "prioritization", "place", "order" ]
aliases = [ "/questions/13869" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Precedence in place name display](/questions/13869/precedence-in-place-name-display)

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
<span id="post-13869-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13869-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13869-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi there,</p>
<p>I'm wondering if it was possible to specify in an easy way which place name label should take precedence over others.</p>
<p>Concretely, there are a bunch of place=city's around where I live (<a href="http://www.openstreetmap.org/?mlat=-32.89&amp;mlon=151.8&amp;zoom=6&amp;layers=M)">http://www.openstreetmap.org/?mlat=-32.89&amp;mlon=151.8&amp;zoom=6&amp;layers=M)</a> but the "wrong" city label is rendered --- Cessnock has only 18,000 odd inhabitants, where as Newcastle has around 500,000. Yet Cessnock's label is rendered, not Newcastle's. How can I give the renderer a clue that he better ought render Newcastle's label?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-prioritization" rel="tag" title="see questions tagged &#39;prioritization&#39;">prioritization</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span> <span class="post-tag tag-link-order" rel="tag" title="see questions tagged &#39;order&#39;">order</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jun '12, 06:53</strong></p>
<img src="https://secure.gravatar.com/avatar/9234009f8e41476a37dc94d88cb4b567?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="floz&#39;s gravatar image" />
<p><span>floz</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="floz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13869" class="comments-container">
<span id="13909"></span>
<div id="comment-13909" class="comment">
<div id="post-13909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>have you already tried to type "label" in the text search box at the top of this site ... according to the headlines from the results, you can read some informations there ... maybe someone other also has found misplaced labels ...</p>
</div>
<div id="comment-13909-info" class="comment-info">
<span class="comment-age">(29 Jun '12, 15:49)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-13869" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13869-form-container" class="comment-form-container">
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

<span id="13912"></span>

<div id="answer-container-13912" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13912-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13912-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-13912-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="floz has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The standard map style displays lables in the following order:</p>
<ol>
<li><em>place=country</em> | <em>state</em></li>
<li><em>place=city</em> | <em>metropolis</em> | <em>town</em> and <em>capital=yes</em></li>
<li><em>place=city</em> | <em>metropolis</em> | <em>town</em> | <em>large_town</em> | <em>small_town</em></li>
<li><em>place=suburb</em> | <em>village</em> | <em>large_village</em> | <em>hamlet</em> | <em>locality</em> | <em>isolated_dwelling</em> | <em>farm</em></li>
</ol>
<p>Different may styles can display tags in any other order and may use other tags like <em>population=</em>. You should not tag for the renderer but rather use the documentation in the <a href="http://wiki.openstreetmap.org/wiki/Key:place">wiki</a> to decide how to tag.</p>
<p>In your case I would say that Newcastle is a city while Cessnock is only a town.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jun '12, 18:41</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-13912" class="comments-container">
<span id="13917"></span>
<div id="comment-13917" class="comment">
<div id="post-13917-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks very much!</p>
</div>
<div id="comment-13917-info" class="comment-info">
<span class="comment-age">(30 Jun '12, 09:18)</span> <span class="comment-user userinfo">floz</span>
</div>
</div>
</div>
<div id="comment-tools-13912" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13912-form-container" class="comment-form-container">
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

