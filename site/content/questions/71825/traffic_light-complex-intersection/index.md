+++
type = "question"
title = "[traffic_light] Complex intersection"
description = '''Hi, Which one is the best between this picture, perheaps something else, I don&#x27;t know :/ Complex:  Simple:  Thank for the help,'''
date = "2019-11-25T22:18:00Z"
lastmod = "2019-11-26T11:58:00Z"
weight = 71825
keywords = [ "intersection", "traffic_lights", "complex" ]
aliases = [ "/questions/71825" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[traffic_light\] Complex intersection](/questions/71825/traffic_light-complex-intersection)

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
<span id="post-71825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71825-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-71825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Which one is the best between this picture, perheaps something else, I don't know :/</p>
<p>Complex: <img src="/upfiles/Complex.PNG" alt="alt text" /></p>
<p>Simple: <img src="/upfiles/Simple.PNG" alt="alt text" /></p>
<p>Thank for the help,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-intersection" rel="tag" title="see questions tagged &#39;intersection&#39;">intersection</span> <span class="post-tag tag-link-traffic_lights" rel="tag" title="see questions tagged &#39;traffic_lights&#39;">traffic_lights</span> <span class="post-tag tag-link-complex" rel="tag" title="see questions tagged &#39;complex&#39;">complex</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '19, 22:18</strong></p>
<img src="https://secure.gravatar.com/avatar/8ddbdd9e0573ad084e34ada81c6a793b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Winultimate&#39;s gravatar image" />
<p><span>Winultimate</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Winultimate has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-71825" class="comments-container">
&#10;</div>
<div id="comment-tools-71825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71825-form-container" class="comment-form-container">
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

<span id="71826"></span>

<div id="answer-container-71826" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-71826-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-71826-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-71826-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Winultimate has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Winultimate... in these pictures, it looks like each individual lane of traffic has been drawn as a separate way (line). This is probably incorrect mapping.</p>
<p>Normally we would draw a single way to represent each entire avenue. (Or, in the case of a divided highway, also known as a dual carriagway, we would draw two ways, one representing the traffic going in each direction.)</p>
<p>The turn behavior of individual lanes can optionally be indicated with additional tags added on the avenue. You can read some documentation of this at <a href="https://wiki.openstreetmap.org/wiki/Key:turn#Turning_indications_per_lane">https://wiki.openstreetmap.org/wiki/Key:turn#Turning_indications_per_lane</a>.</p>
<p>So the short answer is that, best I can tell, neither of the pictures look correct.</p>
<p>Before you can map the intersection correctly, the roads themselves need to be fixed. Then I believe you would be able to use a single intersection point and a single traffic light, like in the bottom picture.</p>
<p>Good luck, J</p>
<p>PS -- Here's an example of a multi-lane intersection that's mapped correctly: <a href="https://www.openstreetmap.org/#map=19/45.18025/0.74665">https://www.openstreetmap.org/#map=19/45.18025/0.74665</a>. Note that there are multiple lanes including turn lanes, but the only turn lane that's drawn separately has a physical separation from the other traffic. (The roads at this intersection do not have any special tags describing the turn lanes; that's useful but not required.)</p>
<p>I think that before you drew in the individual lanes in changeset 77544873, this intersection of Poudrière/Leclerc/Allende/Tassigny was correctly mapped. So probably this changeset should be reverted.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '19, 22:56</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Nov '19, 00:31</strong> </span></p>
</div>
</div>
<div id="comments-container-71826" class="comments-container">
<span id="71833"></span>
<div id="comment-71833" class="comment">
<div id="post-71833-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree, mapping each individual lane as a separate way is wrong, except if there is a physical separation. For mapping roads with multiple lanes the <a href="https://wiki.openstreetmap.org/wiki/Lanes"><code>lane</code></a> key should be used instead, together with <code>turn:lanes</code>.</p>
</div>
<div id="comment-71833-info" class="comment-info">
<span class="comment-age">(26 Nov '19, 09:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="71838"></span>
<div id="comment-71838" class="comment">
<div id="post-71838-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks you for the answer ! Sorry for this, I corrected my changeset to rectify this intersection.</p>
</div>
<div id="comment-71838-info" class="comment-info">
<span class="comment-age">(26 Nov '19, 11:58)</span> <span class="comment-user userinfo">Winultimate</span>
</div>
</div>
</div>
<div id="comment-tools-71826" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-71826-form-container" class="comment-form-container">
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

