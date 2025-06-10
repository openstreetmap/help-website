+++
type = "question"
title = "ID User: need to merge two relations (I think)"
description = '''In Essex England, there is a local walking route named the &#x27;John Ray Way&#x27; between Braintree and Witham. I noticed that someone had assigned a &#x27;John Ray Way&#x27; relation at the Braintree end, and there was another &#x27;John Ray Way&#x27; relation at the Witham end. So I decided to fill in the gaps, assigning &#x27;Jo...'''
date = "2019-12-16T11:55:00Z"
lastmod = "2019-12-16T17:03:00Z"
weight = 72115
keywords = [ "ideditor", "route", "relations" ]
aliases = [ "/questions/72115" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [ID User: need to merge two relations (I think)](/questions/72115/id-user-need-to-merge-two-relations-i-think)

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
<span id="post-72115-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72115-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72115-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Essex England, there is a local walking route named the 'John Ray Way' between Braintree and Witham.</p>
<p>I noticed that someone had assigned a 'John Ray Way' relation at the Braintree end, and there was another 'John Ray Way' relation at the Witham end. So I decided to fill in the gaps, assigning 'John Ray Way' relation to all the paths and roads in between, according to the Essex Highways map: <a href="https://www.essexhighways.org/uploads/files/john_ray_walk.pdf">https://www.essexhighways.org/uploads/files/john_ray_walk.pdf</a></p>
<p>Then I found that maybe there is a problem, because the relation number at the Witham end is 593557, but the relation number at the Braintree end is 2871519 (from hiking.waymarkedtrails.org) ... and I have no idea what the relation ID is for the sections I modified in the middle !?!</p>
<p>I am an ID user. I don't use Potlatch or JOSM or native HTML.</p>
<p>How to fix this situation, so there is a single relation for the entire route (14.5km) ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Dec '19, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/469bf85c2e48ad6395d931ff7e805b4c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="IanG&#39;s gravatar image" />
<p><span>IanG</span><br />
<span class="score" title="41 reputation points">41</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="IanG has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72115" class="comments-container">
&#10;</div>
<div id="comment-tools-72115" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72115-form-container" class="comment-form-container">
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

<span id="72117"></span>

<div id="answer-container-72117" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-72117-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72117-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72117-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>After a bit of discussion on IRC we think in iD you'd have to transfer ways from one relation to the other until they were all in one relation (so select a way, add it to one relation then remove it from the other) and once the one relation is empty it will probably get deleted.</p>
<p>In JOSM (which is what I tend to use for relation related stuff) it is possible to select all the members in one relation at once to make it easier to add to another, and once that is done you can delete one of the relations. I can do this for you if you want. I'd probably keep the lower numbered relation just because it is lower, though I guess that is a personal quirk.</p>
<p>I notice in some places you've added name=John Ray Way to the member ways; I think it should only be a tag on the relation and not the member ways (some of which will have their own names, and some that won't).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Dec '19, 14:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Dec '19, 14:18</strong> </span></p>
</div>
</div>
<div id="comments-container-72117" class="comments-container">
<span id="72119"></span>
<div id="comment-72119" class="comment">
<div id="post-72119-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the quick response, Ed :-)</p>
<p>I would appreciate it if you made the change in JOSM on my behalf. Because both Relations have identical names, I don't actually know how to switch from one to the other in ID !</p>
<p>By all means, go with the lower numbered relation.</p>
<p>All the name=John Ray Way should also be removed - feel free to do that also.</p>
<p>As an aside, I haven't walked this path yet, although do I plan to do so, and will do a bunch more updating of OSM at that time.</p>
</div>
<div id="comment-72119-info" class="comment-info">
<span class="comment-age">(16 Dec '19, 16:16)</span> <span class="comment-user userinfo">IanG</span>
</div>
</div>
<span id="72120"></span>
<div id="comment-72120" class="comment">
<div id="post-72120-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Done in <a href="https://www.openstreetmap.org/changeset/78484433">https://www.openstreetmap.org/changeset/78484433</a> (I also filled in the gap through Cressing Temple's car park).</p>
<p>I suspect it will be an enjoyable walk. Some years ago I cycled Witham to Braintree to fill in some of cycle route 16 in OSM that was missing and that was an enjoyable day.</p>
</div>
<div id="comment-72120-info" class="comment-info">
<span class="comment-age">(16 Dec '19, 17:03)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-72117" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72117-form-container" class="comment-form-container">
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

