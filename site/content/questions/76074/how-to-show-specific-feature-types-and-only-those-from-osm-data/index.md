+++
type = "question"
title = "How to show specific feature types, and only those, from OSM data?"
description = '''I would like to make a map that showed only specific sorts of features, but using the basic OSM data for all of it, and I am asking how to set about doing so. Specifically, I would like a map that showed land (eg the UK) with the ground shown as shaded terrain, and also water features (rivers, canal...'''
date = "2020-08-09T00:36:00Z"
lastmod = "2020-08-09T20:58:00Z"
weight = 76074
keywords = [ "layers", "themes", "features", "display" ]
aliases = [ "/questions/76074" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to show specific feature types, and only those, from OSM data?](/questions/76074/how-to-show-specific-feature-types-and-only-those-from-osm-data)

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
<span id="post-76074-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76074-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76074-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to make a map that showed only specific sorts of features, but using the basic OSM data for all of it, and I am asking how to set about doing so.</p>
<p>Specifically, I would like a map that showed land (eg the UK) with the ground shown as shaded terrain, and also water features (rivers, canals, lakes, sea shore) and nothing else.</p>
<p>Or another example: A map showing land in terrain-shaded form including contours, with all the railway lines present including any related names (e.g. stations), and nothing else.</p>
<p>I am not sure whether I am asking to be able to turn off layers - such as roads, political boundaries etc, or whether the OSM community uses another term for this. I don't want to have to define the "how" of what a thing looks like - I am happy to use an existing representation as appropriate.</p>
<p>Any thoughts?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-layers" rel="tag" title="see questions tagged &#39;layers&#39;">layers</span> <span class="post-tag tag-link-themes" rel="tag" title="see questions tagged &#39;themes&#39;">themes</span> <span class="post-tag tag-link-features" rel="tag" title="see questions tagged &#39;features&#39;">features</span> <span class="post-tag tag-link-display" rel="tag" title="see questions tagged &#39;display&#39;">display</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '20, 00:36</strong></p>
<img src="https://secure.gravatar.com/avatar/2a978d7e7f13da79a41987a8fa31fa68?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rivimey&#39;s gravatar image" />
<p><span>rivimey</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rivimey has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76074" class="comments-container">
&#10;</div>
<div id="comment-tools-76074" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76074-form-container" class="comment-form-container">
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

<span id="76079"></span>

<div id="answer-container-76079" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76079-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76079-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76079-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM doesn't have "layers" in the GIS sense of the word. Different type of objects are indicated by different attributes ("tags") that are attached to object geometries.</p>
<p>You can naturally filter OSM data to just get geometries that you want. But if you want to make multiple different maps you probably would want to store the data in a database and select the geometries you want to render via SQL queries.</p>
<p>A number of points to note:</p>
<ul>
<li><p>the geometries of objects in raw OSM datafiles is not "instantiated" except for Nodes, that means there are no linestrings for ways, that have to be either built after you extracted the OSM data you want, or when the data is imported in to the database (see for example osm2pgsql that does exactly that).</p></li>
<li><p>how to actually render the data depends on what kind of output you want to have. On the one hand you can generate raster images (like on openstreetmap.org) which are created by database queries and further rules on a server, or you could use vector tiles that are rendered on a client (typically in a browser), this has the added advantage that some of the data selection process is done in the client and is substantially more flexible due to that.</p></li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Aug '20, 15:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-76079" class="comments-container">
<span id="76084"></span>
<div id="comment-76084" class="comment">
<div id="post-76084-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the reply. Is there a webite or program that can render OSM sata and allows the displayed tags to be filtered as you suggest?</p>
<p>I don't want to have to build my own application - I'm interested in the map, not the programming.</p>
</div>
<div id="comment-76084-info" class="comment-info">
<span class="comment-age">(09 Aug '20, 16:18)</span> <span class="comment-user userinfo">rivimey</span>
</div>
</div>
<span id="76086"></span>
<div id="comment-76086" class="comment">
<div id="post-76086-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This would depend on intended audience and technology.</p>
<p>But it sounds a bit as if you would be best served by a <a href="https://www.mapbox.com/">mapbox</a> account or similar from other providers.</p>
</div>
<div id="comment-76086-info" class="comment-info">
<span class="comment-age">(09 Aug '20, 20:58)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-76079" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76079-form-container" class="comment-form-container">
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

