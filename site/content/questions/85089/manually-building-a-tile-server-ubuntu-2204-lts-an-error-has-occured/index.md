+++
type = "question"
title = "manually building a tile server ubuntu 22.04 lts an error has occured"
description = '''sudo -u _renderd scripts/get-external-data.py  I build it via https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/  how to fix? thanks a lot. '''
date = "2022-07-16T09:47:00Z"
lastmod = "2022-07-17T06:37:00Z"
weight = 85089
keywords = [ "manually" ]
aliases = [ "/questions/85089" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [manually building a tile server ubuntu 22.04 lts an error has occured](/questions/85089/manually-building-a-tile-server-ubuntu-2204-lts-an-error-has-occured)

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
<span id="post-85089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85089-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>sudo -u _renderd scripts/get-external-data.py <img src="/upfiles/1657960656765.jpg" alt="alt text" /> I build it via <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/</a> how to fix?</p>
<p>thanks a lot. <img src="/upfiles/1657960798051.jpg" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-manually" rel="tag" title="see questions tagged &#39;manually&#39;">manually</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '22, 09:47</strong></p>
<img src="https://secure.gravatar.com/avatar/c66ad6c704973c88fe030ad570ef36a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="weiyilai&#39;s gravatar image" />
<p><span>weiyilai</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="weiyilai has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-85089" class="comments-container">
&#10;</div>
<div id="comment-tools-85089" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85089-form-container" class="comment-form-container">
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

<span id="85090"></span>

<div id="answer-container-85090" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85090-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85090-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-85090-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll probably need to give a few more details about how you got to where you did. The <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-ubuntu-22-04-lts/">instructions</a> don't mention "pip install gdal" anywhere, they get gdal-bin via "apt install"; maybe something went wrong earlier? Also it looks like gdal will only be available to your "weiyi" user, not "_renderd".</p>
<p>I would go around again and note where things start going wrong.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '22, 11:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</img>
</div>
</div>
<div id="comments-container-85090" class="comments-container">
<span id="85099"></span>
<div id="comment-85099" class="comment">
<div id="post-85099-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Done, I reinstalled. No problems occurred during the process</p>
</div>
<div id="comment-85099-info" class="comment-info">
<span class="comment-age">(17 Jul '22, 06:37)</span> <span class="comment-user userinfo">weiyilai</span>
</div>
</div>
</div>
<div id="comment-tools-85090" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85090-form-container" class="comment-form-container">
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

