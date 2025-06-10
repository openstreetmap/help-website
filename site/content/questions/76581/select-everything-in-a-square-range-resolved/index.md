+++
type = "question"
title = "Select everything in a square range [RESOLVED]"
description = '''Searched a fair bit but can&#x27;t seem to find the answer to how to select everything within a range. For instance there&#x27;s a building, outside walk around, multiple layers, made up of hundreds of drawing points. I&#x27;d like to pick it up and move it as seeming to be in the wrong spot (drawn over the slante...'''
date = "2020-09-14T11:42:00Z"
lastmod = "2020-09-16T00:29:00Z"
weight = 76581
keywords = [ "josm", "selection", "moving" ]
aliases = [ "/questions/76581" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Select everything in a square range \[RESOLVED\]](/questions/76581/select-everything-in-a-square-range-resolved)

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
<span id="post-76581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76581-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Searched a fair bit but can't seem to find the answer to how to select everything within a range. For instance there's a building, outside walk around, multiple layers, made up of hundreds of drawing points. I'd like to pick it up and move it as seeming to be in the wrong spot (drawn over the slanted shade rather than the physical position. It seems just cosmetic, but it affects everything around it that needs new drawing of elements and features.</p>
<p>thx</p>
<p>Edit: Trick for me was shift+left mouse key to activated the lasso function.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span> <span class="post-tag tag-link-moving" rel="tag" title="see questions tagged &#39;moving&#39;">moving</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Sep '20, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '20, 14:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span></p>
</div>
</div>
<div id="comments-container-76581" class="comments-container">
<span id="76591"></span>
<div id="comment-76591" class="comment">
<div id="post-76591-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Glad you found the solution.<br />
Just one bit of advise: Don't rely on a single aerial image to judge if objects are located correctly or not. Even from the same provider image positions may vary between areas, zoom levels and dates taken. You should align the images with existing GPS tracks before starting to move objects around. <a href="https://wiki.openstreetmap.org/wiki/Using_Imagery">https://wiki.openstreetmap.org/wiki/Using_Imagery</a></p>
</div>
<div id="comment-76591-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 14:25)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="76592"></span>
<div id="comment-76592" class="comment">
<div id="post-76592-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Another tip when checking imagery alignment is to turn of the visibility of the data layer and just have the imagery and the gps tracks visible until you get it aligned. I find it much easier without the distraction of all the mapped objects.</p>
</div>
<div id="comment-76592-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 15:12)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
<span id="76594"></span>
<div id="comment-76594" class="comment">
<div id="post-76594-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I parse through them all and whichever has the majority gets the momentary vote, but even that is dubious and an educated guess if it's the right place.</p>
<p>GPS tracking where you're not allowed to go is hard to do, but as noted, that was the fix, else I had to squeeze a city bus through a keyhole.</p>
<p>Noticed in the options that you can enter an offset, but it's seemingly not limited to each sat image provider i.e. applies to all... from bad to worse.</p>
<p>I've been leaving the occasional note or fix me tag, and just now a new (to me) feature popped up in the right hand sidebar 'Add a note to the map'</p>
<p>Thx for your tips and insight.</p>
</div>
<div id="comment-76594-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 16:09)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
</div>
<div id="comment-tools-76581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76581-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="76584"></span>

<div id="answer-container-76584" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76584-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76584-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76584-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using Josm you can select all in rectangle using the normal select tool <a href="https://josm.openstreetmap.de/wiki/Help/Action/Select">https://josm.openstreetmap.de/wiki/Help/Action/Select</a><br />
Or you can use the lasso select tool <a href="https://josm.openstreetmap.de/wiki/Help/Action/LassoMode">https://josm.openstreetmap.de/wiki/Help/Action/LassoMode</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Sep '20, 12:51</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Sep '20, 12:52</strong> </span></p>
</div>
</div>
<div id="comments-container-76584" class="comments-container">
<span id="76586"></span>
<div id="comment-76586" class="comment">
<div id="post-76586-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thx, I read some about the range selection capability it being in the menu when clicking a point, not showing. I'll try again and will report the item [RESOLVED] and upvote if your advise does the trick.</p>
</div>
<div id="comment-76586-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 13:06)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
<span id="76588"></span>
<div id="comment-76588" class="comment">
<div id="post-76588-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, that was a battle for the bulges. Eventually, holding the shift key and the left mouse button activated the 'lasso' ability. A trial allowed to move all in range and reverse. Selecting a rectangle and everything 'completely' inside doesn't, left mouse key just drags the map image around. Maybe my mouse button switching impeded a few things up, but for now I'm happy with the 'lasso' trick. Marking [Resolved] and upvoted.</p>
<p>Many thanks, or as some say here Dice mille grazie.</p>
</div>
<div id="comment-76588-info" class="comment-info">
<span class="comment-age">(14 Sep '20, 13:35)</span> <span class="comment-user userinfo">SekeRob</span>
</div>
</div>
</div>
<div id="comment-tools-76584" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76584-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76642"></span>

<div id="answer-container-76642" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76642-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76642-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76642-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>To add for any reader struggling too with grabbing an area and moving, by coincidence hit shift+left mouse button while thinking I was in edit mode. After dragging realized I was in history mode and just selected a square area on the map which then nicely zoomed into that area. Very useful shortcut. Selecting a square in the edit mode I've still not managed.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '20, 18:46</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76642" class="comments-container">
&#10;</div>
<div id="comment-tools-76642" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76642-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="76653"></span>

<div id="answer-container-76653" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76653-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Misunderstood your question about "a range" at first, thought I should still mention this: UtilsPlugin2 can select "All inside" an area. The objects can then be filtered by searching within.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Sep '20, 00:29</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-76653" class="comments-container">
&#10;</div>
<div id="comment-tools-76653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76653-form-container" class="comment-form-container">
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

