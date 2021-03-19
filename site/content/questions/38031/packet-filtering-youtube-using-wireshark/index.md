+++
type = "question"
title = "packet filtering &#x27;YouTube&#x27; using Wireshark"
description = '''Thanks for reading guys. I am a student studying network &amp;amp; security. I and my group were given a task to packet filter &#x27;youtube&#x27; video traffics and we came out with  following method from reading number of threads in wireshark forum and our own research.  However, we are not confident with our m...'''
date = "2014-11-20T19:44:00Z"
lastmod = "2014-11-22T03:59:00Z"
weight = 38031
keywords = [ "youtube", "ports", "port" ]
aliases = [ "/questions/38031" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [packet filtering 'YouTube' using Wireshark](/questions/38031/packet-filtering-youtube-using-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38031-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Thanks for reading guys.</p><p>I am a student studying network &amp; security.</p><p>I and my group were given a task to packet filter 'youtube' video traffics and we came out with</p><p>following method from reading number of threads in wireshark forum and our own research.</p><p>However, we are not confident with our methods and we would like to ask for your advice.</p><p>All of our team members are using Windows 7 and Chrome web browser for this task.</p><p>** filter : tcp.port == 443 or tcp.port == 80<br />
</p><p>We used HTTPS protocol and we included tcp.port == 80 since we found packets on port 80 which we assume were related to youtube video we were trying to packet filter. We combined this filter with frame.number filter in order to identify the first SYN packet and the last Pakcet in order to only capture between those two designated SYN packets. This was because we thought analysing packets during Flow Completion Time is the correct method of packet filtering youtbe video streaming.</p><p>Please correct us if we are wrong.</p><p>Your answers would be much appreciated :)</p></div><div id="question-tags" class="tags-container tags">youtube ports port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Nov '14, 19:44</strong></p><img src="https://secure.gravatar.com/avatar/19a6bfdd404421f76dfa2fd41d89a2dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Snowleopard&#39;s gravatar image" /><p>Snowleopard<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Snowleopard has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Nov '14, 09:29</p></div></div><div id="comments-container-38031" class="comments-container"></div><div id="comment-tools-38031" class="comment-tools"></div><div class="clear"></div><div id="comment-38031-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38068"></span>

<div id="answer-container-38068" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38068-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Filtering for tcp port 80 and 443 will get you all packets that are HTTP or HTTPS, meaning that you get more than just Youtube.</p><p>To filter just Youtube traffic you'd either need to filter on HTTP GET commands containing the partial URL "youtube.com" ("http.request" family of filters, with "contains" operator), or you need to identify the network range of YouTube and include a ip range filter, like "ip.addr==w.x.y.z/maskbits". The latter would also work if you can't see the URL parameter when connection user is encrpyted, but it can be a challenge to find all network ranges used by YouTube.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Nov '14, 03:59</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-38068" class="comments-container"></div><div id="comment-tools-38068" class="comment-tools"></div><div class="clear"></div><div id="comment-38068-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

