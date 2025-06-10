+++
type = "question"
title = "Lengths of river ways and relations, and river route finding?"
description = '''I&#x27;ve added a number of waterway relations and rivers in my area, and I would like to use the OSM data to calculate the total length of each river based on the relation. I would also like to be able to route along the way of the river or stream, for kayaking, canoeing and boating.  Is there already a...'''
date = "2018-08-03T05:40:00Z"
lastmod = "2018-08-07T08:48:00Z"
weight = 65093
keywords = [ "length", "waterway", "river", "relation", "routing" ]
aliases = [ "/questions/65093" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lengths of river ways and relations, and river route finding?](/questions/65093/lengths-of-river-ways-and-relations-and-river-route-finding)

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
<span id="post-65093-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65093-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-65093-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've added a number of waterway relations and rivers in my area, and I would like to use the OSM data to calculate the total length of each river based on the relation. I would also like to be able to route along the way of the river or stream, for kayaking, canoeing and boating.</p>
<p>Is there already a web-based service that can calculate the length of a river way or river relation?</p>
<p>Is there a web service that provides routing along rivers and waterways?</p>
<p>I believe there is a JOSM plugin I could download, but this is quite difficult for me due to slow internet and an old laptop, so online options are easier. But I'm also interested in hearing about other offline options, if nothing else is available</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-river" rel="tag" title="see questions tagged &#39;river&#39;">river</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Aug '18, 05:40</strong></p>
<img src="https://secure.gravatar.com/avatar/984eadc21cb77cb316db4ff21c94b869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joseph%20E&#39;s gravatar image" />
<p><span>Joseph E</span><br />
<span class="score" title="390 reputation points">390</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joseph E has 2 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-65093" class="comments-container">
&#10;</div>
<div id="comment-tools-65093" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65093-form-container" class="comment-form-container">
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

<span id="65165"></span>

<div id="answer-container-65165" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65165-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65165-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-65165-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://ra.osmsurround.org/">OSM Relation Analyzer</a> calculates the length of a relation. JOSM displays the length of selected ways in the status bar.</p>
<p><a href="http://brouter.de/brouter-web/">BRouter-Web</a> has a "river" profile for some basic waterway routing (only river, no streams). I also found <a href="http://routino.grade.de">Routino OpenSeaMap Router</a>, but seems to be Europe only.</p>
<p>I would take the lengths with a grain of salt, as they vary with type of measurement and calculation. E.g. for <a href="https://www.openstreetmap.org/relation/123881">Neckar</a>:</p>
<ul>
<li>362.3 km <a href="https://de.wikipedia.org/wiki/Neckar">Wikipedia</a></li>
<li>351.2 km <a href="http://brouter.de/brouter-web/#zoom=9&amp;lat=48.811&amp;lon=8.592&amp;layer=OpenStreetMap&amp;lonlats=8.556553,48.063196%7C8.435011,49.513674&amp;nogos=&amp;profile=river&amp;alternativeidx=0&amp;format=geojson">BRouter-Web</a> (excluding ~3 km stream)</li>
<li>389.4 km <a href="http://ra.osmsurround.org/analyzeRelation?relationId=123881&amp;_noCache=on">Relation Analyzer</a> (probably includes branches)</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '18, 18:05</strong></p>
<img src="https://secure.gravatar.com/avatar/f92748c8fa508a936bcf2169b30cabf6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ikonor&#39;s gravatar image" />
<p><span>ikonor</span><br />
<span class="score" title="1286 reputation points"><span>1.3k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ikonor has 4 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '18, 18:09</strong> </span></p>
</div>
</div>
<div id="comments-container-65165" class="comments-container">
<span id="65174"></span>
<div id="comment-65174" class="comment">
<div id="post-65174-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, <a href="http://brouter.de/brouter-web/#zoom=9&amp;lat=-4.811&amp;lon=138.592&amp;layer=OpenStreetMap&amp;lonlats=8.556553,48.063196%7C8.435011,49.513674&amp;nogos=&amp;profile=river&amp;alternativeidx=0&amp;format=geojson">BRouter</a> is great! The Relationship Analyzer is also very helpful. I hope it will make it easier for me to add the names to rivers properly.</p>
</div>
<div id="comment-65174-info" class="comment-info">
<span class="comment-age">(07 Aug '18, 08:48)</span> <span class="comment-user userinfo">Joseph E</span>
</div>
</div>
</div>
<div id="comment-tools-65165" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65165-form-container" class="comment-form-container">
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

