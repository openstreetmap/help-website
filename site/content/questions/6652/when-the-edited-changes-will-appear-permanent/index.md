+++
type = "question"
title = "When the edited changes will appear permanent"
description = '''I edited some stuffs recently in the city of Sao Jose dos Campos, Brazil. After what time those additons will appear in the View mode ?'''
date = "2011-07-28T13:51:00Z"
lastmod = "2011-07-28T15:26:00Z"
weight = 6652
keywords = [ "changes" ]
aliases = [ "/questions/6652" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [When the edited changes will appear permanent](/questions/6652/when-the-edited-changes-will-appear-permanent)

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
<span id="post-6652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6652-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-6652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
2
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I edited some stuffs recently in the city of Sao Jose dos Campos, Brazil. After what time those additons will appear in the View mode ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jul '11, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/30d51d566faa53d6c04ea15433d520a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ok2pen&#39;s gravatar image" />
<p><span>ok2pen</span><br />
<span class="score" title="46 reputation points">46</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ok2pen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-6652" class="comments-container">
<span id="6664"></span>
<div id="comment-6664" class="comment">
<div id="post-6664-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The tile rendering process was impacted by a hardware fault on the server this week, so it may be that your changes appeared more slowly than usual.</p>
</div>
<div id="comment-6664-info" class="comment-info">
<span class="comment-age">(28 Jul '11, 15:26)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-6652" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6652-form-container" class="comment-form-container">
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

<span id="6660"></span>

<div id="answer-container-6660" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6660-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-6660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All changes that you upload are instantly and permanently in the map (map-database). For renderings it depends how often the renderer imports data from the main database (and how frequently it re-renders the map).</p>
<p>Mapnik generally (if there is no problem) takes around one minute to get aware of the new data and some more minutes to render the high-zoom-tiles (z15-18). There are different mechanisms in place to deal with tile-expiry (re-rendering of old tiles). One important factor is if the map is actually looked at.</p>
<p>Generally this depends on the map, the activity in the system and on the zoom level. If you added something that is rendered (i.e. there is a rendering rule for it) it will usually appear shortly (some minutes) afterwards on the main mapnik map and with a little delay on tiles@home/osmarender. But sometimes the servers suffer from many parallel requests and might no be able to cope with all rendering request.</p>
<p>Low-zoom-tiles are re-rendered less frequently because they take far longer to calculate (they contain more data). I might take up to a month or so until you can see you additions in lower zoom levels.</p>
<p>If you're under the impression that your tile somehow skipped the re-rendering process (this happens when the rendering queue is full), you can also manually request a re-render by calling the tile and add "/dirty" to it like this: <a href="http://tile.openstreetmap.org/7/63/42.png/dirty">http://tile.openstreetmap.org/7/63/42.png/dirty</a></p>
<p>You can see the current status of the mapnik rendering server here: <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/index.html#renderd">http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/index.html#renderd</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '11, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/f09c0b7a655fed386e070e036e2da248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dieterdreist&#39;s gravatar image" />
<p><span>dieterdreist</span><br />
<span class="score" title="3677 reputation points"><span>3.7k</span></span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="67 badges"><span class="bronze">●</span><span class="badgecount">67</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dieterdreist has 4 accepted answers">3%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jul '11, 15:27</strong> </span></p>
</div>
</div>
<div id="comments-container-6660" class="comments-container">
&#10;</div>
<div id="comment-tools-6660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6660-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="6658"></span>

<div id="answer-container-6658" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-6658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-6658-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-6658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I did some edits 14 hours ago and most of it appears at all zoom levels</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jul '11, 14:26</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-6658" class="comments-container">
&#10;</div>
<div id="comment-tools-6658" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-6658-form-container" class="comment-form-container">
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

