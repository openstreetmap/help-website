+++
type = "question"
title = "how to export all polygons in a chosen area?"
description = '''Hi, I want to able to have all polygons in a city or a specific area. Basically, I like to download them all with their location name. For example, extracting polygon of every building in Prag.  How can I do that?  Thanks'''
date = "2019-07-25T14:30:00Z"
lastmod = "2019-07-26T15:03:00Z"
weight = 70189
keywords = [ "overpass", "extract", "osm", "polygon" ]
aliases = [ "/questions/70189" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to export all polygons in a chosen area?](/questions/70189/how-to-export-all-polygons-in-a-chosen-area)

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
<span id="post-70189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70189-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I want to able to have all polygons in a city or a specific area. Basically, I like to download them all with their location name. For example, extracting polygon of every building in Prag. How can I do that? Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-polygon" rel="tag" title="see questions tagged &#39;polygon&#39;">polygon</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Jul '19, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/855cd4bb720f760e72b5b9f349e209af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="donniedarko123&#39;s gravatar image" />
<p><span>donniedarko123</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="donniedarko123 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70189" class="comments-container">
&#10;</div>
<div id="comment-tools-70189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70189-form-container" class="comment-form-container">
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

<span id="70204"></span>

<div id="answer-container-70204" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70204-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70204-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70204-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>While in principle it is possible to do this with the <a href="http://overpass-turbo.eu/">Overpass API/Overpass turbo</a>, doing it for a larger city is likely to fail because of processing time and output size issues.</p>
<p>The alternative is to download current OSM data covering your area of interest (for example from <a href="http://download.geofabrik.de/">Geofabrik</a>), extract, filter and convert (to a format with instantiated geometries) yourself. For example with <a href="https://osmcode.org/osmium-tool/">Osmium</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jul '19, 15:03</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jul '19, 15:04</strong> </span></p>
</div>
</div>
<div id="comments-container-70204" class="comments-container">
&#10;</div>
<div id="comment-tools-70204" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70204-form-container" class="comment-form-container">
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

