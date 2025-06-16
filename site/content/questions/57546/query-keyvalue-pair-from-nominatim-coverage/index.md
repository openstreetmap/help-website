+++
type = "question"
title = "Query Key,Value Pair From Nominatim &quot;Coverage&quot;"
description = '''I have spent about , 26 minutes, looking for a resource that would allow me to query ,key value pairs , on the Nominatim page to check what type of coverage the city has? (I.E if it is a polygon?)  EXAMPLE Bellevue, Washington https://nominatim.openstreetmap.org/details.php?place_id=172952334 Type b...'''
date = "2017-08-10T15:04:00Z"
lastmod = "2017-08-12T03:56:00Z"
weight = 57546
keywords = [ "python", "query", "api", "osmosis", "nominatim" ]
aliases = [ "/questions/57546" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Query Key,Value Pair From Nominatim "Coverage"](/questions/57546/query-keyvalue-pair-from-nominatim-coverage)

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
<span id="post-57546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57546-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have spent about , 26 minutes, <strong>looking for a resource that would allow me to query ,key value pairs , on the Nominatim page to check what type of</strong> coverage <strong>the city has? (I.E if it is a polygon?)</strong></p>
<hr />
<h2 id="example">EXAMPLE</h2>
<p>Bellevue, Washington <a href="https://nominatim.openstreetmap.org/details.php?place_id=172952334">https://nominatim.openstreetmap.org/details.php?place_id=172952334</a></p>
<pre><code>Type    boundary:administrative
Last Updated    2017-06-20 21:45
Admin Level 8
Rank    City
Importance  0.470508128507761
Coverage    Polygon</code></pre>
<hr />
<p>Where would I even go for this information? "The information that I am looking for is the <strong>key, value pair of "Coverage"</strong></p>
<h2 id="what-i-have-searched-for">What I have searched for:</h2>
<p>I looked on this page and was not able to find it because "Coverage" is not a tag. <a href="https://wiki.openstreetmap.org/wiki/Databases_and_data_access_APIs#Sources_of_OSM_Data">Databases and data access APIs</a></p>
<p>I know it says this "Quite a few people break this file down into smaller files for different regions and make extracts available separately on mirror servers. Various tools are available to cut the Planet file up into smaller areas if required."</p>
<p>One solution that I that I have found is to setup Nominatim db on a server which I do not want to do if I necessarily do not have too.</p>
<h2 id="other-solutions">Other Solutions</h2>
<p>Maybe I can query this with osmosis? But from what I read that , it does is allow you manipulate shape files. If what I seek is not in a shape, how would I be able to know beforehand? <strong>Would it not be useful to know what actual shapes are in the file before you manipulate it?</strong> Maybe this exists?</p>
<p>That is why I would like to look them up in a nominatum query by coverage. I simply would like to check if a list of city names exist as a polygon against the nominatum api. ( I.e Python: for i is in Mylist: return True) <a href="https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.43#Default_Arguments">https://wiki.openstreetmap.org/wiki/Osmosis/Detailed_Usage_0.43#Default_Arguments</a></p>
<p>Maybe I suck at searching, I apologize in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '17, 15:04</strong></p>
<img src="https://secure.gravatar.com/avatar/f53d8e0fa41764d2f69b3c5375501187?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Chris_L&#39;s gravatar image" />
<p><span>Chris_L</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Chris_L has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '17, 15:06</strong> </span></p>
</div>
</div>
<div id="comments-container-57546" class="comments-container">
&#10;</div>
<div id="comment-tools-57546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57546-form-container" class="comment-form-container">
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

<span id="57548"></span>

<div id="answer-container-57548" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57548-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57548-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-57548-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The database query Nominatim runs is (simplified) <code>SELECT name-&gt;'name' from placex where admin_level=8 and ST_GeometryType(geometry) in ('ST_Polygon','ST_MultiPolygon') AS isarea where ...;</code></p>
<p>Without setting up a Nominatim database you won't be able to run such a query against a whole country.</p>
<p>The next best would be to run queries against the Nominatim API <a href="http://nominatim.openstreetmap.org/search.php?city=bellevue&amp;country=united+states&amp;format=jsonv2&amp;polygon_geojson=1">http://nominatim.openstreetmap.org/search.php?city=bellevue&amp;country=united+states&amp;format=jsonv2&amp;polygon_geojson=1</a> and check the type of the geometry value ('Point', 'Polygon', 'MultiPolygon').</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '17, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-57548" class="comments-container">
<span id="57972"></span>
<div id="comment-57972" class="comment">
<div id="post-57972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/150/mtmail"></a><a href="https://help.openstreetmap.org/users/150/mtmail">@mtmail</a> Thank you for your reply. When you say "check the type of the geometry value of each api call ('Point', 'Polygon', 'MultiPolygon')", would that not be computationally expensive and would I not be breaking the terms of service for nominatim? I would then have to parse each query to see if it contains a certain geometry.I think setting up the database, may be the way to go. Does Nominatim have a fuzzy search for the names? I saw this <a href="https://github.com/komoot/photon">https://github.com/komoot/photon</a></p>
</div>
<div id="comment-57972-info" class="comment-info">
<span class="comment-age">(12 Aug '17, 03:56)</span> <span class="comment-user userinfo">Chris_L</span>
</div>
</div>
</div>
<div id="comment-tools-57548" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57548-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

