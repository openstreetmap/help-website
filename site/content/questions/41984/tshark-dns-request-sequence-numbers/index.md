+++
type = "question"
title = "tshark DNS request sequence numbers (?)"
description = '''Hi everyone, I am running tshark on a WAP to make various analyses of my clients&#x27; traffic. One of the things I do is monitor all DNS requests to find out which hosts the clients want to access. All I basically want for further processing (in Python) is the source MAC and DNS name of every query, so ...'''
date = "2015-04-30T09:51:00Z"
lastmod = "2015-04-30T12:07:00Z"
weight = 41984
keywords = [ "tshark", "dns" ]
aliases = [ "/questions/41984" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark DNS request sequence numbers (?)](/questions/41984/tshark-dns-request-sequence-numbers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everyone,</p><p>I am running tshark on a WAP to make various analyses of my clients' traffic. One of the things I do is monitor all DNS requests to find out which hosts the clients want to access. All I basically want for further processing (in Python) is the source MAC and DNS name of every query, so i came up with the following command...</p><pre><code>tshark -n -T fields -e eth.src -e dns.qry.name -f &quot;port 53&quot; -i wlan0</code></pre><p>...and it's working, basically, but some of the tshark output lines start with some kind of sequence number, like this:</p><p>c4:43:8f:c5:60:5c i.instagram.com<br />
<em>1 c4:43:8f:c5:60:5c telegraph-ash.instagram.com</em><br />
c0:4a:00:10:0b:56 telegraph-ash.instagram.com<br />
c0:4a:00:10:0b:56 i.instagram.com<br />
<em>4 c4:43:8f:c5:60:5c dict.leo.org</em><br />
c0:4a:00:10:0b:56 dict.leo.org<br />
</p><p>What are those and how can I get rid of them? As I said, I'm only interested in who asks for which address to resolve.</p><p>Thanks in advance for any help.</p></div><div id="question-tags" class="tags-container tags">tshark dns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Apr '15, 09:51</strong></p><img src="https://secure.gravatar.com/avatar/6ea26cc290201db630ecd0f35b4e58cb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="teenious&#39;s gravatar image" /><p>teenious<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="teenious has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-41984" class="comments-container"><span id="41986"></span><div id="comment-41986" class="comment"><div id="post-41986-score" class="comment-score"></div><div class="comment-text"><p>tshark version and host OS?</p></div><div id="comment-41986-info" class="comment-info"><span class="comment-age">(30 Apr '15, 10:06)</span> grahamb ♦</div></div><span id="41987"></span><div id="comment-41987" class="comment"><div id="post-41987-score" class="comment-score"></div><div class="comment-text"><p>It's tshark 1.10.6 on xubuntu 14.04</p></div><div id="comment-41987-info" class="comment-info"><span class="comment-age">(30 Apr '15, 10:10)</span> teenious</div></div></div><div id="comment-tools-41984" class="comment-tools"></div><div class="clear"></div><div id="comment-41984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41990"></span>

<div id="answer-container-41990" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41990-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That's the packet count number. See the answer to a similar question.</p><blockquote><p><a href="https://ask.wireshark.org/questions/31564/tshark-output-refining">https://ask.wireshark.org/questions/31564/tshark-output-refining</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Apr '15, 12:07</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-41990" class="comments-container"><span id="42002"></span><div id="comment-42002" class="comment"><div id="post-42002-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, Kurt, upgrading tshark solved my problem. I'm a bit embarrassed I didn't stumble upon the other thread myself, but then again, my searches for "packet number" and "sequence number" didn't yield a lot of useful results...</p></div><div id="comment-42002-info" class="comment-info"><span class="comment-age">(01 May '15, 10:13)</span> teenious</div></div></div><div id="comment-tools-41990" class="comment-tools"></div><div class="clear"></div><div id="comment-41990-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

