+++
type = "question"
title = "How to serve OSM mapnik tiles on Windows with Apache for leafLet.js"
description = '''Hi. So I have pre-rendered tiles on Windows using mapnik python scripts. Now I want to serve and route them somehow to our web application. I think we want to use leafLet.js or something like this. I&#x27;ve been googling for solutions and I found many and I think that TileCache will be best: http://tile...'''
date = "2017-01-20T22:29:00Z"
lastmod = "2017-01-24T10:02:00Z"
weight = 54208
keywords = [ "windows", "leaflet", "mapnik", "tileserver" ]
aliases = [ "/questions/54208" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to serve OSM mapnik tiles on Windows with Apache for leafLet.js](/questions/54208/how-to-serve-osm-mapnik-tiles-on-windows-with-apache-for-leafletjs)

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
<span id="post-54208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54208-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-54208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi. So I have pre-rendered tiles on Windows using mapnik python scripts. Now I want to serve and route them somehow to our web application. I think we want to use leafLet.js or something like this. I've been googling for solutions and I found many and I think that TileCache will be best: <a href="http://tilecache.org/docs/README.html">http://tilecache.org/docs/README.html</a> What is your experience with this? What would you recommend for Windows Server 2012 64-bit ?</p>
<p>P.S. Don't tell me to use Linux, I hate Linux, so I am only looking for Windows solutions.</p>
<p>Thank you :-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Jan '17, 22:29</strong></p>
<img src="https://secure.gravatar.com/avatar/f98ed179efe75af596090a497cefeb90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Koles500&#39;s gravatar image" />
<p><span>Koles500</span><br />
<span class="score" title="68 reputation points">68</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Koles500 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-54208" class="comments-container">
<span id="54209"></span>
<div id="comment-54209" class="comment">
<div id="post-54209-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would suggest using Linux as base system! :-) SCNR Have a nice weekend, everyone!</p>
</div>
<div id="comment-54209-info" class="comment-info">
<span class="comment-age">(20 Jan '17, 22:34)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="54210"></span>
<div id="comment-54210" class="comment">
<div id="post-54210-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I asked not to recommend me damn Linux. Please read carefuly and answer only if you have something worth sharing. Thank you.</p>
</div>
<div id="comment-54210-info" class="comment-info">
<span class="comment-age">(20 Jan '17, 22:36)</span> <span class="comment-user userinfo">Koles500</span>
</div>
</div>
<span id="54211"></span>
<div id="comment-54211" class="comment">
<div id="post-54211-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For various reasons, people doing stuff with Windows servers on OSM is fairly rare. However I'm not sure I understand the problem here. It sounds like you:</p>
<ul>
<li>Don't have lots of zoom levels (based on the other question you asked)</li>
<li>Don't want to render tiles for a huge area (likewise), so no need to render on demand.</li>
<li>Don't want to update tiles based on live changes to OSM</li>
</ul>
<p>In that case wouldn't you just copy the tiles you've generated to the web server that's serving them whenever you need to? Clearly I'm missing something here, because if that was the case you wouldn't be asking the question here :)</p>
<p>Would it be possible to explain in a bit more detail what you want the "missing bit in the middle" to do?</p>
</div>
<div id="comment-54211-info" class="comment-info">
<span class="comment-age">(20 Jan '17, 22:53)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="54212"></span>
<div id="comment-54212" class="comment not_top_scorer">
<div id="post-54212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I am getting over various difficulties with pre-rendering and we will have soon nice pre-rendered Europe with quite many zoom levels and symbols, etc. The thing is I have no idea o.O how to serve these tiles to our web application, in other words how to change data source to our other server where I keep these tiles. The tiles are generated in some weird folder structure e.g. C:\Tiles\10\486\330.png - how do I route this thing ?? leafLet.js seems to use X,Y,Z.png HTTP query which looks reasonable, but how to translate such query to tiles rendered by mapnik ?</p>
</div>
<div id="comment-54212-info" class="comment-info">
<span class="comment-age">(20 Jan '17, 22:57)</span> <span class="comment-user userinfo">Koles500</span>
</div>
</div>
<span id="54215"></span>
<div id="comment-54215" class="comment">
<div id="post-54215-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>The good news is that the weird folder structure is what leaflet is expecting. For example, if I look at a tile being served by leaflet at osm.org that covers Tuam at zoom 9 I see <a href="https://a.tile.openstreetmap.org/9/243/165.png">https://a.tile.openstreetmap.org/9/243/165.png</a> . That's what Leaflet expects, and you can (on Linux) have something that plugs into Apache to make that available from a more compact file format or (on any platform) just serve the file at that address.</p>
<p>The problem that you may have with this is that you'll have a <em>lot</em> of small files, possibly too many to reasonably manage on a web server. The Linux "mod_tile / renderd" combination solves this by only rendering tiles on demand, and storing them in larger metatiles (search for "metatile" at <a href="https://github.com/openstreetmap/mod_tile">https://github.com/openstreetmap/mod_tile</a> for more info). There may be something that does this for windows, but I doubt it. Leaflet itself does support various plugins though: <a href="http://leafletjs.com/plugins.html">http://leafletjs.com/plugins.html</a> .</p>
</div>
<div id="comment-54215-info" class="comment-info">
<span class="comment-age">(20 Jan '17, 23:18)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="54218"></span>
<div id="comment-54218" class="comment not_top_scorer">
<div id="post-54218-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I am still positivly thinking about continuing this work on Windows and trying zoom levels 1-16 for whole Europe. What are your reasons to say that "having a lot of small files, possibly too many to reasonably manage on a web server" ?</p>
</div>
<div id="comment-54218-info" class="comment-info">
<span class="comment-age">(21 Jan '17, 00:05)</span> <span class="comment-user userinfo">Koles500</span>
</div>
</div>
<span id="54255"></span>
<div id="comment-54255" class="comment not_top_scorer">
<div id="post-54255-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The "having a lot of small files" point was because I've seen that cause problems on some OSes (QNX most noticably, but also Linux I expect if you're not prepared for the number of inodes you'll need). I've no idea whether modern Windows filesystems would have that problem.</p>
</div>
<div id="comment-54255-info" class="comment-info">
<span class="comment-age">(23 Jan '17, 13:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="54263"></span>
<div id="comment-54263" class="comment">
<div id="post-54263-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You can use mbtiles with leaflet &amp; should work OK with Windows. You will need a utility to convert your 'weird' directory structure to mbtiles. Take a look at this example <a href="https://gitlab.com/IvanSanchez/Leaflet.TileLayer.MBTiles/tree/master">https://gitlab.com/IvanSanchez/Leaflet.TileLayer.MBTiles/tree/master</a></p>
</div>
<div id="comment-54263-info" class="comment-info">
<span class="comment-age">(24 Jan '17, 10:02)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54208" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-54208-form-container" class="comment-form-container">
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

<span id="54251"></span>

<div id="answer-container-54251" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54251-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54251-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-54251-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you are familiar with python I would suggest to use <a href="https://docs.python.org/2/library/simplehttpserver.html">SimpleHTTPServer</a>.</p>
<p>And if you want to create your own http server using python here is <a href="http://pwp.stevecassidy.net/wsgi/static.html">the blog</a>.</p>
<p>And for enterprise grade solution check <a href="http://nginx.org/en/docs/windows.html">nginx</a>, please see the tutorial for <a href="https://www.nginx.com/resources/admin-guide/serving-static-content/">serving static content</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Jan '17, 11:55</strong></p>
<img src="https://secure.gravatar.com/avatar/39d75f04e1a21ba653b41ac75ec1b026?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gagan&#39;s gravatar image" />
<p><span>Gagan</span><br />
<span class="score" title="305 reputation points">305</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gagan has 2 accepted answers">14%</span></p>
</div>
</div>
<div id="comments-container-54251" class="comments-container">
&#10;</div>
<div id="comment-tools-54251" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54251-form-container" class="comment-form-container">
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

