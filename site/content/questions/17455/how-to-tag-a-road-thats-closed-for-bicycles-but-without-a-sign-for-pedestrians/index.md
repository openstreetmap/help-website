+++
type = "question"
title = "How to tag a road thats closed for bicycles, but without a sign for pedestrians ?"
description = '''I came across a tagging problem. How to tag a road thats closed (by sign) for bicycles and mopeds (C15) but not for pedestrians (C16) ? Itsnt logic though, at the end is farmland and a track through woodlands ? A crossing way has a signs with added no agricultural traffic (C9) but not a sign against...'''
date = "2012-11-04T13:16:00Z"
lastmod = "2012-11-04T20:09:00Z"
weight = 17455
keywords = [ "pedestrians", "tag", "traffic-rules", "law" ]
aliases = [ "/questions/17455" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag a road thats closed for bicycles, but without a sign for pedestrians ?](/questions/17455/how-to-tag-a-road-thats-closed-for-bicycles-but-without-a-sign-for-pedestrians)

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
<span id="post-17455-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17455-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-17455-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I came across a tagging problem. How to tag a road thats closed (by sign) for bicycles and mopeds (C15) but not for pedestrians (C16) ? Itsnt logic though, at the end is farmland and a track through woodlands ? A crossing way has a signs with added no agricultural traffic (C9) but not a sign against pedestrians. Leave pedestrians unset ? IMHO its not right. Theres no rule against walking alongside the road, it might be unpleasant but I wont to go to the farmland. So I would tag pedestrians allowed, sidewalks none. Any ideas ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrians" rel="tag" title="see questions tagged &#39;pedestrians&#39;">pedestrians</span> <span class="post-tag tag-link-tag" rel="tag" title="see questions tagged &#39;tag&#39;">tag</span> <span class="post-tag tag-link-traffic-rules" rel="tag" title="see questions tagged &#39;traffic-rules&#39;">traffic-rules</span> <span class="post-tag tag-link-law" rel="tag" title="see questions tagged &#39;law&#39;">law</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '12, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-17455" class="comments-container">
&#10;</div>
<div id="comment-tools-17455" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17455-form-container" class="comment-form-container">
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

<span id="17458"></span>

<div id="answer-container-17458" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17458-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17458-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17458-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Hendrikklaas has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just add the appropriate <a href="http://wiki.openstreetmap.org/wiki/Key:access">access tags</a> as described on the <a href="http://wiki.openstreetmap.org/wiki/Road_signs_in_the_United_Kingdom">road signs wiki page</a>. If there is no sign forbidding pedestrians then you don't have to add any further tag because <em>foot=yes</em> is the <a href="http://wiki.openstreetmap.org/wiki/OSM_tags_for_routing/Access-Restrictions#Default">default</a> for most way types.</p>
<p>In your specific case a <em>vehicle=no</em> seems sufficient as it forbids bicycles, moped and any other motorized vehicle.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Nov '12, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-17458" class="comments-container">
<span id="17470"></span>
<div id="comment-17470" class="comment">
<div id="post-17470-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry Scai, but I didnt mention that motorized vehicles (cars) were allowed to go, so walking alongside it could not be very pleasant. Thats just the puzzle, Id love to walk and will go without a sign 'dont go' or a prohibition order.</p>
</div>
<div id="comment-17470-info" class="comment-info">
<span class="comment-age">(04 Nov '12, 19:11)</span> <span class="comment-user userinfo">Hendrikklaas</span>
</div>
</div>
<span id="17473"></span>
<div id="comment-17473" class="comment">
<div id="post-17473-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>So use <em>bicycle=no</em> and <em>moped=no</em>, I don't see the problem here. Whether walking is pleasant or not is totally irrelevant as long as it is legally allowed.</p>
</div>
<div id="comment-17473-info" class="comment-info">
<span class="comment-age">(04 Nov '12, 20:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17458" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17458-form-container" class="comment-form-container">
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

