+++
type = "question"
title = "Generate map tiles creates error &quot;PostgreSQL&quot;"
description = '''We are trying to generate map tiles of the entire world, and at a certain stage we get the error &quot;invalid memory alloc request size 1677721600&quot; and we cannot proceed.  When we generate a small country it is done fine, but when working on the entire world, the tile generation stops after 25/30% and 8...'''
date = "2013-07-09T20:25:00Z"
lastmod = "2013-07-22T09:34:00Z"
weight = 24141
keywords = [ "postgresql" ]
aliases = [ "/questions/24141" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Generate map tiles creates error "PostgreSQL"](/questions/24141/generate-map-tiles-creates-error-postgresql)

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
<span id="post-24141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24141-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We are trying to generate map tiles of the entire world, and at a certain stage we get the error "invalid memory alloc request size 1677721600" and we cannot proceed.</p>
<p>When we generate a small country it is done fine, but when working on the entire world, the tile generation stops after 25/30% and 85/90%.</p>
<p>How to proceed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '13, 20:25</strong></p>
<img src="https://secure.gravatar.com/avatar/2ee30ca930eebe1f1af803f321ff5125?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Agnoletti&#39;s gravatar image" />
<p><span>Agnoletti</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Agnoletti has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Apr '15, 02:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-24141" class="comments-container">
<span id="24153"></span>
<div id="comment-24153" class="comment">
<div id="post-24153-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would it be possible to provide a few more details about the setup you're using, including the hardware spec of the box that the rendering is running on? Also - there's more than one way to generate map tiles, so details what you're actually running that's running out of memory would help.</p>
</div>
<div id="comment-24153-info" class="comment-info">
<span class="comment-age">(10 Jul '13, 01:55)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="24157"></span>
<div id="comment-24157" class="comment">
<div id="post-24157-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi SomeoneElse, A bit more info:</p>
<p>The error occured during transfer *.osm.bz2 to PostgreSQL database when using osm2pgsql.</p>
<p>Hardware:</p>
<ul>
<li><p>Intel(R) Xeon(R) CPU E31240 @ 3.30GHz (4x2)</p></li>
<li><p>Available RAM ~20 GB</p></li>
<li><p>HDD - 2.7 TB</p></li>
<li><p>Ubuntu 11.04</p></li>
</ul>
<p>Software:</p>
<ul>
<li><p>PostgreSQL 9.2</p></li>
<li><p>PostGIS 2.0</p></li>
<li><p>osm2pgsql 0.69</p></li>
</ul>
<p>For view and editing map style (CartoCSS) was used TileMill.</p>
<p>Pls let me know if more info is needed.</p>
</div>
<div id="comment-24157-info" class="comment-info">
<span class="comment-age">(10 Jul '13, 09:13)</span> <span class="comment-user userinfo">Agnoletti</span>
</div>
</div>
</div>
<div id="comment-tools-24141" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24141-form-container" class="comment-form-container">
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

<span id="24200"></span>

<div id="answer-container-24200" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24200-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>What is your work_mem and maintenance_work_mem in postgresql set to?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jul '13, 10:18</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-24200" class="comments-container">
<span id="24270"></span>
<div id="comment-24270" class="comment">
<div id="post-24270-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In postgresql.conf:</p>
<p>work_mem = 1024MB</p>
<p>maintenance_work_mem = 2048MB</p>
<p>shared_buffers = 1024MB</p>
<p>temp_buffers = 64MB</p>
<p>Last running command:</p>
<p>sudo -u postgres osm2pgsql -m -c -d gis --slim -C 10000 planet-latest.osm.bz2</p>
<p>Additionally:</p>
<p>Approx free RAM on the server ~20GB. Was using default configure file (styles) /usr/share/osm2pgsql/default.style</p>
</div>
<div id="comment-24270-info" class="comment-info">
<span class="comment-age">(15 Jul '13, 20:17)</span> <span class="comment-user userinfo">Agnoletti</span>
</div>
</div>
</div>
<div id="comment-tools-24200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24200-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24429"></span>

<div id="answer-container-24429" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24429-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-24429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Is there anything in the PostgreSQL server logs? It might be that you need to run a re-index on the tables as there could be some weird corruption.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jul '13, 09:34</strong></p>
<img src="https://secure.gravatar.com/avatar/b46466f8e6ef72cc352e347c1c34794f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Scott07&#39;s gravatar image" />
<p><span>Scott07</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Scott07 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24429" class="comments-container">
&#10;</div>
<div id="comment-tools-24429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24429-form-container" class="comment-form-container">
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

