+++
type = "question"
title = "Get area around element"
description = '''Is there a way to get an area around something (a road, a bus way, ...) ? IE: &quot;I want the area around 150m near a tram/bus/cycle way&quot;. I got this query that return all bars around the tram &quot;Ligne E&quot; of Grenoble (city in France). [out:json][timeout:25]; (  area[name=&#x27;Grenoble&#x27;][&quot;admin_level&quot;=&quot;8&quot;];  w...'''
date = "2017-02-10T09:51:00Z"
lastmod = "2017-03-01T08:46:00Z"
weight = 54585
keywords = [ "overpass", "around" ]
aliases = [ "/questions/54585" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Get area around element](/questions/54585/get-area-around-element)

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
<span id="post-54585-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54585-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-54585-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there a way to get an area around something (a road, a bus way, ...) ?</p>
<p>IE: "I want the area around 150m near a tram/bus/cycle way".</p>
<p>I got <a href="http://overpass-turbo.eu/s/mCp">this query</a> that return all bars around the tram "Ligne E" of Grenoble (city in France).</p>
<pre><code>[out:json][timeout:25];
(
  area[name=&#39;Grenoble&#39;][&quot;admin_level&quot;=&quot;8&quot;];
  way(area)[railway=tram][&quot;oneway&quot;=&quot;yes&quot;][&quot;name&quot;=&quot;Ligne E&quot;];
  node(around:150)[&#39;amenity&#39;=&#39;bar&#39;];
);
out body;
&gt;;
out skel qt;</code></pre>
<p><strong>Update:</strong></p>
<p>If we analyse the problem <em>with a simple 2D example</em> :</p>
<p><img src="/upfiles/plan_coordinate.png" alt="alt text" /></p>
<ul>
<li>I have a way (red) from <code>A{2;2}</code> to <code>B{5;2}</code></li>
<li>I need the area (blue) CDEF <code>({1;3}, {6;3}, {6;1}, {1;1})</code>.</li>
</ul>
<p>I know how to get the way : in the query example, it's the <code>way(area)....</code> instruction. <strong>How to get the</strong> blue <strong>area with Overpass</strong> ?</p>
<p><em>With a concrete example</em>, this is what I would like to have : from the blue line (a tramway), I want the purple area (around <code>ZZ</code> meter from this way).</p>
<p><img src="/upfiles/area_around.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-around" rel="tag" title="see questions tagged &#39;around&#39;">around</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '17, 09:51</strong></p>
<img src="https://secure.gravatar.com/avatar/6feabd7b77f0f304fcc22b54a4a61761?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mosmuk&#39;s gravatar image" />
<p><span>mosmuk</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mosmuk has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Feb '17, 08:53</strong> </span></p>
</div>
</div>
<div id="comments-container-54585" class="comments-container">
&#10;</div>
<div id="comment-tools-54585" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54585-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="54760"></span>

<div id="answer-container-54760" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54760-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54760-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-54760-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe you get the area with the "around" operator ?</p>
<p>This <a href="http://overpass-turbo.eu/s/mT0">OverPass query</a> finds all nodes and ways within 50 meter of living streets in Rumst So you first "store" your first result in the set "streets" and then search nodes and ways around those streets.</p>
<p>You will notice that you do no get a nice rectangle as some large areas (closed ways) have one side that is within this 50m range and they are returned as whole.</p>
<p>This <a href="http://overpass-turbo.eu/s/mT4">query</a> does more or less what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Feb '17, 11:24</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</img>
</div>
</div>
<div id="comments-container-54760" class="comments-container">
<span id="54762"></span>
<div id="comment-54762" class="comment">
<div id="post-54762-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This example returns all point of interest or way. What I really need is the coordinates of the shape around the ways (to use it with data from another database than OSM). I'm looking at whether there's a way to compute this outside the OSM queries.</p>
</div>
<div id="comment-54762-info" class="comment-info">
<span class="comment-age">(21 Feb '17, 14:12)</span> <span class="comment-user userinfo">mosmuk</span>
</div>
</div>
<span id="54763"></span>
<div id="comment-54763" class="comment">
<div id="post-54763-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>AFAIK there is no way to find that box with OverPass. This is more suited for QGIS or PostGIS I think. OverPass is about finding OSM data, not finding boxes around data.</p>
</div>
<div id="comment-54763-info" class="comment-info">
<span class="comment-age">(21 Feb '17, 14:59)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-54760" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54760-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54755"></span>

<div id="answer-container-54755" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54755-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You may want to look at <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Select_region_by_polygon">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide#Select_region_by_polygon</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Feb '17, 19:50</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-54755" class="comments-container">
<span id="54757"></span>
<div id="comment-54757" class="comment">
<div id="post-54757-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the idea, but I want to know "how to get the polyline coordinate". I update my question with simple example.</p>
</div>
<div id="comment-54757-info" class="comment-info">
<span class="comment-age">(21 Feb '17, 08:42)</span> <span class="comment-user userinfo">mosmuk</span>
</div>
</div>
</div>
<div id="comment-tools-54755" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54755-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54772"></span>

<div id="answer-container-54772" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54772-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54772-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54772-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Obviously, you are interested in something called - the corridor. The corridor and related apps are well known even from times long before the OSM's birth. Corridor geo-search, thick line rendering, safety monitoring, map-data preparation... are some of those applications.Very shortly:<br />
A corridor area (L,D) is defined by its skeleton/leading line L and distance D (a half-width). Any of the corridor points has a minimum/shortest distance d&lt;=D to its skeleton. All points at d=D distance create the border of the corridor. If a corridor contains its border it is called a closed corridor, else it is open (d&lt; D). When the skeleton is a poly-line (a connected series of edge vectors) the corridor may be decomposed into two primitive area types: circular and rectangular. The circles all have the same radius D and centres in the poly-line nodes. The rectangles have the edge vectors as their middle line height and the 2D line basis. Because of the equivalences between a "point inside or outside a corridor" and a "point inside some and outside all primitives" we can create extraordinary fast and simple algorithms to check whether a point/geometry is inside or outside a given corridor. Namely, the primitives may be sorted to allow early elimination/filtering and the point-in-primitive mostly consists of comparisons. Here are some examples:<br />
Along the coastline from A to B find all houses (of kind) closer than 500m to sea but not closer than 100m.<br />
Create along the coastline of the country (including islands, eventually platforms and so on) a safety belt (corridor) of 25km width. Whenever a (fast) moving object enters/exits the belt issue an alarm and show the locations on map. Note that in this way you could do safety monitoring of thousands of (even very fast) moving objects on a solid laptop.<br />
Detecting corridor replica objects in OSM. For example, there are tens of thousands of area borders where one is in the corridor (of certain width) of another. These are not exact replicas but just versions of the same object by high probability. In the preparation we keep the one with more details. For illustration see the data/borders of the Philcot Lake in Canada or the lakes here <a href="http://osm.org/go/eu0xCXzfD--?layers=TD">http://osm.org/go/eu0xCXzfD--?layers=TD</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Feb '17, 22:36</strong></p>
<img src="https://secure.gravatar.com/avatar/03cd9ea0efd97a7040fda0d6a76aba8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sanser&#39;s gravatar image" />
<p><span>sanser</span><br />
<span class="score" title="695 reputation points">695</span><span title="38 badges"><span class="badge1">●</span><span class="badgecount">38</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="55 badges"><span class="bronze">●</span><span class="badgecount">55</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sanser has 2 accepted answers">5%</span> </br></br></p>
</div>
</div>
<div id="comments-container-54772" class="comments-container">
<span id="54777"></span>
<div id="comment-54777" class="comment">
<div id="post-54777-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It's exactly what I'm looking for. But <a href="https://help.openstreetmap.org/users/5390/escada"></a><a href="https://help.openstreetmap.org/users/5390/escada">@escada</a> seems to say that it's not available in overpass.</p>
</div>
<div id="comment-54777-info" class="comment-info">
<span class="comment-age">(23 Feb '17, 08:07)</span> <span class="comment-user userinfo">mosmuk</span>
</div>
</div>
<span id="54778"></span>
<div id="comment-54778" class="comment">
<div id="post-54778-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Overpass is used to retrieve OSM data, not data that can be deduced from OSM data. The corridor is not in OSM, so you cannot retrieve it with Overpass.</p>
</div>
<div id="comment-54778-info" class="comment-info">
<span class="comment-age">(23 Feb '17, 12:07)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="54847"></span>
<div id="comment-54847" class="comment">
<div id="post-54847-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Though, this not a discussion/argumentation place, the last comment needs some additional words. It is wrong and even (obviously)misleading. It is trivial to understand the difference between a data type and a logical shape used in application models. If an ANYpass tool-set (pretending to do spatial retrieval) does not have a corridor based retrieval model, it is just sad. But with such pretensions the ANYpass certainly contains a circle and rectangle based (the simplest) models. So, my point was that with the suggested corridor decomposition combined with the simplest spatial retrieval models anyone (even with no strong topology, polygon-algebra, programing) background could create the retrieval model (script) in the question.</p>
</div>
<div id="comment-54847-info" class="comment-info">
<span class="comment-age">(01 Mar '17, 08:46)</span> <span class="comment-user userinfo">sanser</span>
</div>
</div>
</div>
<div id="comment-tools-54772" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54772-form-container" class="comment-form-container">
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

