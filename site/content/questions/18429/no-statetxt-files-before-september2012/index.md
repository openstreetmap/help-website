+++
type = "question"
title = "[closed] No state.txt files before September/2012?"
description = '''I&#x27;ve been trying to create a local replica of the main OSM database for a few months now, and ran into all sort of problems. The most serious is a crash in osmosis when loading the full planet.osm into a PostgreSQL database, described here. I do run into this problem if I try to load a planet.osm fi...'''
date = "2012-12-13T21:11:00Z"
lastmod = "2012-12-14T11:16:00Z"
weight = 18429
keywords = [ "state.txt", "planet.osm", "osm", "osmosis" ]
aliases = [ "/questions/18429" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] No state.txt files before September/2012?](/questions/18429/no-statetxt-files-before-september2012)

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
<span id="post-18429-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18429-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18429-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've been trying to create a local replica of the main OSM database for a few months now, and ran into all sort of problems. The most serious is a crash in osmosis when loading the full planet.osm into a PostgreSQL database, described <a href="https://trac.openstreetmap.org/ticket/4597">here</a>.</p>
<p>I do run into this problem if I try to load a planet.osm file from September/2012, but NOT if I load a planet.osm file from ca. 01/Aug/2012.</p>
<p>However, after the (august) planet.osm file is loaded, to setup the replication process, I need the state.txt file from some time before, but near, the age of the main planet.osm, and for that I tried to use the <a href="http://toolserver.org/~mazder/replicate-sequences/">tool</a> listed in the osmosis's documentation contained <a href="https://wiki.openstreetmap.org/wiki/Planet.osm/diffs#Using_the_replication_diffs">here</a>.</p>
<p>To my great surprise, there aren't any files from before 12/Sep/2012! This file has the first sequence number (000/000/001) so there is no way to access state.txt files from dates before that.</p>
<p>My question (at last) is:</p>
<ul>
<li>Is there any other location where old state.txt files could be obtained?</li>
</ul>
<p>(or)</p>
<ul>
<li>Is there any other way to configure the replication of the OSM database without resorting to the state.txt files?</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-state.txt" rel="tag" title="see questions tagged &#39;state.txt&#39;">state.txt</span> <span class="post-tag tag-link-planet.osm" rel="tag" title="see questions tagged &#39;planet.osm&#39;">planet.osm</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Dec '12, 21:11</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>19 Sep '13, 21:50</strong> </span></p>
</div>
</div>
<div id="comments-container-18429" class="comments-container">
&#10;</div>
<div id="comment-tools-18429" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18429-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "The question is answered, right answer was accepted" by MCPicoli 19 Sep '13, 21:50

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18432"></span>

<div id="answer-container-18432" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18432-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MCPicoli has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The old state files are available at <a href="http://planet.openstreetmap.org/cc-by-sa">http://planet.openstreetmap.org/cc-by-sa</a> but we have changed the license between August and now, and you cannot legally take an old planet file and update it with new diffs. This would create a chimera that is of both the new and old licenses simultaneously.</p>
<p>If you really wanted to make an Osmosis import of a current planet file without changing Osmosis, you could probably import all nodes first, and then in a second step prepare an .osc file that contains all the ways and relations and update your database with that.</p>
<p>But before you do - are you absolutely sure that you need (a) the whole planet and (b) in APIDB format? Many people make an APIDB import only to find out later that they had been much better served by e.g. an imposm or osm2pgsql import.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Dec '12, 21:55</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-18432" class="comments-container">
<span id="18446"></span>
<div id="comment-18446" class="comment">
<div id="post-18446-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks!</p>
<p>Given that a database older than the license change would not be correctly updated, I'll not try to load the Aug/2012 file anymore. However, the problem (a.k.a. "crash") within osmosis persist.</p>
<p>Onto the question of "why" having the full planet loaded in APIDB format, the answer is "because I can"... What is the point of the project being so "open", if one is not able to fully replicate it anywhere, anytime? Also, for me all the process, the troubles and the solutions are a huge tool for developing skills on the technologies involved and related.</p>
</div>
<div id="comment-18446-info" class="comment-info">
<span class="comment-age">(14 Dec '12, 11:16)</span> <span class="comment-user userinfo">MCPicoli</span>
</div>
</div>
</div>
<div id="comment-tools-18432" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18432-form-container" class="comment-form-container">
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

