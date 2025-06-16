+++
type = "question"
title = "How to backup JOSM prior to JOSM or plugins upgrade?"
description = '''Like a number of people I suspect, I recently got bitten by https://josm.openstreetmap.de/ticket/12542 . Luckily I was able to find a working version of the reverter plugin and reinstall it. However, what should I have backed up prior to update so that point so that when the update resulted in a non...'''
date = "2016-02-28T12:43:00Z"
lastmod = "2016-03-01T17:38:00Z"
weight = 48396
keywords = [ "josm" ]
aliases = [ "/questions/48396" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to backup JOSM prior to JOSM or plugins upgrade?](/questions/48396/how-to-backup-josm-prior-to-josm-or-plugins-upgrade)

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
<span id="post-48396-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48396-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48396-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Like a number of people I suspect, I recently got bitten by <a href="https://josm.openstreetmap.de/ticket/12542">https://josm.openstreetmap.de/ticket/12542</a> . Luckily I was able to find a working version of the reverter plugin and reinstall it. However, what should I have backed up prior to update so that point so that when the update resulted in a non-functional system I could have restored and carried on?</p>
<p>I suspect that there will be at least two answers needed here - one for Windows and one for people running JOSM on Linux who aren't using a PPA (and does JOSM on OS X use the same directory structure as Linux?).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Feb '16, 12:43</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-48396" class="comments-container">
&#10;</div>
<div id="comment-tools-48396" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48396-form-container" class="comment-form-container">
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

<span id="48433"></span>

<div id="answer-container-48433" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48433-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48433-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-48433-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In Windows, the settings and cache are stored in <code>%APPDATA%\JOSM</code> - for me, that expands to <code>c:\Users\Piskvor\AppData\Roaming\JOSM\</code>; I assume yours would be similar.</p>
<p>In Linux, the stable version stores its data in <code>~/.josm/</code>, the josm-latest version uses <code>~/josm-latest/</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Mar '16, 15:33</strong></p>
<img src="https://secure.gravatar.com/avatar/8200fa5c0cc8feb096558c5972a6191c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Piskvor&#39;s gravatar image" />
<p><span>Piskvor</span><br />
<span class="score" title="1266 reputation points"><span>1.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Piskvor has 9 accepted answers">37%</span></p>
</div>
</div>
<div id="comments-container-48433" class="comments-container">
<span id="48434"></span>
<div id="comment-48434" class="comment">
<div id="post-48434-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would <em>assume</em> that OSX is likely to use the UN*X-style convention, so <code>~/.josm/</code></p>
</div>
<div id="comment-48434-info" class="comment-info">
<span class="comment-age">(01 Mar '16, 15:34)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="48435"></span>
<div id="comment-48435" class="comment">
<div id="post-48435-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For OSX, see at the end of page <a href="https://wiki.openstreetmap.org/wiki/JOSM/Mac,">https://wiki.openstreetmap.org/wiki/JOSM/Mac,</a> the presents are in ~/Library/JOSM/ (earlier versions used ~/.josm though) The cache tile can be found under ~/Library/Caches/JOSM/tiles (see advanced settings in JOSM)</p>
</div>
<div id="comment-48435-info" class="comment-info">
<span class="comment-age">(01 Mar '16, 16:36)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="48437"></span>
<div id="comment-48437" class="comment">
<div id="post-48437-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/9641/piskvor">@Piskvor</a> josm-latest also uses <code>~/.josm/</code>.</p>
</div>
<div id="comment-48437-info" class="comment-info">
<span class="comment-age">(01 Mar '16, 17:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48433" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48433-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="48398"></span>

<div id="answer-container-48398" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48398-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48398-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48398-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can only answer for linux, I have never used a mac and have never used josm on windows.</p>
<p>On linux (fedora) and assuming space isn't a problem, I have simply run the command 'tar zcvf josm.tgz .josm/' and that gives me a complete backup of the .josm folder. It is currently 560MB, it does contain a tile cache in .josm/cache which can be removed if space is a problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Feb '16, 14:12</strong></p>
<img src="https://secure.gravatar.com/avatar/eb2bf53c1e2a0b137c64d07a34ad5a29?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="trigpoint&#39;s gravatar image" />
<p><span>trigpoint</span><br />
<span class="score" title="759 reputation points">759</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="trigpoint has 3 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-48398" class="comments-container">
<span id="48399"></span>
<div id="comment-48399" class="comment">
<div id="post-48399-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>For excluding the cache just add <code>--exclude=".josm/cache/*"</code>.</p>
</div>
<div id="comment-48399-info" class="comment-info">
<span class="comment-age">(28 Feb '16, 14:26)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48398" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48398-form-container" class="comment-form-container">
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

