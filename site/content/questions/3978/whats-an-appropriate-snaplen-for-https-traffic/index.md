+++
type = "question"
title = "What&#x27;s an appropriate snaplen for HTTPS traffic?"
description = '''My web server logs are telling me that I&#x27;m having trouble receiving data from my customers. I want to review the traffic to look for anomalies (lost packets and so forth). The actual traffic is encrypted HTTP, so I don&#x27;t care about the data beyond the information that should be present in the header...'''
date = "2011-05-06T09:29:00Z"
lastmod = "2011-05-07T02:28:00Z"
weight = 3978
keywords = [ "ssl", "dumpcap" ]
aliases = [ "/questions/3978" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What's an appropriate snaplen for HTTPS traffic?](/questions/3978/whats-an-appropriate-snaplen-for-https-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3978-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My web server logs are telling me that I'm having trouble receiving data from my customers. I want to review the traffic to look for anomalies (lost packets and so forth). The actual traffic is encrypted HTTP, so I don't care about the data beyond the information that should be present in the headers (length, etc).</p><p>My plan is to run dumpcap, with appropriate arguments, to log data to a file for later analysis.</p><p>To keep the size of the log file from getting out of control, I'd like to set a packet snapshot length to keep things manageable.</p><p>What snaplen is appropriate for this use case?</p></div><div id="question-tags" class="tags-container tags">ssl dumpcap</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '11, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/8911a98abd797fd928ab9f115becd08c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DanilSuits&#39;s gravatar image" /><p>DanilSuits<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DanilSuits has no accepted answers">0%</span></p></div></div><div id="comments-container-3978" class="comments-container"></div><div id="comment-tools-3978" class="comment-tools"></div><div class="clear"></div><div id="comment-3978-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="3985"></span>

<div id="answer-container-3985" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3985-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I totally agree with Jaap, you should check on <strong>your</strong> network to see what the actual headers look like, there might be vlan tagging, extra TCP options and other stuff enlarging the headers you would like to capture.</p><p>On a "vanilla" network, you would probably want to capture the Ethernet headers (14 bytes), the IP headers (normally 20 bytes) and the TCP headers (normally 20 bytes). IE 54 bytes should be enough, but values ussually seen as default are 68 bytes or 96 bytes. I tend to use 128 bytes in situations where I do not know what to expect up front.</p><p>However, I always try to avoid using a snaplength, because many times you start looking at what seems to be a problem at the network or transport layer, that in the end turns out to be a problem at the application layer. I don't want to have to make new traces every time that happens. So if you have the diskspace, use it :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '11, 02:28</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3985" class="comments-container"><span id="3993"></span><div id="comment-3993" class="comment"><div id="post-3993-score" class="comment-score"></div><div class="comment-text"><p>Yup, we use 128 byte snaplen as default as well. We're forbidden to take full packet captures (w/o various levels of approval), but I find that in most cases, 128 is enough.</p></div><div id="comment-3993-info" class="comment-info"><span class="comment-age">(07 May '11, 20:54)</span> hansangb</div></div></div><div id="comment-tools-3985" class="comment-tools"></div><div class="clear"></div><div id="comment-3985-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="3980"></span>

<div id="answer-container-3980" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3980-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Best way to figure that out is to make a sample capture and have a look.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '11, 10:21</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3980" class="comments-container"></div><div id="comment-tools-3980" class="comment-tools"></div><div class="clear"></div><div id="comment-3980-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

