+++
type = "question"
title = "Slow Internet traffic"
description = '''How can I use wireshark to identify slow network proformance for only internet traffic? Also where is the internet traffic being delayed at. All LAN and WAN traffic for the most part is fast, however when it comes to internet traffic it becomes very very slow. I have installed wireshark on a server ...'''
date = "2011-08-05T13:20:00Z"
lastmod = "2013-09-05T13:36:00Z"
weight = 5537
keywords = [ "slow", "network", "internet" ]
aliases = [ "/questions/5537" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Slow Internet traffic](/questions/5537/slow-internet-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5537-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How can I use wireshark to identify slow network proformance for only internet traffic? Also where is the internet traffic being delayed at. All LAN and WAN traffic for the most part is fast, however when it comes to internet traffic it becomes very very slow. I have installed wireshark on a server and capturing packets filtered with HTTP port 80 traffic. What would be the tell tell sign in the capture packets for internet traffice slowness.</p></div><div id="question-tags" class="tags-container tags">slow network internet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Aug '11, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/0f43e0e0aeb99c2892df7d4d88cf860f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helpomatic&#39;s gravatar image" /><p>helpomatic<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helpomatic has no accepted answers">0%</span></p></div></div><div id="comments-container-5537" class="comments-container"></div><div id="comment-tools-5537" class="comment-tools"></div><div class="clear"></div><div id="comment-5537-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="5538"></span>

<div id="answer-container-5538" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5538-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>In your case you might want to look for requests that take a long time to answer. If you're talking about web traffic you might want to filter for GET and POST requests, or simply any request at all. You can do that by filtering on <code>http.request.method</code>.</p><p>To see how long it takes the webserver to start sending the content you could filter on the HTTP response code, for example <code>http.response.code</code>.</p><p>Combined, you could do <code>http.request.method or http.response.code</code>, and then take a look at the time it took from the request to the response. Keep in mind that this will only tell the time the server needed to start sending content after the request was issued, and that the network latency is included as well. To find out why loading a big web page takes a long time you'd also need to find out where the last packet is, and then determine the delta time between request and complete arrival of all content.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Aug '11, 17:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-5538" class="comments-container"><span id="5543"></span><div id="comment-5543" class="comment"><div id="post-5543-score" class="comment-score"></div><div class="comment-text"><p>Jasper, First I would like to thank you for taking your time to write a response. I must say I am an new to using wireshark, however I was able to use those filters you have requested. They work fine, but for me I am at a lost for words at the time difference. I have saved the capture file, so I can understand when I can interpret what it is telling me.</p></div><div id="comment-5543-info" class="comment-info"><span class="comment-age">(06 Aug '11, 05:02)</span> helpomatic</div></div></div><div id="comment-tools-5538" class="comment-tools"></div><div class="clear"></div><div id="comment-5538-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5580"></span>

<div id="answer-container-5580" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-5580-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Never was able to use the http.request.method or the http.response.code to solve the slow network for internet traffic only. Worked with Verizon and was able to determine that the default route was wrong. After correcting the default route internet is now working fine. A simple traceroute identified the problem. Thank you for your help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '11, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/0f43e0e0aeb99c2892df7d4d88cf860f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helpomatic&#39;s gravatar image" /><p>helpomatic<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helpomatic has no accepted answers">0%</span></p></div></div><div id="comments-container-5580" class="comments-container"></div><div id="comment-tools-5580" class="comment-tools"></div><div class="clear"></div><div id="comment-5580-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="24397"></span>

<div id="answer-container-24397" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24397-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm also just opening Wireshark and it's intimidating. I've been working with ISP and we've got a bunch of unidentified traffic uploading and downloading via the Internet. I would like to pinpoint which users (addresses) are creating the traffic, but don't know how to set it up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Sep '13, 13:36</strong></p><img src="https://secure.gravatar.com/avatar/d9052a201545ee2aee208ab5c07ba2f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="caruncles&#39;s gravatar image" /><p>caruncles<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="caruncles has no accepted answers">0%</span></p></div></div><div id="comments-container-24397" class="comments-container"></div><div id="comment-tools-24397" class="comment-tools"></div><div class="clear"></div><div id="comment-24397-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

