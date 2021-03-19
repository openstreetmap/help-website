+++
type = "question"
title = "HTTP Response before Request"
description = '''I have noticed that for a specific HTTP Request, Wireshark always displays the Request (frame 63) after the Response (frame 60). However, it turns out the request is actually frame 58, which Wireshark has just labelled as a &quot;TCP segment of a reassembled PDU&quot;. On frame 63 you can see that it has incl...'''
date = "2016-07-06T18:09:00Z"
lastmod = "2016-07-07T01:52:00Z"
weight = 53868
keywords = [ "http", "out-of-order", "bug" ]
aliases = [ "/questions/53868" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP Response before Request](/questions/53868/http-response-before-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53868-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have noticed that for a specific HTTP Request, Wireshark always displays the Request (frame 63) after the Response (frame 60). However, it turns out the request is actually frame 58, which Wireshark has just labelled as a "TCP segment of a reassembled PDU". On frame 63 you can see that it has included frame 58, it also turns out that frame 63 is a FIN/ACK frame with 0 bytes payload.</p><p>I should note that the request has a very large HTTP header in it, a https certificate, which is 1738 bytes long, maybe that is what is confusing Wireshark. As a side note, Nginx didn't know what to do the large header either.</p><p>Why is Wireshark choosing frame 63 for the Request, when it could have used 58?</p><p>This looks like a bug in Wireshark to me.</p><p>EDIT: I have attached the packet capture on <a href="https://www.cloudshark.org/captures/6ffcd7e10730">cloudshark</a></p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcpdump_out_of_order.png" alt="wireshark http out of order" /></p></div><div id="question-tags" class="tags-container tags">http out-of-order bug</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jul '16, 18:09</strong></p><img src="https://secure.gravatar.com/avatar/400af70f37e9e9b8a4b536cb03a63838?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joel%20Pearson&#39;s gravatar image" /><p>Joel Pearson<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joel Pearson has one accepted answer">100%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 07 Jul '16, 15:57</p></div></div><div id="comments-container-53868" class="comments-container"><span id="53875"></span><div id="comment-53875" class="comment"><div id="post-53875-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-53875-info" class="comment-info"><span class="comment-age">(06 Jul '16, 22:28)</span> Jaap ♦</div></div><span id="53917"></span><div id="comment-53917" class="comment"><div id="post-53917-score" class="comment-score"></div><div class="comment-text"><p>@Jaap, done now</p></div><div id="comment-53917-info" class="comment-info"><span class="comment-age">(07 Jul '16, 16:07)</span> Joel Pearson</div></div></div><div id="comment-tools-53868" class="comment-tools"></div><div class="clear"></div><div id="comment-53868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53884"></span>

<div id="answer-container-53884" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53884-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Can you check if turning off the TCP protocol setting "Allow Subdissectors to reassemble TCP streams" makes a difference? My guess is that this is just caused by Wireshark doing reassembly, meaning it's waiting until it has all packets belonging to the request before displaying the info line. This would then not a bug but one of two ways how to display packet content in the info column.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Jul '16, 01:52</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-53884" class="comments-container"><span id="53895"></span><div id="comment-53895" class="comment"><div id="post-53895-score" class="comment-score"></div><div class="comment-text"><p>The explanation suggested by @Jasper is valid if the server has really responded to the request before receiving it completely. This looks like an odd enough behaviour to me, but it seems to be true as the capture seems to be taken on a single machine where both client and server are running, so eventual time shifts in merged files are probably not the explanation.</p><p>So if I were you, I would be most interested in this odd behaviour of the server, and I'd try to find out which part of the request PDU is so useless that the server doesn't wait for it to arrive before responding. I could maybe understand this if the response was a negative one, but since it is a 200, it is really weird.</p></div><div id="comment-53895-info" class="comment-info"><span class="comment-age">(07 Jul '16, 03:54)</span> sindy</div></div><span id="53916"></span><div id="comment-53916" class="comment"><div id="post-53916-score" class="comment-score"></div><div class="comment-text"><p>I have attached the capture now on CloudShark. Turning off "Allow Subdissectors to reassemble TCP streams" does fix the problem, but I'm hesitant to not call it a bug. Because it definitely isn't waiting for more data. If you follow the TCP stream it's pretty clear cut, there is nothing after the response. And the 2nd segment in PDU is a TCP FIN/ACK segment with no data. So maybe that means there is a bug in the http subdissector?</p></div><div id="comment-53916-info" class="comment-info"><span class="comment-age">(07 Jul '16, 16:06)</span> Joel Pearson</div></div><span id="53928"></span><div id="comment-53928" class="comment"><div id="post-53928-score" class="comment-score"></div><div class="comment-text"><p>I justed checked - this problem didn't show up in my Wireshark version, but I am on the latest developer build. So I guess this behavior has already been fixed, but not made it's way into the current stable version yet.</p></div><div id="comment-53928-info" class="comment-info"><span class="comment-age">(08 Jul '16, 04:15)</span> Jasper ♦♦</div></div><span id="53930"></span><div id="comment-53930" class="comment"><div id="post-53930-score" class="comment-score">1</div><div class="comment-text"><p>Nightly builds of the development version are available at the <a href="https://www.wireshark.org/download/automated/">automated downloads</a> section of the website.</p></div><div id="comment-53930-info" class="comment-info"><span class="comment-age">(08 Jul '16, 04:26)</span> grahamb ♦</div></div><span id="53935"></span><div id="comment-53935" class="comment"><div id="post-53935-score" class="comment-score"></div><div class="comment-text"><p>Ahh thanks, I'll check it out</p></div><div id="comment-53935-info" class="comment-info"><span class="comment-age">(08 Jul '16, 06:33)</span> Joel Pearson</div></div><span id="54174"></span><div id="comment-54174" class="comment not_top_scorer"><div id="post-54174-score" class="comment-score"></div><div class="comment-text"><p>@Jasper sorry, I finally got around to trying this out. I downloaded the latest nightly build, and the problem is not fixed. I am using Version 2.1.2-70-g83174a2 (v2.1.2rc0-70-g83174a2 from master)</p><p>Maybe you already have "Allow Subdissectors to reassemble TCP streams" off?</p></div><div id="comment-54174-info" class="comment-info"><span class="comment-age">(19 Jul '16, 19:21)</span> Joel Pearson</div></div><span id="54178"></span><div id="comment-54178" class="comment not_top_scorer"><div id="post-54178-score" class="comment-score"></div><div class="comment-text"><p>I just re-checked, I had Version 2.1.1-5-g508e0f4, and it works with both reassembly on and off. So I installed the version you mentioned and it still works. Not sure why we have different results...</p></div><div id="comment-54178-info" class="comment-info"><span class="comment-age">(20 Jul '16, 01:10)</span> Jasper ♦♦</div></div></div><div id="comment-tools-53884" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-53884-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

