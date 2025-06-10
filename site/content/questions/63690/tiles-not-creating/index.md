+++
type = "question"
title = "Tiles not creating"
description = '''Hello I am very new to openstreetmap, I am building my own Tiles server by following this  https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ I belived , i have done all right, all matches. i see a Small world map when i browser  http://192.168.1.32/hot/0/0/0.png but when i am tryin...'''
date = "2018-05-24T14:15:00Z"
lastmod = "2018-05-24T20:42:00Z"
weight = 63690
keywords = [ "rendering" ]
aliases = [ "/questions/63690" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Tiles not creating](/questions/63690/tiles-not-creating)

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
<span id="post-63690-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63690-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-63690-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello I am very new to openstreetmap, I am building my own Tiles server by following this <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> I belived , i have done all right, all matches. i see a Small world map when i browser <a href="http://192.168.1.32/hot/0/0/0.png">http://192.168.1.32/hot/0/0/0.png</a> but when i am trying to create some tiles by following switcheroo-configured Chrome. with link <a href="https://www.openstreetmap.org/#map=8/23.572/91.686">https://www.openstreetmap.org/#map=8/23.572/91.686</a> by selecting Humanitarian, <strong>Its blank</strong> I dont see any log when i do this tail -f /var/log/syslog | grep " TILE " does it mean its not tiling ? Can any one Please help me with this please . Please let me know if you need any out from my server.</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 May '18, 14:15</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-63690" class="comments-container">
<span id="63691"></span>
<div id="comment-63691" class="comment">
<div id="post-63691-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello fosiul,</p>
<p>Could you give us more details on how you configured the “Switcheroo Redirector” extension ?</p>
<p>Thanks !</p>
</div>
<div id="comment-63691-info" class="comment-info">
<span class="comment-age">(24 May '18, 15:04)</span> <span class="comment-user userinfo">jbelien</span>
</div>
</div>
<span id="63693"></span>
<div id="comment-63693" class="comment">
<div id="post-63693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Jbelien Please see the attached picture, I have used From : <a href="https://tile-a.openstreetmap.fr/hot/">https://tile-a.openstreetmap.fr/hot/</a> to: <a href="http://192.168.1.32/hot/">http://192.168.1.32/hot/</a></p>
<p>From : <a href="https://tile-b.openstreetmap.fr/hot/">https://tile-b.openstreetmap.fr/hot/</a> to: <a href="http://192.168.1.32/hot/">http://192.168.1.32/hot/</a></p>
<p>From : <a href="https://tile-c.openstreetmap.fr/hot/">https://tile-c.openstreetmap.fr/hot/</a> to: <a href="http://192.168.1.32/hot/">http://192.168.1.32/hot/</a></p>
</div>
<div id="comment-63693-info" class="comment-info">
<span class="comment-age">(24 May '18, 15:59)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63694"></span>
<div id="comment-63694" class="comment">
<div id="post-63694-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure if it's a cache problem, but I don't see an attached picture. Perhaps store it at an external image host and link to it from here?</p>
</div>
<div id="comment-63694-info" class="comment-info">
<span class="comment-age">(24 May '18, 16:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="63695"></span>
<div id="comment-63695" class="comment">
<div id="post-63695-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi here is the link <a href="https://ibb.co/ktLeT8">https://ibb.co/ktLeT8</a></p>
</div>
<div id="comment-63695-info" class="comment-info">
<span class="comment-age">(24 May '18, 16:11)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63696"></span>
<div id="comment-63696" class="comment">
<div id="post-63696-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Apart from that, Can i not just Generate Tiles from the DB? While reading , I understand, i can use "generate_tiles.py"</p>
<p>Since I have followed this tutorial <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a></p>
<p>and if i want to generate my own tiles with "generate_tiles.py" what do i have to do ?</p>
<p>Thanks for the help</p>
</div>
<div id="comment-63696-info" class="comment-info">
<span class="comment-age">(24 May '18, 16:31)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63698"></span>
<div id="comment-63698" class="comment not_top_scorer">
<div id="post-63698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok I am uploading anoter image. <a href="https://ibb.co/hdEL1T">https://ibb.co/hdEL1T</a></p>
<p>if i Chose one option ( tick) then I can see map showing but they are broken, although i can map, but i dont think they actulling rendering in my disk . becuase the size of bellow it never increased.</p>
<p>renderaccount@opentile2:/var/www/html$ du -sh /var/lib/mod_tile 40K /var/lib/mod_tile renderaccount@opentile2:/var/www/html$</p>
</div>
<div id="comment-63698-info" class="comment-info">
<span class="comment-age">(24 May '18, 17:02)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63701"></span>
<div id="comment-63701" class="comment not_top_scorer">
<div id="post-63701-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was just getting ready to write a similar post :-)</p>
<p>I've got what appears to be the same issue, but have looked in Chrome's console and found the Content Security Policy is blocking images from loading. <a href="https://help.openstreetmap.org/users/15162/fosiul">@fosiul</a>, have you used Chrome's developer tools to see if you have any errors/notices in the browser?</p>
<p>I've gone further and cobbled some html/css/javascript (leaflet) code on the server. I can show maps from there using the MapBox service, but the same code on my server shows a blank map canvas.</p>
<p>I will post a full write up here in a few moments.</p>
</div>
<div id="comment-63701-info" class="comment-info">
<span class="comment-age">(24 May '18, 17:34)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63702"></span>
<div id="comment-63702" class="comment not_top_scorer">
<div id="post-63702-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15162/fosiul">@fosiul</a>, You're seeing some maps load when you un-tick the parts of the redirector extension because the browser is going to openstreetmap.org to get the data.</p>
</div>
<div id="comment-63702-info" class="comment-info">
<span class="comment-age">(24 May '18, 17:37)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-63690" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63690-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="63707"></span>

<div id="answer-container-63707" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63707-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63707-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-63707-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fosiul has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We now have a content security policy in place where the server indicates to the browser what sites we expect various sorts of resources to load from, so if you trick the browser into using a different source like this then it will get rejected by that policy.</p>
<p>If you look at the javascript console you should errors telling you the CSP is being violated by those load attempts.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '18, 18:45</strong></p>
<img src="https://secure.gravatar.com/avatar/dee41dcf0aa0c08cf6b0eb935b7504b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TomH&#39;s gravatar image" />
<p><span>TomH ♦♦</span><br />
<span class="score" title="3325 reputation points"><span>3.3k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="43 badges"><span class="bronze">●</span><span class="badgecount">43</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TomH has 9 accepted answers">20%</span></p>
</div>
</div>
<div id="comments-container-63707" class="comments-container">
<span id="63710"></span>
<div id="comment-63710" class="comment">
<div id="post-63710-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>131Refused to load the image '&lt;url&gt;' because it violates the following Content Security Policy directive: "img-src 'self' data: &lt;url&gt; .wp.com .tile.openstreetmap.org .tile.thunderforest.com .openstreetmap.fr piwik.openstreetmap.org developer.mapquest.com".</p>
<p>/#map=13/23.7498/90.4408&amp;layers=H:1 Refused to load the image 'http://192.168.1.32/hot/13/6154/3539.png' because it violates the following Content Security Policy directive: "img-src 'self' data: www.gravatar.com .wp.com .tile.openstreetmap.org .tile.thunderforest.com .openstreetmap.fr piwik.openstreetmap.org developer.mapquest.com".</p>
</div>
<div id="comment-63710-info" class="comment-info">
<span class="comment-age">(24 May '18, 18:53)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63711"></span>
<div id="comment-63711" class="comment">
<div id="post-63711-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/15162/fosiul"></a><a href="https://help.openstreetmap.org/users/15162/fosiul">@fosiul</a>, Please let us know if putting your own leaflet-based website in place lets you render maps.</p>
<p><a href="https://help.openstreetmap.org/users/1/tomh"></a><a href="https://help.openstreetmap.org/users/1/tomh">@tomh</a>, Thank you for the confirmation.</p>
</div>
<div id="comment-63711-info" class="comment-info">
<span class="comment-age">(24 May '18, 18:56)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
</div>
<div id="comment-tools-63707" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63707-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63705"></span>

<div id="answer-container-63705" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63705-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like someone has (very recently) changed something that's broken this use of switcheroo. My guess is that it's at the osm.org end rather than in Chrome or Switcheroo. For more background about what this particular bit of browser nannying is supposed to do, see <a href="https://www.html5rocks.com/en/tutorials/security/content-security-policy/#source-whitelists">here</a>.</p>
<p>In the meantime, a simple leaflet-based website is probably the way to go. There are lots of leaflet examples around, and <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site">here</a> is a simple one I created earlier.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '18, 18:30</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 May '18, 18:41</strong> </span></p>
</div>
</div>
<div id="comments-container-63705" class="comments-container">
<span id="63712"></span>
<div id="comment-63712" class="comment">
<div id="post-63712-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>, I will have a look at that one you mentioned, however ,</p>
<p>Can I not Generate tile from the Database ? Since I have followed this tutorial , <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a></p>
<p>what is the best way to Genrate tiles from DB ?</p>
</div>
<div id="comment-63712-info" class="comment-info">
<span class="comment-age">(24 May '18, 18:56)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
<span id="63717"></span>
<div id="comment-63717" class="comment">
<div id="post-63717-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you want to generate lots of tiles then have a look at <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load</a> - there's a render_list example there and also a "just the tiles in one area" one.</p>
</div>
<div id="comment-63717-info" class="comment-info">
<span class="comment-age">(24 May '18, 20:42)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-63705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63705-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="63714"></span>

<div id="answer-container-63714" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63714-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi , Regards to <a href="https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site">https://wiki.openstreetmap.org/wiki/User:SomeoneElse/Ubuntu_1804_tileserver_load#An_example_site</a></p>
<p>I think, i am doing somethig silly , to make rendering, i typed this <a href="http://192.168.1.32/map/map.html">http://192.168.1.32/map/map.html</a> with bellow changles, but nothing happend. not sure if i am doing right.</p>
<pre><code>renderaccount@opentile2:/var/www/html/map$ ls -lrt total 24
-rw-r--r-- 1 root root 1422 May 24 19:05 permalink.html drwxr-xr-x 4 root root 4096 May 24 19:12 leaflet-dist drwxr-xr-x 3 root root 4096 May 24 19:14 control drwxr-xr-x 2 root root 4096 May 24 19:27 Scripts
-rw-r--r-- 1 root root 1324 May 24 19:30 map.html renderaccount@opentile2:/var/www/html/map$</code></pre>
<p>I Edited Scripts/leaflet_embed_small.js</p>
<p>var hetznerUrl='//192.168.1.32/hot/{z}/{x}/{y}.png'; var osmUrl='//192.168.1.32/hot/{z}/{x}/{y}.png'; var deUrl='//192.168.1.32/hot/{z}/{x}/{y}.png'; var os201604Url='//192.168.1.32/hot/{z}/{x}/{y}.png'; var wikiUrl='//192.168.1.32/hot/{z}/{x}/{y}.png'; var gps2Url='//192.168.1.32/hot/{z}/{x}/{y}.png'; var mapillaryUrl='//192.168.1.32/hot/{z}/{x}/{y}.png'; var osdiffUrl='//192.168.1.32/hot/{z}/{x}/{y}.png';</p>
<p>edited map.html</p>
<pre><code>renderaccount@opentile2:/var/www/html/map$ cat map.html
&lt;html&gt;
  &lt;head&gt;
&lt;!--    &lt;meta name=&quot;viewport&quot; content=&quot;user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=device-width, height=device-height&quot; /&gt;&lt;/meta&gt; --&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1&quot; /&gt;&lt;/meta&gt;
    &lt;title&gt;Useful Maps&lt;/title&gt;
    &lt;link rel=&quot;stylesheet&quot; type=&quot;text/css&quot; href=&quot;leaflet_dist/leaflet.css&quot; /&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;leaflet_dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;control/Permalink.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;control/Permalink.Marker.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;control/Permalink.Layer.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;control/Permalink.Overlay.js&quot;&gt;&lt;/script&gt;
    &lt;script type=&quot;text/javascript&quot; src=&quot;Scripts/leaflet_embed_small.js&quot;&gt;&lt;/script&gt;
  &lt;/head&gt;
  &lt;body onload=&quot;initmap();&quot;&gt;
    &lt;div id=&quot;rest&quot; style=&quot;font-size:40%&quot;&gt;
      &lt;button id=&quot;button6&quot; onclick=&quot;layers_on();&quot; &gt;Controls&lt;/button&gt;
      &lt;button id=&quot;button7&quot; onclick=&quot;layers_off();&quot; &gt;Off&lt;/button&gt;
      &lt;button id=&quot;button1&quot; onclick=&quot;pan_centre();&quot; &gt;Centre&lt;/button&gt;
      &lt;button id=&quot;button2&quot; onclick=&quot;pan_legend();&quot; &gt;Legend&lt;/button&gt;
      &lt;button id=&quot;button3&quot; onclick=&quot;show_changelog();&quot; &gt;Changelog&lt;/button&gt;
    &lt;/div&gt;
    &lt;div id=&quot;map&quot; style=&quot;position:absolute;top:40px;left:0;right:0;bottom:0;font-size:30%&quot;&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 May '18, 19:45</strong></p>
<img src="https://secure.gravatar.com/avatar/7bb2a94f867841b58214be09992831d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosiul&#39;s gravatar image" />
<p><span>fosiul</span><br />
<span class="score" title="96 reputation points">96</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosiul has one accepted answer">50%</span></p>
</div>
</div>
<div id="comments-container-63714" class="comments-container">
<span id="63715"></span>
<div id="comment-63715" class="comment">
<div id="post-63715-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Before you added the files, did you get the Ubuntu/Apache "It Works!" page to show up?</p>
<p>Now, after you added the code, do you still get that page?</p>
<p>BTW, I suggest you post a new question for this issue. It isn't really an answer for your first question.</p>
</div>
<div id="comment-63715-info" class="comment-info">
<span class="comment-age">(24 May '18, 20:07)</span> <span class="comment-user userinfo">tim_rohrer</span>
</div>
</div>
<span id="63716"></span>
<div id="comment-63716" class="comment">
<div id="post-63716-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>@tim_roher Yes, I agree with you, i will create a new question for this .</p>
<p>Thanks</p>
</div>
<div id="comment-63716-info" class="comment-info">
<span class="comment-age">(24 May '18, 20:19)</span> <span class="comment-user userinfo">fosiul</span>
</div>
</div>
</div>
<div id="comment-tools-63714" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63714-form-container" class="comment-form-container">
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

