+++
type = "question"
title = "Double http response"
description = '''I have been getting a few strange responses from the http server for the tile date. I guestimate this issue to be present about 2% of the time. When I request a tile I get a valid response on the socket like this: HTTP/1.1 200 OK Server: nginx Date: Thu, 27 Feb 2020 08:44:13 GMT Content-Type: image/...'''
date = "2020-02-27T09:45:00Z"
lastmod = "2020-02-27T11:28:00Z"
weight = 73260
keywords = [ "tiles", "http", "proxy", "tileserver" ]
aliases = [ "/questions/73260" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Double http response](/questions/73260/double-http-response)

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
<span id="post-73260-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-73260-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-73260-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been getting a few strange responses from the http server for the tile date. I guestimate this issue to be present about 2% of the time.</p>
<p>When I request a tile I get a valid response on the socket like this:</p>
<pre><code>HTTP/1.1 200 OK
Server: nginx
Date: Thu, 27 Feb 2020 08:44:13 GMT
Content-Type: image/png
Content-Length: 8966
Connection: keep-alive
Keep-Alive: timeout=20
Expect-CT: max-age=0, report-uri=\&quot;https://openstreetmap.report-uri.com/r/d/ct/reportOnly\&quot;
ETag: \&quot;15cf3221a855106d1bb253ddfa9959d5\&quot;
Cache-Control: max-age=59888, stale-while-revalidate=604800, stale-if-error=604800
Expires: Fri, 28 Feb 2020 01:22:20 GMT
Access-Control-Allow-Origin: *
X-TileRender: bowser.openstreetmap.org
X-Cache: MISS from longma.openstreetmap.org
X-Cache-Lookup: MISS from longma.openstreetmap.org:3128
Via: 1.1 longma.openstreetmap.org (squid/4.9)
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload</code></pre>
<p>Note that the Content-Length is announced to be 8966 bytes. In the next read on the socket I receive more data that was announced from the server. If I examine the extra data after the end of the border as announced in Content-Length I get another (valid?) response for the same map tile appended at the end of the data. Headers are slightly different but since the second Content-Length is identical I assume something has gone wrong with caching and that perhaps the cache has appended its response to the original server response:</p>
<pre><code>HTTP/1.1 200 OK
Server: nginx
Date: Thu, 27 Feb 2020 08:44:13 GMT
Content-Type: image/png
Content-Length: 8966
Connection: keep-alive
Keep-Alive: timeout=20
Expect-CT: max-age=0, report-uri=\&quot;https://openstreetmap.report-uri.com/r/d/ct/reportOnly\&quot;
ETag: \&quot;15cf3221a855106d1bb253ddfa9959d5\&quot;
Cache-Control: max-age=65773, stale-while-revalidate=604800, stale-if-error=604800
Expires: Fri, 28 Feb 2020 02:19:39 GMT
Access-Control-Allow-Origin: *
X-TileRender: odin.openstreetmap.org
Age: 2447
X-Cache: HIT from takhisis.openstreetmap.org
X-Cache-Lookup: HIT from takhisis.openstreetmap.org:3128
Via: 1.1 takhisis.openstreetmap.org (squid/4.10)
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload</code></pre>
<p>The second chunk of data seems to indicate that this was a Cache HIT vs. the initial response that announced a MISS.</p>
<p>I will stress again that this data was received in sequence, on the same socket, for one single request. So request for: <a href="http://a.tile.openstreetmap.org/18/135565/89323.png,">http://a.tile.openstreetmap.org/18/135565/89323.png,</a> resolved a.tile.openstreetmap.org to 31.3.110.20. Then I wait for a response, get headers as seen in the first header block above, receive a valid PNG image but then the TCP stream simply contains more data beyond the expected end of the PNG data - a new headers and another (I assume valid) PNG data block.</p>
<p>If I am not mistaken this is highly unusual and violates the HTTP protocol.</p>
<p>So my question is: Is this "normal" and I simply don't understand a part of the HTTP protocol specification or is this a bad response from the OSM servers?</p>
<p>If it is indeed a bad response it would probably make sense to look why this behaviour occurs.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-http" rel="tag" title="see questions tagged &#39;http&#39;">http</span> <span class="post-tag tag-link-proxy" rel="tag" title="see questions tagged &#39;proxy&#39;">proxy</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Feb '20, 09:45</strong></p>
<img src="https://secure.gravatar.com/avatar/1a382d7707f3f684cfe59a7b28b66248?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlesO&#39;s gravatar image" />
<p><span>AlesO</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlesO has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>27 Feb '20, 19:07</strong> </span></p>
</div>
</div>
<div id="comments-container-73260" class="comments-container">
<span id="73274"></span>
<div id="comment-73274" class="comment">
<div id="post-73274-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I'd remove your final paragraph - best stick to one thing at a time!</p>
</div>
<div id="comment-73274-info" class="comment-info">
<span class="comment-age">(27 Feb '20, 11:28)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
</div>
<div id="comment-tools-73260" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-73260-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

