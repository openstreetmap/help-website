+++
type = "question"
title = "Overpass QL find nodes that are not near other nodes"
description = '''I am trying to search all of the highway residential ways, and then get the nodes from those ways, all within an area, and then of those nodes return the ones that are not within a specified distance to other node types. For example, find nodes on a way that are at least 5000m from the nearest freew...'''
date = "2019-06-23T23:11:00Z"
lastmod = "2019-06-24T16:44:00Z"
weight = 69718
keywords = [ "ways", "overpass", "nodes", "near", "ql" ]
aliases = [ "/questions/69718" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass QL find nodes that are not near other nodes](/questions/69718/overpass-ql-find-nodes-that-are-not-near-other-nodes)

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
<span id="post-69718-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69718-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-69718-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to search all of the highway residential ways, and then get the nodes from those ways, all within an area, and then of those nodes return the ones that are not within a specified distance to other node types. For example, find nodes on a way that are at least 5000m from the nearest freeway, or gas station, or food place, etc. Is this possible to implement only with Overpass QL?</p>
<p>This is what I have so far, which only returns me within an area (currently debugging with bbox) those roads that are marked residential.</p>
<pre><code>/*area
  [&quot;leisure&quot;=&quot;nature_reserve&quot;]
  [&quot;name&quot;=&quot;Daniel Boone National Forest&quot;]-&gt;.a;*/          // Redirect result to &quot;.a&quot;*/
out body qt;
(
  way
    ({{bbox}})[&#39;highway&#39;=&#39;residential&#39;];
  // area.a Use again result from &quot;.a&quot;
);
out body qt;
&gt;;
out skel qt;
out;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-near" rel="tag" title="see questions tagged &#39;near&#39;">near</span> <span class="post-tag tag-link-ql" rel="tag" title="see questions tagged &#39;ql&#39;">ql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Jun '19, 23:11</strong></p>
<img src="https://secure.gravatar.com/avatar/10ddd570ffad01514f2a603703a60be9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sreed101&#39;s gravatar image" />
<p><span>sreed101</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sreed101 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-69718" class="comments-container">
<span id="69720"></span>
<div id="comment-69720" class="comment">
<div id="post-69720-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know what your use case is or how to solve the issue with Overpass but if you're open to solving it with osm2pgsql+PostGIS on a local computer then I could suggest something.</p>
</div>
<div id="comment-69720-info" class="comment-info">
<span class="comment-age">(23 Jun '19, 23:53)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="69721"></span>
<div id="comment-69721" class="comment">
<div id="post-69721-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik</a> - that would work! I have a PostGIS setup on my local computer already with an OSM dataset imported.</p>
</div>
<div id="comment-69721-info" class="comment-info">
<span class="comment-age">(24 Jun '19, 01:14)</span> <span class="comment-user userinfo">sreed101</span>
</div>
</div>
</div>
<div id="comment-tools-69718" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69718-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="69724"></span>

<div id="answer-container-69724" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69724-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69724-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69724-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Here's a PostGIS based solution:</p>
<p>I assume that your use case is something like "I want to find out the bits of road in this area where, if someone gets stranded, they are more than 5km away from the nearest X", would that about fit? In that case, I'd assume that while your question talks about nodes in highways, you are not <em>really</em> interested in nodes - if there's a super long straight road in OSM with no nodes for 10km then you'd still be interested in the fact that somewhere in the middle there's a stretch far away from any X.</p>
<p>So there's a ton of ways to solve this in PostGIS and which of them makes most sense depends very much on the total data volume. If I am making the right guesses here then a sensible way could be to first calculate one huge (multi)polygon for what I would call the "safe area", everything that is within 5km of an X. Assuming you have an osm2pgsql import with a suitable projection (standard EPSG:3857 will somewhat work but you'd have to convert the 5000m to Mercator meters to get a precise result), your process would be something like this.</p>
<p>Initially create a 5km circle around every X point (in this example: filling stations) and add that to a new table:</p>
<p><code>select st_buffer(way,5000) as geom into safe_area_building_blocks from planet_osm_point where amenity='fuel';</code></p>
<p>Now since filling stations can also be polygons in OSM, add these too:</p>
<p><code>insert into safe_area_building_blocks select st_buffer(way,5000) from planet_osm_polygon where amenity='fuel';</code></p>
<p>You could now add as many such "insert" statements as you want for different kinds of objects; if you would consider everything within 5km of a motorway safe, you'd do a "... from planet_osm_line where highway='motorway'" and so on.</p>
<p>Now, combine all into one single huge polygon. Note this will take ages if your queries above should yield thousands of polygons; my assumption is that the set is not that huge.</p>
<p><code>select st_union(geom) as geom into safe_area from safe_area_building_blocks;</code></p>
<p>Finally, find all stretches of highway that are outside of the "safe area" (this finds ways fully outside, and for ways partly outside will give only the part that lies outside):</p>
<p><code>select st_difference(way, geom) from planet_osm_line, safe_area where highway is not null and not st_contains(geom, way);</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '19, 07:37</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '19, 07:39</strong> </span></p>
</div>
</div>
<div id="comments-container-69724" class="comments-container">
<span id="69730"></span>
<div id="comment-69730" class="comment">
<div id="post-69730-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry for not being more descriptive in my initial post. My exact use-case is to find locations within national forest areas that are the most remote for dispersed camping, while still remaining close to roadways/dirt roads. Your answer sounds like a really good way to go about doing this. I'll work on this some and post more after. Cheers!</p>
</div>
<div id="comment-69730-info" class="comment-info">
<span class="comment-age">(24 Jun '19, 14:24)</span> <span class="comment-user userinfo">sreed101</span>
</div>
</div>
</div>
<div id="comment-tools-69724" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69724-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="69722"></span>

<div id="answer-container-69722" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69722-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69722-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69722-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not sure it is the best way to solve it, but one approach is to bounce from your residential nodes to the nearby nodes and then back to residential nodes and take the difference between the two sets of residential nodes.</p>
<p>Start by saving the residential nodes into a named set, then search for the nodes that meet your other criteria using the residential nodes and an <code>around:</code> restriction, then search for residential nodes around the other nodes, then use a set difference to find the nodes in the first set of residential nodes that are not in the second set.</p>
<p>Here's a simplified example:</p>
<p><a href="http://overpass-turbo.eu/s/KaO">http://overpass-turbo.eu/s/KaO</a></p>
<pre><code>[bbox:{{bbox}}];
way[highway=residential];
node(w)-&gt;.residential_all;
// union of other features
(node(around.residential_all:100)[amenity]-&gt;.other;);
way(around.other:100)[highway=residential];
node(w)-&gt;.residential_nearby;
(.residential_all; - .residential_nearby;);
out;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '19, 03:28</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-69722" class="comments-container">
<span id="69731"></span>
<div id="comment-69731" class="comment">
<div id="post-69731-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll have to spend some time soon unpacking and understanding this. The initial example still seems to return nodes that are within cities. Thank you for the reply!</p>
</div>
<div id="comment-69731-info" class="comment-info">
<span class="comment-age">(24 Jun '19, 14:28)</span> <span class="comment-user userinfo">sreed101</span>
</div>
</div>
<span id="69732"></span>
<div id="comment-69732" class="comment">
<div id="post-69732-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, it's restricted to the bounding box, move the map to an area you are interested in to try it there.</p>
<p>You'd also have to flesh out the queries for the features you want to avoid.</p>
</div>
<div id="comment-69732-info" class="comment-info">
<span class="comment-age">(24 Jun '19, 16:44)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-69722" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69722-form-container" class="comment-form-container">
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

