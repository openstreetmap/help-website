+++
type = "question"
title = "RST after SYN -&gt; SYN/ACK"
description = '''Hi I need your help: I&#x27;ve got a strange TCP problem...can you guys tell me why a RST is sent after the SYN, SYN/ACK?  Grab the whole file here: TCP_SYN_WIRESHARK.pcap'''
date = "2016-07-26T12:40:00Z"
lastmod = "2016-07-26T13:23:00Z"
weight = 54348
keywords = [ "rst", "syn+ack", "syn", "tcp" ]
aliases = [ "/questions/54348" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [RST after SYN -&gt; SYN/ACK](/questions/54348/rst-after-syn-synack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54348-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54348-score" class="post-score" title="current number of votes">0</div><span id="post-54348-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I need your help: I've got a strange TCP problem...can you guys tell me why a RST is sent after the SYN, SYN/ACK?</p><p><img src="https://dl.dropboxusercontent.com/u/5361095/Screenshot%20from%202016-07-26%2021-31-17.png" alt="Wireshark Screenshot" /></p><p>Grab the whole file here: <a href="https://dl.dropboxusercontent.com/u/5361095/TCP_SYN_WIRESHARK.pcap">TCP_SYN_WIRESHARK.pcap</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rst" rel="tag" title="see questions tagged &#39;rst&#39;">rst</span> <span class="post-tag tag-link-syn+ack" rel="tag" title="see questions tagged &#39;syn+ack&#39;">syn+ack</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jul '16, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/eadbd1aa073e35a7ca23f34d98e0c916?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pesc&#39;s gravatar image" /><p><span>pesc</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pesc has no accepted answers">0%</span></p></img></div></div><div id="comments-container-54348" class="comments-container"></div><div id="comment-tools-54348" class="comment-tools"></div><div class="clear"></div><div id="comment-54348-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54349"></span>

<div id="answer-container-54349" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54349-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54349-score" class="post-score" title="current number of votes">1</div><span id="post-54349-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pesc has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That usually happens if your application developer put a socket timeout value into his code that closes the socket way too quick. Or, in case of a web browser it was closed right after calling the URL, which would also cause a socket close leading to a reset.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Jul '16, 12:44</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-54349" class="comments-container"><span id="54350"></span><div id="comment-54350" class="comment"><div id="post-54350-score" class="comment-score"></div><div class="comment-text"><p>Hmm, I'm using SQUID..any idea how to adjust?</p></div><div id="comment-54350-info" class="comment-info"><span class="comment-age">(26 Jul '16, 12:54)</span> <span class="comment-user userinfo">pesc</span></div></div><span id="54351"></span><div id="comment-54351" class="comment"><div id="post-54351-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I don't know Squid config files that good.</p></div><div id="comment-54351-info" class="comment-info"><span class="comment-age">(26 Jul '16, 12:56)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="54352"></span><div id="comment-54352" class="comment"><div id="post-54352-score" class="comment-score"></div><div class="comment-text"><p>ok thank you! But I'm right that no TCP (SEQ missmatch, etc...) is the problem?</p></div><div id="comment-54352-info" class="comment-info"><span class="comment-age">(26 Jul '16, 13:00)</span> <span class="comment-user userinfo">pesc</span></div></div><span id="54353"></span><div id="comment-54353" class="comment"><div id="post-54353-score" class="comment-score"></div><div class="comment-text"><p>No, TCP sequencing looks fine</p></div><div id="comment-54353-info" class="comment-info"><span class="comment-age">(26 Jul '16, 13:02)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="54354"></span><div id="comment-54354" class="comment"><div id="post-54354-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jasper!</p></div><div id="comment-54354-info" class="comment-info"><span class="comment-age">(26 Jul '16, 13:05)</span> <span class="comment-user userinfo">pesc</span></div></div><span id="54355"></span><div id="comment-54355" class="comment not_top_scorer"><div id="post-54355-score" class="comment-score"></div><div class="comment-text"><p>But the time between SYN -&gt; SYN/ACK is just about 200ms -&gt; that's not abnormal, right?</p></div><div id="comment-54355-info" class="comment-info"><span class="comment-age">(26 Jul '16, 13:10)</span> <span class="comment-user userinfo">pesc</span></div></div><span id="54356"></span><div id="comment-54356" class="comment not_top_scorer"><div id="post-54356-score" class="comment-score"></div><div class="comment-text"><p>I have a delta of about 131 milliseconds, which ain't good but also not uncommon for remote sites. Where do you see 200ms?</p></div><div id="comment-54356-info" class="comment-info"><span class="comment-age">(26 Jul '16, 13:13)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="54357"></span><div id="comment-54357" class="comment not_top_scorer"><div id="post-54357-score" class="comment-score"></div><div class="comment-text"><p>Yeah, I've just rounded up :) You're right, its 131 ms...could it also be a kernel issue?</p></div><div id="comment-54357-info" class="comment-info"><span class="comment-age">(26 Jul '16, 13:15)</span> <span class="comment-user userinfo">pesc</span></div></div><span id="54358"></span><div id="comment-54358" class="comment not_top_scorer"><div id="post-54358-score" class="comment-score"></div><div class="comment-text"><p>Never seen a kernel do that on its own. It's usually an application socket shutting down which forces the kernel to send the reset packet.</p></div><div id="comment-54358-info" class="comment-info"><span class="comment-age">(26 Jul '16, 13:23)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-54349" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-54349-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

