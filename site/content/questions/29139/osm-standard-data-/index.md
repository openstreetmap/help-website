+++
type = "question"
title = "OSM standard data-"
description = '''Does the OSM standard base map change in time using the osc files? What I need to know: if I download data of building footprints today, those building footprints are referred to which date? Do they change with time?'''
date = "2013-12-17T12:52:00Z"
lastmod = "2013-12-17T13:27:00Z"
weight = 29139
keywords = [ "map", "base", "update" ]
aliases = [ "/questions/29139" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [OSM standard data-](/questions/29139/osm-standard-data-)

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
<span id="post-29139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29139-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-29139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Does the OSM standard base map change in time using the osc files? What I need to know: if I download data of building footprints today, those building footprints are referred to which date? Do they change with time?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-base" rel="tag" title="see questions tagged &#39;base&#39;">base</span> <span class="post-tag tag-link-update" rel="tag" title="see questions tagged &#39;update&#39;">update</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Dec '13, 12:52</strong></p>
<img src="https://secure.gravatar.com/avatar/5ce44dbf703bf8ddd04e69d3248fa560?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="udonezar&#39;s gravatar image" />
<p><span>udonezar</span><br />
<span class="score" title="45 reputation points">45</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="udonezar has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-29139" class="comments-container">
<span id="29140"></span>
<div id="comment-29140" class="comment">
<div id="post-29140-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Same question, different approach: OSM base building information for a certain area on the 10th of november is it or is it not the same as 17th of december?</p>
</div>
<div id="comment-29140-info" class="comment-info">
<span class="comment-age">(17 Dec '13, 12:55)</span> <span class="comment-user userinfo">udonezar</span>
</div>
</div>
</div>
<div id="comment-tools-29139" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29139-form-container" class="comment-form-container">
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

<span id="29141"></span>

<div id="answer-container-29141" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-29141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-29141-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-29141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First thing first: do not confuse the data with its rendering. We have many uses of the data, including many renderings and the "standard" rendering you refer to, but we only have one database, which contains all our data.</p>
<p>That data changes very rapidly, and it is an iterative process. When you download data, it is <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">a snapshot of the data</a> at a particular time. If your snapshot is too old for your needs, you can download <a href="https://wiki.openstreetmap.org/wiki/Planet.osm/diffs">diff files</a> which bring you to the latest version.</p>
<p>The data that you fetch from the main database is always "live" and current. Other sources (renderings, extracts, etc) can lag from a few minutes to a few months.</p>
<p>Note also that whenever something changes, the old version of the object is kept in the database as well. You can explore that in your editor or by showing the "map data layer", clicking on an object, and clicking "history" in the left pane. You'll see when the object was changed, by who, in which way, etc. You can also process historical data if you have downloaded a file that contains it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Dec '13, 13:27</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-29141" class="comments-container">
&#10;</div>
<div id="comment-tools-29141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-29141-form-container" class="comment-form-container">
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

