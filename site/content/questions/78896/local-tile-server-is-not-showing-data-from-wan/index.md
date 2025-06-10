+++
type = "question"
title = "Local tile server , is not showing data from WAN"
description = '''Hi Guys, I have successfully installed and setup a tile server with following guide : https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/ Loaded a data for specific region and everything is working OK. However, when i try to access the data from outside, the tile&#x27;s are no...'''
date = "2021-02-17T13:03:00Z"
lastmod = "2021-02-18T13:26:00Z"
weight = 78896
keywords = [ "leaflet", "tiles", "osm", "public" ]
aliases = [ "/questions/78896" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Local tile server , is not showing data from WAN](/questions/78896/local-tile-server-is-not-showing-data-from-wan)

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
<span id="post-78896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78896-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi Guys,</p>
<p>I have successfully installed and setup a tile server with following guide : <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-18-04-lts/</a></p>
<p>Loaded a data for specific region and everything is working OK. However, when i try to access the data from outside, the tile's are not shown.</p>
<p>To be more specific on my firewall i've set up a NAT rule whenever i receive a request on port 10780, my PUBLIC_IP:10780 to forward the request to my tile server on HTTP port. Request is forwarded however on the browser nothing is shown, there're no errors in the apache's log and in the server , everything seems fine with the request its coming to the server, since i can see the public IP of the request in the access log of the apache, only with developer tools i got the following :</p>
<p><img src="https://help.openstreetmap.org/upfiles/picture.PNG" alt="alt text" /></p>
<p>I am using leaflet file and the content of the file is as below :</p>
<pre><code>&lt;!DOCTYPE html&gt;
&lt;html style=&quot;height:100%;margin:0;padding:0;&quot;&gt;
&lt;title&gt;Leaflet page with OSM render server selection&lt;/title&gt;
&lt;meta charset=&quot;utf-8&quot;&gt;
&lt;link rel=&quot;stylesheet&quot; href=&quot;https://unpkg.com/leaflet@1.3/dist/leaflet.css&quot; /&gt;
&lt;script src=&quot;https://unpkg.com/leaflet@1.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
&lt;script src=&quot;https://unpkg.com/leaflet-hash@0.2.1/leaflet-hash.js&quot;&gt;&lt;/script&gt;
&lt;style type=&quot;text/css&quot;&gt;
.leaflet-tile-container { pointer-events: auto; }
&lt;/style&gt;
&lt;/head&gt;
&lt;body style=&quot;height:100%;margin:0;padding:0;&quot;&gt;
&lt;div id=&quot;map&quot; style=&quot;height:100%&quot;&gt;&lt;/div&gt;
&lt;script&gt;
//&lt;![CDATA[
var map = L.map(&#39;map&#39;).setView([47.3686498, 8.5391825], 18);
&#10;L.tileLayer(&#39;http://192.168.155.107/hot/{z}/{x}/{y}.png&#39;, {
    attribution: &#39;&amp;copy; &lt;a href=&quot;https://www.openstreetmap.org/copyright&quot;&gt;OpenStreetMap&lt;/a&gt; contributors&#39;
}).addTo(map);
&#10;var hash = L.hash(map)
//]]&gt;
&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
index.html (END)</code></pre>
<p>If i browse the server within my LAN , <a href="http://192.168.155.107/">http://192.168.155.107/</a> everything is fine, however from outside the tile's are not shown. Can someone help with this , or had similar situation what i need to do in order to access the tile server from outside.</p>
<p>Thanks in advance guys.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-leaflet" rel="tag" title="see questions tagged &#39;leaflet&#39;">leaflet</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span> <span class="post-tag tag-link-public" rel="tag" title="see questions tagged &#39;public&#39;">public</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '21, 13:03</strong></p>
<img src="https://secure.gravatar.com/avatar/b4c6f7d35e4fd1b4561578e5e376ca06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavorB0&#39;s gravatar image" />
<p><span>DavorB0</span><br />
<span class="score" title="22 reputation points">22</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavorB0 has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '21, 13:38</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-78896" class="comments-container">
<span id="78897"></span>
<div id="comment-78897" class="comment">
<div id="post-78897-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You need to use an address that can be reached from the outside. 192.168.155.107 is a private address which probably can't be reached from the outside of your LAN, certainly not from the Internet.</p>
</div>
<div id="comment-78897-info" class="comment-info">
<span class="comment-age">(17 Feb '21, 13:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="78898"></span>
<div id="comment-78898" class="comment">
<div id="post-78898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@Scai</a> i am using my http://${PUBLIC_IP}:{PORT} to access the server. I am achieving this with NAT (network address translation) rule set on the firewall , example i am browsing <a href="http://44.44.44.44:10780">http://44.44.44.44:10780</a> , once the request comes to my firewall its forwarded to the local server 192.168.155.107 on port 80 which apache accepts it. This is not an issue, the request goes without issues, afterwards tile's are not shown for some reason.</p>
</div>
<div id="comment-78898-info" class="comment-info">
<span class="comment-age">(17 Feb '21, 13:24)</span> <span class="comment-user userinfo">DavorB0</span>
</div>
</div>
<span id="78899"></span>
<div id="comment-78899" class="comment">
<div id="post-78899-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Still, your index.html refers to 192.168.155.107. Therefore your browser tries to contact 192.168.155.107 as can be seen in the screenshot. Your browser doesn't know that 192.168.155.107 is located behind 44.44.44.44:10780. You either need to replace 192.168.155.107 with your public IP address and port (not really a good solution in this case, since both the index.html and the tiles seem to be located on the same machine) or you need to specify a relative URL to your tiles instead of an absolute one.</p>
</div>
<div id="comment-78899-info" class="comment-info">
<span class="comment-age">(17 Feb '21, 13:39)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="78928"></span>
<div id="comment-78928" class="comment">
<div id="post-78928-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai"></a><a href="https://help.openstreetmap.org/users/158/scai">@Scai</a> thank you for the hint and the explanation, it did help. Once i changed the leaflet as per your instruction, it worked as a charm.</p>
<p>Additionally, outbound rule needed to be configured on the Linux machine where the tile's are hosted.</p>
<p>Thanks again for the help.</p>
</div>
<div id="comment-78928-info" class="comment-info">
<span class="comment-age">(18 Feb '21, 13:26)</span> <span class="comment-user userinfo">DavorB0</span>
</div>
</div>
</div>
<div id="comment-tools-78896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78896-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

