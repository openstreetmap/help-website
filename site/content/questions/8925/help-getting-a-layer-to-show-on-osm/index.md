+++
type = "question"
title = "Help getting a layer to show on OSM"
description = '''I&#x27;m having trouble getting a layer to show on top of another - a car park to show on top of a sports arena - see https://www.openstreetmap.org/?lat=51.423296&amp;amp;lon=-2.835831&amp;amp;zoom=18&amp;amp;layers=M There should be 2 car parks showing on the stadium (left hand) but I can only get the small one to r...'''
date = "2011-11-11T09:13:00Z"
lastmod = "2011-11-11T10:45:00Z"
weight = 8925
keywords = [ "rendering", "area" ]
aliases = [ "/questions/8925" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Help getting a layer to show on OSM](/questions/8925/help-getting-a-layer-to-show-on-osm)

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
<span id="post-8925-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8925-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8925-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm having trouble getting a layer to show on top of another - a car park to show on top of a sports arena - see <a href="https://www.openstreetmap.org/?lat=51.423296&amp;lon=-2.835831&amp;zoom=18&amp;layers=M">https://www.openstreetmap.org/?lat=51.423296&amp;lon=-2.835831&amp;zoom=18&amp;layers=M</a></p>
<p>There should be 2 car parks showing on the stadium (left hand) but I can only get the small one to render. I've tried making it a higher layer which didn't seem to work so used an inner/outer multi-polygon. This worked for one of the two but not the other. I don't understand!</p>
<p>Any advice please?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Nov '11, 09:13</strong></p>
<img src="https://secure.gravatar.com/avatar/45d62517b772d1ae37975c05be147cf9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FollowMeChaps&#39;s gravatar image" />
<p><span>FollowMeChaps</span><br />
<span class="score" title="325 reputation points">325</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FollowMeChaps has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Nov '11, 09:31</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span></p>
</div>
</div>
<div id="comments-container-8925" class="comments-container">
&#10;</div>
<div id="comment-tools-8925" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8925-form-container" class="comment-form-container">
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

<span id="8927"></span>

<div id="answer-container-8927" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8927-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8927-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8927-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="FollowMeChaps has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think there are a number of issues here, such as how the OSM data gets translated into the database that Mapnik uses for rendering, so the layers tags don't always work in the way you expect. I note though that you've tried using multipolygons to make the car parks holes in the stadium, which has worked for the smaller one but not the larger. I suspect this will be because the larger car park, while given the role of inner, isn't entirely within the outer - see for example <a href="https://www.openstreetmap.org/browse/node/1495166974">this node</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Nov '11, 10:06</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-8927" class="comments-container">
<span id="8929"></span>
<div id="comment-8929" class="comment">
<div id="post-8929-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Gosh, you are a sharp cookie Ed, I didn't spot that. I've tweaked it and will now wait and see if that works. Many thanks. Robin</p>
</div>
<div id="comment-8929-info" class="comment-info">
<span class="comment-age">(11 Nov '11, 10:31)</span> <span class="comment-user userinfo">FollowMeChaps</span>
</div>
</div>
<span id="8930"></span>
<div id="comment-8930" class="comment">
<div id="post-8930-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Refreshing now and the large car park appears, but the small one is now green. I wonder if it is because you have it twice in the multipolygon rather than once? <a href="https://www.openstreetmap.org/browse/way/136294027">https://www.openstreetmap.org/browse/way/136294027</a></p>
</div>
<div id="comment-8930-info" class="comment-info">
<span class="comment-age">(11 Nov '11, 10:45)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8927" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8927-form-container" class="comment-form-container">
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

