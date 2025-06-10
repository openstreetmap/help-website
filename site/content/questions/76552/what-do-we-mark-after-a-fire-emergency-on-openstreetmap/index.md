+++
type = "question"
title = "What do we mark after a fire emergency, on Openstreetmap?"
description = '''Right now there are unfortunately numerous fires that have threatened or burned up cities here in Oregon. https://www.msn.com/en-us/news/us/oregon-fire-evacuation-map-update-as-83-000-medford-residents-forced-to-flee-homes/ar-BB18RvEu?ocid=uxbndlbing With many businesses and homes that have building...'''
date = "2020-09-11T04:31:00Z"
lastmod = "2020-09-11T20:55:00Z"
weight = 76552
keywords = [ "fire", "nodes", "removal" ]
aliases = [ "/questions/76552" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What do we mark after a fire emergency, on Openstreetmap?](/questions/76552/what-do-we-mark-after-a-fire-emergency-on-openstreetmap)

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
<span id="post-76552-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76552-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76552-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Right now there are unfortunately numerous fires that have threatened or burned up cities here in Oregon. <a href="https://www.msn.com/en-us/news/us/oregon-fire-evacuation-map-update-as-83-000-medford-residents-forced-to-flee-homes/ar-BB18RvEu?ocid=uxbndlbing">https://www.msn.com/en-us/news/us/oregon-fire-evacuation-map-update-as-83-000-medford-residents-forced-to-flee-homes/ar-BB18RvEu?ocid=uxbndlbing</a></p>
<p>With many businesses and homes that have buildings burned down, closed, or both, I wonder what is the best way we can best notify everyone relying on Openstreetmap/Osmand. Is there a way one can mark temporarily closed for an entire area? And is there a tag that can be added as burned down vs permanently deleting a node or building area? :(</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fire" rel="tag" title="see questions tagged &#39;fire&#39;">fire</span> <span class="post-tag tag-link-nodes" rel="tag" title="see questions tagged &#39;nodes&#39;">nodes</span> <span class="post-tag tag-link-removal" rel="tag" title="see questions tagged &#39;removal&#39;">removal</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Sep '20, 04:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ff5b5dcb43315c9b07de2d9261ad2d2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="123maps&#39;s gravatar image" />
<p><span>123maps</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="123maps has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76552" class="comments-container">
&#10;</div>
<div id="comment-tools-76552" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76552-form-container" class="comment-form-container">
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

<span id="76559"></span>

<div id="answer-container-76559" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76559-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76559-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-76559-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="123maps has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><strong>Destroyed buildings:</strong> Use a lifecycle prefix on the <code>building=*</code> tag, as InsertUser says.</p>
<p><strong>Amenities (,shops, etc) co-tagged directly on the building way:</strong> Delete the amenity-specific tags, optionally add a lifecycle prefix on the main tag (eg <code>destroyed:amenity=restaurant</code>). Consider tagging old_name=* -- if people still refer to the site by the previous name.</p>
<p><strong>Amenities etc mapped as a node inside a destroyed building:</strong> Delete node or use lifecycle prefix on the main tag.</p>
<p>(Possible edge case: Some amenities, churches for example, may continue to function in ad-hoc accommodations on the previous site.)</p>
<p>~~~</p>
<p>As far as I know, there's no standard way to mark a temporary closure for an entire area, but you can close the roads in that area...</p>
<p><strong>Closed road you expect to reopen within a few weeks:</strong> Don't change road access, possibly add a note or fixme explaining the temporary closure and asking for a resurvey to confirm the re-opening.</p>
<p><strong>Closed road you expect to reopen after several weeks:</strong> Add a <a href="https://wiki.openstreetmap.org/wiki/Conditional_restrictions">conditional access</a> tag like <code>conditional:access=no @ (2020 Sep 1-2020 Nov 15)</code>. This is an imperfect solution for two reasons -- First, data consumers will need to specifically be looking for the conditional access tag, and many of them do not. Second, you have to choose a re-opening date... but don't worry if it's not exactly right, you can remove it if you overestimated the length of the closure and revise it if you underestimated.</p>
<p><strong>Indefinitely closed road:</strong> Tag <code>access=no</code> and add a fixme asking for resurvey.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '20, 20:55</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Sep '20, 20:56</strong> </span></p>
</div>
</div>
<div id="comments-container-76559" class="comments-container">
&#10;</div>
<div id="comment-tools-76559" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76559-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76555"></span>

<div id="answer-container-76555" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76555-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76555-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76555-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Short term closures <a href="https://wiki.openstreetmap.org/wiki/Good_practice#Don.27t_map_temporary_events_and_temporary_features">aren't normally mapped</a> in OSM.</p>
<p>Recently destroyed buildings etc. can be tagged with a <a href="https://wiki.openstreetmap.org/wiki/Lifecycle_prefix">lifecycle prefix</a> like <code>destroyed:</code> or <code>ruins:</code> as appropriate. If all traces of an object have been removed they should normally be deleted as they are no longer verifiable on the ground, however if they are still shown in aerial imagery it is usually acceptable to leave them with a <code>destroyed:</code> or <code>demolished:</code> prefix until the next update.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Sep '20, 10:04</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-76555" class="comments-container">
&#10;</div>
<div id="comment-tools-76555" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76555-form-container" class="comment-form-container">
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

