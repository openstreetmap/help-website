+++
type = "question"
title = "Alignment of Japan Project #9023"
description = '''I started with the Japan project https://tasks.hotosm.org/projects/9023 today and saw there is a big misalignment of the Maxar Premium and the Bing imagery. Maxar seems to be newer, because it contains some buildings that are not on Bing, but when you get an area with buildings mapped using Bing, an...'''
date = "2020-07-10T16:55:00Z"
lastmod = "2020-07-11T12:55:00Z"
weight = 75643
keywords = [ "imagery_offset" ]
aliases = [ "/questions/75643" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Alignment of Japan Project \#9023](/questions/75643/alignment-of-japan-project-9023)

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
<span id="post-75643-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75643-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75643-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I started with the Japan project <a href="https://tasks.hotosm.org/projects/9023">https://tasks.hotosm.org/projects/9023</a> today and saw there is a big misalignment of the Maxar Premium and the Bing imagery. Maxar seems to be newer, because it contains some buildings that are not on Bing, but when you get an area with buildings mapped using Bing, and then switch to Maxar for mapping the rest of the buildings, the old mapped buildings do not fit to the imagery. Can anyone who know this application better than me please take a look and check if the imageries can be aligned for the whole project?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-imagery_offset" rel="tag" title="see questions tagged &#39;imagery_offset&#39;">imagery_offset</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '20, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/99819371743059c215f119ca972cfdb1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tobias%20Barth&#39;s gravatar image" />
<p><span>Tobias Barth</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tobias Barth has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75643" class="comments-container">
<span id="75654"></span>
<div id="comment-75654" class="comment">
<div id="post-75654-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In Japan, use GSI standard map as a guide.</p>
</div>
<div id="comment-75654-info" class="comment-info">
<span class="comment-age">(11 Jul '20, 12:54)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-75643" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75643-form-container" class="comment-form-container">
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

<span id="75645"></span>

<div id="answer-container-75645" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75645-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are <a href="https://wiki.openstreetmap.org/wiki/Imagery_Offset_Database">attempts to save imagery offsets</a>, but as each imagery layer is actually a composite of multiple captures with unknown post-processing and extents and sometimes offsets even differ between zoom levels, this is quite difficult to accomplish.</p>
<p>In iD editor the offset for a particular area can be adjusted by scrolling to the bottom of the pane showing the list of available images and attempting to drag the grey area surrounding the text describing the offset.</p>
<p>If the region is hilly then the distortions required to flatten the imagery can result in significant disagreement between the appearance from various providers. GPS traces are generally considered the most reliable positioning provided there are enough traces to allow for scatter and they aren't in the midst of highrise building which can reflect signals.</p>
<p>Imagery-wise I would normally expect a local agencies orthophotos to be more accurately positioned than any of the global providers. iD and JOSM list some <a href="https://wiki.openstreetmap.org/wiki/GSImaps">Japan specific layers</a>, but I have no knowledge of their accuracy myself.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jul '20, 19:02</strong></p>
<img src="https://secure.gravatar.com/avatar/ec8a0cf213f9797ad1c1ae2c28c2332d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="InsertUser&#39;s gravatar image" />
<p><span>InsertUser</span><br />
<span class="score" title="11005 reputation points"><span>11.0k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="69 badges"><span class="silver">●</span><span class="badgecount">69</span></span><span title="185 badges"><span class="bronze">●</span><span class="badgecount">185</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="InsertUser has 73 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-75645" class="comments-container">
<span id="75649"></span>
<div id="comment-75649" class="comment">
<div id="post-75649-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your fast answer. Seems to be a complex problem because of the 2d projection of a 3d world etc.. Follow-up question: Is there a way to move an entire building, other than moving point by point?</p>
</div>
<div id="comment-75649-info" class="comment-info">
<span class="comment-age">(10 Jul '20, 21:44)</span> <span class="comment-user userinfo">Tobias Barth</span>
</div>
</div>
<span id="75650"></span>
<div id="comment-75650" class="comment">
<div id="post-75650-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, either right click and use the dot with four arrows radiating in the cardinal directions or the shortcut <em>M</em>. For most buildings the sQuare command is heavily used too. Although for the previous editor, <a href="https://wiki.openstreetmap.org/wiki/Roof_modelling">this page</a> still contains some useful tips for buildings. (PS this should technically be a new question)</p>
</div>
<div id="comment-75650-info" class="comment-info">
<span class="comment-age">(11 Jul '20, 00:01)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="75655"></span>
<div id="comment-75655" class="comment">
<div id="post-75655-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/4426/insertuser"></a><a href="https://help.openstreetmap.org/users/4426/insertuser">@InsertUser</a> GSI photos aren't necessarily aligned with GSI standard map, but the latter is a possible "standard" reference.</p>
</div>
<div id="comment-75655-info" class="comment-info">
<span class="comment-age">(11 Jul '20, 12:55)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-75645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75645-form-container" class="comment-form-container">
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

