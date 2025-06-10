+++
type = "question"
title = "Adding countries to an existing OSM Tile Server"
description = '''Hello, I&#x27;ve followed the tutorial @ https://switch2osm.org/manually-building-a-tile-server-18-04-lts/. Since building a tile server for all of Europe took too long I&#x27;ve started with Germany. The map server is working fine. I have pre-rendered all tiles for zoom level 1 to 12. Now I wanted to add oth...'''
date = "2018-12-18T17:52:00Z"
lastmod = "2018-12-21T10:29:00Z"
weight = 67267
keywords = [ "add", "countries" ]
aliases = [ "/questions/67267" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Adding countries to an existing OSM Tile Server](/questions/67267/adding-countries-to-an-existing-osm-tile-server)

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
<span id="post-67267-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67267-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67267-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I've followed the tutorial @ https://switch2osm.org/manually-building-a-tile-server-18-04-lts/. Since building a tile server for all of Europe took too long I've started with Germany. The map server is working fine. I have pre-rendered all tiles for zoom level 1 to 12.</p>
<p>Now I wanted to add other countries to complete Europe but the new data is not showing up on the lower zoom levels.</p>
<p>I used the command: osm2pgsql ... --append --slim -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 20000 --number-processes 2 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/liechtenstein-latest.osm.pbf</p>
<p>This command finished without problems. I can not see Liechtenstein in any zoom level above 13. If I zoom to 13 or 14 it renders the new tiles on the fly and its working fine. If I zoom out tho the map just turns blank. I see no borders or anything. I tried to render with the force command and it seems to pre-render the tiles again. Atleast the timestamp on the file is new, yet no visible changes can be seen. I used the following command:</p>
<p>render_list -f -a -z 1 -Z 7 -n 1 -m ajt -s /var/run/renderd/renderd.sock</p>
<p>What am I missing or doing wrong?</p>
<p>with kind regards, Karl</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-add" rel="tag" title="see questions tagged &#39;add&#39;">add</span> <span class="post-tag tag-link-countries" rel="tag" title="see questions tagged &#39;countries&#39;">countries</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Dec '18, 17:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2a837616ba3a40ffb05281918e20a35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Karl%20Gustav&#39;s gravatar image" />
<p><span>Karl Gustav</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Karl Gustav has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67267" class="comments-container">
<span id="67271"></span>
<div id="comment-67271" class="comment">
<div id="post-67271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could it be a browser caching issue?</p>
</div>
<div id="comment-67271-info" class="comment-info">
<span class="comment-age">(18 Dec '18, 19:18)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="67292"></span>
<div id="comment-67292" class="comment">
<div id="post-67292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've tried different devices and browsers, cleared caches on all of them and pulled the the rendered tiles via wget and they show as blank images.</p>
</div>
<div id="comment-67292-info" class="comment-info">
<span class="comment-age">(20 Dec '18, 12:24)</span> <span class="comment-user userinfo">Karl Gustav</span>
</div>
</div>
</div>
<div id="comment-tools-67267" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67267-form-container" class="comment-form-container">
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

<span id="67293"></span>

<div id="answer-container-67293" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67293-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67293-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-67293-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Karl Gustav has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If you've reloaded the data then you'll need to:</p>
<ul>
<li>Stop and restart apache</li>
<li>Stop and restart renderd</li>
<li>Clear your local browser cache</li>
</ul>
<p>You may also want to:</p>
<ul>
<li>remove previously-rendered "blank" tiles from disk altogether. You can append /status to find the on-disk path for a particular path, see e.g. <a href="https://map.atownsend.org.uk/hot/9/253/166.png/status">https://map.atownsend.org.uk/hot/9/253/166.png/status</a> .</li>
<li>force-rerender tiles using e.g. /dirty for an individual tile - <a href="https://map.atownsend.org.uk/hot/9/253/166.png/dirty">https://map.atownsend.org.uk/hot/9/253/166.png/dirty</a> .</li>
</ul>
<p>I wrote some scripts for doing these sorts of things on a map site I look after - see <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_render.sh">here</a>, <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style/blob/master/update_carto.sh">here</a> and <a href="https://github.com/SomeoneElseOSM/SomeoneElse-style-legend/blob/master/rerender_legend.sh">here</a>. These won't be useful to you exactly as they stand, but they will be helpful for showing examples of the things above that I've said you'll need to do.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Dec '18, 16:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Dec '18, 16:04</strong> </span></p>
</div>
</div>
<div id="comments-container-67293" class="comments-container">
<span id="67306"></span>
<div id="comment-67306" class="comment">
<div id="post-67306-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, with /dirty and /status I got the "broken" tiles to rerender properly.</p>
</div>
<div id="comment-67306-info" class="comment-info">
<span class="comment-age">(21 Dec '18, 10:29)</span> <span class="comment-user userinfo">Karl Gustav</span>
</div>
</div>
</div>
<div id="comment-tools-67293" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67293-form-container" class="comment-form-container">
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

