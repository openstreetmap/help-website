+++
type = "question"
title = "How to mark &quot;bottleneck&quot; of road wrt right of way?"
description = '''Sometimes when roads are particularly narrow (especially if that&#x27;s over a short distance because of some obstacle) there are signs marking which direction has right of way. Is there a way to tag this in the map data?'''
date = "2011-09-15T21:03:00Z"
lastmod = "2011-09-16T09:48:00Z"
weight = 7903
keywords = [ "rightsofway", "tagging" ]
aliases = [ "/questions/7903" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to mark "bottleneck" of road wrt right of way?](/questions/7903/how-to-mark-bottleneck-of-road-wrt-right-of-way)

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
<span id="post-7903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7903-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-7903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Sometimes when roads are particularly narrow (especially if that's over a short distance because of some obstacle) there are signs marking which direction has right of way. Is there a way to tag this in the map data?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rightsofway" rel="tag" title="see questions tagged &#39;rightsofway&#39;">rightsofway</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Sep '11, 21:03</strong></p>
<img src="https://secure.gravatar.com/avatar/7ed68aa4a0636ead841954b7aa09daf3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="domob&#39;s gravatar image" />
<p><span>domob</span><br />
<span class="score" title="76 reputation points">76</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="domob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7903" class="comments-container">
&#10;</div>
<div id="comment-tools-7903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7903-form-container" class="comment-form-container">
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

<span id="7906"></span>

<div id="answer-container-7906" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7906-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-7906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have searched the wiki and taginfo and cannot find any existing tag. It seems like a sensible thing to tag so you could make up a tag. It would probably be good to make it match the one way tagging system. Also check on <a href="http://taginfo.openstreetmap.org">http://taginfo.openstreetmap.org</a> to make sure you don't use an existing tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '11, 22:01</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb4d30bb6d40cf9b3644ff4f453e5bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="quantumstate&#39;s gravatar image" />
<p><span>quantumstate</span><br />
<span class="score" title="455 reputation points">455</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="quantumstate has 3 accepted answers">30%</span></p>
</div>
</div>
<div id="comments-container-7906" class="comments-container">
<span id="7915"></span>
<div id="comment-7915" class="comment">
<div id="post-7915-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, my very first idea would be simply something like "oneway=priority" to mean that it's not really oneway but the direction of the way has priority. Or maybe "oneway=no", "oneway:priority=yes" or something. That should be fairly simple.</p>
<p>I haven't looked into the right-of-way proposal with relations so far, but of course we could also do it with that, I suppose. But since I'm rather new to OSM, I don't think I'm the right person to propose new tagging features.</p>
</div>
<div id="comment-7915-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 07:18)</span> <span class="comment-user userinfo">domob</span>
</div>
</div>
<span id="7923"></span>
<div id="comment-7923" class="comment">
<div id="post-7923-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I think it would be best not to use oneway=priority since this might confuse some applications. The oneway:priority=yes idea sounds good.</p>
</div>
<div id="comment-7923-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 09:44)</span> <span class="comment-user userinfo">quantumstate</span>
</div>
</div>
</div>
<div id="comment-tools-7906" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7906-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7904"></span>

<div id="answer-container-7904" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7904-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If its a traffic calming one then in in potlach2 if you create a node in the road and look at transport tags there is a traffic calming one then obstruction type "chocker" (narrowing) could work.If its a narrow piece of road join the wider bit of road with a section of lower grade of road. This doesn't solve the priority issue though</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '11, 21:44</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Sep '11, 21:49</strong> </span></p>
</div>
</div>
<div id="comments-container-7904" class="comments-container">
<span id="7905"></span>
<div id="comment-7905" class="comment">
<div id="post-7905-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. But my question is about marking the <em>right of way</em> in this case (i.e., which direction has priority over the other if two vehicles come at the same time and can not pass simulaneously). At least here in Austria there are sometimes signs marking this. Can I represent that also in OSM, or just that there is a narrow piece with the ways you suggest?</p>
</div>
<div id="comment-7905-info" class="comment-info">
<span class="comment-age">(15 Sep '11, 21:50)</span> <span class="comment-user userinfo">domob</span>
</div>
</div>
<span id="7907"></span>
<div id="comment-7907" class="comment">
<div id="post-7907-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>We have the same in GB for narrow bridges and traffic calming but I don't know of a tag to show who goes first</p>
</div>
<div id="comment-7907-info" class="comment-info">
<span class="comment-age">(15 Sep '11, 22:15)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="7914"></span>
<div id="comment-7914" class="comment">
<div id="post-7914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Narrow parts of a road are not always the result of traffic calming. There is a more suitable tag called <a href="http://wiki.openstreetmap.org/wiki/Key:narrow">narrow=yes</a>.</p>
</div>
<div id="comment-7914-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 06:45)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="7924"></span>
<div id="comment-7924" class="comment">
<div id="post-7924-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>All good OSM editors shall be able to modify the tag if the way is inverted, e.g. "oneway=yes" becomes a "oneway=-1", "<em>:left" becomes "</em>:right", "<em>:forward" -&gt; "</em>:backward". Perhaps a "priority:forward=yes" ? Or a "traffic_calming:forward=choker" ? You should check around in the wiki, propose something and/or talk on the dedicated mailing list tagging@<a href="http://openstreetmap.org">openstreetmap.org</a> . At the end, it is important to document the consensus on the wiki.</p>
</div>
<div id="comment-7924-info" class="comment-info">
<span class="comment-age">(16 Sep '11, 09:48)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-7904" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7904-form-container" class="comment-form-container">
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

