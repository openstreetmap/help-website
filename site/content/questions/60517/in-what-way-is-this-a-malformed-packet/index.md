+++
type = "question"
title = "In What Way Is This a Malformed Packet?"
description = '''Hello, I am learning to use Wireshark for the first time to debug an application I wrote that exposes an HTTP API. I have noticed that Wireshark shows [Malformed Packet] in the Info field for every 200 (OK) response I receive from my application: 6 0.002723261 ::1 ::1 HTTP 358 HTTP/1.1 200 OK [Malfo...'''
date = "2017-04-02T01:37:00Z"
lastmod = "2017-04-02T08:00:00Z"
weight = 60517
keywords = [ "http", "malformed" ]
aliases = [ "/questions/60517" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [In What Way Is This a Malformed Packet?](/questions/60517/in-what-way-is-this-a-malformed-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60517-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am learning to use Wireshark for the first time to debug an application I wrote that exposes an HTTP API. I have noticed that Wireshark shows [Malformed Packet] in the Info field for every 200 (OK) response I receive from my application:</p><pre><code>6   0.002723261 ::1 ::1 HTTP    358 HTTP/1.1 200 OK [Malformed Packet]</code></pre><p>I don't know in what way these responses are malformed, and my client programs don't seem to have any problem with these responses.</p><p>Here is a typical response:</p><pre><code>`[email protected]|@  J$^8
##HTTP/1.1 200 OK
Date: Sun, 02 Apr 2017 07:38:52 GMT
Content-Type: application/json
Transfer-Encoding: chunked
Server: Jetty(9.3.6.v20151106)

78
{&quot;description&quot;:null,&quot;resultCode&quot;:&quot;WARNING&quot;,&quot;resultMessage&quot;:&quot;Didn\u0027t find and so can\u0027t describe reservation: 1&quot;}</code></pre><p>Can anyone tell me what is wrong with it? I am suspicious of characters preceding "HTTP" but I don't know enough to know whether they are what is causing Wireshark to declare the packets malformed..</p><p>Thank you for your help.</p><p>-Dan</p></div><div id="question-tags" class="tags-container tags">http malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Apr '17, 01:37</strong></p><img src="https://secure.gravatar.com/avatar/2d5f9fde470aae8b05665a08752852ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subuta&#39;s gravatar image" /><p>subuta<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subuta has no accepted answers">0%</span></p></div></div><div id="comments-container-60517" class="comments-container"></div><div id="comment-tools-60517" class="comment-tools"></div><div class="clear"></div><div id="comment-60517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60524"></span>

<div id="answer-container-60524" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60524-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're right, the suspicious characters preceding "HTTP" should not be there. Web browsers are usually ignoring a lot of bad things, as their primary goal is to render a page, so that's why they don't complain. But from a protocol point of view the packet is malformed. The "HTTP" characters must be the first thing following the TCP header, but in your case there's some garbage between the TCP header and HTTP. So you should find out where the garbage bytes come from, and prevent them from being written to the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '17, 08:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-60524" class="comments-container"><span id="60526"></span><div id="comment-60526" class="comment"><div id="post-60526-score" class="comment-score"></div><div class="comment-text"><p>Thank you for the quick and helpful reply, Jasper. I will investigate these garbage characters.</p></div><div id="comment-60526-info" class="comment-info"><span class="comment-age">(02 Apr '17, 10:43)</span> subuta</div></div></div><div id="comment-tools-60524" class="comment-tools"></div><div class="clear"></div><div id="comment-60524-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

