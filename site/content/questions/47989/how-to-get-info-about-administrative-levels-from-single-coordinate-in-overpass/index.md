+++
type = "question"
title = "How to get info about administrative levels from single coordinate in overpass"
description = '''By providing a single coordinate, not a bounding box, I want to extract the administrative areas that is within the coordinate. For example when providing the coordinate for central London, I would like to know all the boundaries that covers the coordinate, actual country, region, sub region adminis...'''
date = "2016-02-07T10:30:00Z"
lastmod = "2016-02-07T17:08:00Z"
weight = 47989
keywords = [ "overpass", "levels", "administrative", "oordinate", "get" ]
aliases = [ "/questions/47989" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to get info about administrative levels from single coordinate in overpass](/questions/47989/how-to-get-info-about-administrative-levels-from-single-coordinate-in-overpass)

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
<span id="post-47989-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47989-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47989-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>By providing a single coordinate, not a bounding box, I want to extract the administrative areas that is within the coordinate. For example when providing the coordinate for central London, I would like to know all the boundaries that covers the coordinate, actual country, region, sub region administrative area etc.</p>
<p>Is it possible to get such information from overpass?</p>
<p>What I am asking for is more or less the same informatio that is given by using the questing mark function i open street map where it presents all such information.</p>
<p>I need to know the id of the boundary, the administrative level and the name of the boundary. An I also would like to know the actual boundary as a polygon.</p>
<p>I want to access it by using either php or javascript...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-levels" rel="tag" title="see questions tagged &#39;levels&#39;">levels</span> <span class="post-tag tag-link-administrative" rel="tag" title="see questions tagged &#39;administrative&#39;">administrative</span> <span class="post-tag tag-link-oordinate" rel="tag" title="see questions tagged &#39;oordinate&#39;">oordinate</span> <span class="post-tag tag-link-get" rel="tag" title="see questions tagged &#39;get&#39;">get</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Feb '16, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/7d879d68e986486305a0f1be2bb9e2fd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SunYour&#39;s gravatar image" />
<p><span>SunYour</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SunYour has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47989" class="comments-container">
&#10;</div>
<div id="comment-tools-47989" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47989-form-container" class="comment-form-container">
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

<span id="47990"></span>

<div id="answer-container-47990" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47990-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47990-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-47990-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SunYour has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The is_in query does just that. Read all about it here:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_.28is_in.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_.28is_in.29</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Feb '16, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-47990" class="comments-container">
<span id="47992"></span>
<div id="comment-47992" class="comment">
<div id="post-47992-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, that is what I was looking for!</p>
<p>This example is what I need to call <a href="http://overpass.osm.rambler.ru/cgi/interpreter?data=%5Bout:json%5D;is_in(59.68,16.77);out;">http://overpass.osm.rambler.ru/cgi/interpreter?data=[out:json];is_in(59.68,16.77);out;</a></p>
<p>Now I need to adapt my parser that used the lovely mapIt solution, but it unfortunately lacked som issues here and there.</p>
<p>I still need to find out how to get the boundary polygon, preferrably as kml if possible.</p>
</div>
<div id="comment-47992-info" class="comment-info">
<span class="comment-age">(07 Feb '16, 16:22)</span> <span class="comment-user userinfo">SunYour</span>
</div>
</div>
<span id="47993"></span>
<div id="comment-47993" class="comment">
<div id="post-47993-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can use <code>out geom</code> to retrieve the geometry:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Print_.28out.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Print_.28out.29</a></p>
<p>There is not support for KML output from Overpass API. You can look at Overpass Turbo for an example of converting the output, togpx and tokml here: <a href="https://github.com/tyrasd/overpass-turbo/tree/master/libs">https://github.com/tyrasd/overpass-turbo/tree/master/libs</a></p>
</div>
<div id="comment-47993-info" class="comment-info">
<span class="comment-age">(07 Feb '16, 17:08)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-47990" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47990-form-container" class="comment-form-container">
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

