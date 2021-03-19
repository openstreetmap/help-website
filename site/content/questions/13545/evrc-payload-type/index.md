+++
type = "question"
title = "EVRC payload type"
description = '''Hi, I would like to parse my EVRC-A / EVRC-B RTP packets (as per RFC3558 and RFC4788) into Windows Wireshark. Which RTP payload does it need to be parsed as EVRC? I went into preferences/EVRC but only found a check box to &quot;Add sissector for Legacy EVRC...&quot;. Is there a way to specify my EVRC payload ...'''
date = "2012-08-10T08:29:00Z"
lastmod = "2012-08-11T04:26:00Z"
weight = 13545
keywords = [ "evrc" ]
aliases = [ "/questions/13545" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [EVRC payload type](/questions/13545/evrc-payload-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13545-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I would like to parse my EVRC-A / EVRC-B RTP packets (as per RFC3558 and RFC4788) into Windows Wireshark. Which RTP payload does it need to be parsed as EVRC? I went into preferences/EVRC but only found a check box to "Add sissector for Legacy EVRC...". Is there a way to specify my EVRC payload type?</p><p>Thanks,</p><p>Mark</p></div><div id="question-tags" class="tags-container tags">evrc</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Aug '12, 08:29</strong></p><img src="https://secure.gravatar.com/avatar/b082d291b1bc6ccf88f53f21771d17e6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maboisv&#39;s gravatar image" /><p>maboisv<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maboisv has no accepted answers">0%</span></p></div></div><div id="comments-container-13545" class="comments-container"></div><div id="comment-tools-13545" class="comment-tools"></div><div class="clear"></div><div id="comment-13545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13554"></span>

<div id="answer-container-13554" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13554-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no need to specify the EVRC type, as the dissector should detect that by itself. There is code in the dissector for these types:</p><ul><li>EVRC-A</li><li>EVRC-B</li><li>EVRC-C (EVRC-WB)</li><li>EVRC NW</li><li>some Legacy encoding, which you can enable with the EVRC preferences</li></ul><blockquote><p><code>http://anonsvn.wireshark.org/wireshark/trunk/epan/dissectors/packet-evrc.c</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Aug '12, 04:26</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-13554" class="comments-container"></div><div id="comment-tools-13554" class="comment-tools"></div><div class="clear"></div><div id="comment-13554-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

