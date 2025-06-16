+++
type = "question"
title = "Bornholm ?"
description = '''I try to load data from Bornholm-Area. But I get Data from an other part of Danmark. I try it with JOSM and with the webinterface. Some idea ?'''
date = "2012-07-11T14:01:00Z"
lastmod = "2012-07-11T15:58:00Z"
weight = 14176
keywords = [ "wrong", "borders" ]
aliases = [ "/questions/14176" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Bornholm ?](/questions/14176/bornholm)

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
<span id="post-14176-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14176-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14176-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I try to load data from Bornholm-Area. But I get Data from an other part of Danmark. I try it with JOSM and with the webinterface. Some idea ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-wrong" rel="tag" title="see questions tagged &#39;wrong&#39;">wrong</span> <span class="post-tag tag-link-borders" rel="tag" title="see questions tagged &#39;borders&#39;">borders</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jul '12, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/71d0f19ce7769ee9d384b774dc5f2720?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fritzfisch01&#39;s gravatar image" />
<p><span>fritzfisch01</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fritzfisch01 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-14176" class="comments-container">
<span id="14177"></span>
<div id="comment-14177" class="comment">
<div id="post-14177-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please explain how exactly you tried to download data. "With JOSM and with the web interface" is not detailed enough to find the problem.</p>
</div>
<div id="comment-14177-info" class="comment-info">
<span class="comment-age">(11 Jul '12, 14:19)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="14190"></span>
<div id="comment-14190" class="comment">
<div id="post-14190-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've just tried searching for bornholm in JOSM and in the search box on osm.org and got bornholm the place=island in both cases. Perhaps you're doing something different?</p>
</div>
<div id="comment-14190-info" class="comment-info">
<span class="comment-age">(11 Jul '12, 15:58)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-14176" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14176-form-container" class="comment-form-container">
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

<span id="14178"></span>

<div id="answer-container-14178" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14178-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14178-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14178-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you mean that you used the map api that is used by all the editors it gives you every node in the bounding box, all the ways that have one or more of these nodes, all nodes that is part of those ways and all relations that referance any of theese. You can read more about it on <a href="https://wiki.openstreetmap.org/wiki/Map_call#Retrieving_map_data_by_bounding_box:_GET_.2Fapi.2F0.6.2Fmap">the wiki</a>.</p>
<p>This means that you will get complete ways that touch your area but can go far away.</p>
<p>Note that if you are using Potlatch, Potlatch 2 or the <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/continuosDownload">continuous download plugin</a> for JOSM it will download the area you are panning to automatically so that it would seem like you have the whole world downloaded. This is also the way that the aerial image layers work.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '12, 14:53</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '12, 16:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-14178" class="comments-container">
&#10;</div>
<div id="comment-tools-14178" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14178-form-container" class="comment-form-container">
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

