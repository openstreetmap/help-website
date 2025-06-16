+++
type = "question"
title = "Overpass: Match not only borders, but also inside area"
description = '''I&#x27;m trying to retrieve the forests within a specific (relatively small) bounding box with Overpass API. I&#x27;m using the following query: [out:json][timeout:25]; (  way[&quot;landuse&quot;=&quot;forest&quot;]({{bbox}});  relation[&quot;landuse&quot;=&quot;forest&quot;]({{bbox}}); ); out body; &amp;gt;; out skel qt;  When the edge of the forest i...'''
date = "2018-11-27T09:15:00Z"
lastmod = "2018-11-28T07:38:00Z"
weight = 66934
keywords = [ "overpass", "overpass-turbo", "query" ]
aliases = [ "/questions/66934" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Overpass: Match not only borders, but also inside area](/questions/66934/overpass-match-not-only-borders-but-also-inside-area)

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
<span id="post-66934-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66934-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66934-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to retrieve the forests within a specific (relatively small) bounding box with Overpass API. I'm using the following query:</p>
<pre><code>[out:json][timeout:25];
(
  way[&quot;landuse&quot;=&quot;forest&quot;]({{bbox}});
  relation[&quot;landuse&quot;=&quot;forest&quot;]({{bbox}});
);
out body;
&gt;;
out skel qt;</code></pre>
<p>When the edge of the forest intersects my bounding box, the query works as intended:</p>
<p><img src="/upfiles/Screenshot_2018-11-27_at_10.09.23.png" alt="alt text" /></p>
<p>But once the bounding box is completely inside of the forest, I receive no results:</p>
<p><img src="/upfiles/Screenshot_2018-11-27_at_10.09.39.png" alt="alt text" /></p>
<p>Is there any way to fix this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Nov '18, 09:15</strong></p>
<img src="https://secure.gravatar.com/avatar/cf616a426b476b0a8aa7c13cbaa648b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="misotrnka&#39;s gravatar image" />
<p><span>misotrnka</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="misotrnka has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-66934" class="comments-container">
&#10;</div>
<div id="comment-tools-66934" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66934-form-container" class="comment-form-container">
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

<span id="66937"></span>

<div id="answer-container-66937" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-66937-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66937-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-66937-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="misotrnka has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It's not a 100% answer, but for forests with names, you can retrieve them using is_in:</p>
<pre><code>is_in(48.21634,17.12552) -&gt;.in;
(
 way(pivot.in)[landuse=forest];
 rel(pivot.in)[landuse=forest];
);
out geom;</code></pre>
<p>the <code>is_in</code> operator returns Overpass-API areas, the pivot statements retrieve the underlying geometries related to those features. You can look in <a href="https://github.com/drolbr/Overpass-API/blob/master/src/rules/areas.osm3s">https://github.com/drolbr/Overpass-API/blob/master/src/rules/areas.osm3s</a> to see the rules for the features that will be returned by is_in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Nov '18, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</img>
</div>
</div>
<div id="comments-container-66937" class="comments-container">
<span id="66948"></span>
<div id="comment-66948" class="comment">
<div id="post-66948-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, this actually works perfectly. I just need to make a query with a bounding box and another query for the center point.</p>
</div>
<div id="comment-66948-info" class="comment-info">
<span class="comment-age">(28 Nov '18, 07:38)</span> <span class="comment-user userinfo">misotrnka</span>
</div>
</div>
</div>
<div id="comment-tools-66937" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66937-form-container" class="comment-form-container">
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

