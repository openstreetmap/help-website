+++
type = "question"
title = "Invalid command &#x27;ModTileRenderSocketName&#x27;"
description = '''Apache does not start with  Syntax error on line 4 of /etc/apache2/sites-enabled/000-default: Invalid command &#x27;ModTileRenderSocketName&#x27; line 4 from 000-default: ModTileRenderSocketName /var/run/renderd/renderd/sock All configuration I have made by this article: http://switch2osm.org/serving-tiles/ma...'''
date = "2013-10-07T09:10:00Z"
lastmod = "2013-10-07T14:41:00Z"
weight = 26974
keywords = [ "renderd", "sock", "name", "error" ]
aliases = [ "/questions/26974" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Invalid command 'ModTileRenderSocketName'](/questions/26974/invalid-command-modtilerendersocketname)

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
<span id="post-26974-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26974-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26974-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Apache does not start with Syntax error on line 4 of /etc/apache2/sites-enabled/000-default: Invalid command 'ModTileRenderSocketName'</p>
<p>line 4 from 000-default: ModTileRenderSocketName /var/run/renderd/renderd/sock</p>
<p>All configuration I have made by this article: <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a></p>
<p>I hope I never forget nothing of steps, but recieve this trouble.</p>
<p>Can anybody help me?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-sock" rel="tag" title="see questions tagged &#39;sock&#39;">sock</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Oct '13, 09:10</strong></p>
<img src="https://secure.gravatar.com/avatar/6ba26607be8c629c07a9f2bec3afcc33?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Achechet&#39;s gravatar image" />
<p><span>Achechet</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Achechet has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26974" class="comments-container">
<span id="26977"></span>
<div id="comment-26977" class="comment">
<div id="post-26977-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Only in one case apache does start, if I comment this line. Is it right?</p>
</div>
<div id="comment-26977-info" class="comment-info">
<span class="comment-age">(07 Oct '13, 12:46)</span> <span class="comment-user userinfo">Achechet</span>
</div>
</div>
</div>
<div id="comment-tools-26974" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26974-form-container" class="comment-form-container">
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

<span id="26976"></span>

<div id="answer-container-26976" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26976-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-26976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>According to <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">switch2osm</a> you have a typo in your file <em>000-default</em> and the correct option is <em>ModTileRender<strong>d</strong>SocketName</em>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Oct '13, 12:38</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26976" class="comments-container">
<span id="26982"></span>
<div id="comment-26982" class="comment">
<div id="post-26982-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It is only my mistake in file /etc/apache2/sites-enabled/000-default/</p>
<p>Just noq all started clear without errors.</p>
<p>Thank you.</p>
</div>
<div id="comment-26982-info" class="comment-info">
<span class="comment-age">(07 Oct '13, 14:41)</span> <span class="comment-user userinfo">Achechet</span>
</div>
</div>
</div>
<div id="comment-tools-26976" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26976-form-container" class="comment-form-container">
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

