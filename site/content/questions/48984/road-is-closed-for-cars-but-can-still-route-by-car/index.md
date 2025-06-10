+++
type = "question"
title = "Road is closed for cars, but can still route by car"
description = '''I have changed a road to be only accessible by foot: http://www.openstreetmap.org/changeset/38218082 It is blocked on several positions with large boulders. A car can never use this road. However when using the routing features, I can still map my route over this road, see for instance:  http://www....'''
date = "2016-04-01T07:15:00Z"
lastmod = "2016-04-01T08:38:00Z"
weight = 48984
keywords = [ "routing", "road", "blocked" ]
aliases = [ "/questions/48984" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Road is closed for cars, but can still route by car](/questions/48984/road-is-closed-for-cars-but-can-still-route-by-car)

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
<span id="post-48984-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48984-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-48984-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have changed a road to be only accessible by foot: <a href="http://www.openstreetmap.org/changeset/38218082">http://www.openstreetmap.org/changeset/38218082</a> It is blocked on several positions with large boulders. A car can never use this road. However when using the routing features, I can still map my route over this road, see for instance: <a href="http://www.openstreetmap.org/directions?engine=osrm_car&amp;route=12.1791%2C-68.2887%3B12.1905%2C-68.2794#map=17/12.18905/-68.27989">http://www.openstreetmap.org/directions?engine=osrm_car&amp;route=12.1791%2C-68.2887%3B12.1905%2C-68.2794#map=17/12.18905/-68.27989</a></p>
<p>It should however use a different road to guide me to the destination. Is my edit somehow wrong, or is the routing information updated less frequent?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-road" rel="tag" title="see questions tagged &#39;road&#39;">road</span> <span class="post-tag tag-link-blocked" rel="tag" title="see questions tagged &#39;blocked&#39;">blocked</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Apr '16, 07:15</strong></p>
<img src="https://secure.gravatar.com/avatar/5718d94ce1c9c879b98086563917dabd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rody&#39;s gravatar image" />
<p><span>Rody</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rody has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-48984" class="comments-container">
&#10;</div>
<div id="comment-tools-48984" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48984-form-container" class="comment-form-container">
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

<span id="48985"></span>

<div id="answer-container-48985" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48985-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48985-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-48985-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Rody has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The <a href="https://www.openstreetmap.org/way/26284967">old way 26284967</a> still exists and is used for routing. Instead of updating the access tags of the existing way you accidentally added a new ways <a href="https://www.openstreetmap.org/way/406443255">406443255</a> and <a href="https://www.openstreetmap.org/way/406901331">406901331</a>. Now there are three overlapping ways which is wrong.</p>
<p>Fix this by deleting your newly added ways 406443255 and 406901331. Then split the old way 26284967 at the relevant nodes and add the access tags again.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Apr '16, 08:07</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-48985" class="comments-container">
<span id="48986"></span>
<div id="comment-48986" class="comment">
<div id="post-48986-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>It's also worth mentioning that external routing sites such as OSRM won't react to changes to OSM data immediately. After you fix it in OSM you may have to wait a few days for external routers to use your change.</p>
</div>
<div id="comment-48986-info" class="comment-info">
<span class="comment-age">(01 Apr '16, 08:21)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="48987"></span>
<div id="comment-48987" class="comment">
<div id="post-48987-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks! I have made the changes and will check in a few days if routing is correct now.</p>
</div>
<div id="comment-48987-info" class="comment-info">
<span class="comment-age">(01 Apr '16, 08:38)</span> <span class="comment-user userinfo">Rody</span>
</div>
</div>
</div>
<div id="comment-tools-48985" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48985-form-container" class="comment-form-container">
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

