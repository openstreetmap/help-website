+++
type = "question"
title = "Length of MP4 Fragment"
description = '''Is there any method of knowing the length of mp4 video in a packet? I have captured packets for a 27 second youtube video. There are 142 PDUs in total. I want to read the TCP data segment in any one of the packets and guess or calculate its length. Any help? Thanks!'''
date = "2014-09-16T05:12:00Z"
lastmod = "2014-09-16T05:17:00Z"
weight = 36358
keywords = [ "mp4", "mp4parer", "youtube", "wireshark" ]
aliases = [ "/questions/36358" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Length of MP4 Fragment](/questions/36358/length-of-mp4-fragment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36358-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any method of knowing the length of mp4 video in a packet? I have captured packets for a 27 second youtube video. There are 142 PDUs in total. I want to read the TCP data segment in any one of the packets and guess or calculate its length. Any help?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">mp4 mp4parer youtube wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '14, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/7953ad2cbdf8a2e2f07eddd90262db99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Qazi&#39;s gravatar image" /><p>Qazi<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Qazi has no accepted answers">0%</span></p></div></div><div id="comments-container-36358" class="comments-container"></div><div id="comment-tools-36358" class="comment-tools"></div><div class="clear"></div><div id="comment-36358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36359"></span>

<div id="answer-container-36359" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36359-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I guess this question could have some answers:</p><p><a href="https://ask.wireshark.org/questions/14280/how-does-wireshark-reassemble-tcp-segments">https://ask.wireshark.org/questions/14280/how-does-wireshark-reassemble-tcp-segments</a></p><p>Unless you really mean the TCP segment length per packet - it can be calculated by taking the IP total length and subtracting the IP and TCP header size from that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '14, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Sep '14, 05:18</p></div></div><div id="comments-container-36359" class="comments-container"><span id="36361"></span><div id="comment-36361" class="comment"><div id="post-36361-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the response Jasper. I think I was not very clear in the question. I am not talking about the length of TCP segment. I want to know the length of video that is being carried by that specific packet.</p></div><div id="comment-36361-info" class="comment-info"><span class="comment-age">(16 Sep '14, 05:25)</span> Qazi</div></div><span id="36363"></span><div id="comment-36363" class="comment"><div id="post-36363-score" class="comment-score"></div><div class="comment-text"><p>I'd guess it's usually all of the segment, but maybe there is also some kind of management info included.</p><p>For knowing how to reassemble a video stream out of the segments you need detailed protocol information about how that kind of stream works (unless it announces it in some way in one of the segments, but again, you'd need protocol specs for interpreting that info)</p></div><div id="comment-36363-info" class="comment-info"><span class="comment-age">(16 Sep '14, 05:29)</span> Jasper ♦♦</div></div></div><div id="comment-tools-36359" class="comment-tools"></div><div class="clear"></div><div id="comment-36359-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

