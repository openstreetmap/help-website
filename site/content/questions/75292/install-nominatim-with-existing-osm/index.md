+++
type = "question"
title = "Install Nominatim with existing OSM"
description = '''I installed an Ubuntu server with OSM which has been used with our applications for 2 years. And now, I would like to install Nominatim. I found the following link https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/ to proceed. But, of course, I have to install all the necessary...'''
date = "2020-06-11T15:21:00Z"
lastmod = "2020-06-11T15:29:00Z"
weight = 75292
keywords = [ "nominatim", "osm", "install", "databases" ]
aliases = [ "/questions/75292" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Install Nominatim with existing OSM](/questions/75292/install-nominatim-with-existing-osm)

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
<span id="post-75292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75292-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I installed an Ubuntu server with OSM which has been used with our applications for 2 years.</p>
<p>And now, I would like to install Nominatim. I found the following link <a href="https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/">https://nominatim.org/release-docs/latest/appendix/Install-on-Ubuntu-18/</a> to proceed. But, of course, I have to install all the necessary OSM data.</p>
<p>So, I will obtain 2 databases, one for OSM, one for Nominatim. Which is really heavy.</p>
<p>My question is very simple, is it possible to install Nominatim on the same server as OSM and use the same database ? If yes, how can I do that ? I didn't find any howto !</p>
<p>Thx for your help</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span> <span class="post-tag tag-link-databases" rel="tag" title="see questions tagged &#39;databases&#39;">databases</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '20, 15:21</strong></p>
<img src="https://secure.gravatar.com/avatar/f9556029fbf4d1fa918da7a23ed68ce4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gduh83&#39;s gravatar image" />
<p><span>gduh83</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gduh83 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-75292" class="comments-container">
&#10;</div>
<div id="comment-tools-75292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75292-form-container" class="comment-form-container">
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

<span id="75294"></span>

<div id="answer-container-75294" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75294-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75294-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75294-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is not. Nominatim has it's own table schema and update script and most data will be dupliated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '20, 15:29</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-75294" class="comments-container">
&#10;</div>
<div id="comment-tools-75294" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75294-form-container" class="comment-form-container">
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

