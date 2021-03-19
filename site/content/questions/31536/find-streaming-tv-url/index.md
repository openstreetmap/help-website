+++
type = "question"
title = "find streaming tv URL"
description = '''hello. is it possible to help me find the channel URL from a streaming tv site? the site is http://www.yourtv.to and it is a free site, so i think there is no problem. i want to create a m3u list for xbmc. i tried to find the URL but i can&#x27;t. the site uses jwplayer. please help me if you can.'''
date = "2014-04-05T00:03:00Z"
lastmod = "2014-04-05T16:57:00Z"
weight = 31536
keywords = [ "stream" ]
aliases = [ "/questions/31536" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [find streaming tv URL](/questions/31536/find-streaming-tv-url)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31536-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31536-score" class="post-score" title="current number of votes">0</div><span id="post-31536-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello. is it possible to help me find the channel URL from a streaming tv site? the site is <a href="http://www.yourtv.to">http://www.yourtv.to</a> and it is a free site, so i think there is no problem. i want to create a m3u list for xbmc. i tried to find the URL but i can't. the site uses jwplayer. please help me if you can.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Apr '14, 00:03</strong></p><img src="https://secure.gravatar.com/avatar/6f33c6f0c5ee38cee8a7849314698c07?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dimitris&#39;s gravatar image" /><p><span>dimitris</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dimitris has no accepted answers">0%</span></p></div></div><div id="comments-container-31536" class="comments-container"></div><div id="comment-tools-31536" class="comment-tools"></div><div class="clear"></div><div id="comment-31536-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31539"></span>

<div id="answer-container-31539" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31539-score" class="post-score" title="current number of votes">0</div><span id="post-31539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use the display filter: http.request.method == "GET"</p><p>When you select a tv station it will request the URL and set a token cookie. Then it will load jwplayer and download the playlist. If you look at the playlist URL you will notice it requires the token that was previously generated e.g. for ZDF</p><pre><code>x://www.yourtv.to/online/live/fernsehen/stream/zdf.html
x://www.yourtv.to/swf/jwplayer.flash.swf?asd
x://31.204.128.190/live/zdf/playlist.m3u8?wmsAuthSign=token</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Apr '14, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/721b9692d2a30fc3b386b7fae9a44220?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Roland&#39;s gravatar image" /><p><span>Roland</span><br />
<span class="score" title="764 reputation points">764</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Roland has 9 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>05 Apr '14, 04:11</strong> </span></p></div></div><div id="comments-container-31539" class="comments-container"><span id="31546"></span><div id="comment-31546" class="comment"><div id="post-31546-score" class="comment-score"></div><div class="comment-text"><p>thank you for your help. i did not understand exactly what you said. i am trying now to learn how wireshark works. i will tell what i did. i open zdf and then stop the capture. i used the filter you said and found this</p><pre><code>1656    43.493092000    192.168.2.4 31.204.128.190  HTTP    548 GET /live/zdf/playlist.m3u8?wmsAuthSign=c2VydmVyX3RpbWU9NC82LzIwMTQgMTA6NDM6MTEgQU0maGFzaF92YWx1ZT1HUUh0RTNrMDlxV3U3Q3N5WDFzMUR3PT0mdmFsaWRtaW51dGVzPTI0MCZpZD01 HTTP/1.1 </code></pre><p>then right click/ follow tcp stream and found this text</p><pre><code>GET /live/zdf/playlist.m3u8?wmsAuthSign=c2VydmVyX3RpbWU9NC82LzIwMTQgMTA6NDM6MTEgQU0maGFzaF92YWx1ZT1HUUh0RTNrMDlxV3U3Q3N5WDFzMUR3PT0mdmFsaWRtaW51dGVzPTI0MCZpZD01 HTTP/1.1

Host: 31.204.128.190
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://www.yourtv.to/swf/jwplayer.flash.swf?asd
Connection: keep-alive

HTTP/1.1 200 OK
Date: Sat, 05 Apr 2014 11:44:44 GMT
Content-Type: application/vnd.apple.mpegurl
Accept-Ranges: bytes
Server: FlashCom/3.5.7
Cache-Control: no-cache
Content-Length: 284

#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1480959,CODECS=&quot;avc1.66.30, mp4a.40.2&quot;,RESOLUTION=720x404
chunklist_w1610455686.m3u8?wmsAuthSign=c2VydmVyX3RpbWU9NC82LzIwMTQgMTA6NDM6MTEgQU0maGFzaF92YWx1ZT1HUUh0RTNrMDlxV3U3Q3N5WDFzMUR3PT0mdmFsaWRtaW51dGVzPTI0MCZpZD01

GET /live/zdf/chunklist_w1610455686.m3u8?wmsAuthSign=c2VydmVyX3RpbWU9NC82LzIwMTQgMTA6NDM6MTEgQU0maGFzaF92YWx1ZT1HUUh0RTNrMDlxV3U3Q3N5WDFzMUR3PT0mdmFsaWRtaW51dGVzPTI0MCZpZD01 HTTP/1.1

Host: 31.204.128.190
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://www.yourtv.to/swf/jwplayer.flash.swf?asd
Connection: keep-alive

HTTP/1.1 200 OK
Date: Sat, 05 Apr 2014 11:44:45 GMT
Content-Type: application/vnd.apple.mpegurl
Accept-Ranges: bytes
Server: FlashCom/3.5.7
Cache-Control: no-cache
Content-Length: 620

#EXTM3U
#EXT-X-VERSION:3
#EXT-X-ALLOW-CACHE:NO
#EXT-X-TARGETDURATION:13
#EXT-X-MEDIA-SEQUENCE:1407
#EXTINF:8.08,
media_w1610455686_1407.ts?wmsAuthSign=c2VydmVyX3RpbWU9NC82LzIwMTQgMTA6NDM6MTEgQU0maGFzaF92YWx1ZT1HUUh0RTNrMDlxV3U3Q3N5WDFzMUR3PT0mdmFsaWRtaW51dGVzPTI0MCZpZD01
#EXTINF:10.16,
media_w1610455686_1408.ts?wmsAuthSign=c2VydmVyX3RpbWU9NC82LzIwMTQgMTA6NDM6MTEgQU0maGFzaF92YWx1ZT1HUUh0RTNrMDlxV3U3Q3N5WDFzMUR3PT0mdmFsaWRtaW51dGVzPTI0MCZpZD01
#EXTINF:12.16,
media_w1610455686_1409.ts?wmsAuthSign=c2VydmVyX3RpbWU9NC82LzIwMTQgMTA6NDM6MTEgQU0maGFzaF92YWx1ZT1HUUh0RTNrMDlxV3U3Q3N5WDFzMUR3PT0mdmFsaWRtaW51dGVzPTI0MCZpZD01

GET /live/zdf/media_w1610455686_1407.ts?wmsAuthSign=c2VydmVyX3RpbWU9NC82LzIwMTQgMTA6NDM6MTEgQU0maGFzaF92YWx1ZT1HUUh0RTNrMDlxV3U3Q3N5WDFzMUR3PT0mdmFsaWRtaW51dGVzPTI0MCZpZD01 HTTP/1.1
Host: 31.204.128.190
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://www.yourtv.to/swf/jwplayer.flash.swf?asd
Connection: keep-alive

HTTP/1.1 200 OK
Date: Sat, 05 Apr 2014 11:44:46 GMT
Content-Type: video/MP2T
Accept-Ranges: bytes
Server: FlashCom/3.5.7
Cache-Control: no-cache
Content-Length: 1376724
</code></pre><p>and i tried to make a m3u file so that i can play it on xbmc</p><pre><code>http://31.204.128.190/live/zdf/chunklist_w1610455686_1407.ts?wmsAuthSign=c2VydmVyX3RpbWU9NC82LzIwMTQgMTA6NDM6MTEgQU0maGFzaF92YWx1ZT1HUUh0RTNrMDlxV3U3Q3N5WDFzMUR3PT0mdmFsaWRtaW51dGVzPTI0MCZpZD01 pageURL=http://www.yourtv.to/online/live/fernsehen/stream/zdf.html swfURL=http://www.yourtv.to/swf/jwplayer.flash.swf?asd keep-alive</code></pre><p>but it does not work. i am probably making something wrong but i dont know what. can you help?</p></div><div id="comment-31546-info" class="comment-info"><span class="comment-age">(05 Apr '14, 05:18)</span> <span class="comment-user userinfo">dimitris</span></div></div><span id="31560"></span><div id="comment-31560" class="comment"><div id="post-31560-score" class="comment-score"></div><div class="comment-text"><p>I can't help you with XBMC.</p></div><div id="comment-31560-info" class="comment-info"><span class="comment-age">(05 Apr '14, 16:57)</span> <span class="comment-user userinfo">Roland</span></div></div></div><div id="comment-tools-31539" class="comment-tools"></div><div class="clear"></div><div id="comment-31539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

