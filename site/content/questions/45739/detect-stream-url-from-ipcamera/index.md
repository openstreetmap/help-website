+++
type = "question"
title = "detect stream url from ipcamera"
description = '''I have an old chinese ip camera connected in my LAN, with its software and plugin for browsers. I have a PC with 192.168.1.8, the ip camera has an ip 192.168.1.111 I can see the video from its software and when connected in the browser, like: http://192.168.1.111/html/index.html from which I must cl...'''
date = "2015-09-09T08:22:00Z"
lastmod = "2015-09-10T01:44:00Z"
weight = 45739
keywords = [ "url", "video", "stream", "ipcamera" ]
aliases = [ "/questions/45739" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [detect stream url from ipcamera](/questions/45739/detect-stream-url-from-ipcamera)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45739-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have an old chinese ip camera connected in my LAN, with its software and plugin for browsers. I have a PC with 192.168.1.8, the ip camera has an ip 192.168.1.111 I can see the video from its software and when connected in the browser, like: <a href="http://192.168.1.111/html/index.html">http://192.168.1.111/html/index.html</a> from which I must click "Local" to receive the video stream. <img src="http://i.imgur.com/l2l95ws.png" alt="alt text" /></p><p>I want to use another third party program that needs the lan URL of the cam's video to connect. In the manual there's nothing and the vendor has closed his site... So I'm trying with wireshark to sniff the url. I tried to capture from a FF tab before opening the home link "http://192.168.1.111/html/index.html" with this filter: ip.addr==192.168.1.111 and here is the results: <a href="https://www.cloudshark.org/captures/5ee1157195ea">https://www.cloudshark.org/captures/5ee1157195ea</a> My test autenthication is: user:prova pass:video</p><p>I haven't seen any direct url of the stream in the data, that seems only HTTP and TCP (no RTSP or other)... Could you help me detect it? If you need more info or different wireshark data, ask me what you need.</p><p>Thank you very much.</p></div><div id="question-tags" class="tags-container tags">url video stream ipcamera</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '15, 08:22</strong></p><img src="https://secure.gravatar.com/avatar/4a4153a0a87482a943a5a5a7754c9cf7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincenzo%20Ferreri&#39;s gravatar image" /><p>Vincenzo Fer...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincenzo Ferreri has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 09 Sep '15, 08:24</p></div></div><div id="comments-container-45739" class="comments-container"></div><div id="comment-tools-45739" class="comment-tools"></div><div class="clear"></div><div id="comment-45739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45747"></span>

<div id="answer-container-45747" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45747-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your data might be in <code>tcp.stream eq 33</code> as it is the largest stream of packets according to the Statistics &gt; Conversations &gt; TCP &gt; sort on bytes info. The client seems to target the server with some XML that contains an authentication string and a channel to ask for? Then the server answers with more XML specs on how to transfer the stream. &lt;?xml version="1.0" encoding="gb2312" ?&gt; seems to point at 'chinese characters in the xml , maybe hard to read...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Sep '15, 01:44</strong></p><img src="https://secure.gravatar.com/avatar/69710b84acce4cdf0a0cbdcb5930fda1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marc&#39;s gravatar image" /><p>Marc<br />
<span class="score" title="147 reputation points">147</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="16 badges"><span class="bronze">●</span><span class="badgecount">16</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marc has 3 accepted answers">27%</span></p></div></div><div id="comments-container-45747" class="comments-container"><span id="45767"></span><div id="comment-45767" class="comment"><div id="post-45767-score" class="comment-score"></div><div class="comment-text"><p>So, is it impossible to connect to this camera from a third party prog?</p></div><div id="comment-45767-info" class="comment-info"><span class="comment-age">(10 Sep '15, 13:06)</span> Vincenzo Fer...</div></div><span id="45779"></span><div id="comment-45779" class="comment"><div id="post-45779-score" class="comment-score"></div><div class="comment-text"><p>Hi Vincenzo, i don't think it is impossible .. but depends on many factors, is your 3rd party prog configurable to talk like a browser when addressing the cam? Time spent vs the money of a different one etc.</p></div><div id="comment-45779-info" class="comment-info"><span class="comment-age">(11 Sep '15, 00:08)</span> Marc</div></div><span id="45781"></span><div id="comment-45781" class="comment"><div id="post-45781-score" class="comment-score"></div><div class="comment-text"><p>Well, I see the most progs need an url of video stream to connect... they doesn't act like a browser, maybe they use http commands for PTZ motors... For the "chinese characters" found in the above TCP stream, do you think it's possible to decode to normal text, so I can recover this URL stream? If that's not possible, I'll give up...</p></div><div id="comment-45781-info" class="comment-info"><span class="comment-age">(11 Sep '15, 02:05)</span> Vincenzo Fer...</div></div></div><div id="comment-tools-45747" class="comment-tools"></div><div class="clear"></div><div id="comment-45747-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

