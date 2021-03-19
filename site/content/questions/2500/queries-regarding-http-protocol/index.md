+++
type = "question"
title = "queries regarding http protocol"
description = '''Hi, I wanted to ask following questions for long. I tried fetching information from various RFCs, mailing lists, forums etc. but no luck. Finally I found this site and decided to post questions here. They are as follows: How can we get request Vs response delay for HTTP protocol? How exactly to plot...'''
date = "2011-02-22T12:28:00Z"
lastmod = "2011-02-22T14:26:00Z"
weight = 2500
keywords = [ "performance" ]
aliases = [ "/questions/2500" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [queries regarding http protocol](/questions/2500/queries-regarding-http-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2500-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I wanted to ask following questions for long. I tried fetching information from various RFCs, mailing lists, forums etc. but no luck. Finally I found this site and decided to post questions here. They are as follows:</p><p>How can we get request Vs response delay for HTTP protocol?</p><p>How exactly to plot LOAD(*) graphs for HTTP protocol?</p><p>How can I use wireshark to identify performance bottleneck between proxy server and web server?</p><p>Regards, Vijay</p></div><div id="question-tags" class="tags-container tags">performance</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '11, 12:28</strong></p><img src="https://secure.gravatar.com/avatar/d1e5efe891c907bf6be8231eca9db31a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vijay%20Gharge&#39;s gravatar image" /><p>Vijay Gharge<br />
<span class="score" title="36 reputation points">36</span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="20 badges"><span class="bronze">●</span><span class="badgecount">20</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vijay Gharge has no accepted answers">0%</span></p></div></div><div id="comments-container-2500" class="comments-container"></div><div id="comment-tools-2500" class="comment-tools"></div><div class="clear"></div><div id="comment-2500-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2506"></span>

<div id="answer-container-2506" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2506-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The HTTP protocol does not have response times yet. It is something I have started working on a while back, but it got stranded as HTTP pipelining kinda makes it a little more complex as I initially thought :-)</p><p>Because there is no response time analysis, there is also no way to use the LOAD(*) graphs for HTTP. You will have to analyze the problems manually unfortunately.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '11, 14:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-2506" class="comments-container"><span id="2552"></span><div id="comment-2552" class="comment"><div id="post-2552-score" class="comment-score"></div><div class="comment-text"><p>Thanks sake for this.</p></div><div id="comment-2552-info" class="comment-info"><span class="comment-age">(24 Feb '11, 08:13)</span> Vijay Gharge</div></div></div><div id="comment-tools-2506" class="comment-tools"></div><div class="clear"></div><div id="comment-2506-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

