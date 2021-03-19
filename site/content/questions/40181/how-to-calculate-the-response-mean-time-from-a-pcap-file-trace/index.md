+++
type = "question"
title = "how to calculate the response mean time from a pcap file trace"
description = '''Hi , I did lot of search but i didn&#x27;t find what i am interessting into. Here is my story. I am living in the GSM world. we can capture network traffic based on SIgtran interface ( SS7 over IP ). so on the sms world , you have always a request , then an ack from the platform ( HLR; MSC ). by example ...'''
date = "2015-03-02T04:21:00Z"
lastmod = "2015-03-03T03:41:00Z"
weight = 40181
keywords = [ "ss7", "gsm" ]
aliases = [ "/questions/40181" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to calculate the response mean time from a pcap file trace](/questions/40181/how-to-calculate-the-response-mean-time-from-a-pcap-file-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40181-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi , I did lot of search but i didn't find what i am interessting into. Here is my story. I am living in the GSM world. we can capture network traffic based on SIgtran interface ( SS7 over IP ). so on the sms world , you have always a request , then an ack from the platform ( HLR; MSC ). by example if you send a SRI request ( send routing information ) you will have a specific tcap.otid, the response will have the same value for tcap.dtid ( origin and destination ). this is usefull to follow a specific transaction in the middle of millions. what i want to do , is to calculate the response mean time for request using this correlation. it can be done manually for each request but it is tough. i ear about Lua , but is there any tools that can take a pcap trace and with a script calulate the response time? or is it possible to do this directly with wireshark ?. thx by advance for the help or your feedback half</p></div><div id="question-tags" class="tags-container tags">ss7 gsm</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '15, 04:21</strong></p><img src="https://secure.gravatar.com/avatar/e725c8d10c690c5d2a96fba7ac7b531a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="halfshiva&#39;s gravatar image" /><p>halfshiva<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="halfshiva has no accepted answers">0%</span></p></div></div><div id="comments-container-40181" class="comments-container"></div><div id="comment-tools-40181" class="comment-tools"></div><div class="clear"></div><div id="comment-40181-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40204"></span>

<div id="answer-container-40204" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40204-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi half,</p><p>As far as I'm aware there isn't a quick solution for what you are trying to do. You can do this with tshark/wireshark and lua but coding will be required.</p><p>You'd need to write a <a href="http://wiki.wireshark.org/Lua/Taps">lua tap</a> in which you would</p><p>a) build a table of transactions and then do analysis on them</p><p>b) consider corner cases where you don't capture start of transaction or end of it</p><p>c) periodically print output to text file and use that or feed data into database of some sort</p><p>I'd read through lua questions in this forum especially answers from <a href="https://ask.wireshark.org/users/4318/hadriel">Hadriel</a> he often posts code snippets.</p><p>And github is another great resource for finding wireshark lua code snippets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Mar '15, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-40204" class="comments-container"><span id="40256"></span><div id="comment-40256" class="comment"><div id="post-40256-score" class="comment-score"></div><div class="comment-text"><p>Hi Izopizo</p><p>Thx for your feedback,</p><p>I was scared about a response like this ^^</p><p>But i was more scary to learn about LUA and finally that could not help me. but regarding your response, it won't be a loose of time at all.</p><p>As soon i will perform what i expect , i will give feedback on this. This could be useful for GSM operator to know the average delivery time for short message or anything else that dealt with SS7 and TCAP protocol layer.</p><p>Br Half</p></div><div id="comment-40256-info" class="comment-info"><span class="comment-age">(04 Mar '15, 05:24)</span> halfshiva</div></div></div><div id="comment-tools-40204" class="comment-tools"></div><div class="clear"></div><div id="comment-40204-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

