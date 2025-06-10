+++
type = "question"
title = "josm on local database?"
description = '''Hello all, I just startet working with OSM. I installed a local postgres/postgis database and populated it with OSM-data. Is it possible to get josm to work on that local database instead of fetching data over internet from OSM-server? I want to do exercises, play a little bit around without destoyi...'''
date = "2015-03-09T18:09:00Z"
lastmod = "2015-03-09T19:51:00Z"
weight = 41586
keywords = [ "josm", "database" ]
aliases = [ "/questions/41586" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [josm on local database?](/questions/41586/josm-on-local-database)

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
<span id="post-41586-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41586-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41586-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello all, I just startet working with OSM. I installed a local postgres/postgis database and populated it with OSM-data. Is it possible to get josm to work on that local database instead of fetching data over internet from OSM-server? I want to do exercises, play a little bit around without destoying the public server. Thanks in advance Wolfgang</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Mar '15, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/018aebbb51626e151e5dccdf3966e551?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wolfgangbremen&#39;s gravatar image" />
<p><span>wolfgangbremen</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wolfgangbremen has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41586" class="comments-container">
&#10;</div>
<div id="comment-tools-41586" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41586-form-container" class="comment-form-container">
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

<span id="41589"></span>

<div id="answer-container-41589" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41589-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41589-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-41589-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you are already running the "rails-port" you already have everything you need, just point JOSM at your API URL (see <a href="https://josm.openstreetmap.de/wiki/Help/Preferences/Connection">https://josm.openstreetmap.de/wiki/Help/Preferences/Connection</a> ).</p>
<p>If you don't have the rails port running see: <a href="https://github.com/openstreetmap/openstreetmap-website">https://github.com/openstreetmap/openstreetmap-website</a></p>
<p>Naturally you don't actually have to run it yourself, you can use the dev servers with no danger of impacting anybody else (however they don't have a lot/any data loaded).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Mar '15, 19:51</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Mar '15, 19:51</strong> </span></p>
</div>
</div>
<div id="comments-container-41589" class="comments-container">
&#10;</div>
<div id="comment-tools-41589" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41589-form-container" class="comment-form-container">
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

