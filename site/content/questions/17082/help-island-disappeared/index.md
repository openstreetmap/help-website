+++
type = "question"
title = "help: island disappeared"
description = '''https://www.openstreetmap.org/?lat=35.10685&amp;amp;lon=-81.02689&amp;amp;zoom=17&amp;amp;layers=M There was an island displaying in this spot until just recently. Not sure what happened to it. You can see it when in editing mode but not in Mapnik anymore. I tried adding place=island (which wasn&#x27;t there before) ...'''
date = "2012-10-22T05:24:00Z"
lastmod = "2012-10-22T23:01:00Z"
weight = 17082
keywords = [ "island" ]
aliases = [ "/questions/17082" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [help: island disappeared](/questions/17082/help-island-disappeared)

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
<span id="post-17082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17082-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-17082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><a href="https://www.openstreetmap.org/?lat=35.10685&amp;lon=-81.02689&amp;zoom=17&amp;layers=M">https://www.openstreetmap.org/?lat=35.10685&amp;lon=-81.02689&amp;zoom=17&amp;layers=M</a></p>
<p>There was an island displaying in this spot until just recently. Not sure what happened to it. You can see it when in editing mode but not in Mapnik anymore. I tried adding place=island (which wasn't there before) but that didn't fix it. Also noticed that there was a multipolygon tag on it but it didn't say inner or outer so I added outer (since the nearby coast around the same lake had outer too). Still doesn't show up even when rendering the tile using /dirty. Why did it disappear and how do I get it to display properly again? Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-island" rel="tag" title="see questions tagged &#39;island&#39;">island</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '12, 05:24</strong></p>
<img src="https://secure.gravatar.com/avatar/228a09e620f374c61a25e546d76bc6a0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gopanthers&#39;s gravatar image" />
<p><span>gopanthers</span><br />
<span class="score" title="366 reputation points">366</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gopanthers has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-17082" class="comments-container">
&#10;</div>
<div id="comment-tools-17082" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17082-form-container" class="comment-form-container">
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

<span id="17090"></span>

<div id="answer-container-17090" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17090-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gopanthers has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The lake is a multipolygon. Looking at the <a href="https://www.openstreetmap.org/browse/relation/299167">history</a>, it's possible to see that one of the members previously was:</p>
<p>Way Copperhead Island (42890481) as inner</p>
<p>whereas now that's no longer there - this is why there's no longer a "hole" in the lake for the island. The <a href="https://www.openstreetmap.org/browse/way/42890481">way</a> for the island still exists, so add it back as a member of the lake <a href="https://www.openstreetmap.org/browse/relation/299167">relation</a> with type=inner (in addition to the other relation that it is already part of) and it should be fixed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Oct '12, 09:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-17090" class="comments-container">
<span id="17113"></span>
<div id="comment-17113" class="comment">
<div id="post-17113-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That fixed it. Thanks.</p>
<p>I don't want to hijack my own question but I had a lot of trouble following the edit history of a particular way. You pointed me towards <a href="https://www.openstreetmap.org/browse/way/42890481">https://www.openstreetmap.org/browse/way/42890481</a> which is the way that creates the border of the island, but hitting history gave me tons of unrelated edits that included, but were much larger than this tiny island. So when something gets messed up, what's the easiest way to see the edits done only to that way or node so you can figure out where it want wrong?</p>
<p>Thanks again.</p>
</div>
<div id="comment-17113-info" class="comment-info">
<span class="comment-age">(22 Oct '12, 22:10)</span> <span class="comment-user userinfo">gopanthers</span>
</div>
</div>
<span id="17114"></span>
<div id="comment-17114" class="comment">
<div id="post-17114-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you're looking at the browse page for an object, in this case:</p>
<p><a href="https://www.openstreetmap.org/browse/way/42890481">https://www.openstreetmap.org/browse/way/42890481</a></p>
<p>Down at the bottom of the screen there will be a "view history" option. That will show in this case:</p>
<p><a href="https://www.openstreetmap.org/browse/way/42890481/history">https://www.openstreetmap.org/browse/way/42890481/history</a></p>
<p>Ignore the "history" tab at the top - that will show all recent edits in the area, not just to the item in question.</p>
<p>If you're editing using Potlatch 2, you can click "advanced" at the bottom left and double-click on the way number at the top left to see a brief list of changes to the item. Clicking more info on that screen takes you to the <a href="https://www.openstreetmap.org/browse/way/42890481">browse page</a>.</p>
<p>The "view history" option works most of the time; the exception is when there's an awful lot of history, and you'll instead get a message "Sorry, the data for the relation with the id XYZ, took too long to retrieve".</p>
</div>
<div id="comment-17114-info" class="comment-info">
<span class="comment-age">(22 Oct '12, 23:01)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-17090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17090-form-container" class="comment-form-container">
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

