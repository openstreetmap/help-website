+++
type = "question"
title = "missing polygons or rendering issue?"
description = '''I am experimenting with setting up an OSM tile server. So far, I have downloaded a recent version of the data, loaded it into PostGIS using osm2pgsql, and set up renderd and mod_tile on my server instance. I have a test harness that shows some missing polygons along the River Thames: http://174.129....'''
date = "2013-11-27T22:55:00Z"
lastmod = "2013-11-28T17:04:00Z"
weight = 28563
keywords = [ "rendering", "tileserver", "polygon", "missing" ]
aliases = [ "/questions/28563" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [missing polygons or rendering issue?](/questions/28563/missing-polygons-or-rendering-issue)

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
<span id="post-28563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28563-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-28563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am experimenting with setting up an OSM tile server.</p>
<p>So far, I have downloaded a recent version of the data, loaded it into PostGIS using osm2pgsql, and set up renderd and mod_tile on my server instance.</p>
<p>I have a test harness that shows some missing polygons along the River Thames:</p>
<p><a href="http://174.129.244.158/jlmap.html">http://174.129.244.158/jlmap.html</a></p>
<p>Is there a straightforward approach to debugging this? How do I determine if the polygons are missing, or if it is a missing tag or rendering error.</p>
<p>Thanks in advance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span> <span class="post-tag tag-link-missing" rel="tag" title="see questions tagged &#39;missing&#39;">missing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '13, 22:55</strong></p>
<img src="https://secure.gravatar.com/avatar/2ccafb68c71bc85b0626afb0152c036e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="john_willyn&#39;s gravatar image" />
<p><span>john_willyn</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="john_willyn has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Nov '13, 20:01</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-28563" class="comments-container">
<span id="28565"></span>
<div id="comment-28565" class="comment">
<div id="post-28565-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Haven't looked into this in detail, but the fact that the default osm.org map (and, in fact, the various other renders available on osm.org) all show the correct riverbank there suggests to me that it's not a data issue.</p>
</div>
<div id="comment-28565-info" class="comment-info">
<span class="comment-age">(27 Nov '13, 23:27)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="28578"></span>
<div id="comment-28578" class="comment">
<div id="post-28578-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You're missing dozens of polygons - residential areas around south london, Wimbledon Common etc. It looks like your import has failed somehow.</p>
</div>
<div id="comment-28578-info" class="comment-info">
<span class="comment-age">(28 Nov '13, 09:21)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-28563" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28563-form-container" class="comment-form-container">
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

<span id="28573"></span>

<div id="answer-container-28573" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28573-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28573-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-28573-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The general way to approach such a problem would be (note that with the web site design constantly changing, the process might differ slightly if you read this at a later time)</p>
<ul>
<li>go to www.openstreetmap org</li>
<li>zoom very far into an area that has at least one line of the polygon you're interested in</li>
<li>activate the data layer (click the layer button on the right then activate the "map data" checkbox)</li>
<li>click on the blue line in the map and select "details" on the left hand side</li>
<li>make a note of the way ID, and also look at the bottom of the node list where it should say "part of..." and point to a riverbank relation</li>
<li>use pgsql (or pgadmin or similar) to connect to your database</li>
<li>in the planet_osm_polygons table you should have an object with an osm_id of the negative (!) id of the relation</li>
<li>if that isn't there, check if your planet_osm_rels has an entry with the positive (!) id of the relation and if planet_osm_ways has all the constituent ways; likely something is missing and therefore the polygon could not be constructed. Check your source data in that case. If however the building blocks are all there but the polygon is not, then for some reason osm2pgsql decided not to create the polygon - either due to a bug or due to tag filtering via the style file or LUA code.</li>
<li>if however the polygon is there in your database but not on the tiles then there must be some kind of problem down the line, in your rendering rules.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Nov '13, 07:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-28573" class="comments-container">
<span id="28586"></span>
<div id="comment-28586" class="comment">
<div id="post-28586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the very detailed instructions. Unfortunately, I only see the node numbers listed in the node list, and not any relations, or at least anything I can identify as a relation. I scouted around in the tables and tried to figure out the structure, but none of the id's look they were listed in the node list.</p>
<p>The way ID is 204068876 in case anyone wants to help guide me further. At least this seems to be one of the missing polygons.</p>
<p>I do suspect my import was partially bad, and I noticed a couple of errors reported in 'pending ways', but thought the relations and polygons completed without errors.</p>
<p>Thanks again.</p>
</div>
<div id="comment-28586-info" class="comment-info">
<span class="comment-age">(28 Nov '13, 17:04)</span> <span class="comment-user userinfo">john_willyn</span>
</div>
</div>
</div>
<div id="comment-tools-28573" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28573-form-container" class="comment-form-container">
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

