+++
type = "question"
title = "Pink tiles and empty /var/lib/mod_tiles folder"
description = '''Hi, I have used my spare time the last week to set up a tile server, but I am getting tired of seeing pink tiles, so I hope someone here can help me. The setup is as follows: I have rented a Virtual server. It runs ubuntu 14.04. On the server I host some of my domains. One of these domains is lamhau...'''
date = "2015-08-29T08:10:00Z"
lastmod = "2015-08-31T17:19:00Z"
weight = 44962
keywords = [ "pink", "tiles", "empty", "mod_tile" ]
aliases = [ "/questions/44962" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Pink tiles and empty /var/lib/mod_tiles folder](/questions/44962/pink-tiles-and-empty-varlibmod_tiles-folder)

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
<span id="post-44962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-44962-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-44962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I have used my spare time the last week to set up a tile server, but I am getting tired of seeing pink tiles, so I hope someone here can help me.</p>
<p>The setup is as follows: I have rented a Virtual server. It runs ubuntu 14.04.</p>
<p>On the server I host some of my domains. One of these domains is <a href="http://lamhauge.dk">lamhauge.dk</a>. In my setup file for lamhauge.dk under /etc/apache2/sites-available I have set '/var/www/osm' as "Document root".</p>
<p>I have renamed slipperymap.html to index.htm, and changed the coordinates to be my danish hometown.</p>
<p>This means that if you enter the domain <a href="http://lamhauge.dk">lamhauge.dk</a>, you see a map - or rather, you see a lot of pink tiles. The mapnik map works fine.</p>
<p>I have followed the guide on <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/.">https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/.</a> I have imported the danish map only. None of the installations or imports has given error messages.</p>
<p>The only problem I can find is that the /var/lib/mod_tile directory is empty. When I do a 'ls -la /var/lib/mod_tile/' I get this result:</p>
<pre><code>total 8
drwxrwxrwx  2 www-data www-data 4096 aug 24 21:14 .
drwxr-xr-x 52 root     root     4096 aug 24 18:28 ..
-rwxrwxrwx  1 www-data www-data    0 aug 25 23:05 planet-import-complete</code></pre>
<p>I hope someone can give me an idea of what is wrong...</p>
<p>Thanks David</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pink" rel="tag" title="see questions tagged &#39;pink&#39;">pink</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-empty" rel="tag" title="see questions tagged &#39;empty&#39;">empty</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Aug '15, 08:10</strong></p>
<img src="https://secure.gravatar.com/avatar/35111ee49793d56171926788b6728899?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DLamhauge&#39;s gravatar image" />
<p><span>DLamhauge</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DLamhauge has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-44962" class="comments-container">
<span id="44972"></span>
<div id="comment-44972" class="comment">
<div id="post-44972-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello David,</p>
<p>without knowing a solution for you I recommend to search for "pink" on this FAQ site, because "pink tiles" are a typical error I have read years before.</p>
<p>Or do an internet search about "OSM pink tiles" or similar.</p>
</div>
<div id="comment-44972-info" class="comment-info">
<span class="comment-age">(30 Aug '15, 15:05)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="44999"></span>
<div id="comment-44999" class="comment">
<div id="post-44999-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank for your recommendation, Stephan75. I have read numerous post after searching for "pink tiles", "mod_tile", "dir empty" and the like. I have tried to put "Header set Access-Control-Allow-Origin "*" " in the config file as someone suggested, but nothing seems to help.</p>
</div>
<div id="comment-44999-info" class="comment-info">
<span class="comment-age">(31 Aug '15, 17:19)</span> <span class="comment-user userinfo">DLamhauge</span>
</div>
</div>
</div>
<div id="comment-tools-44962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-44962-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

