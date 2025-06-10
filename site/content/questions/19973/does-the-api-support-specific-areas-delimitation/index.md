+++
type = "question"
title = "Does the API support specific areas delimitation?"
description = '''This is related to my last question: https://help.openstreetmap.org/questions/19938/how-to-detect-when-a-nominatim-request-is-not-precise Since there is no way to see if Nominatim is being precise in the request, I thought about delimiting specific areas using OSM API. Then I save the delimited area...'''
date = "2013-02-15T21:20:00Z"
lastmod = "2013-02-16T00:58:00Z"
weight = 19973
keywords = [ "api", "osm", "precision", "nominatim" ]
aliases = [ "/questions/19973" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Does the API support specific areas delimitation?](/questions/19973/does-the-api-support-specific-areas-delimitation)

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
<span id="post-19973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19973-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is related to my last question:</p>
<p><a href="https://help.openstreetmap.org/questions/19938/how-to-detect-when-a-nominatim-request-is-not-precise">https://help.openstreetmap.org/questions/19938/how-to-detect-when-a-nominatim-request-is-not-precise</a></p>
<p>Since there is no way to see if Nominatim is being precise in the request, I thought about delimiting specific areas using OSM API. Then I save the delimited areas into a database and check to see if the point is inside those areas. If it is, then use Nominatim. Else, he redirects to another reverse geocoder.</p>
<p>Also, the user can have the possibility to map that area, so it uses Nominatim next time. So, is the API capable of doing what I want? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-precision" rel="tag" title="see questions tagged &#39;precision&#39;">precision</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Feb '13, 21:20</strong></p>
<img src="https://secure.gravatar.com/avatar/dc06a3de85eb8aa3a8331e85c1390a79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gabriel_casado&#39;s gravatar image" />
<p><span>gabriel_casado</span><br />
<span class="score" title="41 reputation points">41</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gabriel_casado has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-19973" class="comments-container">
&#10;</div>
<div id="comment-tools-19973" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19973-form-container" class="comment-form-container">
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

<span id="19976"></span>

<div id="answer-container-19976" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-19976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19976-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-19976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gabriel_casado has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The main api of OpenStreetMap is meant for editors. While it could do what you want, you shouldn't use it for that.</p>
<p>Luckily there is an alternative that you can use: The Overpass API. Look at the following two links for a solution for rectangular areas:</p>
<ul>
<li><a href="http://wiki.openstreetmap.org/wiki/Overpass_API#The_map_query">http://wiki.openstreetmap.org/wiki/Overpass API#The map query</a></li>
<li><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/XAPI_Compatibility_Layer#Map_call">http://wiki.openstreetmap.org/wiki/Overpass API/XAPI Compatibility Layer#Map call</a></li>
</ul>
<p>And the next one for areas with other shapes:</p>
<ul>
<li><a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Select_Region_by_Polygon">http://wiki.openstreetmap.org/wiki/Overpass API/Language Guide#Select Region by Polygon</a></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Feb '13, 23:18</strong></p>
<img src="https://secure.gravatar.com/avatar/fed945e27bb98de054a867827550812e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cartinus&#39;s gravatar image" />
<p><span>cartinus</span><br />
<span class="score" title="7033 reputation points"><span>7.0k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="66 badges"><span class="silver">●</span><span class="badgecount">66</span></span><span title="105 badges"><span class="bronze">●</span><span class="badgecount">105</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cartinus has 35 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-19976" class="comments-container">
<span id="19978"></span>
<div id="comment-19978" class="comment">
<div id="post-19978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey cartinus, thanks again for the quick response. I'll surely look into the Overpass API.</p>
</div>
<div id="comment-19978-info" class="comment-info">
<span class="comment-age">(16 Feb '13, 00:58)</span> <span class="comment-user userinfo">gabriel_casado</span>
</div>
</div>
</div>
<div id="comment-tools-19976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19976-form-container" class="comment-form-container">
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

