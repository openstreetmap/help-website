+++
type = "question"
title = "Routing Directions"
description = '''I am working on mapping a private community. I added a couple of addresses (for validation purposes), gave it a few weeks, and am testing turn-by-turn directions. The destination addresses is &quot;2736, Tyrol Nook Drive, Innsbrook, Warren County, Missouri, 63390, United States&quot; If I use OSRM and Grassho...'''
date = "2023-08-09T21:45:00Z"
lastmod = "2023-08-10T10:15:00Z"
weight = 87650
keywords = [ "osrm", "turn-by-turn", "routing" ]
aliases = [ "/questions/87650" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Routing Directions](/questions/87650/routing-directions)

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
<span id="post-87650-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87650-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87650-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am working on mapping a private community. I added a couple of addresses (for validation purposes), gave it a few weeks, and am testing turn-by-turn directions. The destination addresses is "2736, Tyrol Nook Drive, Innsbrook, Warren County, Missouri, 63390, United States" If I use OSRM and Grasshopper my turn-by-turn directions are not correct, missing data or showing old data. Valhalla does turn by turn correctly. My questions is, before I go to the effort of updating all the addresses is the community, will my turn-by-turn stuff eventually work on OSRM, why are they not working now?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-turn-by-turn" rel="tag" title="see questions tagged &#39;turn-by-turn&#39;">turn-by-turn</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Aug '23, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/7e86c8bb7affb96b3b6325334cfa0b99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tkarez&#39;s gravatar image" />
<p><span>tkarez</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tkarez has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87650" class="comments-container">
&#10;</div>
<div id="comment-tools-87650" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87650-form-container" class="comment-form-container">
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

<span id="87651"></span>

<div id="answer-container-87651" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87651-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks as if the demo OSRM instance used at osm.org has not updated the data yet (the same applies to the Graphhopper instance used). If you look here at <a href="https://fast-routing-api.demo.routingapi.net/">https://fast-routing-api.demo.routingapi.net/</a> with your destination, you'll see that a more recent OSRM data update will route to your destination the same way Valhalla does.</p>
<p>So the mapping you did will eventually work on osm.org as well as soon as the demo instance at routing.openstreetmap.de will update the data.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Aug '23, 10:15</strong></p>
<img src="https://secure.gravatar.com/avatar/e06ed329df6032df14b5639de4d64782?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Spiekerooger&#39;s gravatar image" />
<p><span>Spiekerooger</span><br />
<span class="score" title="3148 reputation points"><span>3.1k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Spiekerooger has 18 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Aug '23, 10:26</strong> </span></p>
</div>
</div>
<div id="comments-container-87651" class="comments-container">
&#10;</div>
<div id="comment-tools-87651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87651-form-container" class="comment-form-container">
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

