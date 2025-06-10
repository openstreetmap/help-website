+++
type = "question"
title = "[closed] What highway type for only bus traffic?"
description = '''A residential road in a town was changed to service by a user. When asked why, the answer was:  - The road now only allow bus traffic.  - And because the wiki says: &quot;residential tag is used on roads that provide access to, or within, residential areas but which are not normally used as through route...'''
date = "2022-07-01T20:08:00Z"
lastmod = "2022-07-05T11:41:00Z"
weight = 84938
keywords = [ "highway" ]
aliases = [ "/questions/84938" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] What highway type for only bus traffic?](/questions/84938/closed-what-highway-type-for-only-bus-traffic)

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
<span id="post-84938-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84938-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84938-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>A residential road in a town was changed to service by a user.</p>
<p>When asked why, the answer was: - The road now only allow bus traffic. - And because the wiki says: "residential tag is used on roads that provide access to, or within, residential areas but which are not normally used as through routes. Most traffic on a residential road will be for the access to, or from, residential properties. Roads carrying through traffic, or non-residential traffic, should instead be tagged with another highway tag"</p>
<p>In this case maybe "residential" is not the best, but I feel "service" is even worse. My suggestion is "unclassfied", but what's the best way tagging this?</p>
<p>Path the changed highway: <a href="https://www.openstreetmap.org/way/62775579">https://www.openstreetmap.org/way/62775579</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-highway" rel="tag" title="see questions tagged &#39;highway&#39;">highway</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Jul '22, 20:08</strong></p>
<img src="https://secure.gravatar.com/avatar/7fbbe44e24bdb695025fddb0879817a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Msiipola&#39;s gravatar image" />
<p><span>Msiipola</span><br />
<span class="score" title="227 reputation points">227</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Msiipola has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '22, 08:11</strong> </span></p>
</div>
</div>
<div id="comments-container-84938" class="comments-container">
&#10;</div>
<div id="comment-tools-84938" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84938-form-container" class="comment-form-container">
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

<span id="84940"></span>

<div id="answer-container-84940" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84940-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Msiipola has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is actually a <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dbusway"><code>highway=busway</code></a> tag for dedicated bus roads, but it is quite rare and as the wiki says should only be used if no pedestrians can travel along (or beside) it. It looks from the aerial imagery that this road may still have sidewalks?</p>
<p>Depending on local rules and signage this might be <code>highway=service</code> + <code>access=no</code> + <code>bus=yes</code>, or possibly the slightly more permissive access tags of <code>motor_vehicle=no</code> + <code>psv=yes</code>.</p>
<p>More info on access rules in general can be found on <a href="https://wiki.openstreetmap.org/wiki/Key:access">this page</a> on the wiki. I think I would probably try to tag the access rules explicitly whatever top level highway tag I settled on, even if it was implied by a busway tag.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Jul '22, 23:23</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-84940" class="comments-container">
<span id="84956"></span>
<div id="comment-84956" class="comment">
<div id="post-84956-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is a tendency to map certain bus only roads as service, but I've always felt this is a artificial in some cases.</p>
</div>
<div id="comment-84956-info" class="comment-info">
<span class="comment-age">(03 Jul '22, 17:07)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="84967"></span>
<div id="comment-84967" class="comment">
<div id="post-84967-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, the road still have sidewalks. The only change was only allow buses on the road. The road is now tagged as "unclassfied".</p>
</div>
<div id="comment-84967-info" class="comment-info">
<span class="comment-age">(04 Jul '22, 17:35)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
<span id="84975"></span>
<div id="comment-84975" class="comment">
<div id="post-84975-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>After some thought the other user changed the road to unclassfied from residential and service. I assume I have to be content with that.</p>
</div>
<div id="comment-84975-info" class="comment-info">
<span class="comment-age">(05 Jul '22, 08:11)</span> <span class="comment-user userinfo">Msiipola</span>
</div>
</div>
<span id="84978"></span>
<div id="comment-84978" class="comment">
<div id="post-84978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You don't <em>have</em> to be content with that, but <code>unclassified</code> is pretty standard for a minor "public" road so it's probably as good a classification as any.</p>
</div>
<div id="comment-84978-info" class="comment-info">
<span class="comment-age">(05 Jul '22, 11:41)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-84940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84940-form-container" class="comment-form-container">
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

