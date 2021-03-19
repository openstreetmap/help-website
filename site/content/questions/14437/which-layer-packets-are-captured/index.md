+++
type = "question"
title = "Which layer packets are captured?"
description = '''Hello, Can you please let me know at which layer snoop captures packets? Is it after physical layer or? Thanks, Siva'''
date = "2012-09-21T09:58:00Z"
lastmod = "2012-09-21T11:49:00Z"
weight = 14437
keywords = [ "layer" ]
aliases = [ "/questions/14437" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Which layer packets are captured?](/questions/14437/which-layer-packets-are-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14437-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, Can you please let me know at which layer snoop captures packets? Is it after physical layer or?</p><p>Thanks, Siva</p></div><div id="question-tags" class="tags-container tags">layer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '12, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/49a0e0b5276367497f3db29731dc4cf8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vnkt4u&#39;s gravatar image" /><p>vnkt4u<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vnkt4u has no accepted answers">0%</span></p></div></div><div id="comments-container-14437" class="comments-container"></div><div id="comment-tools-14437" class="comment-tools"></div><div class="clear"></div><div id="comment-14437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14439"></span>

<div id="answer-container-14439" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14439-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Is that "snoop" as in "the Solaris (and IRIX?) packet analyzer named "snoop"" or "snoop" as in "packet analyzers in general, including Wireshark"?</p><p>In either case, if you use the OSI model, the capturing is usually done at the data link layer, above the physical layer, at least for LAN traffic. For WANs it might be above some part of the data link layer; for example, ATM traffic might not capture each ATM cell individually, but might get an entire AAL5 PDU as a single reassembled frame, and PPP over a T-carrier or E-carrier link might show PPP frames without the underlying "HDLC-like framing".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Sep '12, 11:49</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-14439" class="comments-container"></div><div id="comment-tools-14439" class="comment-tools"></div><div class="clear"></div><div id="comment-14439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

