+++
type = "question"
title = "slow tile render or even not render with error code 500-504"
description = '''Hi. I&#x27;m developing project with your osm soft. Now i have the problem with slow rendering or not rendering tiles. Can it cause to many requests from 1 ip address? Or some other reason?'''
date = "2018-10-31T13:06:00Z"
lastmod = "2019-02-06T18:14:00Z"
weight = 66602
keywords = [ "tiles", "slow", "tileserver" ]
aliases = [ "/questions/66602" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [slow tile render or even not render with error code 500-504](/questions/66602/slow-tile-render-or-even-not-render-with-error-code-500-504)

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
<span id="post-66602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66602-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-66602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi.</p>
<p>I'm developing project with your osm soft. Now i have the problem with slow rendering or not rendering tiles. Can it cause to many requests from 1 ip address? Or some other reason?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '18, 13:06</strong></p>
<img src="https://secure.gravatar.com/avatar/7027e9d763a398bfb9f9a67fdae4f09b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jedi&#39;s gravatar image" />
<p><span>jedi</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jedi has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-66602" class="comments-container">
<span id="66605"></span>
<div id="comment-66605" class="comment">
<div id="post-66605-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>You'll need to provide more information about what you're doing. Is this a tile renderer you've set up yourself (and if so, which one and how did you set it up?), or are you using an existing rendering service? We'll also need to know how you're using the tiles (e.g. in an app, a website, etc.).</p>
</div>
<div id="comment-66605-info" class="comment-info">
<span class="comment-age">(31 Oct '18, 16:35)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="66606"></span>
<div id="comment-66606" class="comment">
<div id="post-66606-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My project is under angular 6. I'm using leaflet library as <a href="https://github.com/Asymmetrik/ngx-leaflet">ng module</a>. But settings is simple and similar as <a href="https://leafletjs.com/index.html">here</a>.</p>
<pre><code>let LAYER_OSM = {
  id: &#39;openstreetmap&#39;,
  name: &#39;Open Street Map&#39;,
  enabled: true,
  layer: L.tileLayer(&#39;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&#39;, {
    maxZoom: 18,
    attribution: &#39;Open Street Map&#39;
  })
};</code></pre>
<p>But sometimes tile loading is very slow or even not loading.</p>
<p><img src="https://help.openstreetmap.org/upfiles/map1_4WuMymD.png" alt="alt text" /> <img src="https://help.openstreetmap.org/upfiles/map2.png" alt="alt text" /> <img src="https://help.openstreetmap.org/upfiles/map3.png" alt="alt text" /></p>
</div>
<div id="comment-66606-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 08:44)</span> <span class="comment-user userinfo">jedi</span>
</div>
</div>
<span id="66610"></span>
<div id="comment-66610" class="comment">
<div id="post-66610-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you retry one of the failing tile URLs (e.g. <a href="https://a.tile.openstreetmap.org/9/255/169.png">https://a.tile.openstreetmap.org/9/255/169.png</a> ) does it work? If so I'd suspect the network connection between your server and the tile cache.</p>
</div>
<div id="comment-66610-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 11:19)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="66611"></span>
<div id="comment-66611" class="comment">
<div id="post-66611-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Direct request finally works but takes for that about 20 sec(</p>
</div>
<div id="comment-66611-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 11:27)</span> <span class="comment-user userinfo">jedi</span>
</div>
</div>
<span id="66620"></span>
<div id="comment-66620" class="comment">
<div id="post-66620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>OK, I'd track that problem down first then, trying to find the "part of the network connection that makes things slow". There's a bunch of stuff in the OSM wiki that explains how the tiles are rendered (from where and for where).</p>
</div>
<div id="comment-66620-info" class="comment-info">
<span class="comment-age">(01 Nov '18, 15:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="66798"></span>
<div id="comment-66798" class="comment not_top_scorer">
<div id="post-66798-score" class="comment-score">
-1
</div>
<div class="comment-text">
<p>Hello!</p>
<p>Is there something new about my problem?</p>
</div>
<div id="comment-66798-info" class="comment-info">
<span class="comment-age">(16 Nov '18, 09:13)</span> <span class="comment-user userinfo">jedi</span>
</div>
</div>
<span id="67909"></span>
<div id="comment-67909" class="comment not_top_scorer">
<div id="post-67909-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello there. Just wanted to add that I use OSM frequently and the same issue has been happening for me very often lately. The tile server often responds with status codes 504 and 502, and sometimes 500 and even 404 (!). This has been going on for a few weeks at least, so I don't think it could be any kind of maintenance. And looking at the screenshot the author posted in the OP, we are probably from the same region/country, so we both must be served by the same tile server.</p>
<p>Sometimes the tile server returns an error message (<a href="https://imgur.com/W4ZBrjj">example</a>), so it's definitely not a problem with my connection.</p>
</div>
<div id="comment-67909-info" class="comment-info">
<span class="comment-age">(06 Feb '19, 13:22)</span> <span class="comment-user userinfo">Player701</span>
</div>
</div>
<span id="67914"></span>
<div id="comment-67914" class="comment not_top_scorer">
<div id="post-67914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have similar issue at zoom 16 while browsing openstreetmap.org. Some tiles are not loaded at this zoom level. When trying to load individual tiles i get 404 - not found. for example <a href="https://www.openstreetmap.org/#map=16/34.0636/49.6836">here</a> and this <a href="https://b.tile.openstreetmap.org/16/41815/26163.png">tile</a>. This is the first time I see this issue. A <a href="http://s9.picofile.com/file/8351477026/jjj.png">screenshot</a> of what I see (I've reduced the zoom level of my browser window). i tested it with two different ISPs, same issue on both. thanks</p>
</div>
<div id="comment-67914-info" class="comment-info">
<span class="comment-age">(06 Feb '19, 18:14)</span> <span class="comment-user userinfo">iriman</span>
</div>
</div>
</div>
<div id="comment-tools-66602" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-66602-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

