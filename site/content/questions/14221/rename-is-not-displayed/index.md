+++
type = "question"
title = "rename is not displayed"
description = '''I have renamed a park (https://www.openstreetmap.org/?lat=50.964052&amp;amp;lon=6.965101&amp;amp;zoom=18&amp;amp;layers=M) but the new name is not displayed. How can I enforce an update of the tile cache?'''
date = "2012-07-12T10:30:00Z"
lastmod = "2012-07-12T13:44:00Z"
weight = 14221
keywords = [ "rename" ]
aliases = [ "/questions/14221" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [rename is not displayed](/questions/14221/rename-is-not-displayed)

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
<span id="post-14221-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14221-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14221-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have renamed a park (<a href="https://www.openstreetmap.org/?lat=50.964052&amp;lon=6.965101&amp;zoom=18&amp;layers=M)">https://www.openstreetmap.org/?lat=50.964052&amp;lon=6.965101&amp;zoom=18&amp;layers=M)</a> but the new name is not displayed. How can I enforce an update of the tile cache?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rename" rel="tag" title="see questions tagged &#39;rename&#39;">rename</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jul '12, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/868381534720a64e9eb7511f8bee6021?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beckmi&#39;s gravatar image" />
<p><span>beckmi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beckmi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14221" class="comments-container">
&#10;</div>
<div id="comment-tools-14221" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14221-form-container" class="comment-form-container">
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

<span id="14222"></span>

<div id="answer-container-14222" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14222-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14222-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-14222-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You will need to wait until the rendering server <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/replication_delay.html">catches up</a> with your changes first, then follow the instructions about adding /dirty in the answer to <a href="/questions/178/how-often-does-the-main-mapnik-map-get-updated">this earlier question</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jul '12, 10:39</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jul '12, 10:40</strong> </span></p>
</div>
</div>
<div id="comments-container-14222" class="comments-container">
<span id="14228"></span>
<div id="comment-14228" class="comment">
<div id="post-14228-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The map tiles re-generation is stoped currently. Watch the 'tile service' status on this wiki: <a href="https://wiki.openstreetmap.org/wiki/Platform_Status">https://wiki.openstreetmap.org/wiki/Platform_Status</a></p>
</div>
<div id="comment-14228-info" class="comment-info">
<span class="comment-age">(12 Jul '12, 13:02)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="14230"></span>
<div id="comment-14230" class="comment">
<div id="post-14230-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>... and it's working now. Also, you can take "<a href="https://wiki.openstreetmap.org/wiki/Key:designation">designation</a>" off as that's about the "legal classification" rather than the "name".</p>
<p>For example, a number of footpaths in England and Wales (but not all) have a legal status of "Public Footpath" and that's what therefore get marked with an appropriate "designation" tag. It's not intended to be used for "name", "description" or "note".</p>
</div>
<div id="comment-14230-info" class="comment-info">
<span class="comment-age">(12 Jul '12, 13:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-14222" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14222-form-container" class="comment-form-container">
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

