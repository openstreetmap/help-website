+++
type = "question"
title = "HTTP dissector failed to re-assemble"
description = '''I&#x27;m using wireshark to sniff HTTPs packets. In some cases, HTTPs response was not reassembled by wireshark.  I give all ssl session keys to wireshark, so keys doesn&#x27;t cause the problem.  When I followed SSL stream, I got the result below. GET /api/webimage/5357a5d5090b5553a9c78ed2-1-large.jpg HTTP/1...'''
date = "2017-03-29T02:21:00Z"
lastmod = "2017-03-29T02:21:00Z"
weight = 60397
keywords = [ "dissector", "dissect_http", "https" ]
aliases = [ "/questions/60397" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP dissector failed to re-assemble](/questions/60397/http-dissector-failed-to-re-assemble)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60397-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using wireshark to sniff HTTPs packets.</p><p>In some cases, HTTPs response was not reassembled by wireshark.</p><p>I give all ssl session keys to wireshark, so keys doesn't cause the problem.</p><p>When I followed SSL stream, I got the result below.</p><pre><code>GET /api/webimage/5357a5d5090b5553a9c78ed2-1-large.jpg HTTP/1.1
host: contestimg.wish.com
Connection: Keep-Alive
User-Agent: Mozilla/5.0 (Linux; Android 6.0.1; SM-N916S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.97 Mobile Safari/537.36

HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 181501
Connection: keep-alive
Date: Wed, 29 Mar 2017 07:35:48 GMT
Cache-Control: max-age=1208728
ETag: &quot;99df3c51782782beb9ef06ab89c911990521e3f6&quot;
Server: TornadoServer/2.1git-cl
Timing-Allow-Origin: *
X-Cache: Miss from cloudfront
Via: 1.1 1787e729a1c3fb1d4583d4cb9052972b.cloudfront.net (CloudFront)
X-Amz-Cf-Id: QayZ8W4yd8fjBeGqcL1Fzzy1cVQATFyYabfxE5LkMUz7bN60DGq74A==

......JFIF.............C.....................................   ... ......

.....
.

...C...........
...</code></pre><p>Also, when I followed HTTP stream, I got the result below which shows only request.</p><pre><code>GET /api/webimage/5357a5d5090b5553a9c78ed2-1-large.jpg HTTP/1.1
host: contestimg.wish.com
Connection: Keep-Alive
User-Agent: Mozilla/5.0 (Linux; Android 6.0.1; SM-N916S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.97 Mobile Safari/537.36</code></pre><p>Actually, this was an image request, and I got the image and saw in a mobile.</p><p>In addition, all TLSv1.2(HTTPs) packets related to this HTTP response seemed to be collected when I saw wireshark.</p><p><strong>What should I do to solve this problem?</strong></p><p><strong>When wireshark's HTTP dissector fails to reassemble HTTP request/response?</strong></p><p><strong>Is it possible that wireshark's HTTP dissector fail although all packets related to HTTP request/response arrived?</strong><br />
</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">dissector dissect_http https</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Mar '17, 02:21</strong></p><img src="https://secure.gravatar.com/avatar/87bd4688cb1f3f5e7305a9ba267c50fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hyunho&#39;s gravatar image" /><p>Hyunho<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hyunho has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-60397" class="comments-container"></div><div id="comment-tools-60397" class="comment-tools"></div><div class="clear"></div><div id="comment-60397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

