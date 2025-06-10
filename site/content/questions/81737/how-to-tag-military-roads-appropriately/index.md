+++
type = "question"
title = "How to tag military roads appropriately"
description = '''In my area there are a few roads through a military area that are tagged inconsistently. Some are &quot;service road&quot; and some are &quot;unclassified road&quot;. I am pretty sure they should be the same thing, but I don&#x27;t know which one. And I don&#x27;t know what other tags I should put there. Some context:  There are...'''
date = "2021-09-14T15:23:00Z"
lastmod = "2021-09-14T19:09:00Z"
weight = 81737
keywords = [ "roads", "tags" ]
aliases = [ "/questions/81737" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag military roads appropriately](/questions/81737/how-to-tag-military-roads-appropriately)

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
<span id="post-81737-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81737-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81737-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In my area there are a few roads through a military area that are tagged inconsistently. Some are "service road" and some are "unclassified road". I am pretty sure they should be the same thing, but I don't know which one. And I don't know what other tags I should put there. Some context:</p>
<ul>
<li>There are a couple roads that lead through the military area. They are somewhat useful connections between surrounding areas.</li>
<li>They are quite nice to ride on. Well maintained and nice forest.</li>
<li>The roads are normally open to non-motorized civilian vehicles or pedestrians.</li>
<li>They are closed to motorized civilian vehicles.</li>
<li>They are obviously used by military vehicles.</li>
<li>Occasionally (rarely) they are closed for the public.</li>
<li>If you use them, you have to follow a couple rules, most notably, you can't leave the roads inside the military area and just go through the forest.</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-roads" rel="tag" title="see questions tagged &#39;roads&#39;">roads</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '21, 15:23</strong></p>
<img src="https://secure.gravatar.com/avatar/39c0e81573717c00f8f89f3525f00e46?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bernhard&#39;s gravatar image" />
<p><span>Bernhard</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bernhard has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '21, 16:48</strong> </span></p>
</div>
</div>
<div id="comments-container-81737" class="comments-container">
&#10;</div>
<div id="comment-tools-81737" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81737-form-container" class="comment-form-container">
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

<span id="81742"></span>

<div id="answer-container-81742" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81742-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81742-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-81742-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It shouldn't make a difference if the roads are inside a military area or not.</p>
<p>First of all the road type (<a href="https://wiki.openstreetmap.org/wiki/Key:highway"><code>highway=*</code></a>) should be selected based on its individual importance or function. It could be <code>tertiary</code>, <code>unclassified</code>, <code>track</code> or even something else. Take a look at the descriptions on the wiki to select the best.</p>
<p>Then you have to set the appropriate <a href="https://wiki.openstreetmap.org/wiki/Key:access">access tags</a>. From your description I guess it could be <code>motor_vehicle=private</code> and <code>access=permissive</code>, meaning the road is generally open to non-motorized traffic but this permission may be revoked. If there are certain times where the roads are closed generally (e.g. at night or Monday-Wednesday) you should apply <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional restrictions</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '21, 16:54</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-81742" class="comments-container">
<span id="81743"></span>
<div id="comment-81743" class="comment">
<div id="post-81743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, thanks, then I guess tertiary seems reasonable. And service seems inappropriate. I mean, it also serves as the service road for the military facilities, but as a civilian, that's not relevant and it's more like a lower grade connecting road.</p>
</div>
<div id="comment-81743-info" class="comment-info">
<span class="comment-age">(14 Sep '21, 19:09)</span> <span class="comment-user userinfo">Bernhard</span>
</div>
</div>
</div>
<div id="comment-tools-81742" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81742-form-container" class="comment-form-container">
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

