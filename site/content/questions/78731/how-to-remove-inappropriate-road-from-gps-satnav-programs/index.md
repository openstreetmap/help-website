+++
type = "question"
title = "How to remove inappropriate road from GPS / SATNAV programs."
description = '''As many road users no longer read maps and rely on satnav they are now using a road which is not the direct route, it is single track, the road principally serves 2 local farms and as a result is frequently blocked by very large tractor / trailer units (or the units are travelling very fast!), the r...'''
date = "2021-02-08T17:20:00Z"
lastmod = "2021-02-08T21:42:00Z"
weight = 78731
keywords = [ "satnav" ]
aliases = [ "/questions/78731" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to remove inappropriate road from GPS / SATNAV programs.](/questions/78731/how-to-remove-inappropriate-road-from-gps-satnav-programs)

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
<span id="post-78731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78731-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As many road users no longer read maps and rely on satnav they are now using a road which is not the direct route, it is single track, the road principally serves 2 local farms and as a result is frequently blocked by very large tractor / trailer units (or the units are travelling very fast!), the road is only 3 metres wide and has several chicane corners and is not the best route. Delivery drivers (and plant machinery deliveries) and building contractors and are beginning to use the road and thus the situation is getting worse. There is a perfectly good road to the village which is wider (2 vehicles can pass each other!). I am completely new to this but am wondering if somebody can help me change the satnav routing to use the main road.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-satnav" rel="tag" title="see questions tagged &#39;satnav&#39;">satnav</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Feb '21, 17:20</strong></p>
<img src="https://secure.gravatar.com/avatar/7369a90e4bfdce38765dcff246618c00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rikds&#39;s gravatar image" />
<p><span>Rikds</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rikds has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78731" class="comments-container">
&#10;</div>
<div id="comment-tools-78731" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78731-form-container" class="comment-form-container">
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

<span id="78733"></span>

<div id="answer-container-78733" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78733-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78733-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78733-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How routing engines interpret OSM's data is up to them.</p>
<p>There are tags for <a href="https://wiki.openstreetmap.org/wiki/Key:width#Width_of_streets">width</a> and more widely supported tags for number of <a href="https://wiki.openstreetmap.org/wiki/Lanes">lanes</a>. These could be used by routers to adjust their route weighting, but I'm not sure if any actually do. Mapping any <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dpassing_place">passing places</a> that exist might similarly act as a bit of a warning to data consumers (or users, if rendered) although they too may be completely ignored. There is also a recently approved tag for signposted <a href="https://wiki.openstreetmap.org/wiki/Key:hazard">hazards</a> on roads that may be relevant to some of the tight corners you mention, but as it was approved less than two months ago I'd expect few people, if any, are interpreting these tags yet.</p>
<p>If the road is actually a service road or farm track that has been mis-tagged then feel free to <a href="https://wiki.openstreetmap.org/wiki/Highway_tagging_samples/out_of_town">re-classify</a> it according to it's actual status, but please do not introduce inaccuracies just because they are convenient for a particular purpose (the same goes for the main road into town).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '21, 21:07</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-78733" class="comments-container">
&#10;</div>
<div id="comment-tools-78733" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78733-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78736"></span>

<div id="answer-container-78736" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78736-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78736-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-78736-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Well, there is nothing you can do to force satnavs to use a specific route. But you can help satnavs making the best decision by providing all the necessary information to them. In particular tag the two roads with the appropriate values for highway classification, speed limits, number of lanes, stop signs, surface, smoothness, access rights, width etc. You can find information on all on those in our <a href="https://wiki.openstreetmap.org/wiki/Highways">Wiki</a>. Use the search function there.</p>
<p>That will not change the routing of the rather simple satnavs but the more intelligent ones will finally generate the most appropriate routes.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Feb '21, 21:38</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-78736" class="comments-container">
<span id="78737"></span>
<div id="comment-78737" class="comment">
<div id="post-78737-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If they are using OpenStreetMap as a source.</p>
<p>Which probably most are not.</p>
</div>
<div id="comment-78737-info" class="comment-info">
<span class="comment-age">(08 Feb '21, 21:42)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-78736" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78736-form-container" class="comment-form-container">
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

