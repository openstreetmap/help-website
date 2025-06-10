+++
type = "question"
title = "Bus route is not visible after I have completed it."
description = '''I have finished adding a bus route in Biên Hòa on the in-browser editor of OSM, but the bus route is not shown in red, whereas the bus lines in nearby Hồ Chí Minh City are clearly visible. It doesn&#x27;t show on the map, but browsing the relation makes it visible in orange. But the routemaster isn&#x27;t vie...'''
date = "2021-08-04T03:32:00Z"
lastmod = "2021-08-04T16:17:00Z"
weight = 81184
keywords = [ "route" ]
aliases = [ "/questions/81184" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bus route is not visible after I have completed it.](/questions/81184/bus-route-is-not-visible-after-i-have-completed-it)

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
<span id="post-81184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81184-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have finished adding a bus route in Biên Hòa on the in-browser editor of OSM, but the bus route is not shown in red, whereas the bus lines in nearby Hồ Chí Minh City are clearly visible.</p>
<p>It doesn't show on the map, but browsing the <a href="https://www.openstreetmap.org/relation/13051180">relation</a> makes it visible in orange. But the <a href="https://www.openstreetmap.org/relation/13051411">routemaster</a> isn't viewable at all.</p>
<p>Can someone fix this?</p>
<p>Regards.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Aug '21, 03:32</strong></p>
<img src="https://secure.gravatar.com/avatar/93255c756b969944b0b9bbf271a33813?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turtle-bienhoa&#39;s gravatar image" />
<p><span>turtle-bienhoa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turtle-bienhoa has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81184" class="comments-container">
&#10;</div>
<div id="comment-tools-81184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81184-form-container" class="comment-form-container">
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

<span id="81189"></span>

<div id="answer-container-81189" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81189-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81189-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81189-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I'm not entirely sure this is the reason for the not rendering but the route modeling does not follow the defined scheme.</p>
<p>In the relation you have added all the road segments which is fine. In PTV2 additionally to the road you can also add stops and platforms (have a look at the <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Dbus#Members">Wiki</a> again). Those need to get role names (e.g. <code>stop</code> or <code>platform</code>). In your relation you also added a building and a bus station to the route without assigning roles. That might have confused the renderer.</p>
<p>Try correcting the role assignment and also <a href="https://wiki.openstreetmap.org/wiki/Tag:route%3Dbus#Order_of_members">the sequence</a>. You first have to add all stop positions and platforms, only then the road segments.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '21, 10:14</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81189" class="comments-container">
<span id="81191"></span>
<div id="comment-81191" class="comment">
<div id="post-81191-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which renderer or layer are you referring to? As far as I know the standard layer does not display bus routes. The public transport layer does, but it updates much less frequently, so you may need to wait.</p>
<p>The tagging of the master route looks odd (probably not affecting rendering though). You have route_master=1 instead of =bus, and I think route=bus is not needed.</p>
</div>
<div id="comment-81191-info" class="comment-info">
<span class="comment-age">(04 Aug '21, 10:42)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="81194"></span>
<div id="comment-81194" class="comment">
<div id="post-81194-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In my experience the public transport map (layers=O) picks up changes quite fast (minutes). At least it did when I was heavily mapping bus routes one and a half years ago.</p>
</div>
<div id="comment-81194-info" class="comment-info">
<span class="comment-age">(04 Aug '21, 12:06)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
</div>
<div id="comment-tools-81189" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81189-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="81199"></span>

<div id="answer-container-81199" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81199-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81199-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81199-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have fixed the master route. I have added some bus stops along the way (the ones I know).</p>
<p>If possible, can a veteran in creating bus routes fix this?</p>
<p>Thank you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Aug '21, 15:46</strong></p>
<img src="https://secure.gravatar.com/avatar/93255c756b969944b0b9bbf271a33813?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turtle-bienhoa&#39;s gravatar image" />
<p><span>turtle-bienhoa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turtle-bienhoa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Aug '21, 15:46</strong> </span></p>
</div>
</div>
<div id="comments-container-81199" class="comments-container">
<span id="81201"></span>
<div id="comment-81201" class="comment">
<div id="post-81201-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Edit: It is showing now. Thanks a lot!</p>
</div>
<div id="comment-81201-info" class="comment-info">
<span class="comment-age">(04 Aug '21, 16:17)</span> <span class="comment-user userinfo">turtle-bienhoa</span>
</div>
</div>
</div>
<div id="comment-tools-81199" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81199-form-container" class="comment-form-container">
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

