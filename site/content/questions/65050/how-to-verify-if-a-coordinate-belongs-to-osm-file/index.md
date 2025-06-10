+++
type = "question"
title = "How to verify if a coordinate belongs to OSM file?"
description = '''I have a OSM file (I&#x27;m actually using OSRM), and I have a list of coordinates of the type (lat,lon). I need a way to test whether each coordinate is inside the boundaries of the OSM file (as the file can be of only a small region of the world, i.e., I&#x27;m using Berlin for testing purposes). I tried se...'''
date = "2018-08-01T02:09:00Z"
lastmod = "2018-08-02T08:02:00Z"
weight = 65050
keywords = [ "osrm", "search", "osm", "coordinates" ]
aliases = [ "/questions/65050" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to verify if a coordinate belongs to OSM file?](/questions/65050/how-to-verify-if-a-coordinate-belongs-to-osm-file)

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
<span id="post-65050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65050-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a OSM file (I'm actually using OSRM), and I have a list of coordinates of the type (lat,lon). I need a way to test whether each coordinate is inside the boundaries of the OSM file (as the file can be of only a small region of the world, i.e., I'm using Berlin for testing purposes).</p>
<p>I tried searching for solutions, but none seemed clear enough to me. I've read some suggestions on using PostGIS, though I'm not particularly aware of how this would work, as I need to test the existence of a coordinate that not necessarily has a corresponding node in the OSM file to begin with (only a closest one).</p>
<p>Note: I'm building an application in C++, to run solely as a local application. Speed on this test is not a particular issue, although I'll be using lists with a few thousands coordinates.</p>
<p>Any hints on how to proceed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Aug '18, 02:09</strong></p>
<img src="https://secure.gravatar.com/avatar/42da8adc3f056c970ce062f6e211d5df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lonatico&#39;s gravatar image" />
<p><span>Lonatico</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lonatico has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Aug '18, 12:18</strong> </span></p>
</div>
</div>
<div id="comments-container-65050" class="comments-container">
<span id="65052"></span>
<div id="comment-65052" class="comment">
<div id="post-65052-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What does "a valid coordinate in the OSM file" mean exactly? That the coordinate is inside the bounding box / polygon of your OSM file? Or that something (a POI, a street) exists at this coordinate?</p>
</div>
<div id="comment-65052-info" class="comment-info">
<span class="comment-age">(01 Aug '18, 07:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="65058"></span>
<div id="comment-65058" class="comment">
<div id="post-65058-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai"></a><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>, thanks for the comment. It would be the first option, that is, whether the coordinate is inside the boundaries of my OSM file. I don't really care what is in this coordinate, as long as I can know it is a coordinate inside the file limits. (edit: I have updated the question to better state this).</p>
</div>
<div id="comment-65058-info" class="comment-info">
<span class="comment-age">(01 Aug '18, 12:16)</span> <span class="comment-user userinfo">Lonatico</span>
</div>
</div>
</div>
<div id="comment-tools-65050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65050-form-container" class="comment-form-container">
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

<span id="65063"></span>

<div id="answer-container-65063" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65063-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>At least the XML format for OSM data will contain a "bounds" object with a bounding box, see <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">https://wiki.openstreetmap.org/wiki/OSM_XML</a> That is however just a rough approximation of the area covered by the data, in particular if you extracted OSM data using a polygon it will be too large. If that is the case (that you extracted data using a polygon), I would suggest simply doing a point in/covered by polygon test to determine if the location is covered. While this is built into PostGIS, if you are not using it anyway you can simply use one of the many C++ libraries (depending a bit in what format you have the polygon).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Aug '18, 16:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '18, 08:53</strong> </span></p>
</div>
</div>
<div id="comments-container-65063" class="comments-container">
<span id="65069"></span>
<div id="comment-65069" class="comment">
<div id="post-65069-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, but as you said it is a rough approximation (sadly too rough for my need). I think I didn't extract OSM data using a polygon (in fact I'm not sure what this means).</p>
<p>I have managed to locate a polygon file in Geofabrik website, which appears to give me a set of coordinates that define the borders of the entire region/polygon. From that I could just use an algorithm for checking point-in-polygon, but the problem is that for wide areas (e.g., a continental country) I would have the problem of earth's curvature in the calculation. Do you have any suggestion on that?</p>
</div>
<div id="comment-65069-info" class="comment-info">
<span class="comment-age">(02 Aug '18, 00:31)</span> <span class="comment-user userinfo">Lonatico</span>
</div>
</div>
<span id="65071"></span>
<div id="comment-65071" class="comment">
<div id="post-65071-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15466/lonatico">@Lonatico</a> This is a question for <a href="http://gis.stackexchange.com/">http://gis.stackexchange.com/</a> since it isn't OSM-specific.</p>
</div>
<div id="comment-65071-info" class="comment-info">
<span class="comment-age">(02 Aug '18, 07:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="65072"></span>
<div id="comment-65072" class="comment">
<div id="post-65072-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15466/lonatico"></a><a href="https://help.openstreetmap.org/users/15466/lonatico">@Lonatico</a> you would be using the WGS84 coordinates (which are defined on the WGS84 geoid) as coordinates on a plane which is the <a href="https://en.wikipedia.org/wiki/Equirectangular_projection">plate carrée projection</a>. While the result is (naturally) distorted, simple topological relationships still hold (except over the -180°/180° boundary where if you limit the coordinate range to -180° - 180° you will need to split the boundary polygons).</p>
</div>
<div id="comment-65072-info" class="comment-info">
<span class="comment-age">(02 Aug '18, 08:02)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-65063" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65063-form-container" class="comment-form-container">
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

