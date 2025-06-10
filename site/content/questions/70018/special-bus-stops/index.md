+++
type = "question"
title = "Special bus stops"
description = '''Some bus routes in my area have special stops off the normal route that buses only stop at when someone calls a phone number listed on a sign by the stop. Is there any consensus on how to include stops like these as part of the routes?'''
date = "2019-07-13T03:56:00Z"
lastmod = "2019-07-14T18:49:00Z"
weight = 70018
keywords = [ "busroute", "busstops" ]
aliases = [ "/questions/70018" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Special bus stops](/questions/70018/special-bus-stops)

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
<span id="post-70018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70018-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Some bus routes in my area have special stops off the normal route that buses only stop at when someone calls a phone number listed on a sign by the stop. Is there any consensus on how to include stops like these as part of the routes?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-busroute" rel="tag" title="see questions tagged &#39;busroute&#39;">busroute</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Jul '19, 03:56</strong></p>
<img src="https://secure.gravatar.com/avatar/4d9b429d88332cf1460ceef378d28f14?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Itserpol&#39;s gravatar image" />
<p><span>Itserpol</span><br />
<span class="score" title="71 reputation points">71</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Itserpol has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-70018" class="comments-container">
&#10;</div>
<div id="comment-tools-70018" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70018-form-container" class="comment-form-container">
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

<span id="70065"></span>

<div id="answer-container-70065" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-70065-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-70065-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-70065-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Itserpol has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I don't think there is an established way mapping those, nor marking them in the route. Entire lines that only operate on a phone call get sometimes tagged with on_demand=yes (<a href="https://www.openstreetmap.org/relation/6231339">example</a>). I'd suggest using that tag on your stops, too.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Jul '19, 16:12</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-70065" class="comments-container">
<span id="70066"></span>
<div id="comment-70066" class="comment">
<div id="post-70066-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's a good idea for the stops, but now I'm thinking about the way segments on the extra "leg" of the route. It would be helpful if they could be specified as on_demand=yes as well for the route, but then a way could potentially need on_demand tags for every route relation it belongs to. Would it make sense to assign a role to those extra segments, and perhaps the stops as well?</p>
</div>
<div id="comment-70066-info" class="comment-info">
<span class="comment-age">(14 Jul '19, 16:27)</span> <span class="comment-user userinfo">Itserpol</span>
</div>
</div>
<span id="70068"></span>
<div id="comment-70068" class="comment">
<div id="post-70068-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If I saw this on a station I might assume it was a request stop which has <a href="https://wiki.openstreetmap.org/wiki/Tag:railway%3Dhalt">specific tagging</a> for railways. <a href="https://wiki.openstreetmap.org/wiki/Relation:route_master">Route master</a> tagging can handle variant routes, but the mailing lists or the forums are a better place for tag creation.</p>
</div>
<div id="comment-70068-info" class="comment-info">
<span class="comment-age">(14 Jul '19, 18:49)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-70065" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-70065-form-container" class="comment-form-container">
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

