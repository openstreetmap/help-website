+++
type = "question"
title = "Taginfo data updates"
description = '''Hello, Does anyone know if taginfo utilizes changesets to keep its database up to date? If so how is this performed? I understand that the initial load is a simple planet xml import with the update_all.sh utility. '''
date = "2016-08-16T17:46:00Z"
lastmod = "2016-08-16T18:31:00Z"
weight = 51449
keywords = [ "changesets", "taginfo" ]
aliases = [ "/questions/51449" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Taginfo data updates](/questions/51449/taginfo-data-updates)

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
<span id="post-51449-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51449-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-51449-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Does anyone know if taginfo utilizes changesets to keep its database up to date? If so how is this performed? I understand that the initial load is a simple planet xml import with the update_all.sh utility.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changesets" rel="tag" title="see questions tagged &#39;changesets&#39;">changesets</span> <span class="post-tag tag-link-taginfo" rel="tag" title="see questions tagged &#39;taginfo&#39;">taginfo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Aug '16, 17:46</strong></p>
<img src="https://secure.gravatar.com/avatar/943c484e8c04680902357de8f080dcc0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cellington&#39;s gravatar image" />
<p><span>Cellington</span><br />
<span class="score" title="216 reputation points">216</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cellington has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-51449" class="comments-container">
&#10;</div>
<div id="comment-tools-51449" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51449-form-container" class="comment-form-container">
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

<span id="51450"></span>

<div id="answer-container-51450" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-51450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51450-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-51450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It doesn't use updates directly. Rather, a local copy of the planet file is kept, and updated every day, and then processed by taginfo.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Aug '16, 17:50</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-51450" class="comments-container">
<span id="51451"></span>
<div id="comment-51451" class="comment">
<div id="post-51451-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. So the process essentially appends the daily changeset to a local copy of the planet file via osmosis. So once the data is processed by taginfo, the old data is replaced by the new data?</p>
<p>Thanks.</p>
</div>
<div id="comment-51451-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 18:01)</span> <span class="comment-user userinfo">Cellington</span>
</div>
</div>
<span id="51452"></span>
<div id="comment-51452" class="comment">
<div id="post-51452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes that's how it works.</p>
</div>
<div id="comment-51452-info" class="comment-info">
<span class="comment-age">(16 Aug '16, 18:31)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-51450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51450-form-container" class="comment-form-container">
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

