+++
type = "question"
title = "tshark 2.0.2 does not support gsm_a.imsi field ?"
description = '''hi, I am using tshark version 2.0.2, and tshark is not able to decode the field gsm_a.imsi (SGSAP message). Observing the below error message when I execute the tshark command. tshark -r test.pcap -T fields -e gsm_a.imsi tshark: Some fields aren&#x27;t valid:  gsm_a.imsi test.pcap has the sgsap message w...'''
date = "2016-04-14T12:26:00Z"
lastmod = "2016-04-14T14:19:00Z"
weight = 51679
keywords = [ "tshark", "error" ]
aliases = [ "/questions/51679" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [tshark 2.0.2 does not support gsm\_a.imsi field ?](/questions/51679/tshark-202-does-not-support-gsm_aimsi-field)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51679-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi,</p><p>I am using tshark version 2.0.2, and tshark is not able to decode the field gsm_a.imsi (SGSAP message).</p><p>Observing the below error message when I execute the tshark command.</p><p>tshark -r test.pcap -T fields -e gsm_a.imsi tshark: Some fields aren't valid: gsm_a.imsi</p><p>test.pcap has the sgsap message with imsi IE.</p><p>Anyone observing the same problem ? Can you please let me know how to resolve this issue. Thanks</p></div><div id="question-tags" class="tags-container tags">tshark error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '16, 12:26</strong></p><img src="https://secure.gravatar.com/avatar/1d6f98501f12ada1577d59b763710338?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="srikanthtl&#39;s gravatar image" /><p>srikanthtl<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="srikanthtl has no accepted answers">0%</span></p></div></div><div id="comments-container-51679" class="comments-container"></div><div id="comment-tools-51679" class="comment-tools"></div><div class="clear"></div><div id="comment-51679-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51686"></span>

<div id="answer-container-51686" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51686-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>That field was renamed to <code>e212.imsi</code> (this is actually a common IMSI field--so you can find all messages about a given IMSI, regardless of the protocol (at least for protocols that have been converted to use that field)).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '16, 14:19</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-51686" class="comments-container"><span id="51687"></span><div id="comment-51687" class="comment"><div id="post-51687-score" class="comment-score"></div><div class="comment-text"><p>Thanks..it works now</p></div><div id="comment-51687-info" class="comment-info"><span class="comment-age">(14 Apr '16, 14:32)</span> srikanthtl</div></div><span id="51688"></span><div id="comment-51688" class="comment"><div id="post-51688-score" class="comment-score"></div><div class="comment-text"><p>(I converted your answer to a comment.)</p><p>If an answer answers your question, please be sure to accept it (by clicking on the checkmark next to the answer). That way the question will no longer show up as unanswered.</p></div><div id="comment-51688-info" class="comment-info"><span class="comment-age">(14 Apr '16, 14:50)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-51686" class="comment-tools"></div><div class="clear"></div><div id="comment-51686-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

