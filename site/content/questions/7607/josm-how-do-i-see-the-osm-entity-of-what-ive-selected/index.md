+++
type = "question"
title = "JOSM - How do I see the OSM entity of what I&#x27;ve selected"
description = '''If I select an item (e.g. a &quot;highway=residential&quot; with no other tags yet) in JOSM, the item appears in the &quot;Selection&quot; panel at the right-hand side. Unfortunately, however, it&#x27;s displayed as &quot;highway (2 nodes)&quot; not as &quot;way 125419318&quot;. Is it possible to make the selection list always should the item ...'''
date = "2011-09-04T14:48:00Z"
lastmod = "2011-09-04T17:27:00Z"
weight = 7607
keywords = [ "josm", "selection", "panel" ]
aliases = [ "/questions/7607" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [JOSM - How do I see the OSM entity of what I've selected](/questions/7607/josm-how-do-i-see-the-osm-entity-of-what-ive-selected)

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
<span id="post-7607-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7607-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-7607-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>If I select an item (e.g. a "<code>highway=residential</code>" with no other tags yet) in JOSM, the item appears in the "Selection" panel at the right-hand side.</p>
<p>Unfortunately, however, it's displayed as "highway (2 nodes)" not as "way 125419318". Is it possible to make the selection list always should the item ID? Obviously, I can select the item and "inspect" it but that's a lot of clumsy messing around with the mouse and a popup window. Similarly ctrl-i and ctrl-h work to open browser pages for the item, but I suspect that there's a setting somewhere to make IDs appear in the main list.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span> <span class="post-tag tag-link-panel" rel="tag" title="see questions tagged &#39;panel&#39;">panel</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '11, 14:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Sep '11, 16:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span></p>
</div>
</div>
<div id="comments-container-7607" class="comments-container">
&#10;</div>
<div id="comment-tools-7607" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7607-form-container" class="comment-form-container">
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

<span id="7614"></span>

<div id="answer-container-7614" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7614-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7614-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-7614-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Add the line</p>
<blockquote>
<p>osm-primitives.showid=true</p>
</blockquote>
<p>to your JOSM preferences file.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Sep '11, 16:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-7614" class="comments-container">
<span id="7615"></span>
<div id="comment-7615" class="comment">
<div id="post-7615-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks - I actually got to it via Edit / Preferences / Display / Look and Feel / Show Object ID in selection lists</p>
</div>
<div id="comment-7615-info" class="comment-info">
<span class="comment-age">(04 Sep '11, 17:27)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7614" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7614-form-container" class="comment-form-container">
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

