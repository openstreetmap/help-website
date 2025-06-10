+++
type = "question"
title = "Export Road (Way) data for large regions"
description = '''I would like to export road/higway/way data for a large region. the end product im trying to get is a vector file or all the streets, roads and ways of london. the problem so far has been that the osm maps have to many nodes to be exported. openmade, which lets you customize the map style, to my kno...'''
date = "2010-11-23T02:16:00Z"
lastmod = "2010-12-11T00:28:00Z"
weight = 1590
keywords = [ "large", "export", "extract" ]
aliases = [ "/questions/1590" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Export Road (Way) data for large regions](/questions/1590/export-road-way-data-for-large-regions)

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
<span id="post-1590-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1590-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-1590-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to export road/higway/way data for a large region. the end product im trying to get is a vector file or all the streets, roads and ways of london.</p>
<p>the problem so far has been that the osm maps have to many nodes to be exported. openmade, which lets you customize the map style, to my knowledge, doesnt let you download maps with the visible data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-large" rel="tag" title="see questions tagged &#39;large&#39;">large</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-extract" rel="tag" title="see questions tagged &#39;extract&#39;">extract</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Nov '10, 02:16</strong></p>
<img src="https://secure.gravatar.com/avatar/0ace8b219f26d112782da1fc78ee197f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smombartz&#39;s gravatar image" />
<p><span>smombartz</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smombartz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-1590" class="comments-container">
<span id="1767"></span>
<div id="comment-1767" class="comment">
<div id="post-1767-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i've tried installing OSM and im getting a java error. its quite frustrating. im happy to pay someone to get the street data (paths, ways, roads) of a few major cities (london, paris, new york, cairo, shanghai, tokyo, istanbul, edinburgh, buenos aires, valetta, rome) or help me figure out OSM. (its for a screen printed poster series)</p>
<p>million thanks again, Sascha</p>
</div>
<div id="comment-1767-info" class="comment-info">
<span class="comment-age">(11 Dec '10, 00:28)</span> <span class="comment-user userinfo">smombartz</span>
</div>
</div>
</div>
<div id="comment-tools-1590" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1590-form-container" class="comment-form-container">
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

<span id="1593"></span>

<div id="answer-container-1593" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1593-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1593-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-1593-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Download a suitable subset of OSM data from the web (e.g. the <a href="http://download.geofabrik.de/osm/europe/great_britain/england.osm.pbf">England</a> extract from Geofabrik), then run <a href="http://wiki.openstreetmap.org/wiki/Osmosis">Osmosis</a> to cut out your region of interest from that.</p>
<p>A possible Osmosis command line to cut out the M25 rectangle from the England extract is:</p>
<pre><code>osmosis --read-pbf england.osm.pbf --bb left=-0.55 right=0.29 top=51.72 bottom=51.25 clipIncompleteEntities=true --write-xml london-m25.osm</code></pre>
<ul>
<li>but do read up on the various possible modifiers to the --bb action on the Osmosis wiki page and select those that match your application best.</li>
</ul>
<p>You can also throw in the --way-key and/or --used-node filters to reduce the extract to highway data only.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '10, 07:16</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Nov '10, 07:17</strong> </span></p>
</div>
</div>
<div id="comments-container-1593" class="comments-container">
<span id="1651"></span>
<div id="comment-1651" class="comment">
<div id="post-1651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>great, thanks! ill give that a try.</p>
</div>
<div id="comment-1651-info" class="comment-info">
<span class="comment-age">(26 Nov '10, 20:25)</span> <span class="comment-user userinfo">smombartz</span>
</div>
</div>
</div>
<div id="comment-tools-1593" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1593-form-container" class="comment-form-container">
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

