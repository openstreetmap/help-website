+++
type = "question"
title = "Find all higher-level administrative areas that contain a specified node?"
description = '''I&#x27;m trying to retrieve a hierarchical list administrative areas that &quot;contain&quot; a certain node. For example, if I have a node that has the tag &quot;street&quot; with the name &quot;Sukhumvit&quot;, then I want to find the neighborhood, sub-district, district, city, province, state, higher level administrative areas, an...'''
date = "2014-05-09T08:12:00Z"
lastmod = "2014-05-09T15:09:00Z"
weight = 33022
keywords = [ "boundaries", "admin_boundary", "search", "geocoding" ]
aliases = [ "/questions/33022" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Find all higher-level administrative areas that contain a specified node?](/questions/33022/find-all-higher-level-administrative-areas-that-contain-a-specified-node)

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
<span id="post-33022-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33022-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33022-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to retrieve a hierarchical list administrative areas that "contain" a certain node.</p>
<p>For example, if I have a node that has the tag "street" with the name "Sukhumvit", then I want to find the neighborhood, sub-district, district, city, province, state, higher level administrative areas, and country who's boundaries contain this node.</p>
<p>More specifically, in the case of Sukhumvit (a street in Thailand), it would have to return things nodes with the tag neighborhood (name=Sukhumvit), district (name=Watthana District), city (name=Bangkok), country (name=Thailand), and more.</p>
<p>Is it possible to retrieve all nodes with pre-specified tags that have geographic boundaries surrounding a certain latitude and longitude position? I'm willing to import OSM data into solutions like ElasticSearch if that helps.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-boundaries" rel="tag" title="see questions tagged &#39;boundaries&#39;">boundaries</span> <span class="post-tag tag-link-admin_boundary" rel="tag" title="see questions tagged &#39;admin_boundary&#39;">admin_boundary</span> <span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 May '14, 08:12</strong></p>
<img src="https://secure.gravatar.com/avatar/04361eba6e039eecdd3458e2545f03e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomM&#39;s gravatar image" />
<p><span>TomM</span><br />
<span class="score" title="41 reputation points">41</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomM has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33022" class="comments-container">
&#10;</div>
<div id="comment-tools-33022" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33022-form-container" class="comment-form-container">
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

<span id="33025"></span>

<div id="answer-container-33025" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33025-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33025-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-33025-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="TomM has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have already been told that re-inventing Nominatim will be a lot of work. I hope that you don't expect us to re-invent Nominatim for you on this platform ;)</p>
<p>First of all, streets are not usually represented by nodes, but by ways. You do not have "a node that has the tag street with the name Sukhumvit". You have a way with the tag <code>highway</code> and the name <code>Sukhumvit</code>, and that way will be built from nodes, which have a location.</p>
<p>Then, nodes don't have geographic boundaries so your question does not make sense. What you are looking for is administrative boundaries which may be given in the form of a single, closed way, or, more commonly, a multipolygon relation. Existing SQL database importers like osm2pgsql (used by Nominatim) or imposm will resolve these into proper polygons for you, as will the Osmium C++ library. You can also do this yourself but that would mean reinventing another type of wheel, as constructing polygons from the OSM data is not trivial.</p>
<p>Once you have these polygons, you can use geometric operations to find out which of them enclose your polygon. Again, PostGIS (used by Nominatim) can do this, and is indeed used by Nominatim to build such a hierarchy like the one you're looking for. Alternatively, you can use libraries like GEOS for C/C++ or its bindings in various scripting languages. Doing this efficiently will require building indexes.</p>
<p>But aside from the polygons, you will still want to look at single nodes that do not enclose the position you are interesed in, but are just in the vicinity - for example, there might be a node tagged "place=neighbourhood, name=Sukhumvit", which simply sits somewhere in the vicinity of the street that you are looking for, and you have to apply heuristics to determine whether or not your street should be counted as belonging to that neighbourhood. Again, this is something that Nominatim already does.</p>
<p>Are you sure you still want to build your own geocoder?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '14, 08:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-33025" class="comments-container">
<span id="33027"></span>
<div id="comment-33027" class="comment">
<div id="post-33027-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I read ElasticSearch's documentation and was under the impression that querying for locations within such administrative boundaries was trivial using their solution. The reason I am hesitant to use Nominatim is that it doesn't seem to accomodate for partial-match full-text search, because when I search for "Sukhumvit 21 11th Flr." it doesn't return anything, while "Sukhumvit 21" does. ElasticSearch seems more capable of searching for partial matches. I like Photon, but it is not useful for me because it doesn't return any administrative areas (<a href="https://github.com/komoot/photon/issues/30)">https://github.com/komoot/photon/issues/30)</a></p>
</div>
<div id="comment-33027-info" class="comment-info">
<span class="comment-age">(09 May '14, 09:09)</span> <span class="comment-user userinfo">TomM</span>
</div>
</div>
<span id="33030"></span>
<div id="comment-33030" class="comment">
<div id="post-33030-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Maybe you can get in touch with the people behind Pelias. See video at State of the Map US 2014 <a href="http://stateofthemap.us/session/pelias/">http://stateofthemap.us/session/pelias/</a> they use Elastic Search for reverse Geocoding</p>
</div>
<div id="comment-33030-info" class="comment-info">
<span class="comment-age">(09 May '14, 09:26)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="33047"></span>
<div id="comment-33047" class="comment">
<div id="post-33047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>an entry about Pelias was missing in the OSM wiki about <a href="http://wiki.openstreetmap.org/wiki/Search_engines">http://wiki.openstreetmap.org/wiki/Search_engines</a> ... done</p>
</div>
<div id="comment-33047-info" class="comment-info">
<span class="comment-age">(09 May '14, 15:09)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-33025" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33025-form-container" class="comment-form-container">
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

