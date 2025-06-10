+++
type = "question"
title = "Not all history is visible through the API?"
description = '''I&#x27;m looking for a problem at map=15/47.0720/22.1241 and specifically I&#x27;m looking for any deletions related to way/84965365. JOSM and the OSM website show only 2 versions in the history, while Potlatch shows several other edits, from January 2016. Why does this difference appear and how can I see wha...'''
date = "2016-03-22T11:04:00Z"
lastmod = "2016-03-22T13:15:00Z"
weight = 48772
keywords = [ "history" ]
aliases = [ "/questions/48772" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Not all history is visible through the API?](/questions/48772/not-all-history-is-visible-through-the-api)

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
<span id="post-48772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48772-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for a problem at map=15/47.0720/22.1241 and specifically I'm looking for any deletions related to way/84965365. JOSM and the OSM website show only 2 versions in the history, while Potlatch shows several other edits, from January 2016. Why does this difference appear and how can I see what those "hidden" changes do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Mar '16, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/957fce0ab30dec2899aab5c7ac4d567b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Strainu&#39;s gravatar image" />
<p><span>Strainu</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Strainu has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48772" class="comments-container">
&#10;</div>
<div id="comment-tools-48772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48772-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="48774"></span>

<div id="answer-container-48774" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48774-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Strainu has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Potlatch looks to be showing you node edits which wouldn't have affected the way (so not adding/removing nodes or changing way tags).</p>
<p><a href="http://www.openstreetmap.org/node/986138464/history">This is just one example</a> - find others by looking at the <a href="http://www.openstreetmap.org/api/0.6/way/84965365/full">XML for the way</a> and looking for node versions greater than 1.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '16, 12:01</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '16, 12:06</strong> </span></p>
</div>
</div>
<div id="comments-container-48774" class="comments-container">
<span id="48775"></span>
<div id="comment-48775" class="comment">
<div id="post-48775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Ed. I'm pretty sure one of the many edits of that user deleted a multipolygon relation that rendered the now white area as agricultural (CLC data dissapeared). Is there any way to find out which change did that except going through them one by one?</p>
</div>
<div id="comment-48775-info" class="comment-info">
<span class="comment-age">(22 Mar '16, 12:30)</span> <span class="comment-user userinfo">Strainu</span>
</div>
</div>
<span id="48776"></span>
<div id="comment-48776" class="comment">
<div id="post-48776-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I checked for deleted ways using Potlatch 1 and found this one: <a href="http://www.openstreetmap.org/way/87489584">http://www.openstreetmap.org/way/87489584</a> which was farmland (history times out, but api call for v8 shows tags <a href="http://www.openstreetmap.org/api/0.6/way/87489584/8">http://www.openstreetmap.org/api/0.6/way/87489584/8</a> )</p>
</div>
<div id="comment-48776-info" class="comment-info">
<span class="comment-age">(22 Mar '16, 12:49)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="48777"></span>
<div id="comment-48777" class="comment">
<div id="post-48777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You can get a rough idea where to start by looking at Potlatch 2's history (which shows node changes). Unfortunately you'll have to match up the dates and times yourself - the most recent change seems to be <a href="https://www.openstreetmap.org/changeset/36879542">https://www.openstreetmap.org/changeset/36879542</a> . Their changes don't seem to include relation changes though, so it may not have been them.</p>
<p>The CLC polygons are huge though - it might have been another user some distance from that way.</p>
</div>
<div id="comment-48777-info" class="comment-info">
<span class="comment-age">(22 Mar '16, 12:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48778"></span>
<div id="comment-48778" class="comment">
<div id="post-48778-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another option for way history:</p>
<p><a href="http://osm.mapki.com/history/way.php?id=87489584">http://osm.mapki.com/history/way.php?id=87489584</a></p>
</div>
<div id="comment-48778-info" class="comment-info">
<span class="comment-age">(22 Mar '16, 13:00)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48779"></span>
<div id="comment-48779" class="comment">
<div id="post-48779-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks <a href="http://help.openstreetmap.org/users/339/edloach">@EdLoach</a> and <a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> for your help and all the useful pointers and tools you provided. I've reverted the changelist as the data added was significantly less than what we lost.</p>
</div>
<div id="comment-48779-info" class="comment-info">
<span class="comment-age">(22 Mar '16, 13:15)</span> <span class="comment-user userinfo">Strainu</span>
</div>
</div>
</div>
<div id="comment-tools-48774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48774-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48773"></span>

<div id="answer-container-48773" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48773-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48773-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48773-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There should not be any hidden version.</p>
<p><a href="http://www.openstreetmap.org/way/84965365/history">http://www.openstreetmap.org/way/84965365/history</a></p>
<p>Indeed, in Potlatch it shows more nodes, wierd</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '16, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/92a51d3af99ee124bb9e06dd35249910?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Badita%20Florin&#39;s gravatar image" />
<p><span>Badita Florin</span><br />
<span class="score" title="112 reputation points">112</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Badita Florin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48773" class="comments-container">
&#10;</div>
<div id="comment-tools-48773" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48773-form-container" class="comment-form-container">
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

