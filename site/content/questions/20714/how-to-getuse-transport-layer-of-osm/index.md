+++
type = "question"
title = "How to get/use transport layer of OSM?"
description = '''Hi, I&#x27;m a newbie here and recently I started tu read about osmdroid for develop an android app using OSM but I need to use the transpor layer of my country for obtain routes (subway routes) and I don&#x27;t know if it&#x27;s possible to do that. I&#x27;d like to get the info about the coordinates,etc. of the subwa...'''
date = "2013-03-14T19:04:00Z"
lastmod = "2013-03-15T08:10:00Z"
weight = 20714
keywords = [ "android", "public-transport", "transport-route-view" ]
aliases = [ "/questions/20714" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get/use transport layer of OSM?](/questions/20714/how-to-getuse-transport-layer-of-osm)

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
<span id="post-20714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I'm a newbie here and recently I started tu read about osmdroid for develop an android app using OSM but I need to use the transpor layer of my country for obtain routes (subway routes) and I don't know if it's possible to do that. I'd like to get the info about the coordinates,etc. of the subway routes.</p>
<p>Thanks in advance ;)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-transport-route-view" rel="tag" title="see questions tagged &#39;transport-route-view&#39;">transport-route-view</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '13, 19:04</strong></p>
<img src="https://secure.gravatar.com/avatar/47cff4dbddd9dd5ec4bb5bab78cdabf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Haunterck&#39;s gravatar image" />
<p><span>Haunterck</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Haunterck has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20714" class="comments-container">
&#10;</div>
<div id="comment-tools-20714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20714-form-container" class="comment-form-container">
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

<span id="20719"></span>

<div id="answer-container-20719" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20719-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20719-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-20719-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From your description I conclude that you are actually interested in the transport <em>data</em> and not the transport <em>layer</em>. The transport layer is just one possible <em>representation</em> of the data and contains only a subset of the original information. You will have a hard time getting things like coordinates, station names etc. from a rendered image.</p>
<p>To obtain the actual <em>data</em> you can either get <a href="https://wiki.openstreetmap.org/wiki/Planet.osm">the whole planet</a> or a specific <a href="https://wiki.openstreetmap.org/wiki/Planet.osm#Country_and_area_extracts">extract</a> which seems better suited for your case. Another possibility is to download only the data relevant for your specific purpose by using the <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a>. The big advantage is that you have to retrieve and process way less data than with a full extract.</p>
<p>OSM's data currently consists of three different <a href="https://wiki.openstreetmap.org/wiki/Elements">element types</a>: <em>nodes</em>, <em>ways</em> and <em>relations</em>. These elements have additional <a href="https://wiki.openstreetmap.org/wiki/Tags">tags</a> used to describe them. The elements and tags you are interested in are described in our wiki and particularly consist of <a href="https://wiki.openstreetmap.org/wiki/Relation:route#Public_transport_routes">route relations</a> and <a href="https://wiki.openstreetmap.org/wiki/Public_transport">public transport tags</a>.</p>
<p>To extract these specific objects from the data you can either use <a href="https://wiki.openstreetmap.org/wiki/Osmosis">osmosis</a>/<a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> when having the full planet or an extract, or directly pass your filter to the previously mentioned Overpass API.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Mar '13, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20719" class="comments-container">
&#10;</div>
<div id="comment-tools-20719" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20719-form-container" class="comment-form-container">
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

