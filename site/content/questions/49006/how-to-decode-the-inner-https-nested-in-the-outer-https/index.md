+++
type = "question"
title = "How to decode the inner https nested in the outer https?"
description = '''I sent https request over another https, which is from the client to the web proxy, to the original web server. Here, the inner https is the payload of outer https. I have decoded the outer https, and the CONNECT request is decoded as plain text. but the inner https application data is encrypted by ...'''
date = "2016-01-09T04:55:00Z"
lastmod = "2016-01-09T05:11:00Z"
weight = 49006
keywords = [ "tunnel", "decode", "decrypt", "https", "wireshark" ]
aliases = [ "/questions/49006" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode the inner https nested in the outer https?](/questions/49006/how-to-decode-the-inner-https-nested-in-the-outer-https)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49006-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I sent https request over another https, which is from the client to the web proxy, to the original web server. Here, the inner https is the payload of outer https.</p><p>I have decoded the outer https, and the CONNECT request is decoded as plain text. but the inner https application data is encrypted by the web server.</p><p>I tried "export PDU to files ...", then reopen the file, but no luck.</p><p>So, is it possible to decrypt the inner https in the outer https by wireshark? I used wireshark 1.12, I have the private keys of the web proxy and the web server, so I can decrypt the https from client to proxy, and https from client to web server.</p><p>or any other suggestion to decrypt the inner https?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">tunnel decode decrypt https wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '16, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/b49e210250b2a8926f9d9f2681af7a8f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld2012&#39;s gravatar image" /><p>helloworld2012<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld2012 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Jan '16, 04:59</p></div></div><div id="comments-container-49006" class="comments-container"><span id="49031"></span><div id="comment-49031" class="comment"><div id="post-49031-score" class="comment-score"></div><div class="comment-text"><p>Can you try Wireshark 2.0? Perhaps the issue of SSL proxied over HTTPS is already fixed in there (never tried it though).</p></div><div id="comment-49031-info" class="comment-info"><span class="comment-age">(09 Jan '16, 12:45)</span> Lekensteyn</div></div><span id="49449"></span><div id="comment-49449" class="comment"><div id="post-49449-score" class="comment-score"></div><div class="comment-text"><p>tried with 2.0.1. no luck. :-(</p></div><div id="comment-49449-info" class="comment-info"><span class="comment-age">(22 Jan '16, 02:12)</span> helloworld2012</div></div></div><div id="comment-tools-49006" class="comment-tools"></div><div class="clear"></div><div id="comment-49006-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49008"></span>

<div id="answer-container-49008" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49008-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I sent https request over another https, which is from the client to the web proxy,</p></blockquote><p>traffic from client to web proxy is not encrypted it's plain HTTP using the CONNECT method, so I wonder how you have HTTPS over HTTPS. Can you please post a sample capture file?</p><p>Your web proxy might 'intercept' SSL/TLS, meaning it terminates the TLS session of the client and it opens a second TLS session to the server to be able to scan the content. Is that the case?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jan '16, 05:11</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-49008" class="comments-container"><span id="49010"></span><div id="comment-49010" class="comment"><div id="post-49010-score" class="comment-score"></div><div class="comment-text"><p>Actually, client connects proxy with SSL, so, CONNECT request is also encrypted by the outer SSL. you may check my attachments, one is for SSL over http, then over SSL, the other is for CONNECT request and inner https nested in outer https, since these content are in one decoded SSL stream window.</p><p>proxy only terminates the outer SSL, the inner https is encrypted by web server, so proxy cannot intercept.</p><p>Actually, I want to decode the inner https, just to double confirm the inner https nested in outer https, and so on :-) but from all kinds of clues, seems it is true so far.</p><p>I want to decode the application data in the second snapshot.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/httpsOverHttps2.png" alt="alt text" /> <img src="https://osqa-ask.wireshark.org/upfiles/httpsOverHttps.png" alt="alt text" /></p><p>Thanks</p></div><div id="comment-49010-info" class="comment-info"><span class="comment-age">(09 Jan '16, 05:49)</span> helloworld2012</div></div><span id="49019"></span><div id="comment-49019" class="comment"><div id="post-49019-score" class="comment-score"></div><div class="comment-text"><p>O.K. that looks strange. May I have the pcap file for futher analysis?</p></div><div id="comment-49019-info" class="comment-info"><span class="comment-age">(09 Jan '16, 11:44)</span> Kurt Knochner ♦</div></div><span id="49450"></span><div id="comment-49450" class="comment"><div id="post-49450-score" class="comment-score"></div><div class="comment-text"><p>Sorry for the late reply. Sure. Any email address or something else to upload to you?</p></div><div id="comment-49450-info" class="comment-info"><span class="comment-age">(22 Jan '16, 02:19)</span> helloworld2012</div></div></div><div id="comment-tools-49008" class="comment-tools"></div><div class="clear"></div><div id="comment-49008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

