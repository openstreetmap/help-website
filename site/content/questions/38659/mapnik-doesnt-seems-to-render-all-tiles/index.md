+++
type = "question"
title = "Mapnik doesn&#x27;t seems to render all tiles."
description = '''Hello! First, excuse my (very) bad English ... I’m here to gather some help about map rendering :p I&#x27;m currently trying to make a local tile server with Graphhopper ( router ), and Leaflet.JS ( for interactive maps ). I download the OSM file for the Alsace country ( in France ). Imported the OSM to ...'''
date = "2014-11-19T02:46:00Z"
lastmod = "2014-11-19T13:53:00Z"
weight = 38659
keywords = [ "mapnik" ]
aliases = [ "/questions/38659" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Mapnik doesn't seems to render all tiles.](/questions/38659/mapnik-doesnt-seems-to-render-all-tiles)

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
<span id="post-38659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38659-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>Hello!</strong></p>
<p>First, excuse my (very) bad English ... I’m here to gather some help about map rendering :p</p>
<p>I'm currently trying to make a local tile server with Graphhopper ( router ), and Leaflet.JS ( for interactive maps ). I download the OSM file for the Alsace country ( in France ).</p>
<p>Imported the OSM to a PostGre Database with osm2pgsql, then rendering tiles with mapnik ( zoomlevel 0 to 16 ). Everything worked fines, but ... Mapnik doesn't seems to render all tiles, some parts, but not all.</p>
<p>Here is a sample capture to demonstrate : <a href="http://i.imgur.com/wD8q4wM.png">http://i.imgur.com/wD8q4wM.png</a> ( the grey part are the missing tiles ) We can easily find what tiles/coordinates are missing with HTTP sniffing ( for example with the Firefox Dev tools ).</p>
<p>Should I generate tiles with Mapnik and OSM file directly ?</p>
<p><strong>Thank you in advance! :)</strong></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Nov '14, 02:46</strong></p>
<img src="https://secure.gravatar.com/avatar/b5c4b79805499e2f869ec8a7cbd83079?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FoxyAntho&#39;s gravatar image" />
<p><span>FoxyAntho</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FoxyAntho has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-38659" class="comments-container">
&#10;</div>
<div id="comment-tools-38659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38659-form-container" class="comment-form-container">
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

<span id="38660"></span>

<div id="answer-container-38660" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-38660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-38660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-38660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My first idea is a time-out from your tile server, not a problem in mapnik itself. The time to render a tile varies a lot. We should analyze your config and the logs of the software calling mapnik to see why some tiles are absent (renderd ?). I know there is a timeout configurable and you can also set the quadtile size. This all depends on your machine perfs.<br />
Tu peux aussi contacter la liste de diffusion <a href="https://lists.openstreetmap.org/listinfo/dev-fr">dev-fr@openstreetmap.org</a> pour parler avec d'autres devs fr qui ont le même type d'expérience que toi (inscription nécessaire) ou <a href="http://forum.openstreetmap.fr/index.php">le forum fr</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Nov '14, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span> </br></p>
</div>
</div>
<div id="comments-container-38660" class="comments-container">
<span id="38664"></span>
<div id="comment-38664" class="comment">
<div id="post-38664-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><strong>Thanks for your reply :)</strong></p>
<p>I'm not using Renderd but Manpnik to generate tiles files.</p>
<p>Why I know they are a missing : I look-up at Apache logs --&gt; 404 ( not found error ).</p>
</div>
<div id="comment-38664-info" class="comment-info">
<span class="comment-age">(19 Nov '14, 13:24)</span> <span class="comment-user userinfo">FoxyAntho</span>
</div>
</div>
<span id="38665"></span>
<div id="comment-38665" class="comment">
<div id="post-38665-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>mapnik is generating tiles but apache is not calling mapnik directly. You need a plugin in apache that is checking if tiles have to be (re)rendered and sends a render request to a "mapnik rendering job manager", either done by tirex or renderd deamons. These deamons can drop a render request if it takes too long to serve the tile to the web client. But timeout is configurable. Again, contact the dev or dev-fr mailing lists to get more info. This help site is more for newcomers, not devs.</p>
</div>
<div id="comment-38665-info" class="comment-info">
<span class="comment-age">(19 Nov '14, 13:53)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-38660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-38660-form-container" class="comment-form-container">
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

