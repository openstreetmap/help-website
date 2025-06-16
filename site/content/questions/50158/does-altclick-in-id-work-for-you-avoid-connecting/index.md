+++
type = "question"
title = "Does Alt+Click in iD work for you (avoid connecting)?"
description = '''According to this wiki page on iD Shortcuts (which I know is not &#x27;official documentation&#x27;) you can use Alt+Click when drawing a line or area to place a node without connecting to an existing object. This would be quite useful, to avoid unwanted connections. But it doesn&#x27;t seem to work for me. A note...'''
date = "2016-06-11T23:55:00Z"
lastmod = "2016-06-15T01:13:00Z"
weight = 50158
keywords = [ "ideditor", "draw", "shortcut" ]
aliases = [ "/questions/50158" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does Alt+Click in iD work for you (avoid connecting)?](/questions/50158/does-altclick-in-id-work-for-you-avoid-connecting)

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
<span id="post-50158-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50158-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50158-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>According to <a href="https://wiki.openstreetmap.org/wiki/ID/Shortcuts">this wiki page on iD Shortcuts</a> (which I know is not 'official documentation') you can use Alt+Click when drawing a line or area to place a node without connecting to an existing object. This would be quite useful, to avoid unwanted connections. But it doesn't seem to work for me.</p>
<p>A note on that page says with Firefox you should use full-screen mode to avoid an unwanted browser interaction regarding the Alt key. I've tried it with Firefox (38.8.0ESR) and also Seamonkey (2.40), both full-screen and regular mode, all on Linux. When I press Alt, it does in fact prevent highlighting of another Way that my cursor touches. But it won't recognize the click to add a point there. If I release Alt, of course, it adds a node but connects to that object.</p>
<p>Does it work for anyone? If it does, I'll just assume it is something about my browser/desktop environment causing this.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-ideditor" rel="tag" title="see questions tagged &#39;ideditor&#39;">ideditor</span> <span class="post-tag tag-link-draw" rel="tag" title="see questions tagged &#39;draw&#39;">draw</span> <span class="post-tag tag-link-shortcut" rel="tag" title="see questions tagged &#39;shortcut&#39;">shortcut</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '16, 23:55</strong></p>
<img src="https://secure.gravatar.com/avatar/c1e98ded2982cd352d4c77075aa0cd74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ljb_nj&#39;s gravatar image" />
<p><span>ljb_nj</span><br />
<span class="score" title="659 reputation points">659</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ljb_nj has one accepted answer">12%</span></p>
</div>
</div>
<div id="comments-container-50158" class="comments-container">
&#10;</div>
<div id="comment-tools-50158" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50158-form-container" class="comment-form-container">
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

<span id="50207"></span>

<div id="answer-container-50207" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50207-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50207-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-50207-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It turns out that my Linux desktop environment (Xfce) grabs Alt+Click for itself, and does not deliver it to any application. It doesn't matter if the browser is in Full Screen Mode or not - it never sees the click.</p>
<p>Workaround #1: Using either Shift+Alt+Click or Ctrl+Alt+Click instead of Alt+Click seems to work: adds a node without connecting.</p>
<p>Workaround #2 (Xfce specific): Go to Settings, Window Manager Tweaks, Accessibility tab, and change "Key used to grab and move windows" from Alt to None. Then Alt+Click works in iD.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jun '16, 01:13</strong></p>
<img src="https://secure.gravatar.com/avatar/c1e98ded2982cd352d4c77075aa0cd74?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ljb_nj&#39;s gravatar image" />
<p><span>ljb_nj</span><br />
<span class="score" title="659 reputation points">659</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ljb_nj has one accepted answer">12%</span></p>
</div>
</div>
<div id="comments-container-50207" class="comments-container">
&#10;</div>
<div id="comment-tools-50207" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50207-form-container" class="comment-form-container">
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

