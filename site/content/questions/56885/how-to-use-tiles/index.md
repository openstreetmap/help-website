+++
type = "question"
title = "How to use tiles?"
description = '''Hello, I&#x27;ve followed this well done tutorial https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/ But I&#x27;m missing something... I downloaded the map &quot;azerbaijan-latest.osm.pbf&quot; but I don&#x27;t understand how to access / display it with the web browser. Must I install Javascript API? How to...'''
date = "2017-07-05T12:21:00Z"
lastmod = "2017-07-06T10:19:00Z"
weight = 56885
keywords = [ "openstreetmap", "tiles" ]
aliases = [ "/questions/56885" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to use tiles?](/questions/56885/how-to-use-tiles)

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
<span id="post-56885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56885-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-56885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I've followed this well done tutorial <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> But I'm missing something...</p>
<p>I downloaded the map "azerbaijan-latest.osm.pbf" but I don't understand how to access / display it with the web browser. Must I install Javascript API? How to use it?</p>
<p>Thanks, Matt</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Jul '17, 12:21</strong></p>
<img src="https://secure.gravatar.com/avatar/e2352f3439236c1cbb72ae94772c8186?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="matt-&#39;s gravatar image" />
<p><span>matt-</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="matt- has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-56885" class="comments-container">
&#10;</div>
<div id="comment-tools-56885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-56885-form-container" class="comment-form-container">
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

<span id="56886"></span>

<div id="answer-container-56886" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56886-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-56886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Have you seen the <a href="https://switch2osm.org/using-tiles/">Using Tiles</a> section of the guide at the bottom of "Build a tileserver" guide? That will explain how to use the tiles.</p>
<p>You mention you have a <code>.osm.pbf</code> file, but you have to import that into PostgreSQL with <code>osm2pgsql</code>. The "Loading Data" section of the <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">Building a Tile server</a> page will tell you how to import that.</p>
<p>Are you getting stuck on any particular step?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '17, 12:28</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
</div>
<div id="comments-container-56886" class="comments-container">
<span id="56887"></span>
<div id="comment-56887" class="comment">
<div id="post-56887-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello rorym,</p>
<p>This community seems to be very quick, fortunately for me!</p>
<p>Yes, I've followed the "Loading Data" and it was imported successfully. I'm stuck with "Using Tiles"; I don't know how to use my tile file with the javascript layer.</p>
</div>
<div id="comment-56887-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 12:37)</span> <span class="comment-user userinfo">matt-</span>
</div>
</div>
<span id="56888"></span>
<div id="comment-56888" class="comment">
<div id="post-56888-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You don't use the file directly with JS. You use the mod_tile based webserver. Have you followed the guide for "Using Tiles"? Have you gotten stuck on any of those bits</p>
</div>
<div id="comment-56888-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 12:49)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="56896"></span>
<div id="comment-56896" class="comment">
<div id="post-56896-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is not a lot mentioned in "Using tiles", just links to API and map providers.</p>
</div>
<div id="comment-56896-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:43)</span> <span class="comment-user userinfo">matt-</span>
</div>
</div>
<span id="56898"></span>
<div id="comment-56898" class="comment">
<div id="post-56898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There's a link to <a href="https://switch2osm.org/using-tiles/getting-started-with-leaflet/">https://switch2osm.org/using-tiles/getting-started-with-leaflet/</a> , though actually Leaflet's own site <a href="http://leafletjs.com/">http://leafletjs.com/</a> is pretty good for examples and tutorials etc.</p>
</div>
<div id="comment-56898-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56900"></span>
<div id="comment-56900" class="comment not_top_scorer">
<div id="post-56900-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It doesn't explain how to include .pbf files.</p>
</div>
<div id="comment-56900-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:58)</span> <span class="comment-user userinfo">matt-</span>
</div>
</div>
<span id="56901"></span>
<div id="comment-56901" class="comment not_top_scorer">
<div id="post-56901-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> describes what to do with pbf files - add the data from them to a database with osm2pgsql, then make tiles available using "mod_tile" and "apache".</p>
</div>
<div id="comment-56901-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 14:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56903"></span>
<div id="comment-56903" class="comment not_top_scorer">
<div id="post-56903-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes. But once it's available, how do you use it?</p>
</div>
<div id="comment-56903-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 14:43)</span> <span class="comment-user userinfo">matt-</span>
</div>
</div>
<span id="56904"></span>
<div id="comment-56904" class="comment not_top_scorer">
<div id="post-56904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think you might need to explain a bit more what the problem is. You've asked "how do you use it?" in a comment on an answer that links to "how you use it" so there's clearly a miscommunication happening somewhere.</p>
<p>We don't know what you've done and what you haven't done; we don't know what works for you and what doesn't. All we know is that you see no tiles. That could be down to any one of an OS problem, web server, mod_tile, fonts, node version, data loading and probably many more.</p>
<p>Perhaps it would help to add an OSM diary entry (or a Github, gist, or some other way of sharing a reasonable amont of text) explaining what you did and what happened. For example, when you typed "renderd -f -c /usr/local/etc/renderd.conf" as per the instructions, what happened? When you pointed a web browser at <a href="http://yourserveripaddress/hot/0/0/0.png">http://yourserveripaddress/hot/0/0/0.png</a> , what happened then?</p>
</div>
<div id="comment-56904-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 14:50)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56910"></span>
<div id="comment-56910" class="comment not_top_scorer">
<div id="post-56910-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're right, I was not enough specific.</p>
<p>I managed to go some steps further. I included the Leaflet library.</p>
<p>Now, on this page : <a href="https://switch2osm.org/using-tiles/getting-started-with-leaflet/">https://switch2osm.org/using-tiles/getting-started-with-leaflet/</a> , in the "leafletembed.js" file, we load the map on South-England. That works.</p>
<p>In this tutorial : <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> , we download and insert the map of Azerbaijan in the database. How can I read it with my web browser?</p>
</div>
<div id="comment-56910-info" class="comment-info">
<span class="comment-age">(06 Jul '17, 07:48)</span> <span class="comment-user userinfo">matt-</span>
</div>
</div>
<span id="56914"></span>
<div id="comment-56914" class="comment">
<div id="post-56914-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>At the bit in <a href="https://switch2osm.org/using-tiles/getting-started-with-leaflet/">https://switch2osm.org/using-tiles/getting-started-with-leaflet/</a> where it says "Point a web browser at: <a href="http://yourserveripaddress/hot/0/0/0.png">http://yourserveripaddress/hot/0/0/0.png"</a> - that's the first point in the process where you're testing that you can read it with your web browser. If that doesn't work, then you'll need to backtrack - look at what was displayed when you ran "renderd -f -c /usr/local/etc/renderd.conf", for example.</p>
</div>
<div id="comment-56914-info" class="comment-info">
<span class="comment-age">(06 Jul '17, 10:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56886" class="comment-tools">
<span class="comments-showing"> showing 5 of 10 </span> <a href="#" class="show-all-comments-link">show 5 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-56886-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="56890"></span>

<div id="answer-container-56890" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-56890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-56890-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-56890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In addition to Rorym's answer, there's another option mentioned over at <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> - if you're using the Chrome or Chromium browser you can add an add-on to that that allows you to rewrite parts of URLs. This allows you to see your tiles on the <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> site. Basically, install this add-on:</p>
<pre><code>https://chrome.google.com/webstore/detail/switcheroo-redirector/cnmciclhnghalnpfhhleggldniplelbg?hl=en</code></pre>
<p>Click on the little "S" that appears to the right of the address bar and add "<strong>tile-a.openstreetmap.fr/hot/</strong>" in the "From" column and something like "<strong>mywebserverurl/maps/hot/</strong>" in the "To" column, then add the same rule twice more for “<strong>tile-b</strong>” and “<strong>tile-c”</strong>. Then when you browse to <a href="https://www.openstreetmap.org/">https://www.openstreetmap.org/</a> (http, not https) and select the "Humanitarian" layer, you'll see your tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Jul '17, 13:26</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-56890" class="comments-container">
<span id="56891"></span>
<div id="comment-56891" class="comment">
<div id="post-56891-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually, that's the only part of the procedure that didn't work. I don't see my tiles.</p>
</div>
<div id="comment-56891-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:28)</span> <span class="comment-user userinfo">matt-</span>
</div>
</div>
<span id="56892"></span>
<div id="comment-56892" class="comment">
<div id="post-56892-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You're definitely trying http not https?</p>
</div>
<div id="comment-56892-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56893"></span>
<div id="comment-56893" class="comment">
<div id="post-56893-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Trying http</p>
</div>
<div id="comment-56893-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:34)</span> <span class="comment-user userinfo">matt-</span>
</div>
</div>
<span id="56894"></span>
<div id="comment-56894" class="comment">
<div id="post-56894-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>Example screenshot</span></p>
</div>
<div id="comment-56894-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:39)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56895"></span>
<div id="comment-56895" class="comment">
<div id="post-56895-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><img src="/upfiles/2017-07-05_14_40_30-.png" alt="screenshot" /></p>
<p>I've just realized... There is no "hot" folder on my server. Should it be put in /var/www/hot ?</p>
</div>
<div id="comment-56895-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:42)</span> <span class="comment-user userinfo">matt-</span>
</div>
</div>
<span id="56897"></span>
<div id="comment-56897" class="comment not_top_scorer">
<div id="post-56897-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just chose "hot" as a convenient folder name - if your tiles are somewhere else, just add "somewhere else" in the "to" part of each switcheroo line. For completeness, the full path to an example HOT tile is something like <a href="http://tile-a.openstreetmap.fr/hot/9/253/166.png">http://tile-a.openstreetmap.fr/hot/9/253/166.png</a> where "9" is the zoom, 253 the "x" co-ordinate and 166 the "y" co-ordinate.</p>
</div>
<div id="comment-56897-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="56899"></span>
<div id="comment-56899" class="comment not_top_scorer">
<div id="post-56899-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I set "hot" as per the guide <a href="https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/">https://switch2osm.org/manually-building-a-tile-server-16-04-2-lts/</a> . I created "hot" folder in /var/www, yet it doesn't work.</p>
</div>
<div id="comment-56899-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 13:53)</span> <span class="comment-user userinfo">matt-</span>
</div>
</div>
<span id="56902"></span>
<div id="comment-56902" class="comment not_top_scorer">
<div id="post-56902-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Where the tiles get created is controlled by /usr/local/etc/renderd.conf . It's likely then when you run renderd, you're getting some sort of error. That's why it says to run renderd in the foreground first ("renderd -f -c /usr/local/etc/renderd.conf") and check that tiles are rendered by pointing a web browser at <a href="http://yourserveripaddress/hot/0/0/0.png">http://yourserveripaddress/hot/0/0/0.png</a> .</p>
</div>
<div id="comment-56902-info" class="comment-info">
<span class="comment-age">(05 Jul '17, 14:41)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-56890" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-56890-form-container" class="comment-form-container">
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

