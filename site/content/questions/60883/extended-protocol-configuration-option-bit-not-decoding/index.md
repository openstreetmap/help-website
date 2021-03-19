+++
type = "question"
title = "extended Protocol Configuration Option bit not decoding"
description = '''Hello, I am using latest version of wireshark (v 2.2.6). But am getting malformed packet error when am adding ePCO in Attach Request. Also the same bit is not coming in indication flag in S11 messages (Create Session request and Modify bearer request) along with ePCO value. And also am expecting the...'''
date = "2017-04-19T03:28:00Z"
lastmod = "2017-04-19T04:46:00Z"
weight = 60883
keywords = [ "epco" ]
aliases = [ "/questions/60883" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [extended Protocol Configuration Option bit not decoding](/questions/60883/extended-protocol-configuration-option-bit-not-decoding)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60883-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am using latest version of wireshark (v 2.2.6). But am getting malformed packet error when am adding ePCO in Attach Request. Also the same bit is not coming in indication flag in S11 messages (Create Session request and Modify bearer request) along with ePCO value. And also am expecting the epCO bit and value in Attach Accept message as part of NAS message.</p><p>Can you please let me know whether I can get a fix for the above issue?</p><p>Br, Rajeev</p></div><div id="question-tags" class="tags-container tags">epco</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '17, 03:28</strong></p><img src="https://secure.gravatar.com/avatar/4e676b8c405e5833924c3721e2f7dcc2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MME&#39;s gravatar image" /><p>MME<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MME has no accepted answers">0%</span></p></div></div><div id="comments-container-60883" class="comments-container"></div><div id="comment-tools-60883" class="comment-tools"></div><div class="clear"></div><div id="comment-60883-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="60885"></span>

<div id="answer-container-60885" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60885-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should follow the information in the Wiki page <a href="https://wiki.wireshark.org/ReportingBugs">Reporting Bugs</a> to create a Bugzilla entry (attaching a capture), which is the preferred method for reporting a bug.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '17, 03:32</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-60885" class="comments-container"><span id="60886"></span><div id="comment-60886" class="comment"><div id="post-60886-score" class="comment-score"></div><div class="comment-text"><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13621">Bug 13621</a> has been successfully created</p></div><div id="comment-60886-info" class="comment-info"><span class="comment-age">(19 Apr '17, 04:12)</span> MME</div></div></div><div id="comment-tools-60885" class="comment-tools"></div><div class="clear"></div><div id="comment-60885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="60888"></span>

<div id="answer-container-60888" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-60888-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>the ePCO bit decoding (along with most of R13 3GPP features) are in Wireshark 2.3.X development branch, not 2.X stable branch. Please use a <a href="https://www.wireshark.org/download/automated/">development build</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '17, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-60888" class="comments-container"></div><div id="comment-tools-60888" class="comment-tools"></div><div class="clear"></div><div id="comment-60888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

