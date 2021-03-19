+++
type = "question"
title = "HTTP = Requests + Responses?"
description = '''Hi, I used these 3 filters to count http packet numbers: For Http packets: &quot;port http&quot; For Http request packets: &quot;tcp dst port 80 and (((ip[2:2] - ((ip[0]&amp;amp;0xf)&amp;lt;&amp;lt;2)) - ((tcp[12]&amp;amp;0xf0)&amp;gt;&amp;gt;2)) != 0)&quot; For Http response packets: &quot;tcp src port 80 and (((ip[2:2] - ((ip[0]&amp;amp;0xf)&amp;lt;&amp;lt;...'''
date = "2014-06-17T00:03:00Z"
lastmod = "2014-06-17T07:52:00Z"
weight = 33882
keywords = [ "count", "http", "request", "response" ]
aliases = [ "/questions/33882" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [HTTP = Requests + Responses?](/questions/33882/http-requests-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33882-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I used these 3 filters to count http packet numbers:</p><p>For Http packets: "port http"</p><p>For Http request packets: "tcp dst port 80 and (((ip[2:2] - ((ip[0]&amp;0xf)&lt;&lt;2)) - ((tcp[12]&amp;0xf0)&gt;&gt;2)) != 0)"</p><p>For Http response packets: "tcp src port 80 and (((ip[2:2] - ((ip[0]&amp;0xf)&lt;&lt;2)) - ((tcp[12]&amp;0xf0)&gt;&gt;2)) != 0)"</p><p>And with this file:</p><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=http.cap">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=http.cap</a> I got this result:</p><p>Http pkt count= 479 Http req count= 1 Http res count= 168</p><p>The question is: How come req + res != total? What are those 310 packets?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">count http request response</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Jun '14, 00:03</strong></p><img src="https://secure.gravatar.com/avatar/07da332d5eb4e9d3e3c205c281a4d003?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abd&#39;s gravatar image" /><p>abd<br />
<span class="score" title="21 reputation points">21</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Jun '14, 00:04</p></div></div><div id="comments-container-33882" class="comments-container"><span id="33891"></span><div id="comment-33891" class="comment"><div id="post-33891-score" class="comment-score"></div><div class="comment-text"><p>I think those other 310 packets are "continuation or non-http traffic packet" when you enable "Reassemble HTTP Headers spanning multiple TCP Segment" in http preferences, it will disappear.</p></div><div id="comment-33891-info" class="comment-info"><span class="comment-age">(17 Jun '14, 05:04)</span> kishan pandey</div></div></div><div id="comment-tools-33882" class="comment-tools"></div><div class="clear"></div><div id="comment-33882-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33893"></span>

<div id="answer-container-33893" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33893-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Those 310 packets, are probably those that you filtered 'away' with the following term</p><blockquote><p>(((ip[2:2] - ((ip[0]&amp;0xf)&lt;&lt;2)) - ((tcp[12]&amp;0xf0)&gt;&gt;2)) != 0)</p></blockquote><p>as that the difference between 'port http' which is equivalent to</p><blockquote><p>tcp dst port 80 or tcp scr port 80</p></blockquote><p>So, if you filter for (in the first step)</p><blockquote><p>port http and (((ip[2:2] - ((ip[0]&amp;0xf)&lt;&lt;2)) - ((tcp[12]&amp;0xf0)&gt;&gt;2)) != 0)</p></blockquote><p>you should get the same results.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Jun '14, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-33893" class="comments-container"><span id="33915"></span><div id="comment-33915" class="comment"><div id="post-33915-score" class="comment-score"></div><div class="comment-text"><p>Thanks. Well, there is something that I didn't know about http. There are many packets in response of a request, that don't have Application Layer Header. They're probably the continuation of a response packet(with Application Layer Header) which didn't finished in the response packet itself. So, my stats is actually true. HTTP != Req pkts + Res pkts. Thanks you sooo much for leading me to understand this.</p><p>Thanks</p></div><div id="comment-33915-info" class="comment-info"><span class="comment-age">(17 Jun '14, 21:09)</span> abd</div></div><span id="33932"></span><div id="comment-33932" class="comment"><div id="post-33932-score" class="comment-score"></div><div class="comment-text"><p>Good.</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-33932-info" class="comment-info"><span class="comment-age">(18 Jun '14, 09:48)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33893" class="comment-tools"></div><div class="clear"></div><div id="comment-33893-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

