+++
type = "question"
title = "Turbo Overpass buildings with nearest building over 1 km away"
description = '''Can anyone help me get the query for all buildings which are 1 km or more away from any other building in Overpass Turbo? The search area here is limited. All I have at the moment is  area[admin_level=4][name=Zeeland]; node(area)[building]; out;  When I extend it to include also area buildings, I ge...'''
date = "2017-05-16T23:27:00Z"
lastmod = "2017-05-17T15:01:00Z"
weight = 56201
keywords = [ "overpassapi", "overpass", "overpass-turbo" ]
aliases = [ "/questions/56201" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Turbo Overpass buildings with nearest building over 1 km away](/questions/56201/turbo-overpass-buildings-with-nearest-building-over-1-km-away)

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
<span id="post-56201-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56201-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56201-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Can anyone help me get the query for all buildings which are 1 km or more away from any other building in Overpass Turbo?</p>
<p>The search area here is limited. All I have at the moment is</p>
<pre><code>area[admin_level=4][name=Zeeland];
node(area)[building];
out;</code></pre>
<p>When I extend it to include also area buildings, I get a timeout one</p>
<pre><code>area[admin_level=4][name=Zeeland]-&gt;.a;
(
node(area.a)[building];
area(area.a)[building];
);
out;</code></pre>
<p>How to solve that and secondly, how to add the restriction that each other building node or building area is 1 km or more away?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 May '17, 23:27</strong></p>
<img src="https://secure.gravatar.com/avatar/1fb0d12cfde0dfa6aa364a5758928ea8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pander&#39;s gravatar image" />
<p><span>pander</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pander has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 May '17, 11:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-56201" class="comments-container">
&#10;</div>
<div id="comment-tools-56201" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56201-form-container" class="comment-form-container">
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

<span id="56202"></span>

<div id="answer-container-56202" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56202-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56202-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56202-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'll defer to the Overpass Pros but I think you are over-stretching what Overpass can do here.</p>
<p>If you say the search area is limited, import the area into a PostGIS database with osm2pgsql and then do this:</p>
<pre><code>SELECT building.osm_id 
FROM planet_osm_polygon building
WHERE 
   building.building IS NOT NULL AND
   (SELECT COUNT(*) FROM planet_osm_polygon other WHERE
   other.building IS NOT NULL AND 
   other.osm_id &lt;&gt; building.osm_id AND
   ST_DWITHIN(other.way,building.way,1000) LIMIT 1) = 0;</code></pre>
<p>This searches in a "1000 mercator units" radius, you might have to adapt it to your particular area. Also, you might want to exclude "building=no", too. If you want to look for nodes with building tags too, then my recommendation would be to first create temporary table with the polygon centroids for all buildings and mix in the points. Will run much faster too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '17, 23:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-56202" class="comments-container">
<span id="56206"></span>
<div id="comment-56206" class="comment">
<div id="post-56206-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply. The eventual results should not be that many and I have seen similar examples in Overpass. (I will try to find them and post them here.) Setting up a PostGIS and importing is not favorable as I would like others to to the same query and tweak it. And I need otherwise set up a complete system with updates and security etc. In what way is this over-stretching Overpass?</p>
</div>
<div id="comment-56206-info" class="comment-info">
<span class="comment-age">(17 May '17, 09:19)</span> <span class="comment-user userinfo">pander</span>
</div>
</div>
<span id="56207"></span>
<div id="comment-56207" class="comment">
<div id="post-56207-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Here is a similar example in Overpass: <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Highway_around_schools_with_inappropriate_maxspeed_.28since_0.7.54.29">https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_API_by_Example#Highway_around_schools_with_inappropriate_maxspeed_.28since_0.7.54.29</a></p>
</div>
<div id="comment-56207-info" class="comment-info">
<span class="comment-age">(17 May '17, 09:31)</span> <span class="comment-user userinfo">pander</span>
</div>
</div>
<span id="56208"></span>
<div id="comment-56208" class="comment">
<div id="post-56208-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://nominatim.openstreetmap.org/details.php?place_id=158600066">Zeeland</a> is a large area containing thousands of buildings whereas the "highway around schools" query is limited to rather small areas around schools. I don't think these two queries are comparable.</p>
</div>
<div id="comment-56208-info" class="comment-info">
<span class="comment-age">(17 May '17, 10:22)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="56212"></span>
<div id="comment-56212" class="comment">
<div id="post-56212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Simple query on a map that has three buildings results in 30 MB data and abort of query from my side.</p>
<p>[out:json][timeout:25]; ( area<a href="%7B%7Bbbox%7D%7D">"building"="house"</a>; ); out body;</p>
<blockquote>
<p>; out skel qt;</p>
</blockquote>
<p>Is there something wrong with Overpass? I did lots of tests today and for very small areas, it (I guess) tries to query the entire world. Also for</p>
<p>[out:json][timeout:25]; area[admin_level=10][name=Ottoland]-&gt;.a; ( area(area.a)[building="house"]; ); out;</p>
</div>
<div id="comment-56212-info" class="comment-info">
<span class="comment-age">(17 May '17, 15:01)</span> <span class="comment-user userinfo">pander</span>
</div>
</div>
</div>
<div id="comment-tools-56202" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56202-form-container" class="comment-form-container">
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

