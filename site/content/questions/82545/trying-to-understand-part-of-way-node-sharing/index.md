+++
type = "question"
title = "trying to understand &quot;part of way&quot; node sharing"
description = '''I&#x27;m new to osm and poking around between the docs and map. I came across this node shared between this railway and this footpath.  A check of the raster on google maps shows that it&#x27;s a dirt path that crosses the train tracks.  Is this correct? To me this suggests you can &quot;transfer&quot; between ways her...'''
date = "2021-11-12T14:58:00Z"
lastmod = "2021-11-12T18:42:00Z"
weight = 82545
keywords = [ "ways", "nodes" ]
aliases = [ "/questions/82545" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [trying to understand "part of way" node sharing](/questions/82545/trying-to-understand-part-of-way-node-sharing)

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
<span id="post-82545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82545-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to osm and poking around between the docs and map. I came across <a href="https://www.openstreetmap.org/node/8451799044#map=19/38.79522/-77.26963">this node</a> shared between <a href="https://www.openstreetmap.org/way/111535204#map=18/38.79533/-77.26860">this railway</a> and <a href="https://www.openstreetmap.org/way/910319607#map=18/38.79543/-77.26880">this footpath</a>.</p>
<p>A check of the <a href="https://www.google.com/maps/place/38%C2%B047&#39;42.8%22N+77%C2%B016&#39;10.7%22W/@38.7954397,-77.270142,268m/data=!3m1!1e3!4m5!3m4!1s0x0:0xcf0fe1f0f8159633!8m2!3d38.795216!4d-77.2696271">raster on google maps</a> shows that it's a dirt path that crosses the train tracks.</p>
<p>Is this correct? To me this suggests you can "transfer" between ways here.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ways" rel="tag" title="see questions tagged &#39;ways&#39;">ways</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Nov '21, 14:58</strong></p>
<img src="https://secure.gravatar.com/avatar/f41614b3291bb862ee474ad426227d62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="zappytoes&#39;s gravatar image" />
<p><span>zappytoes</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="zappytoes has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82545" class="comments-container">
&#10;</div>
<div id="comment-tools-82545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82545-form-container" class="comment-form-container">
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

<span id="82546"></span>

<div id="answer-container-82546" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82546-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82546-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-82546-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It may be questionable if a dirt path crossing a railway line should be mapped at all. But leaving that question aside the situation is correctly mapped.</p>
<p>You can see that the node in question is tagged with <a href="https://wiki.openstreetmap.org/wiki/Tag:railway%3Dcrossing"><code>railway=crossing</code></a> wich highlights this exact situation. And of course you can transfer between the ways here. Nothing physical (no level difference, wall, ...) stops you from sverving off the path and continue walking on the tracks.</p>
<p>And only since the two ways share a node is it obvious for a data consumer that both ways are physically connected. A router may give you a warning walking along the path that you have to watch out for trains.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '21, 15:24</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Nov '21, 15:27</strong> </span></p>
</div>
</div>
<div id="comments-container-82546" class="comments-container">
<span id="82547"></span>
<div id="comment-82547" class="comment">
<div id="post-82547-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I see how that tag works in this situation.</p>
<p>My ultimate goal is to understand route/directions algorithms, so I was curious what info I would use to deal with that node.</p>
</div>
<div id="comment-82547-info" class="comment-info">
<span class="comment-age">(12 Nov '21, 15:41)</span> <span class="comment-user userinfo">zappytoes</span>
</div>
</div>
<span id="82550"></span>
<div id="comment-82550" class="comment">
<div id="post-82550-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Roads can be connected to all sorts of objects: landuses, buildings, waterways, bridges, ...</p>
<p>I guess for routing purposes you would create a graph of only routable ways (roads for cars, roads (but not motorways) and paths for pedestrians, etc.). What's routable can be determined by the way's primary tag but also by access and some other tags. So if you think a pedestrian shouldn't walk along railroad tracks you would exclude those from your graph alltogether and you would not be concerned about the node at all. Of course it's not that simple (nodes might constitute barriers) but you get the gist.</p>
</div>
<div id="comment-82550-info" class="comment-info">
<span class="comment-age">(12 Nov '21, 18:42)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-82546" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82546-form-container" class="comment-form-container">
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

