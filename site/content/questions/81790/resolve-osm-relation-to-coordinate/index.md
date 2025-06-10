+++
type = "question"
title = "Resolve osm relation to coordinate"
description = '''Hi, I would like to resolve a list of negative OSMids/relations to a coordinate. For example, Paris with a relation of &quot;-71525&quot; would like to get a pair of coordinates back. I already tried using the Overpassturbo API, but there I only get a list of nodes and other entities, not the coordinates. Doe...'''
date = "2021-09-17T12:09:00Z"
lastmod = "2022-01-26T00:19:00Z"
weight = 81790
keywords = [ "overpass", "overpass-turbo", "coordinates", "relations" ]
aliases = [ "/questions/81790" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Resolve osm relation to coordinate](/questions/81790/resolve-osm-relation-to-coordinate)

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
<span id="post-81790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81790-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-81790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I would like to resolve a list of negative OSMids/relations to a coordinate. For example, Paris with a relation of "-71525" would like to get a pair of coordinates back. I already tried using the Overpassturbo API, but there I only get a list of nodes and other entities, not the coordinates.</p>
<p>Does anybody know how to do it?</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-coordinates" rel="tag" title="see questions tagged &#39;coordinates&#39;">coordinates</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Sep '21, 12:09</strong></p>
<img src="https://secure.gravatar.com/avatar/9954cbab977ab2236c4d1ad43b434bbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Garome&#39;s gravatar image" />
<p><span>Garome</span><br />
<span class="score" title="15 reputation points">15</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Garome has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81790" class="comments-container">
<span id="81791"></span>
<div id="comment-81791" class="comment">
<div id="post-81791-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why do you have a negative id for the relation? The relation is a closed polygon. Do you want a single co-ordinate pair for the centroid or a pair for each node?</p>
</div>
<div id="comment-81791-info" class="comment-info">
<span class="comment-age">(17 Sep '21, 13:36)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
<span id="81792"></span>
<div id="comment-81792" class="comment">
<div id="post-81792-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I used a list of nodes and relations with positive and negative values, where the positive values refer to nodes and the negative values refer to relations. The positive values/nodes I already converted into a coordinate, but for the negative ones/relations I have no idea how to do it. I would like to get a single coordinate for each relation back (for the centroid). Thanks for your reply!</p>
</div>
<div id="comment-81792-info" class="comment-info">
<span class="comment-age">(17 Sep '21, 13:54)</span> <span class="comment-user userinfo">Garome</span>
</div>
</div>
<span id="81793"></span>
<div id="comment-81793" class="comment">
<div id="post-81793-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think the "negative" before the value is only for separating nodes and relations. So I for Paris the relation is "71525" and not "-71525".</p>
</div>
<div id="comment-81793-info" class="comment-info">
<span class="comment-age">(17 Sep '21, 14:20)</span> <span class="comment-user userinfo">Garome</span>
</div>
</div>
<span id="83194"></span>
<div id="comment-83194" class="comment">
<div id="post-83194-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For completeness, I believe that the negative id just means that it's a value from a database loaded by osm2pgsql from a relation. osm2pgsql will add way 12345 as "12345" and relation 12345 as "-12345" to the _line or _polygon tables. Just remove the "-" to get the OSM relation number.</p>
</div>
<div id="comment-83194-info" class="comment-info">
<span class="comment-age">(25 Jan '22, 18:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="83202"></span>
<div id="comment-83202" class="comment">
<div id="post-83202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh for crying out loud, not once did Garome mention osm2pgsql.</p>
</div>
<div id="comment-83202-info" class="comment-info">
<span class="comment-age">(26 Jan '22, 00:15)</span> <span class="comment-user userinfo">DaveF</span>
</div>
</div>
</div>
<div id="comment-tools-81790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81790-form-container" class="comment-form-container">
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

<span id="83065"></span>

<div id="answer-container-83065" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83065-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-83065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Garome has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Given your clarification not using a negative id, you could simply do like this:</p>
<pre><code>[out:csv(::type,::id,name,::lat,::lon)][timeout:20];
(rel(71525);) -&gt; .object;
.object out center;</code></pre>
<p>Which will give you the coordinates of the centre:</p>
<pre><code>@type       @id     name    @lat        @lon
relation    71525   Paris   48.8588657  2.3469411</code></pre>
<p>The relation is shown on <a href="https://www.openstreetmap.org/relation/71525">https://www.openstreetmap.org/relation/71525</a> and its centre is marked on <a href="https://www.openstreetmap.org/?mlat=48.8588657&amp;mlon=2.3469411">https://www.openstreetmap.org/?mlat=48.8588657&amp;mlon=2.3469411</a>. (Observe that the centre of an area might also be outside the area depending on the area's shape.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jan '22, 16:27</strong></p>
<img src="https://secure.gravatar.com/avatar/ffb12f7c2548687764b2de9e4562d2d9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="G%C3%A5seborg&#39;s gravatar image" />
<p><span>Gåseborg</span><br />
<span class="score" title="311 reputation points">311</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gåseborg has 4 accepted answers">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jan '22, 16:37</strong> </span></p>
</div>
</div>
<div id="comments-container-83065" class="comments-container">
<span id="83199"></span>
<div id="comment-83199" class="comment">
<div id="post-83199-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks a lot for your answer!</p>
</div>
<div id="comment-83199-info" class="comment-info">
<span class="comment-age">(25 Jan '22, 21:32)</span> <span class="comment-user userinfo">Garome</span>
</div>
</div>
</div>
<div id="comment-tools-83065" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83065-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="83203"></span>

<div id="answer-container-83203" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-83203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-83203-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-83203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For those who want to do it even more simply.</p>
<p><a href="https://overpass-turbo.eu/s/1frI">https://overpass-turbo.eu/s/1frI</a></p>
<pre><code>[out:csv(::type,::id,name,::lat,::lon)];
rel(71525);
out center;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '22, 00:19</strong></p>
<img src="https://secure.gravatar.com/avatar/c9c8b421ad22f51ddd62f23413717036?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DaveF&#39;s gravatar image" />
<p><span>DaveF</span><br />
<span class="score" title="3264 reputation points"><span>3.3k</span></span><span title="84 badges"><span class="badge1">●</span><span class="badgecount">84</span></span><span title="98 badges"><span class="silver">●</span><span class="badgecount">98</span></span><span title="133 badges"><span class="bronze">●</span><span class="badgecount">133</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DaveF has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-83203" class="comments-container">
&#10;</div>
<div id="comment-tools-83203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-83203-form-container" class="comment-form-container">
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

