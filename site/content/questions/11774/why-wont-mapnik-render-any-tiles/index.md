+++
type = "question"
title = "Why won&#x27;t Mapnik render any tiles?"
description = '''I am using Ubuntu 11.10 32 bit. I have followed the instructions from here but am not getting any tiles on the map (localhost/osm/slippymap.html) when I select &quot;local tiles&quot;. It works properly when I select &quot;Mapnik&quot; (which gets the tiles from openstreetmap). Firebug shows multiple &quot;NetworkError: 404...'''
date = "2012-04-06T16:32:00Z"
lastmod = "2013-02-22T05:16:00Z"
weight = 11774
keywords = [ "tiles", "mapnik", "mod_tile" ]
aliases = [ "/questions/11774" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Why won't Mapnik render any tiles?](/questions/11774/why-wont-mapnik-render-any-tiles)

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
<span id="post-11774-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11774-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11774-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using Ubuntu 11.10 32 bit. I have followed the instructions from <a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">here</a> but am not getting any tiles on the map (localhost/osm/slippymap.html) when I select "local tiles". It works properly when I select "Mapnik" (which gets the tiles from openstreetmap). Firebug shows multiple "NetworkError: 404 Not Found - <a href="http://localhost/osm/x/xxx/xxx.png">http://localhost/osm/x/xxx/xxx.png".</a> Indeed there are no tiles in var/lib/mod_tile. When I enter "localhost/mod_tile" I get 'NoResp' on everything. When I enter render_list -f -a I get "socket connect failed for: /tmp/osm-renderd". I think the import of .osm into PostgreSQL went properly; the messages returned looked like those described <a href="http://switch2osm.org/serving-tiles/manually-building-a-tile-server/">here</a> (under the Importing data into the database section) and I can see data in the database through pgAdmin. I set permissions on var/lib/mod_tile to 777. Is Mapnik not communicating with mod_tile? Contents of etc/renderd.conf is:</p>
<p>[renderd] stats_file=/var/run/renderd/renderd.stats socketname=/var/run/renderd/renderd.sock num_threads=4 tile_dir=/var/lib/mod_tile ; DOES NOT WORK YET [mapnik] plugins_dir=/usr/lib/mapnik/0.7/input font_dir=/usr/share/fonts/truetype/ttf-dejavu font_dir_recurse=false [default] URI=/osm/ XML=/etc/mapnik-osm-data/osm.xml ;HOST=tile.openstreetmap.org ;HTCPHOST=proxy.openstreetmap.org</p>
<p>I see that "DOES NOT WORK YET" but am unsure what, exactly, doesn't work since this tutorial says that one should have a working tileserver if everything goes OK.</p>
<p>Contents of /var/run/renderd/renderd.stats is '0' for everthing.</p>
<p>I'm totally new to mapping, new to PostgreSQL and fairly new to linux. Thanks for any help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Apr '12, 16:32</strong></p>
<img src="https://secure.gravatar.com/avatar/af8387f11be652a161c9771b36caf25b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidLR&#39;s gravatar image" />
<p><span>DavidLR</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidLR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11774" class="comments-container">
&#10;</div>
<div id="comment-tools-11774" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11774-form-container" class="comment-form-container">
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

<span id="11851"></span>

<div id="answer-container-11851" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11851-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-11851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In the end I re-installed Ubuntu 11.10, deleting everything from the previous install. Ran all Ubuntu updates, then ran the script, installed pgAdmin, set a password and granted superuser privileges to 'www-data', changed /etc/postgresql/9.1/main/pg_hba.conf to 'trust' on both 'local alls', ran osm2psql using www-data user and password, and I now generate my own tiles. This script works perfectly on a fresh install; one that's been used and abused, no.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Apr '12, 23:10</strong></p>
<img src="https://secure.gravatar.com/avatar/af8387f11be652a161c9771b36caf25b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidLR&#39;s gravatar image" />
<p><span>DavidLR</span><br />
<span class="score" title="71 reputation points">71</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidLR has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11851" class="comments-container">
<span id="20141"></span>
<div id="comment-20141" class="comment">
<div id="post-20141-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi David, please give us the commande lines that resolved your problem. Thank you</p>
</div>
<div id="comment-20141-info" class="comment-info">
<span class="comment-age">(22 Feb '13, 03:18)</span> <span class="comment-user userinfo">Yahya_Romdhane</span>
</div>
</div>
<span id="20143"></span>
<div id="comment-20143" class="comment">
<div id="post-20143-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you explain more precisely</p>
</div>
<div id="comment-20143-info" class="comment-info">
<span class="comment-age">(22 Feb '13, 04:57)</span> <span class="comment-user userinfo">Yahya_Romdhane</span>
</div>
</div>
<span id="20145"></span>
<div id="comment-20145" class="comment">
<div id="post-20145-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have the same problem and I resolved itbut not perfectly because I still unable to display tiles from an other computer Did you resolve this problem?</p>
</div>
<div id="comment-20145-info" class="comment-info">
<span class="comment-age">(22 Feb '13, 05:16)</span> <span class="comment-user userinfo">Yahya_Romdhane</span>
</div>
</div>
</div>
<div id="comment-tools-11851" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11851-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="11790"></span>

<div id="answer-container-11790" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-11790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-11790-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-11790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just had this exact problem.</p>
<p>I followed the step's 'ben' took in the following thread.</p>
<p><a href="http://www.bitchx.com/log/osm-o/osm-o-05-May-2010/osm-o-05-May-2010-02.php">http://www.bitchx.com/log/osm-o/osm-o-05-May-2010/osm-o-05-May-2010-02.php</a></p>
<p>to resolve my problems i ran 'renderd -f' and saw that it was failing on www-data not have accessing to the database. (I had used my own usernames etc.. when setting everything up). I gave www-data ownership of the gis db, and now everything is running fine, and when I switch to local tiles, I have data!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '12, 23:41</strong></p>
<img src="https://secure.gravatar.com/avatar/9ef4e665e6e82f6b5f08952ff8c69d23?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="John%20Perrin&#39;s gravatar image" />
<p><span>John Perrin</span><br />
<span class="score" title="76 reputation points">76</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="John Perrin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-11790" class="comments-container">
<span id="11852"></span>
<div id="comment-11852" class="comment">
<div id="post-11852-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>didn't work for me, but thanks. Also tried granting public all to each table, still, no good. I just re-installed everything.</p>
</div>
<div id="comment-11852-info" class="comment-info">
<span class="comment-age">(09 Apr '12, 23:16)</span> <span class="comment-user userinfo">DavidLR</span>
</div>
</div>
<span id="20144"></span>
<div id="comment-20144" class="comment">
<div id="post-20144-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I have the same problem and I resolved itbut not perfectly because I still unable to display tiles from an other computers. Did you resolve this problem?</p>
</div>
<div id="comment-20144-info" class="comment-info">
<span class="comment-age">(22 Feb '13, 05:15)</span> <span class="comment-user userinfo">Yahya_Romdhane</span>
</div>
</div>
</div>
<div id="comment-tools-11790" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-11790-form-container" class="comment-form-container">
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

