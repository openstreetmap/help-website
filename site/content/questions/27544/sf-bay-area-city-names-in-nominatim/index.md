+++
type = "question"
title = "SF Bay Area city names in nominatim"
description = '''In my installation of Nominatim, reverse queries are showing the wrong city name for numerous locations in the San Francisco Bay Area. However the “official” Nominatim website seems to do it correctly: Shows city as “San Jose” (correct): http://nominatim.openstreetmap.org/reverse?format=json&amp;amp;lat...'''
date = "2013-10-28T07:58:00Z"
lastmod = "2013-11-23T11:22:00Z"
weight = 27544
keywords = [ "nominatim", "reverse" ]
aliases = [ "/questions/27544" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SF Bay Area city names in nominatim](/questions/27544/sf-bay-area-city-names-in-nominatim)

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
<span id="post-27544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27544-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-27544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my installation of Nominatim, reverse queries are showing the wrong city name for numerous locations in the San Francisco Bay Area. However the “official” Nominatim website seems to do it correctly:</p>
<p>Shows city as “San Jose” (correct): <a href="http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=37.342&amp;lon=-121.886&amp;zoom=&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=json&amp;lat=37.342&amp;lon=-121.886&amp;zoom=&amp;addressdetails=1</a></p>
<p>Shows city as “Santa Clara” (incorrect): <a href="http://osm.ourcast.com/ocreverse.php?lat=37.342&amp;lng=-121.886">http://osm.ourcast.com/ocreverse.php?lat=37.342&amp;lng=-121.886</a></p>
<p>Also here is an incorrect street’s details page: <a href="http://osm.ourcast.com/details.php?place_id=29332445">http://osm.ourcast.com/details.php?place_id=29332445</a></p>
<p>I found this question which suggests that I can fix the city names by drawing the city as a relation. But as it is working on the official Nominatim, doesn’t that mean that the correct city boundaries are in the OSM dataset, and my installation is just displaying it incorrectly? <a href="/questions/17207/wrong-city-names">https://help.openstreetmap.org/questions/17207/wrong-city-names</a></p>
<p>My nominatim url is here: <a href="http://osm.ourcast.com/nominatim.php">http://osm.ourcast.com/nominatim.php</a></p>
<p>Any help is greatly appreciated!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-reverse" rel="tag" title="see questions tagged &#39;reverse&#39;">reverse</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '13, 07:58</strong></p>
<img src="https://secure.gravatar.com/avatar/96d98fb13947dc1b70b3d7edd33a4b6b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mparncutt&#39;s gravatar image" />
<p><span>mparncutt</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mparncutt has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27544" class="comments-container">
<span id="27545"></span>
<div id="comment-27545" class="comment">
<div id="post-27545-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You don't need to create this relation, it already <a href="https://www.openstreetmap.org/browse/relation/112143">exists</a> and also <a href="http://nominatim.openstreetmap.org/details.php?place_id=3673062065">indexed by the official Nominatim instance</a>. I guess your instance did not index this relation and thus provides a less accurate geolocation result. Maybe some problem during the import? Or did you import a dataset which didn't contain relations?</p>
</div>
<div id="comment-27545-info" class="comment-info">
<span class="comment-age">(28 Oct '13, 08:31)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="27789"></span>
<div id="comment-27789" class="comment">
<div id="post-27789-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Did you end up finding a solution to this? I'm also having this problem with SF Bay Area.</p>
</div>
<div id="comment-27789-info" class="comment-info">
<span class="comment-age">(04 Nov '13, 20:00)</span> <span class="comment-user userinfo">baekacaek</span>
</div>
</div>
</div>
<div id="comment-tools-27544" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27544-form-container" class="comment-form-container">
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

<span id="27546"></span>

<div id="answer-container-27546" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27546-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-27546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The boundary relation for San Jose is broken. You can see a few errors reported by <a href="http://tools.geofabrik.de/osmi/?view=multipolygon&amp;lon=-121.87803&amp;lat=37.31113&amp;zoom=12&amp;opacity=0.95&amp;overlays=invalid_geometry_hull,duplicate_ways,intersections,intersection_lines,ring_not_closed_hull,ring_not_closed,unconnected_end_nodes,touching_inner_rings_hull,touching_inner_rings,role_mismatch_hull,role_mismatch,duplicate_tags_hull,duplicate_tags,ways,role_markers,way_end_nodes,way_nodes">OSM Inspector</a>. Nominatim has a mechanism to keep old versions of boundaries around when it finds a broken one. That is why you see the difference between the osm.org instance and your import.</p>
<p>If you have just imported your database, you can get a list of broken polygons under the URL your.instance/polygons.php (you don't seem to have exported that on your instance but it still should be there). This list is not updated when diffs are applied, so the list on osm.org is not really useful at the moment.</p>
<p>Once the data is fixed in OSM, things will sort themselves out in Nominatim when diffs are applied. If you don't use diffs, you can also manually reimport the relation with:</p>
<pre><code>./utils/update.php --import-relation [relation id] --index --index-instances 2</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '13, 08:38</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-27546" class="comments-container">
<span id="28327"></span>
<div id="comment-28327" class="comment">
<div id="post-28327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd firstly like to thank the people who have replied thus far!</p>
<p>As suggested, I’ve fixed the relation for San Jose and this is now live on OpenStreetMap and has found its way into my instance through the diffs: <a href="http://osm.ourcast.com/details.php?osmid=112143&amp;osmtype=R">http://osm.ourcast.com/details.php?osmid=112143&amp;osmtype=R</a></p>
<p>But it does not appear to have solved the problem.</p>
<p>I also notice that I don’t get proper place names for Berkeley, even though the Berkeley relation is intact (and always has been).</p>
<p>Here are some comparisons between my instance and the official Nominatim instance:</p>
<p>Hearst Ave, Berkeley:</p>
<p>The city is correctly shown as “Berkeley” in the address, referencing the boundary:administrative for Berkeley <a href="http://nominatim.openstreetmap.org/details.php?osmid=207140275&amp;osmtype=W">http://nominatim.openstreetmap.org/details.php?osmid=207140275&amp;osmtype=W</a></p>
<p>The city is incorrectly shown as “Alameda” in the address, referencing the place:city for Alameda. The boundary:administrative for Berkeley appears there, but is greyed out, and so doesn’t appear in the address returned by the API: <a href="http://osm.ourcast.com/details.php?osmid=207140275&amp;osmtype=W">http://osm.ourcast.com/details.php?osmid=207140275&amp;osmtype=W</a></p>
<p>The two instances also disagree on the neighbourhood (I don’t know which is correct) but I don’t mind too much about this, as my application doesn’t use neighbourhood.</p>
<p>East Saint James St includes the boundary:administrative for San Jose as part of the address: <a href="http://nominatim.openstreetmap.org/details.php?osmid=157781928&amp;osmtype=W">http://nominatim.openstreetmap.org/details.php?osmid=157781928&amp;osmtype=W</a></p>
<p>East Saint James St does not reference the boundary:administrative for San Jose, even though it is now available on the instance: <a href="http://osm.ourcast.com/details.php?osmid=157781928&amp;osmtype=W">http://osm.ourcast.com/details.php?osmid=157781928&amp;osmtype=W</a></p>
</div>
<div id="comment-28327-info" class="comment-info">
<span class="comment-age">(21 Nov '13, 07:55)</span> <span class="comment-user userinfo">mparncutt</span>
</div>
</div>
<span id="28330"></span>
<div id="comment-28330" class="comment">
<div id="post-28330-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It's possible that Nominatim did not propagate the boundary changes for efficiency reasons. Try to force a reindex on the entire city by running the following command directly on your DB: <code>select place_force_update(&lt;place_id&gt;)</code> where <code>&lt;place_id&gt;</code> should be the internal Nominatim id. You can find it in the URL of the details page (possibly after clicking GOTO of the first address entry). It is 171218834 for San Jose in your DB.</p>
</div>
<div id="comment-28330-info" class="comment-info">
<span class="comment-age">(21 Nov '13, 09:22)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
<span id="28385"></span>
<div id="comment-28385" class="comment">
<div id="post-28385-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't have that function because I was using Nominatim 2.0.1. I've tried to upgrade to the latest Nominatim from git, but now I have this additional issue when I was trying to import the file as suggested in here: <a href="https://github.com/twain47/Nominatim/pull/54#issuecomment-17277092">https://github.com/twain47/Nominatim/pull/54#issuecomment-17277092</a></p>
<p>But I get this error: <a href="http://pastebin.com/E7nC0aNg">http://pastebin.com/E7nC0aNg</a></p>
<p>I also seem unable to run updates anymore. It imports 0 nodes/ways/relations each time :(</p>
</div>
<div id="comment-28385-info" class="comment-info">
<span class="comment-age">(22 Nov '13, 05:05)</span> <span class="comment-user userinfo">mparncutt</span>
</div>
</div>
<span id="28417"></span>
<div id="comment-28417" class="comment">
<div id="post-28417-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You can't update to 2.1 without a reimport, there have been some other changes to the database schema as well. If you cannot reimport, go back to 2.0.1 and just install the <code>place_force_update</code> function from <code>sql/functions.sql</code> from 2.1.</p>
</div>
<div id="comment-28417-info" class="comment-info">
<span class="comment-age">(23 Nov '13, 11:22)</span> <span class="comment-user userinfo">lonvia</span>
</div>
</div>
</div>
<div id="comment-tools-27546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27546-form-container" class="comment-form-container">
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

