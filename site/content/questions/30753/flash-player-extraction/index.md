+++
type = "question"
title = "Flash Player Extraction"
description = '''Hi, I apologize if this has been asked before. I&#x27;m using Wireshark to attempt to download the source of a stream on a flash player, but I&#x27;ve been having trouble figuring out where to go from the TCP stream. After capturing packets and following the TCP stream, here is what I got: GET /z/mp4/vod9/966...'''
date = "2014-03-13T00:09:00Z"
lastmod = "2014-03-13T21:10:00Z"
weight = 30753
keywords = [ "flash" ]
aliases = [ "/questions/30753" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Flash Player Extraction](/questions/30753/flash-player-extraction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30753-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I apologize if this has been asked before. I'm using Wireshark to attempt to download the source of a stream on a flash player, but I've been having trouble figuring out where to go from the TCP stream. After capturing packets and following the TCP stream, here is what I got:</p><pre><code>GET /z/mp4/vod9/966000/966502.mp4/0_7d43fa406fd425c7_Seg1-Frag3?hdntl=exp=1394780401~acl=%2fz%2fmp4%2fvod9%2f966000%2f966502.mp4%2f*~data=hdntl~hmac=aea1bafcae3f200e7aef29d463fe32325e2d354422f7456436bba763097f25f3&amp;als=9.66,30,8.57,0,635,10044,24.31,1,0,118,f,2.35,249.04,f,s,TVJGVFPHVFST,3.0.3,118&amp;hdcore=3.0.3 HTTP/1.1

Host: vodcdn.mnet.com

User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Referer: http://mwave.interest.me/front/flash/cjem_player_tv.swf?v=9

Cookie: hdntl=exp=1394780401~acl=%2fz%2fmp4%2fvod9%2f966000%2f966502.mp4%2f*~data=hdntl~hmac=aea1bafcae3f200e7aef29d463fe32325e2d354422f7456436bba763097f25f3

Connection: keep-alive

HTTP/1.0 200 OK

Server: AkamaiGHost

Mime-Version: 1.0

Content-Type: video/f4f

Content-Length: 891154

Date: Thu, 13 Mar 2014 07:00:05 GMT

Connection: keep-alive

Set-Cookie: _alid_=NaJME14M80S87dPjgAIAqQ==; path=/z//mp4/vod9/966000/966502.mp4/; domain=vodcdn.mnet.com</code></pre><p>I attempted going to vodcdn.mnet.com/z//mp4/vod9/966000/966502.mp4/ and other combinations, but all give me Access Denied errors.</p><p>The video I am attempting to get the URL for can be seen here <a href="http://mwave.interest.me/mnettv/videodetail.m?searchVideoDetailVO.clip_id=160106.">http://mwave.interest.me/mnettv/videodetail.m?searchVideoDetailVO.clip_id=160106.</a> The video seems to be downloading in fragments, though I'm not sure...</p><p>Am I simply not getting the correct URL or is there something else I have to do?</p><p>Thanks for any help!</p></div><div id="question-tags" class="tags-container tags">flash</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '14, 00:09</strong></p><img src="https://secure.gravatar.com/avatar/073db3237cf24290e05b65025aa95fc7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johnnorman929&#39;s gravatar image" /><p>johnnorman929<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johnnorman929 has no accepted answers">0%</span></p></div></div><div id="comments-container-30753" class="comments-container"><span id="30763"></span><div id="comment-30763" class="comment"><div id="post-30763-score" class="comment-score"></div><div class="comment-text"><blockquote><p>attempt to download the <strong>source of a stream</strong></p></blockquote><p>what do you mean by that?</p></div><div id="comment-30763-info" class="comment-info"><span class="comment-age">(13 Mar '14, 06:03)</span> Kurt Knochner ♦</div></div><span id="30779"></span><div id="comment-30779" class="comment"><div id="post-30779-score" class="comment-score"></div><div class="comment-text"><p>Sorry I wasn't clear, I'm trying to rip the video that is being shown by the player.</p></div><div id="comment-30779-info" class="comment-info"><span class="comment-age">(13 Mar '14, 13:41)</span> johnnorman929</div></div></div><div id="comment-tools-30753" class="comment-tools"></div><div class="clear"></div><div id="comment-30753-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30785"></span>

<div id="answer-container-30785" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30785-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can get the manifest out of Wireshark (as an exported HTTP object) and use this process to rip the streams: <a href="https://github.com/K-S-V/Scripts/wiki">https://github.com/K-S-V/Scripts/wiki</a></p><p>That process lends itself really well to automation also, if you need to pull a lot of video files.</p><p>Edit: Specifically, with those mp4Seg[x]-Frag[xx] files, you should be able to find a .f4m file to accompany it. From that, take the value of the media href attribute (should be a URL) and use it as the 'manifest' input in that linked process.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '14, 21:10</strong></p><img src="https://secure.gravatar.com/avatar/f533c5f20f9c9afbf4b03de08a100e11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Quadratic&#39;s gravatar image" /><p>Quadratic<br />
<span class="score" title="1885 reputation points"><span>1.9k</span></span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Quadratic has 23 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 13 Mar '14, 21:13</p></div></div><div id="comments-container-30785" class="comments-container"></div><div id="comment-tools-30785" class="comment-tools"></div><div class="clear"></div><div id="comment-30785-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

