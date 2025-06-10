+++
type = "question"
title = "Can I export only needed coordinates from a certain area?"
description = '''Hello OpenStreetMap users, I am working with a simulation program and would like to add all supermarkets in a city as GIS nodes on my map. I read I can get all coordinates for supermarkets using openstreetmap. However, when I click on export it exports all points and nodes from a selected area. This...'''
date = "2019-06-07T14:13:00Z"
lastmod = "2019-06-07T14:30:00Z"
weight = 69533
keywords = [ "export" ]
aliases = [ "/questions/69533" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Can I export only needed coordinates from a certain area?](/questions/69533/can-i-export-only-needed-coordinates-from-a-certain-area)

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
<span id="post-69533-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69533-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69533-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello OpenStreetMap users,</p>
<p>I am working with a simulation program and would like to add all supermarkets in a city as GIS nodes on my map. I read I can get all coordinates for supermarkets using openstreetmap. However, when I click on export it exports all points and nodes from a selected area. This area can only be a certain part of the city, otherwise it would be too big and it is impossible to download. Looks like the only option I would have it to find every supermarket by hand, download coordinates for all buildings in the area and then select the ones I want by hand. Is that really the only option I have or is there any easier way how to select just the buildings I need and download an osm file with just the information I need?</p>
<p>Any help would be appreciated :) KR</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Jun '19, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/890083efa8b7e40c7d0c513c524a0f35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="barborapetrovic&#39;s gravatar image" />
<p><span>barborapetrovic</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="barborapetrovic has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69533" class="comments-container">
&#10;</div>
<div id="comment-tools-69533" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69533-form-container" class="comment-form-container">
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

<span id="69535"></span>

<div id="answer-container-69535" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69535-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69535-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-69535-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A frequently used tool for partical extracts from OSM is "Overpass Turbo" and you will find many examples for data extraction with it here, or on the OSM wiki. Some objects like supermarkets will sometimes be mapped as a point and sometimes as a polygon, in which case you might want to retrieve the centre of the polygon; Overpass can do that too.</p>
<p>A more flexible approach is loading the OSM data for the region of interest into a PostGIS database on your local machine, then you can make even more complex queries, but it requires setting up the database whereas Overpass is already available.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Jun '19, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-69535" class="comments-container">
&#10;</div>
<div id="comment-tools-69535" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69535-form-container" class="comment-form-container">
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

