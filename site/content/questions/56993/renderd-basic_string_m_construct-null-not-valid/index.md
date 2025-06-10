+++
type = "question"
title = "[renderd] basic_string::_M_construct null not valid"
description = '''Hi, I got the following error message at start of the renderd service. An error occurred while loading the map layer &#x27;ajt&#x27;: basic_string::_M_construct null not valid I followed the following guide to build my local tile server: switch2osm tile server 16 04 02 I did then combined 4 pbf file into one ...'''
date = "2017-07-10T16:43:00Z"
lastmod = "2017-07-11T11:23:00Z"
weight = 56993
keywords = [ "rendering", "renderd" ]
aliases = [ "/questions/56993" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[renderd\] basic_string::\_M_construct null not valid](/questions/56993/renderd-basic_string_m_construct-null-not-valid)

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
<span id="post-56993-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56993-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56993-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I got the following error message at start of the renderd service.<br />
An error occurred while loading the map layer 'ajt': basic_string::_M_construct null not valid</p>
<p>I followed the following guide to build my local tile server: <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">switch2osm tile server 16 04 02</a><br />
I did then combined 4 pbf file into one with osmosis command</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jul '17, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/8c66fe187d8862a5b8c779b0fa3ac9b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DeimosOmegaChan&#39;s gravatar image" />
<p><span>DeimosOmegaChan</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DeimosOmegaChan has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-56993" class="comments-container">
<span id="56996"></span>
<div id="comment-56996" class="comment">
<div id="post-56996-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That looks like there's a problem with the style file. What style are you using? Could you post the full renderd startup information in a gist or other online document and link to it here?</p>
<p>The problem might be any one of a number of issues, so people would need to know what OS you were running on, what version, and any other customisations. Did it use to work and has it stopped following a database reload?</p>
</div>
<div id="comment-56996-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 17:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56997"></span>
<div id="comment-56997" class="comment">
<div id="post-56997-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I use the style "openstreetmap-carto" from the tutorial. I only noticed it after I imported data from several map files. The map rendering became unstable. Some parts of the map won't rendering properly. I read too the apache error log, there was written that I have sometimes no permission to the socket file of renderd.</p>
<p>I can tell more details tomorrow.</p>
</div>
<div id="comment-56997-info" class="comment-info">
<span class="comment-age">(10 Jul '17, 18:44)</span> <span class="comment-user userinfo">DeimosOmegaChan</span>
</div>
</div>
<span id="57009"></span>
<div id="comment-57009" class="comment">
<div id="post-57009-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I use Ubuntu 16.04.</p>
</div>
<div id="comment-57009-info" class="comment-info">
<span class="comment-age">(11 Jul '17, 11:22)</span> <span class="comment-user userinfo">DeimosOmegaChan</span>
</div>
</div>
</div>
<div id="comment-tools-56993" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56993-form-container" class="comment-form-container">
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

<span id="57010"></span>

<div id="answer-container-57010" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57010-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-57010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I solved the problem by deleting the ajt directory after importing data into the database from the combined file.<br />
I have then restarted renderd server.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jul '17, 11:23</strong></p>
<img src="https://secure.gravatar.com/avatar/8c66fe187d8862a5b8c779b0fa3ac9b3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DeimosOmegaChan&#39;s gravatar image" />
<p><span>DeimosOmegaChan</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DeimosOmegaChan has no accepted answers">0%</span> </br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jul '17, 11:23</strong> </span></p>
</div>
</div>
<div id="comments-container-57010" class="comments-container">
&#10;</div>
<div id="comment-tools-57010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57010-form-container" class="comment-form-container">
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

