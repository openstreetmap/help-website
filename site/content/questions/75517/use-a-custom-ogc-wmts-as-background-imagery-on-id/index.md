+++
type = "question"
title = "Use a custom OGC WMTS as background imagery (on ID)"
description = '''Hi, I&#x27;d like to be able to use a custom WMTS (served through a dockerized QGIS server; https://hub.docker.com/r/camptocamp/qgis-server) as background aerial imagery on the ID editor. When I try to set this up, the example given is like that: Example : https://{switch:a,b,c}.tile.openstreetmap.org/{z...'''
date = "2020-07-03T17:28:00Z"
lastmod = "2020-07-05T18:24:00Z"
weight = 75517
keywords = [ "url", "wmts", "id", "ogc", "imagery" ]
aliases = [ "/questions/75517" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Use a custom OGC WMTS as background imagery (on ID)](/questions/75517/use-a-custom-ogc-wmts-as-background-imagery-on-id)

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
<span id="post-75517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75517-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I'd like to be able to use a custom WMTS (served through a dockerized QGIS server; <a href="https://hub.docker.com/r/camptocamp/qgis-server)">https://hub.docker.com/r/camptocamp/qgis-server)</a> as background aerial imagery on the ID editor.</p>
<p>When I try to set this up, the example given is like that:</p>
<p>Example : https://{switch:a,b,c}.tile.openstreetmap.org/{zoom}/{x}/{y}.png</p>
<p>But this doesn't look like a WMTS URL.</p>
<p>This is the plain http (no https) URL I actually have for a random tile:</p>
<p><a href="http://baseurl/?SERVICE=WMTS&amp;VERSION=1.3.0&amp;REQUEST=GetTile&amp;LAYER=my_custom_layer&amp;STYLE=default&amp;TileMatrixSet=EPSG:3857&amp;TileMatrix=17&amp;TileRow=45220&amp;TileCol=65950&amp;format=image/png">http://baseurl/?SERVICE=WMTS&amp;VERSION=1.3.0&amp;REQUEST=GetTile&amp;LAYER=my_custom_layer&amp;STYLE=default&amp;TileMatrixSet=EPSG:3857&amp;TileMatrix=17&amp;TileRow=45220&amp;TileCol=65950&amp;format=image/png</a></p>
<p>How can I use it?</p>
<p>I already tried to replace the values of TileMatrix, TileRow and TileCol by {z}, {y} and {x} but it doesn't work (I also cannot see any requests arriving on the tile server).</p>
<p>Notice;<br />
the URL is working perfectly well in a web browser (Fig. 1) and in JOSM.</p>
<p><img src="https://i.stack.imgur.com/wZst0.png" alt="tile sample" /></p>
<p>Fig. 1: <em>A tile sample when I browse the previous given URL using Firefox 78.0.1 (64-bit).</em></p>
<p>Thanks.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-url" rel="tag" title="see questions tagged &#39;url&#39;">url</span> <span class="post-tag tag-link-wmts" rel="tag" title="see questions tagged &#39;wmts&#39;">wmts</span> <span class="post-tag tag-link-id" rel="tag" title="see questions tagged &#39;id&#39;">id</span> <span class="post-tag tag-link-ogc" rel="tag" title="see questions tagged &#39;ogc&#39;">ogc</span> <span class="post-tag tag-link-imagery" rel="tag" title="see questions tagged &#39;imagery&#39;">imagery</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Jul '20, 17:28</strong></p>
<img src="https://secure.gravatar.com/avatar/93c67fbeb492e14f45072515ab416289?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="s-k&#39;s gravatar image" />
<p><span>s-k</span><br />
<span class="score" title="46 reputation points">46</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="s-k has no accepted answers">0%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Jul '20, 13:10</strong> </span></p>
</div>
</div>
<div id="comments-container-75517" class="comments-container">
<span id="75519"></span>
<div id="comment-75519" class="comment">
<div id="post-75519-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do the values of "TileMatrix=", "TileCol=" and "TileRow=" correspond to {zoom},{x} and {y}?</p>
</div>
<div id="comment-75519-info" class="comment-info">
<span class="comment-age">(03 Jul '20, 18:47)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="75537"></span>
<div id="comment-75537" class="comment">
<div id="post-75537-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I think it is standardized by the OGC; I've look at the tiles numbers for some regions and it's matching the OSM tiling scheme. I also tried to replace these values in my long WMTS URL but it doesn't work.</p>
</div>
<div id="comment-75537-info" class="comment-info">
<span class="comment-age">(04 Jul '20, 19:23)</span> <span class="comment-user userinfo">s-k</span>
</div>
</div>
<span id="75539"></span>
<div id="comment-75539" class="comment">
<div id="post-75539-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Presumably if you just display</p>
<p><a href="http://baseurl/?SERVICE=WMTS&amp;VERSION=1.3.0&amp;REQUEST=GetTile&amp;LAYER=my_custom_layer&amp;STYLE=default&amp;TileMatrixSet=EPSG:3857&amp;TileMatrix=17&amp;TileRow=45220&amp;TileCol=65950&amp;format=image/png">http://baseurl/?SERVICE=WMTS&amp;VERSION=1.3.0&amp;REQUEST=GetTile&amp;LAYER=my_custom_layer&amp;STYLE=default&amp;TileMatrixSet=EPSG:3857&amp;TileMatrix=17&amp;TileRow=45220&amp;TileCol=65950&amp;format=image/png</a></p>
<p>in a browser window you do get a tile?</p>
</div>
<div id="comment-75539-info" class="comment-info">
<span class="comment-age">(05 Jul '20, 02:28)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="75540"></span>
<div id="comment-75540" class="comment not_top_scorer">
<div id="post-75540-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Indeed;</p>
<p><img src="https://i.stack.imgur.com/wZst0.png" alt="sample" /></p>
<p>In Firefox 78.0.1 (64-bit).</p>
<p>And I see the same when using JOSM. (But JOSM uses the <code>GetCapabilities</code> to let the user chose the layer before displaying it. Maybe ID should do the same?)</p>
</div>
<div id="comment-75540-info" class="comment-info">
<span class="comment-age">(05 Jul '20, 08:34)</span> <span class="comment-user userinfo">s-k</span>
</div>
</div>
<span id="75541"></span>
<div id="comment-75541" class="comment">
<div id="post-75541-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Do you use the WMTS host through SSL (https) or plain HTTP?</p>
</div>
<div id="comment-75541-info" class="comment-info">
<span class="comment-age">(05 Jul '20, 11:20)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="75542"></span>
<div id="comment-75542" class="comment not_top_scorer">
<div id="post-75542-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>standard http, as in the URL given in the main post.</p>
</div>
<div id="comment-75542-info" class="comment-info">
<span class="comment-age">(05 Jul '20, 12:53)</span> <span class="comment-user userinfo">s-k</span>
</div>
</div>
<span id="75546"></span>
<div id="comment-75546" class="comment">
<div id="post-75546-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>So your browser may not show the tiles as of a mixed content warning. See for any errors in the dev console of your browser.</p>
</div>
<div id="comment-75546-info" class="comment-info">
<span class="comment-age">(05 Jul '20, 14:30)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
<span id="75549"></span>
<div id="comment-75549" class="comment not_top_scorer">
<div id="post-75549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh,..! Actually ID itself is trying, by default, to get the tile using https, that's why it doesn't work. Any idea if I can switch ID in a standard "http" mode for querying those background imagery tiles? Otherwise I will have to check for my server to use SSL I guess...</p>
</div>
<div id="comment-75549-info" class="comment-info">
<span class="comment-age">(05 Jul '20, 17:50)</span> <span class="comment-user userinfo">s-k</span>
</div>
</div>
<span id="75551"></span>
<div id="comment-75551" class="comment not_top_scorer">
<div id="post-75551-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So I would recommend to add SSL to your server. You can use Let's Encrypt to do this without buying a certificate anywhere.</p>
</div>
<div id="comment-75551-info" class="comment-info">
<span class="comment-age">(05 Jul '20, 18:24)</span> <span class="comment-user userinfo">Spiekerooger</span>
</div>
</div>
</div>
<div id="comment-tools-75517" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-75517-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

