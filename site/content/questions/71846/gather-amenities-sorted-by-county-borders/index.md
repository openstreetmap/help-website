+++
type = "question"
title = "Gather amenities sorted by county borders"
description = '''Hello everyone,  my goal is to gather the number of certain amenitys (for example: amenity=bar) in Germany, but sorted in a csv by the county border (admin_level=6) they belong to. This works fine for one county border in Overpass Turbo: [out:csv(::type,::id, name,&quot;addr:postcode&quot;, &quot;addr:city&quot;)]; are...'''
date = "2019-11-26T17:00:00Z"
lastmod = "2019-12-13T18:43:00Z"
weight = 71846
keywords = [ "region", "csv", "overpass-turbo", "amenity" ]
aliases = [ "/questions/71846" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Gather amenities sorted by county borders](/questions/71846/gather-amenities-sorted-by-county-borders)

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
<span id="post-71846-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71846-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-71846-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>my goal is to gather the number of certain amenitys (for example: amenity=bar) in Germany, but sorted in a csv by the county border (admin_level=6) they belong to.</p>
<p>This works fine for one county border in Overpass Turbo:</p>
<pre><code>[out:csv(::type,::id, name,&quot;addr:postcode&quot;, &quot;addr:city&quot;)];
area[admin_level=6][&quot;name&quot;=&quot;Bautzen&quot;];  
( 
   node[&quot;amenity&quot;=&quot;bar&quot;](area);
   way[&quot;amenity&quot;=&quot;bar&quot;](area);
   rel[&quot;amenity&quot;=&quot;bar&quot;](area);
);
out body;
&gt;;
out skel qt;</code></pre>
<p>But Germany has 403 of them, so inserting each of them in a new query would be way to much effort. On the other hand I don't now how to match the amenitys, when I do a seach for the whole of Germany. For example, this isn't possible via the postcode, because not every amenity have one assigned.</p>
<p>Is there a good and faster way to gather these informations with the right assignment ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-region" rel="tag" title="see questions tagged &#39;region&#39;">region</span> <span class="post-tag tag-link-csv" rel="tag" title="see questions tagged &#39;csv&#39;">csv</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Nov '19, 17:00</strong></p>
<img src="https://secure.gravatar.com/avatar/12d3c077816229dbe8dd6863592e88f5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Detektiv%20Mittens&#39;s gravatar image" />
<p><span>Detektiv Mit...</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Detektiv Mittens has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '19, 19:22</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span></p>
</div>
</div>
<div id="comments-container-71846" class="comments-container">
&#10;</div>
<div id="comment-tools-71846" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71846-form-container" class="comment-form-container">
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

<span id="71847"></span>

<div id="answer-container-71847" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71847-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-71847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Detektiv Mittens has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since it looks like you want to make many of these queries, don't hammer someone else's server with it - do it yourself. Load the OSM data for Germany into a PostGIS database with osm2pgsql, then run this query:</p>
<pre><code>SELECT 
  county.name, count(*)
FROM 
  planet_osm_point poi, 
  planet_osm_polygon county
WHERE 
  poi.amenity=&#39;bar&#39;
  AND county.boundary=&#39;administrative&#39;
  AND county.admin_level=&#39;6&#39;
  AND st_contains(county.way, poi.way)
GROUP BY county.name;</code></pre>
<p>This will only give you the point-shaped bars, and you have to repeat this with "planet_osm_polygon poi" instead of "planet_osm_point poi" to count the polygon-shaped ones. (You can also count both at once but that makes the query harder to understand.) You can even count a large number of different amenities in one go:</p>
<pre><code>SELECT 
  poi.amenity, county.name, count(*)
FROM 
  planet_osm_point poi, 
  planet_osm_polygon county
WHERE 
  poi.amenity in (&#39;bar&#39;, &#39;restaurant&#39;, &#39;pub&#39;)
  AND county.boundary=&#39;administrative&#39;
  AND county.admin_level=&#39;6&#39;
  AND st_contains(county.way, poi.way)
GROUP BY poi.amenity, county.name;</code></pre>
<p>(BTW, note that these queries will omit Hamburg and Berlin due to lack of an adminlevel 6 boundary.)</p>
<p>If you are interested in OSM statistics then using your own PostGIS and learning a little SQL is really useful.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Nov '19, 17:38</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-71847" class="comments-container">
<span id="71891"></span>
<div id="comment-71891" class="comment">
<div id="post-71891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your detailed answer. I hoped that there was a more simpler way, but I will try to fiddle around with PostGis and see how far I get.</p>
</div>
<div id="comment-71891-info" class="comment-info">
<span class="comment-age">(28 Nov '19, 18:04)</span> <span class="comment-user userinfo">Detektiv Mit...</span>
</div>
</div>
<span id="72097"></span>
<div id="comment-72097" class="comment">
<div id="post-72097-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hey I have some further questions, if you don't mind and if it is still fitting for this thread. I successfully build the database and run different queries, like you showed me.</p>
<p>I am wondering now about the accuracies of the data. When I am for example run a query for ‘amenity=prison’ I got as a result for planet_osm_point poi: 34 and for planet_osm_polygon county: 285 in total. The official statistic shows the number of 179 prisons in whole Germany.</p>
<p>I am wondering why the difference is so large? I am aware that OSM-Data isn’t often complete, but then I would have expected the number to be smaller than the official one. Do you always have to expect some points to be counted twice? And is normally legit to combine ‘point’ and ‘polygon’ or does it become more inaccurate then? Thanks for your help!</p>
</div>
<div id="comment-72097-info" class="comment-info">
<span class="comment-age">(13 Dec '19, 16:43)</span> <span class="comment-user userinfo">Detektiv Mit...</span>
</div>
</div>
<span id="72101"></span>
<div id="comment-72101" class="comment">
<div id="post-72101-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Most likely you're hitting issues where there's a prison complex consisting of 10 buildings and each is tagged, individually, as amenity=prison. There are various ways to address this problem. One is to use a suitable "clustering" function in PostGIS, and tell it to combine into one all "prisons" that are less than, say, 500m of each other.</p>
<p>For example, there are four prisons in OSM here: <a href="https://www.openstreetmap.org/#map=17/52.54077/13.32037">https://www.openstreetmap.org/#map=17/52.54077/13.32037</a> when in reality it's either one or two depending on what you count.</p>
</div>
<div id="comment-72101-info" class="comment-info">
<span class="comment-age">(13 Dec '19, 18:43)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-71847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71847-form-container" class="comment-form-container">
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

