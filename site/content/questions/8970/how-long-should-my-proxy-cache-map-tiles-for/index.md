+++
type = "question"
title = "How long should my proxy cache map tiles for?"
description = '''IE doesn&#x27;t like &#x27;mixed content&#x27;, i.e. both https and https. A badly worded warning is pushed into the face of the user. Now Chrome is beginning to give warnings, too. So if you have an aplication that is secured with https, and get tiles directly from OSM (that only serves via http), the user will b...'''
date = "2011-11-14T09:31:00Z"
lastmod = "2011-11-14T21:45:00Z"
weight = 8970
keywords = [ "redirect", "cache", "proxy", "https" ]
aliases = [ "/questions/8970" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How long should my proxy cache map tiles for?](/questions/8970/how-long-should-my-proxy-cache-map-tiles-for)

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
<span id="post-8970-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8970-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8970-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>IE doesn't like 'mixed content', i.e. both https and https. A badly worded warning is pushed into the face of the user. Now Chrome is beginning to give warnings, too.</p>
<p>So if you have an aplication that is secured with https, and get tiles directly from OSM (that only serves via http), the user will be distracted by bogous warnings.</p>
<p>Solution: cook your own forwarding proxy that serves tiles via https.</p>
<p>(The old trick to just return a redirect (301, 'Moved Permanently') to the real osm URL no longer works so well, and is btw slow).</p>
<p>For extra flavour, add caching. It's easy; it only takes 10-20 lines of Java servlet code. This both increases map load speed and reduces load on the osm server. :-) just keep the tiles in files, and re-read if file.lastModfied is older than y hours.</p>
<p>Now, here's the question. How long should such a forward proxy cache a tile? One hour? One day? Some other value?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-redirect" rel="tag" title="see questions tagged &#39;redirect&#39;">redirect</span> <span class="post-tag tag-link-cache" rel="tag" title="see questions tagged &#39;cache&#39;">cache</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span> <span class="post-tag tag-link-https" rel="tag" title="see questions tagged &#39;https&#39;">https</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '11, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/904f2244bfce1fd7812a92589eee2e39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tmpsa&#39;s gravatar image" />
<p><span>tmpsa</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tmpsa has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Nov '11, 17:23</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span></p>
</div>
</div>
<div id="comments-container-8970" class="comments-container">
&#10;</div>
<div id="comment-tools-8970" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8970-form-container" class="comment-form-container">
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

<span id="8998"></span>

<div id="answer-container-8998" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8998-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8998-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-8998-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="https://wiki.openstreetmap.org/wiki/Tile_Usage_Policy">The Tile Usage Policy</a> states that you should</p>
<blockquote>
<p>Cache Tile downloads locally according to HTTP Expiry Header, alternatively a minimum of 7 days.</p>
</blockquote>
<p>Every tile is served with a bunch of HTTP headers, some of which let the client know how long they should cache the tiles for. You don't normally have access to the HTTP headers, but you can find them out using various tools, such as <code>curl -I</code>. For example:</p>
<pre><code>~$ curl -I http://tile.openstreetmap.org/0/0/0.png
HTTP/1.0 200 OK
Content-Length: 8574
Access-Control-Allow-Origin: *
Content-Type: image/png
Date: Mon, 14 Nov 2011 21:37:16 GMT
Server: Apache/2.2.14 (Ubuntu)
ETag: &quot;e1d1be17c7acd4b4cb5fb8e233fb929e&quot;
Expires: Sun, 20 Nov 2011 22:47:03 GMT
Cache-Control: max-age=522587
Age: 24
X-Cache: HIT from konqi.openstreetmap.org
X-Cache-Lookup: HIT from konqi.openstreetmap.org:3128
Via: 1.1 konqi.openstreetmap.org:3128 (squid/2.7.STABLE9)
Connection: close</code></pre>
<p>The Expires header says that you would cache this tile until the date and time shown. The tile server uses a variety of mechanisms to estimate the length of time each tile should be cached, including how recently it was redrawn, what zoom level its on and so on.</p>
<p>Most caching proxies will, by default, read and use the dates shown in the Expiry header, and you probably won't have to do any configuration. If your caching proxy for some reason can't read the Expiry header, you should configure it to cache everything for 7 days instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '11, 21:45</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-8998" class="comments-container">
&#10;</div>
<div id="comment-tools-8998" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8998-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8972"></span>

<div id="answer-container-8972" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8972-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<blockquote>
<p>Cache Tile downloads locally according to HTTP Expiry Header, alternatively a minimum of 7 days.</p>
</blockquote>
<p>From <a href="https://wiki.openstreetmap.org/wiki/Tile_Usage_Policy">the Tile Usage Policy</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '11, 10:28</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-8972" class="comments-container">
<span id="8976"></span>
<div id="comment-8976" class="comment">
<div id="post-8976-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I can't parse that statement. It's, um, a bit terse. What, exactly, does it mean?</p>
</div>
<div id="comment-8976-info" class="comment-info">
<span class="comment-age">(14 Nov '11, 10:57)</span> <span class="comment-user userinfo">tmpsa</span>
</div>
</div>
<span id="8994"></span>
<div id="comment-8994" class="comment">
<div id="post-8994-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you don't know what an HTTP Expiry header is, cache for seven days.</p>
</div>
<div id="comment-8994-info" class="comment-info">
<span class="comment-age">(14 Nov '11, 17:22)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
</div>
<div id="comment-tools-8972" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8972-form-container" class="comment-form-container">
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

