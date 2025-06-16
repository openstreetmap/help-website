+++
type = "question"
title = "Get *all* PoI via Overpass?"
description = '''This is my first time using Overpass. I want a list of all the PoI within a bounding box. I can get a list of all nodes using http://overpass-api.de/api/interpreter?data=[out:json];node(51.7248487,-1.2328819,51.7249487,-1.2329819);out;  I just want the shops, cafes, bus stops, benches, etc - not the...'''
date = "2014-08-17T16:00:00Z"
lastmod = "2014-08-18T14:49:00Z"
weight = 35922
keywords = [ "overpass", "api", "poi" ]
aliases = [ "/questions/35922" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Get \*all\* PoI via Overpass?](/questions/35922/get-all-poi-via-overpass)

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
<span id="post-35922-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35922-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35922-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This is my first time using Overpass.</p>
<p>I want a list of <strong>all</strong> the PoI within a bounding box.</p>
<p>I can get a list of all <em>nodes</em> using</p>
<pre><code>http://overpass-api.de/api/interpreter?data=[out:json];node(51.7248487,-1.2328819,51.7249487,-1.2329819);out;</code></pre>
<p>I just want the shops, cafes, bus stops, benches, etc - not the empty nodes. Is there any way to prune out all the nodes and just get the places / things?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '14, 16:00</strong></p>
<img src="https://secure.gravatar.com/avatar/52cb49a66755f31abf4df9a6549f0f9c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terence%20Eden&#39;s gravatar image" />
<p><span>Terence Eden</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terence Eden has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35922" class="comments-container">
&#10;</div>
<div id="comment-tools-35922" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35922-form-container" class="comment-form-container">
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

<span id="35923"></span>

<div id="answer-container-35923" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35923-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-35923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Terence Eden has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to realise that some POI (i.e. restaurants, etc.) are not represented by points, but by ways or even relations. The following query returns all amenities and shops <a href="http://overpass-turbo.eu/s/4BV">http://overpass-turbo.eu/s/4BV</a> in the visible box. Replace the BBox with the one you need.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '14, 16:15</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-35923" class="comments-container">
<span id="35925"></span>
<div id="comment-35925" class="comment">
<div id="post-35925-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>bus stops are not amenities, nor shops. So you might have to add highway=bus_stop and public_transport=stop_position</p>
</div>
<div id="comment-35925-info" class="comment-info">
<span class="comment-age">(17 Aug '14, 17:15)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-35923" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35923-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35956"></span>

<div id="answer-container-35956" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35956-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35956-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35956-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you get any result file from overpass-api or overpass-turbo.eu in format of raw OSM data in XML format, you can try <strong><a href="https://wiki.openstreetmap.org/wiki/Osmconvert">osmconvert</a></strong> to produce a list of all POIs in CSV format.</p>
<p>Try also <a href="https://wiki.openstreetmap.org/wiki/Osmfilter">osmfilter</a> if needed.</p>
<p>Search for CSV on this FAQ to find some more hints.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '14, 14:49</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-35956" class="comments-container">
&#10;</div>
<div id="comment-tools-35956" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35956-form-container" class="comment-form-container">
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

