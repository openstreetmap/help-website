+++
type = "question"
title = "How do I stop rivers from rendering where the riverbanks are mapped?"
description = '''There are a number of rivers near me that have both the riverbanks mapped, and a rough centre-line mapped for meta data such as whether they&#x27;re navigable and their names. In estuaries, this can cause Osmarender to render fake banks (e.g. http://osm.org/go/0EH2q0Ox--?layers=0B00FTF ) where further in...'''
date = "2010-07-12T13:26:00Z"
lastmod = "2010-07-12T13:38:00Z"
weight = 125
keywords = [ "rendering", "tagging" ]
aliases = [ "/questions/125" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I stop rivers from rendering where the riverbanks are mapped?](/questions/125/how-do-i-stop-rivers-from-rendering-where-the-riverbanks-are-mapped)

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
<span id="post-125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-125-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>There are a number of rivers near me that have both the riverbanks mapped, and a rough centre-line mapped for meta data such as whether they're navigable and their names.</p>
<p>In estuaries, this can cause Osmarender to render fake banks (e.g. <a href="http://osm.org/go/0EH2q0Ox--?layers=0B00FTF">http://osm.org/go/0EH2q0Ox--?layers=0B00FTF</a> ) where further inland, Mapnik has a habit of rendering the river beyond its banks (e.g. <a href="http://osm.org/go/0EHS3x2j">http://osm.org/go/0EHS3x2j</a> ).</p>
<p>Is there some way of telling all renderers to not render the segments in these cases?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '10, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/8c8779a33adeec01e05d5a480c7cd3c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rowland&#39;s gravatar image" />
<p><span>Rowland</span><br />
<span class="score" title="596 reputation points">596</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rowland has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-125" class="comments-container">
&#10;</div>
<div id="comment-tools-125" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-125-form-container" class="comment-form-container">
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

<span id="127"></span>

<div id="answer-container-127" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-127-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-127-score" class="post-score" title="current number of votes">
10
</div>
<span id="post-127-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rowland has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can make sure that the rivers centerline does not cross any island, but you should neither remove it nor play any tricks to make the rendering look nicer. If the rendering of correct data looks bad it's the renderer that needs tweaking, not the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '10, 13:38</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-127" class="comments-container">
&#10;</div>
<div id="comment-tools-127" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-127-form-container" class="comment-form-container">
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

