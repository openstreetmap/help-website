+++
type = "question"
title = "Primary landuse of a postal code"
description = '''I&#x27;m looking for a way to have a list of U.S. postal codes and the primary type of the area (=landuse?) For example: residential, commercial, military base, airport etc. '''
date = "2016-06-21T10:05:00Z"
lastmod = "2016-06-22T09:55:00Z"
weight = 50351
keywords = [ "landuse", "api", "newbie" ]
aliases = [ "/questions/50351" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Primary landuse of a postal code](/questions/50351/primary-landuse-of-a-postal-code)

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
<span id="post-50351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50351-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm looking for a way to have a list of U.S. postal codes and the primary type of the area (=landuse?) For example: residential, commercial, military base, airport etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-landuse" rel="tag" title="see questions tagged &#39;landuse&#39;">landuse</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-newbie" rel="tag" title="see questions tagged &#39;newbie&#39;">newbie</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jun '16, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/96aec0ab02d6686a75591c7703d9e9b4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Owen32&#39;s gravatar image" />
<p><span>Owen32</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Owen32 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50351" class="comments-container">
<span id="50352"></span>
<div id="comment-50352" class="comment">
<div id="post-50352-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>cross-posted: <a href="https://stackoverflow.com/questions/37939161/zipcodes-and-area-type-landuse">https://stackoverflow.com/questions/37939161/zipcodes-and-area-type-landuse</a></p>
</div>
<div id="comment-50352-info" class="comment-info">
<span class="comment-age">(21 Jun '16, 10:44)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="50357"></span>
<div id="comment-50357" class="comment">
<div id="post-50357-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>also see this answer for limitations of US zip code polygons: <a href="/questions/46371/need-help-showing-zip-codes-on-map-and-their-boundaries">https://help.openstreetmap.org/questions/46371/need-help-showing-zip-codes-on-map-and-their-boundaries</a></p>
</div>
<div id="comment-50357-info" class="comment-info">
<span class="comment-age">(21 Jun '16, 15:03)</span> <span class="comment-user userinfo">neuhausr</span>
</div>
</div>
</div>
<div id="comment-tools-50351" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50351-form-container" class="comment-form-container">
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

<span id="50354"></span>

<div id="answer-container-50354" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50354-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50354-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-50354-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That's entirely possible.</p>
<p>First you download OSM in the format you require.</p>
<p>Then you decide what the possible "types" are. You query your data to group all things that are within such a type. Mind you: the same place might have different types (for example an airport has shops). So then you have to decide whether or not you want to prioritize (eg shops take a bite out of airports, airports hide underlying shops, or both count in their own way). You will also have to account for some features being mapped as both an area and a node (eg a shop in a commercial area). I solved this by giving shops an arbitrary area.</p>
<p>Once you have everything in place, you do a spatial join of points and postal codes, and/or split polygons along the borders of your postal codes. Et voila, you can start counting.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jun '16, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/1df835d513b1282e0edd7405d29cd8d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joost%20schouppe&#39;s gravatar image" />
<p><span>joost schouppe</span><br />
<span class="score" title="3427 reputation points"><span>3.4k</span></span><span title="24 badges"><span class="badge1">●</span><span class="badgecount">24</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="87 badges"><span class="bronze">●</span><span class="badgecount">87</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joost schouppe has 9 accepted answers">12%</span></p>
</div>
</div>
<div id="comments-container-50354" class="comments-container">
<span id="50356"></span>
<div id="comment-50356" class="comment">
<div id="post-50356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain by a specific example? What is the API call for specific lat_lon and get the landuse?</p>
</div>
<div id="comment-50356-info" class="comment-info">
<span class="comment-age">(21 Jun '16, 13:46)</span> <span class="comment-user userinfo">Owen32</span>
</div>
</div>
<span id="50365"></span>
<div id="comment-50365" class="comment">
<div id="post-50365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do you want to do this on user demand on the fly for one area, or are you building a national dataset?</p>
<p>If you want to do the second, you will not be using our API. You will need to download the data (e.g. from download.geofabrik.de ) and convert it to suit your needs (I often use pbf to sqlite, but more people use a postgis solution). Then you will need to study the OSM datamodel (use wiki.openstreetmap.org) enough for you to make decent choices.</p>
<p>This all assuming you get decent polygons for your areas of interest (as I just read neuhausr's link)</p>
</div>
<div id="comment-50365-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 07:28)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
<span id="50374"></span>
<div id="comment-50374" class="comment">
<div id="post-50374-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How can I do it using the API? Determine the primary type of an area\zipcode?</p>
</div>
<div id="comment-50374-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 09:32)</span> <span class="comment-user userinfo">Owen32</span>
</div>
</div>
<span id="50375"></span>
<div id="comment-50375" class="comment">
<div id="post-50375-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The most userfriendly is overpass-turbo. See this example: <a href="http://overpass-turbo.eu/s/gV0">http://overpass-turbo.eu/s/gV0</a> . You can export the data as well as the query. It is possible to have Overpass geocode an area in stead of using a bounding box. You can learn more about the Overpass API on the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">wiki</a> and find many related questions on this forum.</p>
</div>
<div id="comment-50375-info" class="comment-info">
<span class="comment-age">(22 Jun '16, 09:55)</span> <span class="comment-user userinfo">joost schouppe</span>
</div>
</div>
</div>
<div id="comment-tools-50354" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50354-form-container" class="comment-form-container">
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

