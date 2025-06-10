+++
type = "question"
title = "Quality condition of the paths"
description = '''Hi, Is there a way to qualify the quality of the paths? For example &quot;avoid after a heavy rain because too muddy&quot; or &quot;beware several fallen trunks requiring the carrying of the bicycle&quot; or &quot;many deep ruts due to forestry machinery&quot; This would prevent a nice hike from turning into a nightmare (like it...'''
date = "2022-05-06T12:46:00Z"
lastmod = "2022-05-06T20:19:00Z"
weight = 84380
keywords = [ "paths" ]
aliases = [ "/questions/84380" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Quality condition of the paths](/questions/84380/quality-condition-of-the-paths)

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
<span id="post-84380-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84380-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84380-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>Is there a way to qualify the quality of the paths? For example "avoid after a heavy rain because too muddy" or "beware several fallen trunks requiring the carrying of the bicycle" or "many deep ruts due to forestry machinery"</p>
<p>This would prevent a nice hike from turning into a nightmare (like it happened to me).</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-paths" rel="tag" title="see questions tagged &#39;paths&#39;">paths</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 May '22, 12:46</strong></p>
<img src="https://secure.gravatar.com/avatar/a3a0bd5441316e7389e839847fe513e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VDZD&#39;s gravatar image" />
<p><span>VDZD</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VDZD has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84380" class="comments-container">
&#10;</div>
<div id="comment-tools-84380" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84380-form-container" class="comment-form-container">
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

<span id="84383"></span>

<div id="answer-container-84383" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84383-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84383-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-84383-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>First of all you can always add a <a href="https://wiki.openstreetmap.org/wiki/Key:note"><code>note</code></a> on a way to add such information. The use of this tag by data consumers is limited, though. We have a series of keys that define attributes of physical accessibility that get recognized by renderers and routers (at least by those dedicated to hiking/cycling/...). The most suitable are:<br />
<a href="https://wiki.openstreetmap.org/wiki/Key:surface"><code>surface</code></a><br />
<a href="https://wiki.openstreetmap.org/wiki/Key:smoothness"><code>smoothness</code></a><br />
<a href="https://wiki.openstreetmap.org/wiki/Key:sac_scale"><code>sac_scale</code></a><br />
<a href="https://wiki.openstreetmap.org/wiki/Key:mtb:scale"><code>mtb_scale</code></a><br />
<a href="https://wiki.openstreetmap.org/wiki/Key:trail_visibility"><code>trail_visibility</code></a><br />
<a href="https://wiki.openstreetmap.org/wiki/Key:tracktype"><code>tracktype</code></a> (for highway=track)</p>
<p>These are all somewhat subjective attributes but try to stick to the given examples and try to find a tagging that applies for most of the year and normal weather conditions. If has rained you can avoid paths with <code>surface=ground</code> but the way is not generally <code>smoothness=very_horrible</code> because of that.</p>
<p>If fallen trunks are left permanently you can consider that in your rating. If they just have not been removed yet after the last storm please leave them out. We don't maintain live data and some applications only update their databases every several months.</p>
<p>If there are actual physical permanent obstacles blocking the way you could also add one of the <a href="https://wiki.openstreetmap.org/wiki/Key:barrier">barriers</a> to the path.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '22, 15:08</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '22, 15:08</strong> </span></p>
</div>
</div>
<div id="comments-container-84383" class="comments-container">
<span id="84390"></span>
<div id="comment-84390" class="comment">
<div id="post-84390-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Permanent fallen logs can usually be tagged as <a href="https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dlog"><code>barrier=log</code></a>.</p>
</div>
<div id="comment-84390-info" class="comment-info">
<span class="comment-age">(06 May '22, 20:19)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
</div>
<div id="comment-tools-84383" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84383-form-container" class="comment-form-container">
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

