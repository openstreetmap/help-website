+++
type = "question"
title = "Using MATE with MGCP"
description = '''I have wireshark version 1.12.8 and am trying to use MATE to analyse MGCP capture. Using the following mate file: Pdu mgcp_pdu Proto mgcp Transport ip {  Extract addr From ip.addr;  Extract transid From mgcp.transid;  Extract endpoint From mgcp.req.endpoint;  Extract callid From mgcp.param.callid; }...'''
date = "2015-12-13T18:28:00Z"
lastmod = "2016-02-12T12:57:00Z"
weight = 48499
keywords = [ "mate", "mgcp" ]
aliases = [ "/questions/48499" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using MATE with MGCP](/questions/48499/using-mate-with-mgcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48499-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have wireshark version 1.12.8 and am trying to use MATE to analyse MGCP capture.</p><p>Using the following mate file:</p><pre><code>Pdu mgcp_pdu Proto mgcp Transport ip {
    Extract addr From ip.addr;
    Extract transid From mgcp.transid;
    Extract endpoint From mgcp.req.endpoint;
    Extract callid From mgcp.param.callid;
};
Done;</code></pre><p>Starting wireshark with option to load mate file.</p><p>wireshark -o "mate.config: mgcp.mate" -r mcgp.cap</p><p>After loading files wireshark show the MATE heading in the Packet Details frame but only with source and destination ip addresses. None of MGCP parameters are displayed. Is this a bug or am I doing something wrong?</p><p>Thanks,</p><p>Paul</p></div><div id="question-tags" class="tags-container tags">mate mgcp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '15, 18:28</strong></p><img src="https://secure.gravatar.com/avatar/93e6b9944d62463aace3c62d2300cf7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paul%20Hughes&#39;s gravatar image" /><p>Paul Hughes<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paul Hughes has no accepted answers">0%</span></p></div></div><div id="comments-container-48499" class="comments-container"></div><div id="comment-tools-48499" class="comment-tools"></div><div class="clear"></div><div id="comment-48499-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50165"></span>

<div id="answer-container-50165" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50165-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This seems like a bug to me. I can't figure out how to get any mgcp fields to be <em>"mate-extracted"</em> either. I would suggest filing a <a href="https://bugs.wireshark.org/bugzilla/">bug report</a> for it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '16, 12:57</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-50165" class="comments-container"></div><div id="comment-tools-50165" class="comment-tools"></div><div class="clear"></div><div id="comment-50165-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

