+++
type = "question"
title = "Why are alpine_hut elements not rendered in cycle map?"
description = '''I like the cycle map also for hiking, but it seems that all items tagged as alpine_hut are not rendered in the map. Please see here for an example: http://www.openstreetmap.org/#map=17/47.53950/12.88899 Shelters are rendered. I couldn&#x27;t find a reason why alpine huts should be excluded.'''
date = "2014-08-19T11:04:00Z"
lastmod = "2014-08-19T21:11:00Z"
weight = 35988
keywords = [ "alps", "rendering", "opencyclemap", "alpine_hut" ]
aliases = [ "/questions/35988" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Why are alpine_hut elements not rendered in cycle map?](/questions/35988/why-are-alpine_hut-elements-not-rendered-in-cycle-map)

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
<span id="post-35988-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35988-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35988-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I like the cycle map also for hiking, but it seems that all items tagged as alpine_hut are not rendered in the map.</p>
<p>Please see here for an example: <a href="http://www.openstreetmap.org/#map=17/47.53950/12.88899" title="http://www.openstreetmap.org/#map=17/47.53950/12.88899">http://www.openstreetmap.org/#map=17/47.53950/12.88899</a></p>
<p>Shelters are rendered. I couldn't find a reason why alpine huts should be excluded.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-alps" rel="tag" title="see questions tagged &#39;alps&#39;">alps</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-opencyclemap" rel="tag" title="see questions tagged &#39;opencyclemap&#39;">opencyclemap</span> <span class="post-tag tag-link-alpine_hut" rel="tag" title="see questions tagged &#39;alpine_hut&#39;">alpine_hut</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Aug '14, 11:04</strong></p>
<img src="https://secure.gravatar.com/avatar/5e1b94c3db9d66649030515fe688893e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redingo&#39;s gravatar image" />
<p><span>redingo</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redingo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35988" class="comments-container">
<span id="35990"></span>
<div id="comment-35990" class="comment">
<div id="post-35990-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>maybe because the typical cyclist does not ride along alpine huts ?</p>
</div>
<div id="comment-35990-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 14:00)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-35988" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35988-form-container" class="comment-form-container">
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

<span id="36001"></span>

<div id="answer-container-36001" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36001-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36001-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36001-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="redingo has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not familar with OCM development (thats Andys workbench) but try a general answer:</p>
<p>Every map style <strong>focus on a dedicated peergroup</strong> so the vizualisation makes sense (not to complex while still beeing informative). Thus the designers need to pick features and decide for a styling. In the case of OSM, they need to fight with a massive amount of (conflicting) tagging schemas while still take care that the results are predictive and don't create visual clutter at some areas, while leaving others as pure 'deserts' with no details.</p>
<p>That said, for example my area at the sea doesn't know anything about <strong>alpine huts</strong>, as we just don't have any :-) You might want to pick an <a href="https://wiki.openstreetmap.org/wiki/Maps">different map style</a> that focus a bit more on alpine areas, or ping the OCM author and please him to add this feature.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Aug '14, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/49a7d0e0408e9cf2f698faac0f4d837a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iii&#39;s gravatar image" />
<p><span>iii</span><br />
<span class="score" title="4892 reputation points"><span>4.9k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="40 badges"><span class="silver">●</span><span class="badgecount">40</span></span><span title="82 badges"><span class="bronze">●</span><span class="badgecount">82</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iii has 16 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-36001" class="comments-container">
&#10;</div>
<div id="comment-tools-36001" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36001-form-container" class="comment-form-container">
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

