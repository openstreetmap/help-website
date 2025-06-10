+++
type = "question"
title = "Why does this way only show up at one zoom level (16)?"
description = '''The way in question: https://www.openstreetmap.org/way/1016429692 With Firefox it only shows up as the Peace Hills (waste) Transfer Station at zoom level 16, any other zoom level and it is just a blank hole in the forest. With Chromium it is a blank hole at all zoom levels. Have I defined the way in...'''
date = "2022-05-24T09:01:00Z"
lastmod = "2022-06-07T15:59:00Z"
weight = 84573
keywords = [ "zoomlevel", "firefox", "blank" ]
aliases = [ "/questions/84573" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why does this way only show up at one zoom level (16)?](/questions/84573/why-does-this-way-only-show-up-at-one-zoom-level-16)

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
<span id="post-84573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84573-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The way in question: <a href="https://www.openstreetmap.org/way/1016429692">https://www.openstreetmap.org/way/1016429692</a> With Firefox it only shows up as the Peace Hills (waste) Transfer Station at zoom level 16, any other zoom level and it is just a blank hole in the forest. With Chromium it is a blank hole at all zoom levels. Have I defined the way incorrectly? It is not that this is a new change, I've been tinkering with this for months, I've just only gotten around to trying to debug it now.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-zoomlevel" rel="tag" title="see questions tagged &#39;zoomlevel&#39;">zoomlevel</span> <span class="post-tag tag-link-firefox" rel="tag" title="see questions tagged &#39;firefox&#39;">firefox</span> <span class="post-tag tag-link-blank" rel="tag" title="see questions tagged &#39;blank&#39;">blank</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '22, 09:01</strong></p>
<img src="https://secure.gravatar.com/avatar/a86a6c6d658f142a63e296bc23234e5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JMGonk&#39;s gravatar image" />
<p><span>JMGonk</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JMGonk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84573" class="comments-container">
<span id="84728"></span>
<div id="comment-84728" class="comment">
<div id="post-84728-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>FYI, there's no requirement for the area tag.</p>
</div>
<div id="comment-84728-info" class="comment-info">
<span class="comment-age">(07 Jun '22, 15:59)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-84573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84573-form-container" class="comment-form-container">
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

<span id="84575"></span>

<div id="answer-container-84575" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84575-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JMGonk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>amenity=waste_transfer_station</code> is not rendered yet. You need a <code>landuse=industrial</code>, which is still correct. <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/4366">https://github.com/gravitystorm/openstreetmap-carto/issues/4366</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '22, 09:40</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '22, 09:41</strong> </span></p>
</div>
</div>
<div id="comments-container-84575" class="comments-container">
<span id="84599"></span>
<div id="comment-84599" class="comment">
<div id="post-84599-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That did it, thanks.</p>
</div>
<div id="comment-84599-info" class="comment-info">
<span class="comment-age">(27 May '22, 11:42)</span> <span class="comment-user userinfo">JMGonk</span>
</div>
</div>
</div>
<div id="comment-tools-84575" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84575-form-container" class="comment-form-container">
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

