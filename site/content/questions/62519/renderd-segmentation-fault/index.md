+++
type = "question"
title = "renderd segmentation fault"
description = '''Hey, I did all the instructions as described in this guide but I still getting error in the final step (renderd -f -c /usr/local/etc/renderd.conf). Output Thanks!'''
date = "2018-03-06T07:50:00Z"
lastmod = "2018-03-08T10:54:00Z"
weight = 62519
keywords = [ "renderd", "tileserver" ]
aliases = [ "/questions/62519" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [renderd segmentation fault](/questions/62519/renderd-segmentation-fault)

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
<span id="post-62519-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62519-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-62519-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hey,</p>
<p>I did all the instructions as described in this <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">guide</a> but I still getting error in the final step (renderd -f -c /usr/local/etc/renderd.conf).</p>
<p><a href="https://pastebin.com/Kkmq390B">Output</a></p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Mar '18, 07:50</strong></p>
<img src="https://secure.gravatar.com/avatar/0a2b7fb7128d2fe03ad3c9cf46c12465?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Niro11&#39;s gravatar image" />
<p><span>Niro11</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Niro11 has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Mar '18, 08:10</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-62519" class="comments-container">
<span id="62541"></span>
<div id="comment-62541" class="comment">
<div id="post-62541-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just to check - what OS is this on? Ubuntu 16.04 or something else?</p>
<p>A "Segmentation fault" normally means "something went horribly wrong" - likely a problem with the build of renderd.</p>
</div>
<div id="comment-62541-info" class="comment-info">
<span class="comment-age">(07 Mar '18, 09:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62519" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62519-form-container" class="comment-form-container">
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

<span id="62568"></span>

<div id="answer-container-62568" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-62568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-62568-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-62568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>16.04.01 lts The problem was solved. The style mapnik.xml is incorrect. remove this fixed the issue</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Mar '18, 09:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0a2b7fb7128d2fe03ad3c9cf46c12465?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Niro11&#39;s gravatar image" />
<p><span>Niro11</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Niro11 has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-62568" class="comments-container">
<span id="62578"></span>
<div id="comment-62578" class="comment">
<div id="post-62578-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've made your comment and answer - hope you don't mind!</p>
</div>
<div id="comment-62578-info" class="comment-info">
<span class="comment-age">(08 Mar '18, 10:54)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-62568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-62568-form-container" class="comment-form-container">
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

