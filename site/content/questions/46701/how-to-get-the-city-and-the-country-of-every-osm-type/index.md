+++
type = "question"
title = "How to get the city and the country of every osm type?"
description = '''Hello, i want to collect all points that have &quot;amenity=school&quot; as tag and i created the following raw data URL: http://overpass-api.de/api/interpreter?data=[out:json];(node[amenity=school];&amp;gt;;way[amenity=school];&amp;gt;;relation[amenity=school];&amp;gt;;);out; Since not all the points have address tags, ...'''
date = "2015-11-19T08:18:00Z"
lastmod = "2015-11-19T17:21:00Z"
weight = 46701
keywords = [ "city", "nominatim", "address", "overpass-api", "country" ]
aliases = [ "/questions/46701" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get the city and the country of every osm type?](/questions/46701/how-to-get-the-city-and-the-country-of-every-osm-type)

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
<span id="post-46701-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46701-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46701-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, i want to collect all points that have "amenity=school" as tag and i created the following raw data URL:</p>
<p><a href="http://overpass-api.de/api/interpreter?data=%5Bout:json%5D;(node%5Bamenity=school%5D;%3E;way%5Bamenity=school%5D;%3E;relation%5Bamenity=school%5D;%3E;);out;">http://overpass-api.de/api/interpreter?data=[out:json];(node[amenity=school];&gt;;way[amenity=school];&gt;;relation[amenity=school];&gt;;);out;</a></p>
<p>Since not all the points have address tags, is it possibile to combine the Nominatim's reverse geocoding capabilities with the overpass-api query to get all the points with related city and country?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-city" rel="tag" title="see questions tagged &#39;city&#39;">city</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span> <span class="post-tag tag-link-country" rel="tag" title="see questions tagged &#39;country&#39;">country</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '15, 08:18</strong></p>
<img src="https://secure.gravatar.com/avatar/50334ab2e351e4f5af1917f7f6ef8dc8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andreanovenove&#39;s gravatar image" />
<p><span>Andreanovenove</span><br />
<span class="score" title="126 reputation points">126</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="18 badges"><span class="bronze">●</span><span class="badgecount">18</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andreanovenove has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-46701" class="comments-container">
&#10;</div>
<div id="comment-tools-46701" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46701-form-container" class="comment-form-container">
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

<span id="46718"></span>

<div id="answer-container-46718" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46718-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I am not 100% but I think that overpassAPI and overpass-turbo cannot deliver any reverse geocoding.</p>
<p>So you need an own solution, either by Nominatim, or by anothzer search engine or framework ... see <a href="https://wiki.openstreetmap.org/wiki/Search_engines">Search_engines</a></p>
<p>Also do a search on this FAQ site for "bulk geocoding" and "reverse geocoding".</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '15, 16:38</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-46718" class="comments-container">
<span id="46720"></span>
<div id="comment-46720" class="comment">
<div id="post-46720-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL#Query_for_areas_.28is_in.29">is_in</a> query acts as a reverse geocode, but there is not an Overpass operator to mark up the input items with the geocoding results, it would have to be used in a manner similar to nominatim.</p>
</div>
<div id="comment-46720-info" class="comment-info">
<span class="comment-age">(19 Nov '15, 17:21)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-46718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46718-form-container" class="comment-form-container">
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

