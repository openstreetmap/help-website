+++
type = "question"
title = "Pink tiles instead of map"
description = '''Hi all, I&#x27;ve just built an OSM server as per the instructions on www.switch2osm.org using the package method. Everything seems to be working ok. I am able to browse the map on localhost the ubuntu server. The only problem is when I use an browser on the external IP address, all the tiles appear in p...'''
date = "2012-09-13T22:09:00Z"
lastmod = "2014-05-03T18:26:00Z"
weight = 16050
keywords = [ "pink", "map", "tiles", "localhost" ]
aliases = [ "/questions/16050" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Pink tiles instead of map](/questions/16050/pink-tiles-instead-of-map)

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
<span id="post-16050-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16050-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16050-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I've just built an OSM server as per the instructions on www.switch2osm.org using the package method. Everything seems to be working ok. I am able to browse the map on localhost the ubuntu server. The only problem is when I use an browser on the external IP address, all the tiles appear in pink.</p>
<p>I have read that this maybe a cross domain browsing issue with apache. If anyone else has experienced this issue can they let me know and what solution you found.</p>
<p>Thanks in advance,</p>
<p>Dave</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pink" rel="tag" title="see questions tagged &#39;pink&#39;">pink</span> <span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-localhost" rel="tag" title="see questions tagged &#39;localhost&#39;">localhost</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '12, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/a4a6d4c69a4768aa486878b00720901c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davieg&#39;s gravatar image" />
<p><span>Davieg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davieg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16050" class="comments-container">
<span id="16079"></span>
<div id="comment-16079" class="comment">
<div id="post-16079-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you don't get any reply on this help site, you might better contact the OSM developers community through its mailing list at dev@openstreetmap.org. (subscription required, see the <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">mailing list doc</a>)</p>
</div>
<div id="comment-16079-info" class="comment-info">
<span class="comment-age">(14 Sep '12, 11:41)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="16224"></span>
<div id="comment-16224" class="comment">
<div id="post-16224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Based on the other information (socket bind failures etc.) I'm not sure that what you're seeing a purely a cross-site-scripting issue. As Pieren says, you'll probably get more response on the "dev" mailing list or perhaps on one of the <a href="https://wiki.openstreetmap.org/wiki/IRC">IRC channels</a> (e.g. #osm or #osm-dev).</p>
<p>Is the Ubuntu server a physical box or a VM, and if a VM how is networking set up?</p>
<p>When you say "I can browse the map" does that mean that you've got an OL or Leaflet-based map on the same Ubuntu server as well? If so, when you browse to the root of the webserver from your remote browser do you get an "It works!" page?</p>
</div>
<div id="comment-16224-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 16:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-16050" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16050-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="25060"></span>

<div id="answer-container-25060" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25060-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-25060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just found an answer to the pink tile problem. Just edit your /var/www/osm/slippymap.html file and change "localhost" to the external IP address of your map server. For me, this was the IP address of the bridged network virtual card on VirtualBox. Maps now show up.</p>
<p>I tracked this problem by right clicking the broken image and trying to open it in a new browser window. The URL contained "localhost" rather than the IP of the map server.</p>
<p>Geoff</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '13, 07:50</strong></p>
<img src="https://secure.gravatar.com/avatar/52ff2ce08336ff151c3a558682596192?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Snowpaddler&#39;s gravatar image" />
<p><span>Snowpaddler</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Snowpaddler has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-25060" class="comments-container">
<span id="25092"></span>
<div id="comment-25092" class="comment">
<div id="post-25092-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>In order to prevent this confusion the upstream slippymap.html file has been changed to use relative URLs. However, this hasn't yet made it into the packages linked to from switch2osm.org.</p>
<p>However, I have now added a comment regarding this issue to switch2osm.org which hopefully clarifies this and prevents people of running into this issue in the future.</p>
</div>
<div id="comment-25092-info" class="comment-info">
<span class="comment-age">(08 Aug '13, 20:48)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
</div>
<div id="comment-tools-25060" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25060-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16331"></span>

<div id="answer-container-16331" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16331-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16331-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-16331-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi datendelphin,</p>
<p>Thanks for your help. I think I made too mank changes to the config files which caused the binding error. I rolled back the PC to a previous configuration ( I'm using vmware) and started to troubleshoot again. I realised I made a schoolboy error. I never changed the IP address for the map server in the slippymap.html file. That explains why it worked on the local host and not on a remote PC. Once I made that change everything worked fine. Maybe this post may help others avoid my mistake.</p>
<p>Thanks again.</p>
<p>Dave</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '12, 23:16</strong></p>
<img src="https://secure.gravatar.com/avatar/86fe7151ce2322a4242bae79d4250c76?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="davieg&#39;s gravatar image" />
<p><span>davieg</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="davieg has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-16331" class="comments-container">
&#10;</div>
<div id="comment-tools-16331" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16331-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="16113"></span>

<div id="answer-container-16113" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-16113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-16113-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-16113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should include</p>
<p><code>Header set Access-Control-Allow-Origin "*"</code></p>
<p>in your apache config, next to the lines where you configure mod-tile (look for the LoadTileConfigFile keyword). It should be inside the virtual host you have your tile server running in.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Sep '12, 13:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0697f0a3c5fdeff1999768f7df9cb2af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="datendelphin&#39;s gravatar image" />
<p><span>datendelphin</span><br />
<span class="score" title="234 reputation points">234</span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="datendelphin has one accepted answer">14%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Sep '12, 20:34</strong> </span></p>
</div>
</div>
<div id="comments-container-16113" class="comments-container">
<span id="16219"></span>
<div id="comment-16219" class="comment">
<div id="post-16219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi datendelphin,</p>
<p>Thanks for responding to my question. I built the server using the instructions on this page (<a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/)">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/)</a> so I didn't have too much configuration to do. I'm new enough to Linux and am just working my way around it. Which apache config file do I edit is it httpd.conf or httpd-vhosts.conf. There is no mention of mod-tile in http-vhosts.conf and httpd.conf is blank,</p>
<p>Thanks for your help on this ,</p>
<p>Dave</p>
</div>
<div id="comment-16219-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 14:06)</span> <span class="comment-user userinfo">Davieg</span>
</div>
</div>
<span id="16220"></span>
<div id="comment-16220" class="comment">
<div id="post-16220-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just checked the errors that appear when apache restarts and here's what I get: /usr/sbin/apache2ctl: 87: ulimit: error setting limit (Operation not permitted) [Tue Sep 18 13:43:03 2012] [notice] Committing tile config default [Tue Sep 18 13:43:03 2012] [notice] Loading tile config default at /osm/ for zooms 0 - 18 from tile directory /var/lib/mod_tile with extension .png and mime type image/png apache2: apr_sockaddr_info_get() failed for NT-LIS-SR-05.nettronics apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.0.1 for ServerName</p>
</div>
<div id="comment-16220-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 14:46)</span> <span class="comment-user userinfo">Davieg</span>
</div>
</div>
<span id="16221"></span>
<div id="comment-16221" class="comment">
<div id="post-16221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>/usr/sbin/apache2ctl: 87: ulimit: error setting limit (Operation not permitted) [Tue Sep 18 13:43:03 2012] [notice] Committing tile config default [Tue Sep 18 13:43:03 2012] [notice] Loading tile config default at /osm/ for zooms 0 - 18 from tile directory /var/lib/mod_tile with extension .png and mime type image/png apache2: apr_sockaddr_info_get() failed for NT-LIS-SR-05.nettronics apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.0.1 for ServerName (13)Permission denied: make_sock: could not bind to address 0.0.0.0:80 no listening sockets available</p>
</div>
<div id="comment-16221-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 14:46)</span> <span class="comment-user userinfo">Davieg</span>
</div>
</div>
<span id="16222"></span>
<div id="comment-16222" class="comment">
<div id="post-16222-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>, shutting down Unable to open logs Action 'start' failed. The Apache error log may have more information.</p>
<p>I dont know if this helps with the problem,</p>
<p>Dave</p>
</div>
<div id="comment-16222-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 14:47)</span> <span class="comment-user userinfo">Davieg</span>
</div>
</div>
<span id="16229"></span>
<div id="comment-16229" class="comment">
<div id="post-16229-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You might have other problems as well. "Permission denied: make_sock: could not bind to address 0.0.0.0:80" does not look good.</p>
<p>As to where to add the line I suggested:</p>
<p>grep -rn LoadTileConfigFile /etc/apache2/</p>
<p>should tell you which file to edit.</p>
</div>
<div id="comment-16229-info" class="comment-info">
<span class="comment-age">(18 Sep '12, 20:37)</span> <span class="comment-user userinfo">datendelphin</span>
</div>
</div>
</div>
<div id="comment-tools-16113" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-16113-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32847"></span>

<div id="answer-container-32847" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32847-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">http://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a></p>
<p>"If you are not opening slippymap.html on localhost and you are seeing only pink tiles, you will need to edit the html page and replace localhost with the correct server name in ‘new OpenLayers.Layer.OSM(“Local Tiles”…’ or change it to a relative URL."</p>
<p>you need to restart the rendering daemon --&gt; sudo /etc/init.d/renderd restart</p>
<p>It worked for me.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '14, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/60374a0eb625cfe525668f70cf3e4f16?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gisAnal&#39;s gravatar image" />
<p><span>gisAnal</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gisAnal has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32847" class="comments-container">
&#10;</div>
<div id="comment-tools-32847" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32847-form-container" class="comment-form-container">
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

