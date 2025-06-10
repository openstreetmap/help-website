+++
type = "question"
title = "How to query OSM APIs and &#x27;polygons.openstreetmap.fr&#x27; properly?"
description = '''Hi, I&#x27;m pretty new to OSM. I&#x27;m working on web application in WebGL, and I have 2 major questions:   I would like to know how to correctly query for city boundaries polygon. I&#x27;ve tried to use JSONP and http.get requests to get data form &#x27;http://polygons.openstreetmap.fr/get_geojson.py?id=1582777&#x27; but...'''
date = "2016-12-13T09:53:00Z"
lastmod = "2016-12-19T08:30:00Z"
weight = 53527
keywords = [ "usage", "query", "nominatim", "polygon", "multipolygon" ]
aliases = [ "/questions/53527" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to query OSM APIs and 'polygons.openstreetmap.fr' properly?](/questions/53527/how-to-query-osm-apis-and-polygonsopenstreetmapfr-properly)

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
<span id="post-53527-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53527-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53527-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm pretty new to OSM. I'm working on web application in WebGL, and I have 2 major questions:</p>
<ol>
<li><p>I would like to know how to correctly query for city boundaries polygon. I've tried to use JSONP and http.get requests to get data form 'http://polygons.openstreetmap.fr/get_geojson.py?id=1582777' but i cant get it, because of CORS policy. This server seems to be JSONP disabled. Does any other kind of similar API exists?</p></li>
<li><p>To get proper relations of my address i'm querying 'nominatim.openstreetmap.org' multiple times, every time constructing new url. Query for address to get city, city to get country, etc. This works but feels really tiresome. How do I query nominatim, knowing street address and getting all info that I need (city, country, continent) ?</p></li>
</ol>
<p>Can you give me some hints?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-usage" rel="tag" title="see questions tagged &#39;usage&#39;">usage</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-multipolygon" rel="tag" title="see questions tagged &#39;multipolygon&#39;">multipolygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '16, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/f417f1f6d3a7f0ab65f2c0e0db5a974f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Treant&#39;s gravatar image" />
<p><span>Treant</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Treant has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Dec '16, 22:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-53527" class="comments-container">
<span id="53533"></span>
<div id="comment-53533" class="comment">
<div id="post-53533-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>cross-posted: <a href="https://gis.stackexchange.com/questions/221219/proper-query-of-osm-apis">https://gis.stackexchange.com/questions/221219/proper-query-of-osm-apis</a></p>
</div>
<div id="comment-53533-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 11:42)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="53538"></span>
<div id="comment-53538" class="comment">
<div id="post-53538-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you give examples of the Nominatim queries/URLs you're currently using?</p>
</div>
<div id="comment-53538-info" class="comment-info">
<span class="comment-age">(13 Dec '16, 15:25)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="53549"></span>
<div id="comment-53549" class="comment">
<div id="post-53549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/150/mtmail">@mtmail</a></p>
<p>I'm starting with osm_id and lonlat</p>
<p>Getting city name -&gt; from osm_id and lonlat: <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=51.7728321&amp;lon=19.4528033&amp;osm_id=246291409&amp;accept-language=en">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=51.7728321&amp;lon=19.4528033&amp;osm_id=246291409&amp;accept-language=en</a></p>
<p>Getting relation -&gt; from city name: <a href="https://nominatim.openstreetmap.org/search.php?city=Łódź&amp;format=json">https://nominatim.openstreetmap.org/search.php?city=Łódź&amp;format=json</a></p>
<p>Getting polygon -&gt; from relation <a href="http://polygons.openstreetmap.fr/get_geojson.py?id=1582777">http://polygons.openstreetmap.fr/get_geojson.py?id=1582777</a></p>
<p>I only have osm_id and lonlat available and I must query for city, relation, country, continent and so on. Can I do it with one url?</p>
</div>
<div id="comment-53549-info" class="comment-info">
<span class="comment-age">(14 Dec '16, 13:58)</span> <span class="comment-user userinfo">Treant</span>
</div>
</div>
<span id="53550"></span>
<div id="comment-53550" class="comment">
<div id="post-53550-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Cross-posted again <a href="https://forum.openstreetmap.org/viewtopic.php?pid=622337#p622337">https://forum.openstreetmap.org/viewtopic.php?pid=622337#p622337</a> .</p>
</div>
<div id="comment-53550-info" class="comment-info">
<span class="comment-age">(14 Dec '16, 14:38)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-53527" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53527-form-container" class="comment-form-container">
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

<span id="53552"></span>

<div id="answer-container-53552" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53552-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-53552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Treant has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>osm_id</code> of your initial search seems to be a street <a href="http://www.openstreetmap.org/way/246291409">http://www.openstreetmap.org/way/246291409</a></p>
<p>To look up the hierarchy starting from the street to the country try <a href="http://nominatim.openstreetmap.org/hierarchy.php?osmid=246291409&amp;osmtype=W">http://nominatim.openstreetmap.org/hierarchy.php?osmid=246291409&amp;osmtype=W</a> and you need to parse the links in the first line. Then for each type and id you have to do more lookups.</p>
<p>Doing a forward search for "Łódź" is too risky as you might get the wrong place back. Searching by ids (and type N,W,R) is better.</p>
<p>OSM data doesn't contain continents.</p>
<p>The reverse search can include polygons: <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;osm_id=1582777&amp;osm_type=R&amp;polygon_geojson=1">http://nominatim.openstreetmap.org/reverse?format=json&amp;osm_id=1582777&amp;osm_type=R&amp;polygon_geojson=1</a> (for the polygon parameters see) <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Parameters_2">https://wiki.openstreetmap.org/wiki/Nominatim#Parameters_2</a></p>
<p>State and country polygons can become large (several megabytes). In this case set &amp;polygon_threshold to a value between 0 and 1 to simplify the polygon in the result. 0.1 is usually a good compromise.</p>
<p>The public Nominatim service has a usage policy (<a href="https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy).">https://wiki.openstreetmap.org/wiki/Nominatim_usage_policy).</a> Both polygon search, especially with large polygons and the hierarchy lookup are "expensive" (take more server resources than usual queries). If you crawl whole countries you will get blocked. If you send requests too fast you will get blocked. If your goal is to create a website for (paying?) customers and require high availability real-time results you should setup your own Nominatim server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Dec '16, 17:23</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-53552" class="comments-container">
<span id="53606"></span>
<div id="comment-53606" class="comment">
<div id="post-53606-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for your help, this pretty much solves it.</p>
</div>
<div id="comment-53606-info" class="comment-info">
<span class="comment-age">(19 Dec '16, 08:30)</span> <span class="comment-user userinfo">Treant</span>
</div>
</div>
</div>
<div id="comment-tools-53552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53552-form-container" class="comment-form-container">
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

