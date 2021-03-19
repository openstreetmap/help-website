+++
type = "question"
title = "Cannot capture network latency of HTTP request."
description = '''Hi, I&#x27;m trying to capture the latency of a simple HTTP request over the network (internet). I&#x27;ve tried delta, delta conversion, relative time etc. ... Nothing seems to give me the RTT (round trip time) over the network. I used a simple HTTP request with screenshot of Google chrome with debugger. See...'''
date = "2014-01-22T01:49:00Z"
lastmod = "2014-01-22T03:06:00Z"
weight = 29084
keywords = [ "latency", "network" ]
aliases = [ "/questions/29084" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot capture network latency of HTTP request.](/questions/29084/cannot-capture-network-latency-of-http-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29084-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29084-score" class="post-score" title="current number of votes">0</div><span id="post-29084-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to capture the latency of a simple HTTP request over the network (internet). I've tried delta, delta conversion, relative time etc. ... Nothing seems to give me the RTT (round trip time) over the network.</p><p>I used a simple HTTP request with screenshot of Google chrome with debugger. See <img src="https://osqa-ask.wireshark.org/upfiles/TestHttpRequest.jpg" alt="alt text" /></p><p>Also see screenshot of Wireshark capture <img src="https://osqa-ask.wireshark.org/upfiles/WiresharkCaptureScreenshot.jpg" alt="alt text" /></p><p>Thanks, Kapil</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-latency" rel="tag" title="see questions tagged &#39;latency&#39;">latency</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jan '14, 01:49</strong></p><img src="https://secure.gravatar.com/avatar/143b1eb32813ac15979360fa89bc4cbf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kapilok&#39;s gravatar image" /><p><span>kapilok</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kapilok has no accepted answers">0%</span></p></img></div></div><div id="comments-container-29084" class="comments-container"></div><div id="comment-tools-29084" class="comment-tools"></div><div class="clear"></div><div id="comment-29084-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29089"></span>

<div id="answer-container-29089" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29089-score" class="post-score" title="current number of votes">2</div><span id="post-29089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>One way of doing that would be</p><ol><li>Find the GET request (as you did)</li><li>Right click the packet and select "Set Time Reference". This will mark the GET request as new "zero" time</li><li>look at the HTTP decode. In recent versions of Wireshark it should have a blue line saying something like "Response in frame: xyz". Click on it to jump to the answer packet.</li><li>Set your time column to "Seconds since beginning of capture" in the View menu (also often called "Relative Time"). This way the time column will show the time since the start of the file, or the nearest Time Reference point</li><li>Read the latency from the time column</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '14, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jan '14, 06:17</strong> </span></p></div></div><div id="comments-container-29089" class="comments-container"></div><div id="comment-tools-29089" class="comment-tools"></div><div class="clear"></div><div id="comment-29089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

