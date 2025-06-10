+++
type = "question"
title = "dynamic real time data"
description = '''Ok, So if we wanted to have dynamic real time objects in OSM, how would we do it? e.g: pedestrians (whos gps position we know from phone data). There GPS position would need to be continuously updated in OSM server and be available for other users. Anyone know of any projects or layers that do anyth...'''
date = "2016-03-08T12:41:00Z"
lastmod = "2016-03-08T14:02:00Z"
weight = 48565
keywords = [ "dynamic", "realtime" ]
aliases = [ "/questions/48565" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [dynamic real time data](/questions/48565/dynamic-real-time-data)

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
<span id="post-48565-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48565-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48565-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Ok, So if we wanted to have dynamic real time objects in OSM, how would we do it? e.g: pedestrians (whos gps position we know from phone data). There GPS position would need to be continuously updated in OSM server and be available for other users.</p>
<p>Anyone know of any projects or layers that do anything similar to this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-dynamic" rel="tag" title="see questions tagged &#39;dynamic&#39;">dynamic</span> <span class="post-tag tag-link-realtime" rel="tag" title="see questions tagged &#39;realtime&#39;">realtime</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Mar '16, 12:41</strong></p>
<img src="https://secure.gravatar.com/avatar/7f70ecc5f7c06544811a2c55749b8fb6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MadCabbage&#39;s gravatar image" />
<p><span>MadCabbage</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MadCabbage has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48565" class="comments-container">
&#10;</div>
<div id="comment-tools-48565" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48565-form-container" class="comment-form-container">
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

<span id="48568"></span>

<div id="answer-container-48568" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48568-score" class="post-score" title="current number of votes">
7
</div>
<span id="post-48568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM is a database of objects and attributes of objects that have at least a semi-stable geographic location (aka are in the same location at least for weeks, not seconds).</p>
<p>In an application as yours you will typically always store the position of the tracked objects in a completly separate database and only refer to OSM for reverse geo-coding and display purposes.</p>
<p>See <a href="https://help.openstreetmap.org/tags/tracking/">https://help.openstreetmap.org/tags/tracking/</a> and <a href="http://opengts.sourceforge.net/">http://opengts.sourceforge.net/</a> for examples.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '16, 12:50</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Mar '16, 12:50</strong> </span></p>
</div>
</div>
<div id="comments-container-48568" class="comments-container">
<span id="48572"></span>
<div id="comment-48572" class="comment">
<div id="post-48572-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. Very useful links. Yes I suppose that OSM could just be used to Geo-reference the objects in a separate database optimized for temporal context. I am pretty new to all this but was just hoping there was a simple little add on layer for OSM... Alas it doesn't seem that simple.</p>
</div>
<div id="comment-48572-info" class="comment-info">
<span class="comment-age">(08 Mar '16, 14:02)</span> <span class="comment-user userinfo">MadCabbage</span>
</div>
</div>
</div>
<div id="comment-tools-48568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48568-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48567"></span>

<div id="answer-container-48567" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48567-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How would you do it? That's easy - you wouldn't. It's entirely outside the scope of what OSM is.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '16, 12:47</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-48567" class="comments-container">
&#10;</div>
<div id="comment-tools-48567" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48567-form-container" class="comment-form-container">
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

