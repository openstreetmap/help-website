+++
type = "question"
title = "Problems with JOSM on Mac OS X"
description = '''I am having all kinds of problems when using JOSM on Mac OS X (10.7.4):  All rotated (street) labels are offset too far to the right and down. When the street is in the top left of the editing window, the label is more or less placed correctly. But the label is always twice as far from the top left ...'''
date = "2012-07-20T22:54:00Z"
lastmod = "2012-07-22T22:16:00Z"
weight = 14448
keywords = [ "josm", "mac", "osx" ]
aliases = [ "/questions/14448" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Problems with JOSM on Mac OS X](/questions/14448/problems-with-josm-on-mac-os-x)

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
<span id="post-14448-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14448-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14448-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am having all kinds of problems when using JOSM on Mac OS X (10.7.4):</p>
<ul>
<li>All rotated (street) labels are offset too far to the right and down. When the street is in the top left of the editing window, the label is more or less placed correctly. But the label is always twice as far from the top left corner as the street is. If the street is in the middle of the editing window, its label is in the bottom right.</li>
<li>Cmd-Alt-+ and Cmd-Alt-- to zoom in and out don't work. (May be a problem because it's a MacBook keyboard, or because it's Norwegian localized.)</li>
<li>Ctrl-Left and Ctrl-Right to pan the window left and right conflict with the shortcut keys to switch desktops is OS X 10.7 (Lion).</li>
</ul>
<p>Especially the first point is a bit of a showstopper for me, but I would really like to use the keyboard also. Does anybody know if there is something wrong with my setup, or are these known problems with JOSM on OS X?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jul '12, 22:54</strong></p>
<img src="https://secure.gravatar.com/avatar/a2f19e3a960bbc861e85b69c9c13a8e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pbb&#39;s gravatar image" />
<p><span>pbb</span><br />
<span class="score" title="621 reputation points">621</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pbb has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14448" class="comments-container">
&#10;</div>
<div id="comment-tools-14448" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14448-form-container" class="comment-form-container">
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

<span id="14457"></span>

<div id="answer-container-14457" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14457-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14457-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14457-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pbb has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<ul>
<li>That looks like a bug with the label alignment, it moves around when you pan as well. Please submit a new ticket at <a href="https://josm.openstreetmap.de/">josm.openstreetmap.org</a> if it is not submitted before.</li>
<li>Tested with the same keybord setup as you (the same I use every day) and it is an issue. The problem with a lot of shortcuts is that OS X is not delivering a lot of different shortcuts to the java runtime. I have gotten used to rebinding the keys I use a lot, and I have changed the setting for the touchpad so that it is easier to right click and drag.</li>
</ul>
<p>Josm have its many, many, many problems, but it is still much more efficiant then any other editors out there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '12, 11:43</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-14457" class="comments-container">
<span id="14487"></span>
<div id="comment-14487" class="comment">
<div id="post-14487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I updated an existing ticket (<a href="https://josm.openstreetmap.de/ticket/7841)">https://josm.openstreetmap.de/ticket/7841)</a> with my findings. Hope this will be fixed soon :) Do I understand that you <em>don't</em> have the problem with the label alignment?</p>
</div>
<div id="comment-14487-info" class="comment-info">
<span class="comment-age">(22 Jul '12, 22:16)</span> <span class="comment-user userinfo">pbb</span>
</div>
</div>
</div>
<div id="comment-tools-14457" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14457-form-container" class="comment-form-container">
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

