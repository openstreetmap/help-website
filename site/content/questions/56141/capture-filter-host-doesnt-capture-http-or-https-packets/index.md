+++
type = "question"
title = "capture filter host doesn&#x27;t capture http or https packets"
description = '''I&#x27;m trying to capture all traffic to and from a specific host. I created a capture filter as follows: host &amp;lt;ip address&amp;gt;. The capture filter seems to work because ping and ssh packets are captured. However, when I use a browser (Chrome, IE, or Firefox), I&#x27;m unable to capture packets using HTTP ...'''
date = "2016-10-04T11:53:00Z"
lastmod = "2016-10-04T12:04:00Z"
weight = 56141
keywords = [ "host", "capture-filter" ]
aliases = [ "/questions/56141" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter host doesn't capture http or https packets](/questions/56141/capture-filter-host-doesnt-capture-http-or-https-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56141-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to capture all traffic to and from a specific host. I created a capture filter as follows: host &lt;<em>ip address</em>&gt;. The capture filter seems to work because ping and ssh packets are captured. However, when I use a browser (Chrome, IE, or Firefox), I'm unable to capture packets using HTTP or HTTPS. What's going on?</p></div><div id="question-tags" class="tags-container tags">host capture-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Oct '16, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/084ad20c1f4a1764680f93b85a3f3057?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vlm&#39;s gravatar image" /><p>vlm<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vlm has no accepted answers">0%</span></p></div></div><div id="comments-container-56141" class="comments-container"></div><div id="comment-tools-56141" class="comment-tools"></div><div class="clear"></div><div id="comment-56141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56143"></span>

<div id="answer-container-56143" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56143-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using a proxy? If so, all your HTTP/HTTPS traffic is sent there, so if you exclude it with an IP address filter you'll not see any of it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Oct '16, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-56143" class="comments-container"><span id="56144"></span><div id="comment-56144" class="comment"><div id="post-56144-score" class="comment-score"></div><div class="comment-text"><p>Jasper, I do forward to a proxy server. I excluded the IP address and got it to work. Thank you very much.</p></div><div id="comment-56144-info" class="comment-info"><span class="comment-age">(04 Oct '16, 12:21)</span> vlm</div></div></div><div id="comment-tools-56143" class="comment-tools"></div><div class="clear"></div><div id="comment-56143-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

