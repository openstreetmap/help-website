+++
type = "question"
title = "problem getting stream"
description = '''Hello, I&#x27;m new to wireshark and im having problem with collecting a stream from a site. Below is the information from the Follow TCP stream, how do i use this info to direct myself to the required stream. .GET /vod/_definst_/s3/3000032/20160516/3000/0_8djcrumk_0_fxa3haiy_2.mp4/media_b3969197.abst/Se...'''
date = "2016-05-17T11:24:00Z"
lastmod = "2016-05-17T11:24:00Z"
weight = 52686
keywords = [ "follow.tcp.stream" ]
aliases = [ "/questions/52686" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [problem getting stream](/questions/52686/problem-getting-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52686-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm new to wireshark and im having problem with collecting a stream from a site.</p><p>Below is the information from the Follow TCP stream, how do i use this info to direct myself to the required stream.</p><pre><code>.GET /vod/_definst_/s3/3000032/20160516/3000/0_8djcrumk_0_fxa3haiy_2.mp4/media_b3969197.abst/Seg1-Frag10 HTTP/1.1
Host: fli.cf.vod.mp.streamamg.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36
X-Requested-With: ShockwaveFlash/21.0.0.242
Accept: */*
Referer: http://www.player.bradfordcityfc.co.uk/latest-news
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8

HTTP/1.1 200 OK
Content-Type: video/mp4
Content-Length: 2089567
Connection: keep-alive
Accept-Ranges: bytes
Cache-Control: max-age=31536003
Date: Tue, 17 May 2016 13:51:13 GMT
Server: WowzaStreamingEngine/4.4.0
X-Cache: Miss from cloudfront
Via: 1.1 901427b25164532ae97382d031da28b7.cloudfront.net (CloudFront)
X-Amz-Cf-Id: D9pHj5mC2jXFfBKgT5psDGiNKBbF8L48GHrK5lsn6WKOo7DqCKnv-g==</code></pre><p>Regards</p><p>Bobdylan</p></div><div id="question-tags" class="tags-container tags">follow.tcp.stream</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 May '16, 11:24</strong></p><img src="https://secure.gravatar.com/avatar/00c262d066ff6a578f927536b7f46110?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bobdylan74&#39;s gravatar image" /><p>bobdylan74<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bobdylan74 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 May '16, 12:51</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-52686" class="comments-container"><span id="52694"></span><div id="comment-52694" class="comment"><div id="post-52694-score" class="comment-score"></div><div class="comment-text"><p>I think you might have confused the concept of a tcp stream with a video stream.</p><p>The Wireshark option to "Follow TCP stream" is used to display all the traffic over a particular TCP connection, not find a video stream.</p><p>There have been quite a few other questions on this site about locating a video stream, have a search for them.</p></div><div id="comment-52694-info" class="comment-info"><span class="comment-age">(17 May '16, 14:57)</span> grahamb ♦</div></div><span id="52709"></span><div id="comment-52709" class="comment"><div id="post-52709-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the reply jasper, I just tried to follow the steps of a youtube video where he uses the "Follow TCP stream" to find and download a Youtube video...</p><p>thanks bobdylan</p></div><div id="comment-52709-info" class="comment-info"><span class="comment-age">(18 May '16, 01:24)</span> bobdylan74</div></div></div><div id="comment-tools-52686" class="comment-tools"></div><div class="clear"></div><div id="comment-52686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

