+++
type = "question"
title = "Next sequence number calculation in wireshark"
description = '''Hello, I am trying to analyse packets in an ssl stream. Some packets have an additional field in the TCP header [Next Sequence Number : XXXX] which is calculated by wireshark. Would be great if someone could tell me how this calculation is done. Thanks!'''
date = "2012-04-23T11:10:00Z"
lastmod = "2012-04-23T12:09:00Z"
weight = 10405
keywords = [ "wireshark" ]
aliases = [ "/questions/10405" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Next sequence number calculation in wireshark](/questions/10405/next-sequence-number-calculation-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10405-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am trying to analyse packets in an ssl stream. Some packets have an additional field in the TCP header [Next Sequence Number : XXXX] which is calculated by wireshark. Would be great if someone could tell me how this calculation is done.</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Apr '12, 11:10</strong></p><img src="https://secure.gravatar.com/avatar/a75213a03d1ec30ed0108a5911e0bcd1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flyhigh&#39;s gravatar image" /><p>flyhigh<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flyhigh has no accepted answers">0%</span></p></div></div><div id="comments-container-10405" class="comments-container"></div><div id="comment-tools-10405" class="comment-tools"></div><div class="clear"></div><div id="comment-10405-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10407"></span>

<div id="answer-container-10407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10407-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Simple: it takes the current sequence number (specified usually just in front of the "next sequence number" field) and adds the tcp payload length. The easiest way to find the payload length is by looking at the TCP protocol header - at the end, it says "len:".</p><p>By the way, the "Next Sequence Number" is also nice to have to determine the acknowledge number for this packet, because it's the same.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Apr '12, 12:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Apr '12, 12:10</p></div></div><div id="comments-container-10407" class="comments-container"><span id="10408"></span><div id="comment-10408" class="comment"><div id="post-10408-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot! Just one more question : How is the stream index calculated in wireshark. I am trying to parse packets in my code, and perform some operations on the packets in the same TCP stream. So I would like to maintain stream numbers to achieve the same.</p></div><div id="comment-10408-info" class="comment-info"><span class="comment-age">(23 Apr '12, 13:08)</span> flyhigh</div></div><span id="10409"></span><div id="comment-10409" class="comment"><div id="post-10409-score" class="comment-score">1</div><div class="comment-text"><p>SYN-bit can probably tell you more about it, but I think it comes down to this: whenever Wireshark finds a new socket pair (socket being a combination of IP address and TCP port; a pair of it identifying a conversation) it will increase the stream index and assign it to all packets of that conversation.</p><p>Some older versions count it up for UDP conversations, too, but AFAIK SYN-bit wanted to change that. It caused too much confusion why there are gaps in the TCP stream numberings. I just forgot if he already did :-)</p></div><div id="comment-10409-info" class="comment-info"><span class="comment-age">(23 Apr '12, 13:51)</span> Jasper ♦♦</div></div><span id="10410"></span><div id="comment-10410" class="comment"><div id="post-10410-score" class="comment-score">1</div><div class="comment-text"><p>Jasper is correct. When I first implemented the tcp.stream index, I reused a value already available in the code used for conversations (which does include other protocols apart from tcp). This resulted in gaps in the tcp.stream numbering and a lot of confusion.</p><p>Since SVN 38056 (July 16, 2011), this has been changed to using separate numbering for tcp.stream values so that the numbering will monotonously increase for each new tcp session.</p><p>I don't think this code has made it to the 1.6.x versions, but it is included in the 1.7.x versions and will make it into 1.8.0</p></div><div id="comment-10410-info" class="comment-info"><span class="comment-age">(23 Apr '12, 14:04)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-10407" class="comment-tools"></div><div class="clear"></div><div id="comment-10407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

