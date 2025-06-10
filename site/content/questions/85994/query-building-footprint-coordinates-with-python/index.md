+++
type = "question"
title = "Query building footprint coordinates with python?"
description = '''I&#x27;m trying to get the geometry of a building by giving a coordinate.  Input (lat,lng) output (coordinates of the building that it intersects). I want to be able to do this with python from a script within QGIS.  I&#x27;ve tried a library called osmnx and managed to get it to work, however the dependencie...'''
date = "2022-10-25T23:09:00Z"
lastmod = "2022-10-26T21:56:00Z"
weight = 85994
keywords = [ "python", "buildings", "osm", "parcel" ]
aliases = [ "/questions/85994" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query building footprint coordinates with python?](/questions/85994/query-building-footprint-coordinates-with-python)

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
<span id="post-85994-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85994-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85994-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get the geometry of a building by giving a coordinate. Input (lat,lng) output (coordinates of the building that it intersects).</p>
<p>I want to be able to do this with python from a script within QGIS.</p>
<p>I've tried a library called osmnx and managed to get it to work, however the dependencies are horrible. Took me a few pip installs and pip uninstalls to get it working correctly.</p>
<p>I need this script to run on a few different computers and I can see that being a huge issue. This also needs to be in QGIS, so I want to avoid the osmnx module.</p>
<p>Is there a way I can do with with maybe a built in module in python to return the coordinates of a polygon.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-buildings" rel="tag" title="see questions tagged &#39;buildings&#39;">buildings</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-parcel" rel="tag" title="see questions tagged &#39;parcel&#39;">parcel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Oct '22, 23:09</strong></p>
<img src="https://secure.gravatar.com/avatar/b3924436d51bf954e5256776d626bedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KrisMapper&#39;s gravatar image" />
<p><span>KrisMapper</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KrisMapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-85994" class="comments-container">
&#10;</div>
<div id="comment-tools-85994" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85994-form-container" class="comment-form-container">
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

<span id="86002"></span>

<div id="answer-container-86002" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-86002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-86002-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-86002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ended up using the Python requests library with building the url query from <a href="http://overpass-turbo.eu/">http://overpass-turbo.eu/</a> Works great!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Oct '22, 21:56</strong></p>
<img src="https://secure.gravatar.com/avatar/b3924436d51bf954e5256776d626bedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="KrisMapper&#39;s gravatar image" />
<p><span>KrisMapper</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="KrisMapper has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-86002" class="comments-container">
&#10;</div>
<div id="comment-tools-86002" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-86002-form-container" class="comment-form-container">
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

