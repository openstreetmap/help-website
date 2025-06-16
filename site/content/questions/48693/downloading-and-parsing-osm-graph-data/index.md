+++
type = "question"
title = "Downloading and parsing OSM graph data"
description = '''I am a bit lost and I am hoping that someone will help me start and hopefully help others as well. My requirements are pretty straightforward. I want to download raw data for the:  Latitude  Longitude How are nodes connected in the graph Distance between the connected nodes  For example: nodeA nodeB...'''
date = "2016-03-16T02:42:00Z"
lastmod = "2017-06-08T13:41:00Z"
weight = 48693
keywords = [ "export", "extract" ]
aliases = [ "/questions/48693" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Downloading and parsing OSM graph data](/questions/48693/downloading-and-parsing-osm-graph-data)

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
<span id="post-48693-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48693-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48693-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am a bit lost and I am hoping that someone will help me start and hopefully help others as well. My requirements are pretty straightforward. I want to download raw data for the:</p>
<ul>
<li>Latitude</li>
<li>Longitude</li>
<li>How are nodes connected in the graph</li>
<li>Distance between the connected nodes</li>
</ul>
<p>For example:</p>
<pre><code>nodeA  nodeB  Latitude Longitude Distance(meters)
1566   1602   52.29323 -23.23252 125.256
1661   1783   26.23452 -21.24152 261.45
...</code></pre>
<p>For this I understand that I first have to download a .osm file and then read the data with a parser. However, that just seems really vague to me. The documentation seems a bit confusing and not straightforward to me.</p>
<p>So I wanna ask, how can I download the data mentioned above for a specific country or city ? (I want to download the data of Athens).</p>
<p>Then the next question is what file format will those data be in ? and how will I extract the above information from that file ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Mar '16, 02:42</strong></p>
<img src="https://secure.gravatar.com/avatar/029b463e5af8b5dc5d6094a7a4686c6a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="shiro900&#39;s gravatar image" />
<p><span>shiro900</span><br />
<span class="score" title="54 reputation points">54</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="shiro900 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48693" class="comments-container">
&#10;</div>
<div id="comment-tools-48693" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48693-form-container" class="comment-form-container">
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

<span id="48694"></span>

<div id="answer-container-48694" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48694-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48694-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48694-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can get city specific datasets e.g. at <a href="https://mapzen.com/data/metro-extracts/">mapzen</a>, e.g. <a href="https://s3.amazonaws.com/metro-extracts.mapzen.com/athens_greece.osm.bz2">OSM XML format for Athens</a>.</p>
<p>There you have all the nodes of the city. Read about the <a href="https://wiki.openstreetmap.org/wiki/OSM_XML">OSM XML file format</a>.</p>
<p>Write a script in your favourite programming language to parse this, extract the nodes that you need, calculate the distance and write out the list format (CSV, whatever) that you need.</p>
<p>For geographical distance calculations, you need an appropriate geo library, e.g. <a href="https://github.com/OSGeo/proj.4/wiki">Proj</a>. I can’t help you with that, it’s over my head.</p>
<p>Another approach might be feeding the data into a geo enabled database like <a href="http://www.postgis.net">PostGIS</a> und use its functions.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Mar '16, 03:50</strong></p>
<img src="https://secure.gravatar.com/avatar/5a39f1335b6eff433673ed987859fb24?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hraban&#39;s gravatar image" />
<p><span>Hraban</span><br />
<span class="score" title="186 reputation points">186</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hraban has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Mar '16, 03:50</strong> </span></p>
</div>
</div>
<div id="comments-container-48694" class="comments-container">
<span id="48695"></span>
<div id="comment-48695" class="comment">
<div id="post-48695-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For topology - whether nodes are connected by a line or not - you will have to evaluate the "way" objects as well. For distance in meters, use your favourite search engine to dig up the <em>Haversine Formula</em>.</p>
</div>
<div id="comment-48695-info" class="comment-info">
<span class="comment-age">(16 Mar '16, 06:40)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="48697"></span>
<div id="comment-48697" class="comment">
<div id="post-48697-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@FrederikRamm I am just surprised that there is no official library or instructions with examples on how to do that.</p>
</div>
<div id="comment-48697-info" class="comment-info">
<span class="comment-age">(16 Mar '16, 06:57)</span> <span class="comment-user userinfo">shiro900</span>
</div>
</div>
<span id="48699"></span>
<div id="comment-48699" class="comment">
<div id="post-48699-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There's tons of open source routing engines (routino, osrm, graphhopper, osm2pgrouting, ...) where you can look at how it's done. Extracting a graph from OSM data is a very specific requirement that rarely occurs outside of routing engines. There's a couple good general OSM processing libraries (eg Osmium and its Javacript and Python bindings) but that only helps you with parsing, you'll still have to build the kind of graph you want yourself.</p>
</div>
<div id="comment-48699-info" class="comment-info">
<span class="comment-age">(16 Mar '16, 07:51)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="48709"></span>
<div id="comment-48709" class="comment">
<div id="post-48709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@FederikRamm I was trying to install <code>imposm</code> and I got <a href="https://github.com/omniscale/imposm-parser/issues/18">this</a> error which I posted on their github. Do you by any chance know what is happening ?</p>
</div>
<div id="comment-48709-info" class="comment-info">
<span class="comment-age">(16 Mar '16, 15:05)</span> <span class="comment-user userinfo">shiro900</span>
</div>
</div>
</div>
<div id="comment-tools-48694" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48694-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56531"></span>

<div id="answer-container-56531" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56531-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56531-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56531-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Sorry I'm little bit late, but you can use this software</p>
<p><a href="https://github.com/rovaniemi/osm-graph-parser">https://github.com/rovaniemi/osm-graph-parser</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '17, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/254b7f3976f5e610bd9d2bf9c2d08075?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vanhapanda&#39;s gravatar image" />
<p><span>vanhapanda</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vanhapanda has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56531" class="comments-container">
&#10;</div>
<div id="comment-tools-56531" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56531-form-container" class="comment-form-container">
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

