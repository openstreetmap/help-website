+++
type = "question"
title = "Embedded maps not showing"
description = '''We have embedded maps in our site. User creates a record and then can add a position to it that we show in Open Street Map. It has worked perfectly but today 2018-06-04 we discovered that no maps at all are visible for records created today. It just looks like some kind of grid with rectangles and w...'''
date = "2018-06-04T09:29:00Z"
lastmod = "2018-06-08T13:31:00Z"
weight = 64008
keywords = [ "not_shown", "rendering", "tiles", "embed", "tileserver" ]
aliases = [ "/questions/64008" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Embedded maps not showing](/questions/64008/embedded-maps-not-showing)

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
<span id="post-64008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64008-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-64008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We have embedded maps in our site. User creates a record and then can add a position to it that we show in Open Street Map. It has worked perfectly but today 2018-06-04 we discovered that no maps at all are visible for records created today. It just looks like some kind of grid with rectangles and withing them there are a placeholder for an image.</p>
<p>Here are some example links in the rectangles: <a href="http://b.tile.openstreetmap.org/14/9011/4820.png">http://b.tile.openstreetmap.org/14/9011/4820.png</a> <a href="http://b.tile.openstreetmap.org/14/9010/4820.png">http://b.tile.openstreetmap.org/14/9010/4820.png</a> <a href="http://a.tile.openstreetmap.org/14/9012/4820.png">http://a.tile.openstreetmap.org/14/9012/4820.png</a></p>
<p>When I put the links directly in browser it just sais:</p>
<p>This site can’t be reached tile_cache_backend’s server IP address could not be found. Try running Windows Network Diagnostics. DNS_PROBE_FINISHED_NXDOMAIN</p>
<p>However records created before today, there the maps are still visible, like in the link <a href="http://a.tile.openstreetmap.org/14/9015/4835.png">http://a.tile.openstreetmap.org/14/9015/4835.png</a></p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-not_shown" rel="tag" title="see questions tagged &#39;not_shown&#39;">not_shown</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-embed" rel="tag" title="see questions tagged &#39;embed&#39;">embed</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jun '18, 09:29</strong></p>
<img src="https://secure.gravatar.com/avatar/6eed3fca49ab4d4e12447553b65776c6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlliw&#39;s gravatar image" />
<p><span>carlliw</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlliw has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '18, 09:37</strong> </span></p>
</div>
</div>
<div id="comments-container-64008" class="comments-container">
&#10;</div>
<div id="comment-tools-64008" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64008-form-container" class="comment-form-container">
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

<span id="64010"></span>

<div id="answer-container-64010" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64010-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64010-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-64010-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This was an operational issue with the tile caches and should be fixed now.</p>
<p>If you are still seeing the issue you should report the issue (best on <a href="https://irc.openstreetmap.org/">IRC #osm-dev</a>) including which tile cache you are using, visit <a href="https://tile.openstreetmap.org/cgi-bin/debug">https://tile.openstreetmap.org/cgi-bin/debug</a> for that.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jun '18, 10:01</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jun '18, 10:02</strong> </span></p>
</div>
</div>
<div id="comments-container-64010" class="comments-container">
<span id="64013"></span>
<div id="comment-64013" class="comment">
<div id="post-64013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much.</p>
<p>We still experience the same problems. Let me report it accordingly to your suggestion.</p>
</div>
<div id="comment-64013-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 10:17)</span> <span class="comment-user userinfo">carlliw</span>
</div>
</div>
<span id="64014"></span>
<div id="comment-64014" class="comment">
<div id="post-64014-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It seems to work now :-) Thanks for your fast answer.</p>
</div>
<div id="comment-64014-info" class="comment-info">
<span class="comment-age">(04 Jun '18, 10:30)</span> <span class="comment-user userinfo">carlliw</span>
</div>
</div>
</div>
<div id="comment-tools-64010" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64010-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="64099"></span>

<div id="answer-container-64099" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64099-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64099-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64099-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I can't be sure but I think the issues we've been having since ~4th June are the same as the OP given the clue from the OP "This site can’t be reached tile_cache_backend’s server IP address could not be found."</p>
<p><em>Some</em> requests for tiles are being redirected to "http://tile_cache_backend/..."</p>
<p>We've had daily issues since about the same time as the OP, and they're still ongoing today, and the issues can be seen by us by simply visiting the openstreetmap website e.g. <a href="https://www.openstreetmap.org/#map=14/52.1919/0.1424">https://www.openstreetmap.org/#map=14/52.1919/0.1424</a></p>
<p>E.g.</p>
<h1 id="this-request">1 this request:</h1>
<p><a href="https://c.tile.openstreetmap.org/14/8198/5397.png">https://c.tile.openstreetmap.org/14/8198/5397.png</a> is being redirected to: <a href="https://tile_cache_backend/14/8198/5397.png">https://tile_cache_backend/14/8198/5397.png</a></p>
<h1 id="section">2:</h1>
<p><a href="https://a.tile.openstreetmap.org/14/8198/5398.png">https://a.tile.openstreetmap.org/14/8198/5398.png</a> redirects to <a href="https://tile_cache_backend/14/8198/5398.png">https://tile_cache_backend/14/8198/5398.png</a></p>
<h1 id="section-1">3:</h1>
<p><a href="https://b.tile.openstreetmap.org/14/8198/5396.png">https://b.tile.openstreetmap.org/14/8198/5396.png</a> redirects to <a href="https://tile_cache_backend/14/8198/5396.png">https://tile_cache_backend/14/8198/5396.png</a></p>
<p>From the browser console:</p>
<p>20 Refused to load the image '&lt;url&gt;' because it violates the following Content Security Policy directive: "img-src 'self' data: &lt;url&gt; <em>.wp.com</em> .tile.openstreetmap.org <em>.tile.thunderforest.com</em> .openstreetmap.fr piwik.openstreetmap.org developer.mapquest.com".</p>
<p>/#map=15/52.1917/0.1408:1 Refused to load the image 'https://tile_cache_backend/15/16396/10793.png' because it violates the following Content Security Policy directive: "img-src 'self' data: www.gravatar.com <em>.wp.com</em> .tile.openstreetmap.org <em>.tile.thunderforest.com</em> .openstreetmap.fr piwik.openstreetmap.org developer.mapquest.com".</p>
<p>snipped ...</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '18, 13:23</strong></p>
<img src="https://secure.gravatar.com/avatar/904ee9ead8a8ad3adc1b0d7f2637d74f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ijl20&#39;s gravatar image" />
<p><span>ijl20</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ijl20 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64099" class="comments-container">
<span id="64100"></span>
<div id="comment-64100" class="comment">
<div id="post-64100-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'd use IRC but failed</p>
<p>.. tile cache info: tile.openstreetmap.org debug Cache Server: saphira.openstreetmap.org</p>
<p>Render Server: orm.openstreetmap.org Load Average: 61.6</p>
<p>File Status world_boundaries-... Request Headers HTTP_REFERER: <a href="https://help.openstreetmap.org/questions/64008/embedded-maps-not-showing?page=1&amp;focusedAnswerId=64099">https://help.openstreetmap.org/questions/64008/embedded-maps-not-showing?page=1&amp;focusedAnswerId=64099</a> CONTEXT_DOCUMENT_ROOT: /srv/tile.openstreetmap.org/cgi-bin/ CONTEXT_PREFIX: /cgi-bin/ SERVER_SIG:</p>
<p>Apache/2.4.18 (Ubuntu) Server at tile.openstreetmap.org Port 443</p>
<p>REQ_METHOD: GET SVR_PROTOCOL: HTTP/1.0 QRY_STRING: HTTP_USER_AGENT: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36 HTTP_CONNECTION: keep-alive SVR_NAME: tile.openstreetmap.org REMOTE_ADDR: 185.73.44.30 HTTP_VIA: 1.1 saphira.openstreetmap.org:3128 (squid/2.7.STABLE9) SERVER_PORT: 443 SERVER_ADDR: 193.63.75.98 DOC_ROOT: /srv/tile.openstreetmap.org/html</p>
<p>HTTP_HOST: tile.openstreetmap.org SCRIPT_URL: /cgi-bin/debug HTTPS: on HTTP_UPGRADE_INSECURE_REQUESTS: 1 HTTP_CACHE_CONTROL: max-age=518400 REQUEST_URI: /cgi-bin/debug</p>
<p>HTTP_X_FORWARDED_FOR: 128.232.60.94, 127.0.0.1 SCRIPT_NAME: /cgi-bin/debug REMOTE_PORT: 58265</p>
<p>REQUEST_SCHEME: https</p>
</div>
<div id="comment-64100-info" class="comment-info">
<span class="comment-age">(08 Jun '18, 13:31)</span> <span class="comment-user userinfo">ijl20</span>
</div>
</div>
</div>
<div id="comment-tools-64099" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64099-form-container" class="comment-form-container">
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

