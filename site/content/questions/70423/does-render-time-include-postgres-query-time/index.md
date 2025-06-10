+++
type = "question"
title = "Does render time include postgres query time?"
description = '''Hello, I&#x27;ve set up my own tile server (as in the tutorial on the https://switch2osm.org/manually-building-a-tile-server-18-04-lts/) and now I have a few questions about optimization (I guess).  So, the main question is, does the render time: renderd[5037]: DEBUG: START TILE ajt 17 71632-71639 43864-...'''
date = "2019-08-19T15:27:00Z"
lastmod = "2019-08-19T15:27:00Z"
weight = 70423
keywords = [ "renderd", "time" ]
aliases = [ "/questions/70423" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Does render time include postgres query time?](/questions/70423/does-render-time-include-postgres-query-time)

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
<span id="post-70423-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70423-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-70423-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I've set up my own tile server (as in the tutorial on the <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/)">https://switch2osm.org/manually-building-a-tile-server-18-04-lts/)</a> and now I have a few questions about optimization (I guess).</p>
<p>So, the main question is, does the render time:</p>
<p>renderd[5037]: DEBUG: START TILE ajt 17 71632-71639 43864-43871, new metatile renderd[5037]: DEBUG: DONE TILE ajt 17 71632-71639 43864-43871 in 3.534 seconds</p>
<p>include the time that's needed by postgres to complete the queries:</p>
<p>execution time 2038.937 ms, query: SELECT ST_AsBinary("way") AS geom,"feature","link","service" FROM (SELECT way, (CASE WHEN feature IN ('highway_motorway_link', 'highway_trunk_link', 'highway_prima ry_link', 'highway_secondary_link', 'highway_tertiary_link') THEN substr(feature, 0, length(feat ure)-4) ELSE feature END) AS feature, [...]</p>
<p>If yes, then if there's better CartoCss version that has queries optimized for the better indices usage?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-time" rel="tag" title="see questions tagged &#39;time&#39;">time</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '19, 15:27</strong></p>
<img src="https://secure.gravatar.com/avatar/7b5775bcca69a6b6603f02a8255ef2f1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="januzi&#39;s gravatar image" />
<p><span>januzi</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="januzi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70423" class="comments-container">
&#10;</div>
<div id="comment-tools-70423" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70423-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

