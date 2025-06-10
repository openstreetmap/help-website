+++
type = "question"
title = "[closed] Offline OpenStreetMap"
description = '''I have a website with a working map using leaflet and open street map. I now would like to make this work on my pc offline so I can show people, without needing an internet connection. I am only showing a small section of the world and the user doesn&#x27;t need to move much. My code for loading the map ...'''
date = "2013-10-02T02:14:00Z"
lastmod = "2019-05-22T08:42:00Z"
weight = 26903
keywords = [ "tiles", "offline" ]
aliases = [ "/questions/26903" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [\[closed\] Offline OpenStreetMap](/questions/26903/offline-openstreetmap)

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
<span id="post-26903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26903-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have a website with a working map using leaflet and open street map. I now would like to make this work on my pc offline so I can show people, without needing an internet connection. I am only showing a small section of the world and the user doesn't need to move much.</p>
<p>My code for loading the map tile is as follows:</p>
<pre><code>var openStreetMap = L.tileLayer(&#39;http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&#39;, { minZoom: 14, maxZoom: 20 });</code></pre>
<p>I suspect want something like the following - but if there's an easier way to load the map offline let me know!</p>
<pre><code>var openStreetMap = L.tileLayer(&#39;http://{s}.localhost/{z}/{x}/{y}.png&#39;, { minZoom: 14, maxZoom: 20 });</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-offline" rel="tag" title="see questions tagged &#39;offline&#39;">offline</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '13, 02:14</strong></p>
<img src="https://secure.gravatar.com/avatar/2e66d685a80927db323128f38e4e955b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JohnH&#39;s gravatar image" />
<p><span>JohnH</span><br />
<span class="score" title="36 reputation points">36</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JohnH has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>22 May '19, 10:34</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-26903" class="comments-container">
&#10;</div>
<div id="comment-tools-26903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26903-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Closed to prevent questions from help vampires" by Richard 22 May '19, 10:34

</div>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26904"></span>

<div id="answer-container-26904" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26904-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26904-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-26904-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JohnH has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This works even without a local webserver. Just use an URL like</p>
<pre><code>file:///home/jonh/openstreetmap/{z}/{x}/{y}.png</code></pre>
<p>given that your files are located under <em>/home/jonh/openstreetmap/</em>. You can also download a specific area using <a href="http://wiki.openstreetmap.org/wiki/KDE_Marble">Marble</a> and directly access its offline cache, e.g. with the URL</p>
<pre><code>file:///home/jonh/.local/share/marble/maps/earth/openstreetmap/{z}/{x}/{y}.png</code></pre>
<p>But keep the <a href="http://wiki.openstreetmap.org/wiki/Tile_usage_policy">tile usage policy</a> in mind when downloading tiles for an area.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Oct '13, 06:25</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26904" class="comments-container">
<span id="26905"></span>
<div id="comment-26905" class="comment">
<div id="post-26905-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>If you want to produce tiles for a small area, you could use Maperitive for that.</p>
</div>
<div id="comment-26905-info" class="comment-info">
<span class="comment-age">(02 Oct '13, 06:44)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="26925"></span>
<div id="comment-26925" class="comment">
<div id="post-26925-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Marble is the easiest way, just zoom into the area and it will cache the tiles, One could also download a section and load it up in JOSM, Merkaartor or even load the .osm file in Marble.</p>
</div>
<div id="comment-26925-info" class="comment-info">
<span class="comment-age">(03 Oct '13, 14:41)</span> <span class="comment-user userinfo">redsteakraw</span>
</div>
</div>
<span id="26943"></span>
<div id="comment-26943" class="comment">
<div id="post-26943-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks guys, it's working for me - I had to change the leaflet script as per here also '<a href="http://stackoverflow.com/questions/18695623/leaflet-gmapcatcher-change-zxy-template">http://stackoverflow.com/questions/18695623/leaflet-gmapcatcher-change-zxy-template</a>'. GMapCapture put the files into C:\Users\username.GMapCatcher\tiles and I included them in a folder in my web apps images directory.</p>
</div>
<div id="comment-26943-info" class="comment-info">
<span class="comment-age">(04 Oct '13, 03:23)</span> <span class="comment-user userinfo">JohnH</span>
</div>
</div>
<span id="46215"></span>
<div id="comment-46215" class="comment not_top_scorer">
<div id="post-46215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi. I have this url L.tileLayer( 'http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', how can change it and use it for local. And use map Offlien.</p>
</div>
<div id="comment-46215-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 12:52)</span> <span class="comment-user userinfo">Developer7</span>
</div>
</div>
<span id="46221"></span>
<div id="comment-46221" class="comment">
<div id="post-46221-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Which part of my answer is unclear to you?</p>
</div>
<div id="comment-46221-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 14:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46224"></span>
<div id="comment-46224" class="comment not_top_scorer">
<div id="post-46224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Does this very old example help?</p>
<p><a href="https://github.com/SomeoneElseOSM/OSMembedded/blob/master/Scripts/leaflet_embed.js">https://github.com/SomeoneElseOSM/OSMembedded/blob/master/Scripts/leaflet_embed.js</a></p>
<p>Please don't use that other than as an example (at least not without updating Leaflet). There are surely better ways to do "offline maps" now though (canned vector offerings from Mapbox is one possibility).</p>
</div>
<div id="comment-46224-info" class="comment-info">
<span class="comment-age">(29 Oct '15, 15:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46240"></span>
<div id="comment-46240" class="comment not_top_scorer">
<div id="post-46240-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My code is this L.tileLayer( 'http://{s}.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.png', when i try to change it for loacly and use map in offline mod it not works,maybe i take wrong phat?</p>
</div>
<div id="comment-46240-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 09:42)</span> <span class="comment-user userinfo">Developer7</span>
</div>
</div>
<span id="46250"></span>
<div id="comment-46250" class="comment">
<div id="post-46250-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>We can't know without you providing more details. You could also check your browser's developer console. And ideally ask a new question about your issue.</p>
</div>
<div id="comment-46250-info" class="comment-info">
<span class="comment-age">(30 Oct '15, 20:24)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="69268"></span>
<div id="comment-69268" class="comment not_top_scorer">
<div id="post-69268-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i cant solve my problem. can you make video from this tutorial? i need that. plz help me</p>
</div>
<div id="comment-69268-info" class="comment-info">
<span class="comment-age">(22 May '19, 08:42)</span> <span class="comment-user userinfo">mr jacki chan</span>
</div>
</div>
</div>
<div id="comment-tools-26904" class="comment-tools">
<span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-26904-form-container" class="comment-form-container">
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

