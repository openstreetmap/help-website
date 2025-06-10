+++
type = "question"
title = "Getting 504 Gateway Timeout with &quot;Valid document was not found in the cache and only-if-cached directive was specified&quot; for some tiles"
description = '''Requesting, e.g., https://a.tile.openstreetmap.org/17/67225/43067.png shows showed:  The following error was encountered while trying to retrieve the URL: http://b.tile.openstreetmap.org/17/67224/43067.png Valid document was not found in the cache and only-if-cached directive was specified.  You hav...'''
date = "2018-06-11T10:42:00Z"
lastmod = "2018-06-11T18:01:00Z"
weight = 64157
keywords = [ "tiles", "cache", "tileserver" ]
aliases = [ "/questions/64157" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Getting 504 Gateway Timeout with "Valid document was not found in the cache and only-if-cached directive was specified" for some tiles](/questions/64157/getting-504-gateway-timeout-with-valid-document-was-not-found-in-the-cache-and-only-if-cached-directive-was-specified-for-some-tiles)

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
<span id="post-64157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64157-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Requesting, e.g., <a href="https://a.tile.openstreetmap.org/17/67225/43067.png">https://a.tile.openstreetmap.org/17/67225/43067.png</a> <del>shows</del> showed:</p>
<blockquote>
<p>The following error was encountered while trying to retrieve the URL: <a href="http://b.tile.openstreetmap.org/17/67224/43067.png">http://b.tile.openstreetmap.org/17/67224/43067.png</a></p>
<p>Valid document was not found in the cache and only-if-cached directive was specified.</p>
<p>You have issued a request with a only-if-cached cache control directive. The document was not found in the cache, or it required revalidation prohibited by the only-if-cached directive.</p>
</blockquote>
<p>I really don't think the browser is sending that header. Running the following from a different location (just be sure it's not some network issue at work) <del>yields</del> did yield the very same error:</p>
<p><code>curl 'https://b.tile.openstreetmap.org/17/67224/43067.png' -H 'Referer: </code><a href="http://127.0.0.1:4200/demo/embed-mjgp2.html&#39;"><code>http://127.0.0.1:4200/demo/embed-mjgp2.html'</code></a><code> -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36' --compressed --verbose</code></p>
<p>...showing no header like that:</p>
<pre><code>&gt; GET /17/67224/43067.png HTTP/2
&gt; Host: b.tile.openstreetmap.org
&gt; Accept: */*
&gt; Accept-Encoding: deflate, gzip
&gt; Referer: http://127.0.0.1:4200/demo/embed-mjgp2.html
&gt; User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36
...
&lt; HTTP/2 504
&lt; server: nginx
&lt; date: Mon, 11 Jun 2018 08:21:34 GMT
&lt; content-type: text/html
&lt; content-length: 1445
&lt; x-squid-error: ERR_ONLY_IF_CACHED_MISS 0
&lt; x-cache: MISS from konqi.openstreetmap.org
&lt; x-cache-lookup: MISS from konqi.openstreetmap.org:3128
&lt; x-cache: MISS from trogdor.openstreetmap.org
&lt; x-cache-lookup: MISS from trogdor.openstreetmap.org:3128
&lt; via: 1.0 konqi.openstreetmap.org:3128 (squid/2.7.STABLE9), 1.1 trogdor.openstreetmap.org (squid/3.5.12)
&lt; strict-transport-security: max-age=31536000; includeSubDomains</code></pre>
<p>So I guess some internal proxy on the OSM server is adding that header?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-cache" rel="tag" title="see questions tagged &#39;cache&#39;">cache</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Jun '18, 10:42</strong></p>
<img src="https://secure.gravatar.com/avatar/04b5f00a8624ff5e7a3db486b96b125c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="avbentem&#39;s gravatar image" />
<p><span>avbentem</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="avbentem has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Jun '18, 20:20</strong> </span></p>
</div>
</div>
<div id="comments-container-64157" class="comments-container">
<span id="64161"></span>
<div id="comment-64161" class="comment">
<div id="post-64161-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Similar reports at <a href="https://stackoverflow.com/questions/50757554/openstreetmap-often-sends-gateway-timeout-error">https://stackoverflow.com/questions/50757554/openstreetmap-often-sends-gateway-timeout-error</a> and <a href="https://stackoverflow.com/questions/50757102/open-street-map-504">https://stackoverflow.com/questions/50757102/open-street-map-504</a></p>
</div>
<div id="comment-64161-info" class="comment-info">
<span class="comment-age">(11 Jun '18, 13:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-64157" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64157-form-container" class="comment-form-container">
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

<span id="64162"></span>

<div id="answer-container-64162" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64162-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64162-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64162-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="avbentem has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There have been some issues with the squid proxy in recent days. The sysadmins are working on it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Jun '18, 18:01</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-64162" class="comments-container">
&#10;</div>
<div id="comment-tools-64162" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64162-form-container" class="comment-form-container">
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

