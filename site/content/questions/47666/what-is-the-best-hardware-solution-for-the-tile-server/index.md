+++
type = "question"
title = "What is the best hardware solution for the tile server?"
description = '''Hi everyone! I&#x27;ve installed the tile server on a separate machine using SWITCH2OSM Manually building a tile server (14.04) and I&#x27;ve changed mapstyle to openstreetmap-carto. Everything works fine, but at 6-7-8 scales tile generation takes about couple of minutes. I have used PostGIS Tuning, PG Tune, ...'''
date = "2016-01-27T13:37:00Z"
lastmod = "2016-01-28T10:50:00Z"
weight = 47666
keywords = [ "carto", "postgresql", "mapnik" ]
aliases = [ "/questions/47666" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [What is the best hardware solution for the tile server?](/questions/47666/what-is-the-best-hardware-solution-for-the-tile-server)

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
<span id="post-47666-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47666-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47666-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>I've installed the tile server on a separate machine using <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-14-04/">SWITCH2OSM Manually building a tile server (14.04)</a> and I've changed mapstyle to <a href="https://github.com/gravitystorm/openstreetmap-carto">openstreetmap-carto</a>. Everything works fine, but at 6-7-8 scales tile generation takes about couple of minutes.</p>
<p>I have used <a href="https://wiki.openstreetmap.org/wiki/User:Species/PostGIS_Tuning">PostGIS Tuning</a>, <a href="https://github.com/gregs1104/pgtune">PG Tune</a>, <a href="http://pgtune.leopard.in.ua/">PG Tune Online</a>, I have tried to use dozen of PostgreSQL configurations, but tile generation is not fast enough.</p>
<p>My hardware configuration is:</p>
<ul>
<li>Intel(R) Xeon(R) CPU E5-2630 v2 <a href="http://help.openstreetmap.org/users/2422/25or6to4">@2</a>.60GHz</li>
<li>32GB RAM</li>
<li>SSD RAID-5</li>
</ul>
<p>I thought it would be enough.</p>
<p>So the question is: "What is the best hardware solution for the tile server?". I want tile generation to take couple of seconds.</p>
<p>Thanks for help!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-carto" rel="tag" title="see questions tagged &#39;carto&#39;">carto</span> <span class="post-tag tag-link-postgresql" rel="tag" title="see questions tagged &#39;postgresql&#39;">postgresql</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Jan '16, 13:37</strong></p>
<img src="https://secure.gravatar.com/avatar/b747822a88415ab0a0e16accce9fa477?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bobinho&#39;s gravatar image" />
<p><span>Bobinho</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bobinho has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47666" class="comments-container">
<span id="47667"></span>
<div id="comment-47667" class="comment">
<div id="post-47667-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A couple of questions that may help people answer:</p>
<p>o How much data are you importing?</p>
<p>o Are you planning to update the data periodically?</p>
</div>
<div id="comment-47667-info" class="comment-info">
<span class="comment-age">(27 Jan '16, 13:43)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="47668"></span>
<div id="comment-47668" class="comment">
<div id="post-47668-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hello. 1. The whole world 2. May be once a year</p>
</div>
<div id="comment-47668-info" class="comment-info">
<span class="comment-age">(27 Jan '16, 13:45)</span> <span class="comment-user userinfo">Bobinho</span>
</div>
</div>
<span id="47671"></span>
<div id="comment-47671" class="comment">
<div id="post-47671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What performance are you getting (at which zoom and which location), and what did you expect ?</p>
</div>
<div id="comment-47671-info" class="comment-info">
<span class="comment-age">(27 Jan '16, 14:32)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="47699"></span>
<div id="comment-47699" class="comment">
<div id="post-47699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think it could be normal that the tiles for z6-8 take some significant amount of time to render, usually they are not rendered very often but only from time to time on demand. These zoom levels contain a big amount of data and are covering big areas so that the spatial index has less effect than in higher zoom levels.</p>
</div>
<div id="comment-47699-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 10:48)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-47666" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47666-form-container" class="comment-form-container">
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

<span id="47669"></span>

<div id="answer-container-47669" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47669-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47669-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-47669-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You have to accept that tile generation on small zoom levels takes a couple of minutes, and pre-render these tiles in regular intervals. That's what OSM itself does too! The alternative is changing to vector tile technology altogether but then you'd have to re-generate the vector tiles in regular intervals which isn't much faster.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Jan '16, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-47669" class="comments-container">
<span id="47670"></span>
<div id="comment-47670" class="comment">
<div id="post-47670-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>If his update schedule is "once a year", pre-generating shouldn't be a problem.</p>
</div>
<div id="comment-47670-info" class="comment-info">
<span class="comment-age">(27 Jan '16, 14:31)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="47687"></span>
<div id="comment-47687" class="comment">
<div id="post-47687-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have .meta files already, I don't work with .png itself. So, the only way to share not rendered tiles on 6-7-8 zoom levels is pre-render, right?</p>
<p>And it doesn't matter which hardware you have, anyway it will take couple of minutes, yes?</p>
</div>
<div id="comment-47687-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 06:20)</span> <span class="comment-user userinfo">Bobinho</span>
</div>
</div>
<span id="47700"></span>
<div id="comment-47700" class="comment">
<div id="post-47700-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>if you keep the whole database in memory it will speed rendering up a lot</p>
</div>
<div id="comment-47700-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 10:50)</span> <span class="comment-user userinfo">dieterdreist</span>
</div>
</div>
</div>
<div id="comment-tools-47669" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47669-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="47688"></span>

<div id="answer-container-47688" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-47688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47688-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Blockquote And it doesn't matter which hardware you have, anyway it will take couple of minutes, yes?</p>
</blockquote>
<p>Well, I guess you could get yourself one of these: <a href="https://www.oracle.com/engineered-systems/exalytics/features.html">https://www.oracle.com/engineered-systems/exalytics/features.html</a></p>
<p>But I don't think you envisioned needing to buy a new "house" when installing a new home tile server, because that is probably what a true professional business solution like this one is going to cost you...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '16, 07:32</strong></p>
<img src="https://secure.gravatar.com/avatar/dc8a1ef54d3e25744ee52d1ad1459a81?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mboeringa&#39;s gravatar image" />
<p><span>mboeringa</span><br />
<span class="score" title="1542 reputation points"><span>1.5k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mboeringa has 4 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-47688" class="comments-container">
<span id="47689"></span>
<div id="comment-47689" class="comment">
<div id="post-47689-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, I guess so.</p>
<p>The only way is to pre-render tiles.</p>
<p>Where I can find how many GBs I must have to render the whole world on 11 zoom level? This table <a href="http://wiki.openstreetmap.org/wiki/Tile_disk_usage">http://wiki.openstreetmap.org/wiki/Tile_disk_usage</a> is not valid for meta-files. Thank you</p>
</div>
<div id="comment-47689-info" class="comment-info">
<span class="comment-age">(28 Jan '16, 07:51)</span> <span class="comment-user userinfo">Bobinho</span>
</div>
</div>
</div>
<div id="comment-tools-47688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-47688-form-container" class="comment-form-container">
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

