+++
type = "question"
title = "Get streets distance in osm?"
description = '''Hey, I&#x27;m kinda new at this so bare with me. I downloaded my country osm data and put it in postgres. I would like to make a research on the data so I can for example have all the streets in a radius of 5 miles from a location (ultimately I would like to work directly with the data and not go through...'''
date = "2015-04-12T03:21:00Z"
lastmod = "2015-04-12T09:46:00Z"
weight = 42278
keywords = [ "postgresql", "radius", "postgis", "way" ]
aliases = [ "/questions/42278" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Get streets distance in osm?](/questions/42278/get-streets-distance-in-osm)

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
<span id="post-42278-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42278-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42278-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey, I'm kinda new at this so bare with me. I downloaded my country osm data and put it in postgres. I would like to make a research on the data so I can for example have all the streets in a radius of 5 miles from a location (ultimately I would like to work directly with the data and not go through external api's. I looked at the data in the roads table and ,in there, there is that column "way" (900913). Can I use the data in that column to reach my goal ? What does the data in that column really represent ? I know it's something related to projection but it's vague.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-radius" rel="tag" title="see questions tagged &#39;radius&#39;">radius</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-way" rel="tag" title="see questions tagged &#39;way&#39;">way</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Apr '15, 03:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5759ecf7d67bc1209e4a30779684f59a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="activee&#39;s gravatar image" />
<p><span>activee</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="activee has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Apr '15, 13:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-42278" class="comments-container">
&#10;</div>
<div id="comment-tools-42278" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42278-form-container" class="comment-form-container">
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

<span id="42287"></span>

<div id="answer-container-42287" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42287-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-42287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <code>way</code> column contains the geometry of the street (for those objects where the <code>highway</code> column is not null). Your problem can likely be solved using the PostGIS function <code>st_dwithin</code>; for further information, check the PostGIS manual or generic PostGIS resources - this is not an OSM specific question.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Apr '15, 09:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-42287" class="comments-container">
&#10;</div>
<div id="comment-tools-42287" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42287-form-container" class="comment-form-container">
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

