+++
type = "question"
title = "Measure delay and packetloss on HTTP &amp; FTP packet"
description = '''Hi, I just want to know how to measure delay &amp;amp; packetloss on HTTP &amp;amp; FTP packet? My friend told me to decode them first into RTP then the result would be in Telephony -&amp;gt; RTP -&amp;gt; Summary. But I couldn&#x27;t find RTP when I going to decode the HTTP packet. So is there any simple way to do this...'''
date = "2014-03-06T10:14:00Z"
lastmod = "2014-03-06T13:31:00Z"
weight = 30485
keywords = [ "delay", "ftp", "http", "packetloss" ]
aliases = [ "/questions/30485" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Measure delay and packetloss on HTTP & FTP packet](/questions/30485/measure-delay-and-packetloss-on-http-ftp-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30485-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I just want to know how to measure delay &amp; packetloss on HTTP &amp; FTP packet? My friend told me to decode them first into RTP then the result would be in Telephony -&gt; RTP -&gt; Summary. But I couldn't find RTP when I going to decode the HTTP packet. So is there any simple way to do this? FYI, I'm a newbie on using wireshark :)</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">delay ftp http packetloss</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '14, 10:14</strong></p><img src="https://secure.gravatar.com/avatar/d5396afc8eb22685854556215342ec5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aldindha&#39;s gravatar image" /><p>Aldindha<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aldindha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 06 Mar '14, 10:17</p></div></div><div id="comments-container-30485" class="comments-container"></div><div id="comment-tools-30485" class="comment-tools"></div><div class="clear"></div><div id="comment-30485-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30501"></span>

<div id="answer-container-30501" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30501-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>RTP and HTTP/FTP are <strong>not related</strong> for several reason.</p><ul><li>RTP uses <strong>UDP</strong></li><li>HTTP/FTP both use <strong>TCP</strong> (that's the reason why you cannot 'decode as' a HTTP/FTP frame as RTP)</li><li>RTP is used to transmit 'real time' data like voice or video</li><li>HTTP/FTP are both used to transmit 'files' (web pages, documents, images, etc.)</li><li>You cannot use the RTP stream analysis (delay, jitter, packet loss) for HTTP/FTP because of the things listed above!</li></ul><p>So, I guess your friend is mixing up things that are totally unrelated!</p><p>To return to your question: How to measure delay and packet loss of HTTP and FTP connections.</p><p>Regarding <strong>delay</strong> it's up to you to first define what exactly is <strong>delay</strong> for you in the context of HTTP/FTP.</p><p>Regarding <strong>packet loss</strong> go to</p><blockquote><p>Analyze -&gt; Expert Info</p></blockquote><p>and look for <strong>Errors</strong> and <strong>Warnings</strong>. If there is packet loss, you will see</p><ul><li>TCP Retransmission</li><li>TCP DUP ACK</li><li>etc.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '14, 13:31</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30501" class="comments-container"><span id="30514"></span><div id="comment-30514" class="comment"><div id="post-30514-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the answer kurt. What I mean about delay is a sum of time that a packet needed to across the network until destination</p></div><div id="comment-30514-info" class="comment-info"><span class="comment-age">(06 Mar '14, 19:08)</span> Aldindha</div></div><span id="30525"></span><div id="comment-30525" class="comment"><div id="post-30525-score" class="comment-score"></div><div class="comment-text"><p>O.K. if you need that at packet level, select the tcp stream you are interested in, then select</p><blockquote><p>Statistics -&gt; TCP Stream Graph</p></blockquote><p>and choose the graph that's most interesting for you.</p><p>See also the docs of Wireshark.</p></div><div id="comment-30525-info" class="comment-info"><span class="comment-age">(07 Mar '14, 01:39)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-30501" class="comment-tools"></div><div class="clear"></div><div id="comment-30501-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

