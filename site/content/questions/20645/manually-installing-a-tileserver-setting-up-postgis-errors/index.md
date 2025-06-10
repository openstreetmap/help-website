+++
type = "question"
title = "Manually Installing a TileServer: Setting up PostGIS (errors)"
description = '''Hello everybody. I&#x27;m a complete Ubuntu newbie who&#x27;s trying to set up a tile server by following the instructions on http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/ We are running Ubuntu 12.04.2 LTS on VMware Everything goes fine until we need to &quot;Set up PostGIS on the post...'''
date = "2013-03-11T21:25:00Z"
lastmod = "2013-03-12T16:32:00Z"
weight = 20645
keywords = [ "setup", "instructions", "error", "postgis", "tileserver" ]
aliases = [ "/questions/20645" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Manually Installing a TileServer: Setting up PostGIS (errors)](/questions/20645/manually-installing-a-tileserver-setting-up-postgis-errors)

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
<span id="post-20645-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20645-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20645-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everybody. I'm a complete Ubuntu newbie who's trying to set up a tile server by following the instructions on <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/">http://switch2osm.org/serving-tiles/manually-building-a-tile-server-12-04/</a></p>
<p>We are running Ubuntu 12.04.2 LTS on VMware</p>
<p>Everything goes fine until we need to "Set up PostGIS on the postresql database". We enter the "psql -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql -d gis" as instructed.</p>
<p>Instead of the expected output, we get a long list of errors that are like the following "error type "geometry[]" does not exist postgres tileserver"</p>
<p>There are also errors for things like "geometry" etc. This becomes a problem with the next step, where we try to assign ownership. We get an error "relation "geometry_columns" does not exist"</p>
<p>I'm assuming that there is some error when the gis table is populated, but we can't figure out what. Does anyone have any ideas that would point us in the right direction?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-instructions" rel="tag" title="see questions tagged &#39;instructions&#39;">instructions</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Mar '13, 21:25</strong></p>
<img src="https://secure.gravatar.com/avatar/131a10817452bc8a8cb3175af7296255?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MatThePhat&#39;s gravatar image" />
<p><span>MatThePhat</span><br />
<span class="score" title="36 reputation points">36</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MatThePhat has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20645" class="comments-container">
&#10;</div>
<div id="comment-tools-20645" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20645-form-container" class="comment-form-container">
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

<span id="20646"></span>

<div id="answer-container-20646" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20646-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20646-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-20646-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="MatThePhat has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In these situations the root error cause is often the first message that appears, and the rest are only follow-on problems. Try redirecting the error output of your command to a file:</p>
<pre><code>psql -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql -d gis &gt; errors.txt 2&gt;&amp;1</code></pre>
<p>then check the file errors.txt and look at the first unhealthy line(s) and report.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Mar '13, 21:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-20646" class="comments-container">
<span id="20674"></span>
<div id="comment-20674" class="comment">
<div id="post-20674-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you for your advice! We were able to figure out the problem, it had to do with our username in ubuntu vs. our username in postgres being different.</p>
</div>
<div id="comment-20674-info" class="comment-info">
<span class="comment-age">(12 Mar '13, 16:32)</span> <span class="comment-user userinfo">MatThePhat</span>
</div>
</div>
</div>
<div id="comment-tools-20646" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20646-form-container" class="comment-form-container">
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

