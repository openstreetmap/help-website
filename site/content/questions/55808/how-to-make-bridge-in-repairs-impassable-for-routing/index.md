+++
type = "question"
title = "How to make bridge in repairs impassable for routing?"
description = '''I read this and this question. I tried the suggestions (changed highway=pedestrian to construction=pedestrian + highway=construction + access=no) and still when I go to openstreetmap.org both of the routing options show the bridge as passable (on foot). How to make it so that people wouldn&#x27;t get dir...'''
date = "2017-04-24T13:33:00Z"
lastmod = "2017-04-25T00:55:00Z"
weight = 55808
keywords = [ "repair", "construction", "routing", "bridge" ]
aliases = [ "/questions/55808" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to make bridge in repairs impassable for routing?](/questions/55808/how-to-make-bridge-in-repairs-impassable-for-routing)

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
<span id="post-55808-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55808-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55808-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I read <a href="/questions/42891/damaged-bridge-and-footpath-closed-until-repaired">this</a> and <a href="/questions/50247/bridge-under-repair">this</a> question. I tried the suggestions (changed <code>highway=pedestrian</code> to <code>construction=pedestrian</code> + <code>highway=construction</code> + <code>access=no</code>) and still when I go to openstreetmap.org both of the routing options <a href="https://www.openstreetmap.org/directions?engine=mapzen_foot&amp;route=58.38071%2C26.72510%3B58.38101%2C26.72648#map=19/58.38081/26.72611">show</a> the <a href="https://www.openstreetmap.org/way/29420432">bridge</a> as passable (on foot). How to make it so that people wouldn't get directed to cross an unusable bridge?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-repair" rel="tag" title="see questions tagged &#39;repair&#39;">repair</span> <span class="post-tag tag-link-construction" rel="tag" title="see questions tagged &#39;construction&#39;">construction</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Apr '17, 13:33</strong></p>
<img src="https://secure.gravatar.com/avatar/d2d2dc10f2131b64775c01ef05138be8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CharlieHotelRomeo&#39;s gravatar image" />
<p><span>CharlieHotel...</span><br />
<span class="score" title="61 reputation points">61</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CharlieHotelRomeo has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '17, 13:36</strong> </span></p>
</div>
</div>
<div id="comments-container-55808" class="comments-container">
&#10;</div>
<div id="comment-tools-55808" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55808-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="55809"></span>

<div id="answer-container-55809" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55809-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55809-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55809-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Keep in mind that routing engines take some time to update their data and re-calculate their routing graph. Your changes are not immediately reflected by routers although the renderer already shows them.</p>
<p>Also I think the current tagging isn't quite clear. There is an access=no tag but there is also a <em>more specific</em> foot=yes tag. <em>I think</em> some routers still allow foot routing along highway=construction <em>if</em> foot=yes is present. The same may apply to bicycle routing. Therefore I would remove the foot=yes and bicycle=yes tags and re-add them as soon as the construction has finished.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '17, 13:41</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Apr '17, 13:42</strong> </span></p>
</div>
</div>
<div id="comments-container-55809" class="comments-container">
<span id="55811"></span>
<div id="comment-55811" class="comment">
<div id="post-55811-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks I'll try that and update this when there's any change.</p>
</div>
<div id="comment-55811-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 13:45)</span> <span class="comment-user userinfo">CharlieHotel...</span>
</div>
</div>
</div>
<div id="comment-tools-55809" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55809-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55819"></span>

<div id="answer-container-55819" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55819-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>CharlieHotel, If a construction only takes a few days don't tag it at all, its to short to be practical. A router should start to recalculate as soon as you leave the original signed route. So even when you did not notice the official D tour signs "follow 3/D" until your back on the old route or way, the router will guide you perfectly to the old / original destination if the road/bridge ahead is signed as closed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Apr '17, 14:40</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-55819" class="comments-container">
<span id="55823"></span>
<div id="comment-55823" class="comment">
<div id="post-55823-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes I read that from elsewhere too. But in this instance the repairs are said to take until some month in autumn. So I thought a bit less than half a year should be enough to warrant the edit.</p>
</div>
<div id="comment-55823-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 15:28)</span> <span class="comment-user userinfo">CharlieHotel...</span>
</div>
</div>
<span id="55826"></span>
<div id="comment-55826" class="comment">
<div id="post-55826-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Then just do it. But remember to solve the construction tags later as well.</p>
</div>
<div id="comment-55826-info" class="comment-info">
<span class="comment-age">(24 Apr '17, 15:48)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
</div>
<div id="comment-tools-55819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55819-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55840"></span>

<div id="answer-container-55840" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55840-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55840-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-55840-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://www.openstreetmap.org/way/36167267">This bridge</a> was damaged in a flood on 29 October 2015 and is in the process of being replaced with a new bridge. To stop the routing engines I found I had to explicitly set each mode of transport to no. I.e. access=no, foot=no, bicycle=no, horse=no, motor_vehicle=no, cycleway=no, etc. This caused the section of road beyond the bridge to become a routing island in overpass turbo. Even though an alternative access route for residents and service vehicles existed across private land because that alternative route had private access restrictions on it, the isolated road remained a routing island.</p>
<p>Perhaps you need to explicitly tag foot=no to prevent the pedestrian routing.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Apr '17, 00:55</strong></p>
<img src="https://secure.gravatar.com/avatar/1a623cf4b5df74bee1b91d0c21736921?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Huttite&#39;s gravatar image" />
<p><span>Huttite</span><br />
<span class="score" title="560 reputation points">560</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Huttite has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-55840" class="comments-container">
&#10;</div>
<div id="comment-tools-55840" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55840-form-container" class="comment-form-container">
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

