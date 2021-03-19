+++
type = "question"
title = "Save only filtered SIP&#92;RTP results in a file"
description = '''We are testing a new SIP connection that uses MPLS on our production servers. The calls come in using SIP via our Telco, then if the caller asks to be connected to an agent we do a bridged transfer (via our MPLS connection) to the agent. We need to set up wireshark tracing and save them to files. Un...'''
date = "2015-02-05T08:01:00Z"
lastmod = "2015-02-05T08:30:00Z"
weight = 39670
keywords = [ "filter", "sip", "rtp", "file" ]
aliases = [ "/questions/39670" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Save only filtered SIP\\RTP results in a file](/questions/39670/save-only-filtered-siprtp-results-in-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39670-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are testing a new SIP connection that uses MPLS on our production servers. The calls come in using SIP via our Telco, then if the caller asks to be connected to an agent we do a bridged transfer (via our MPLS connection) to the agent.</p><p>We need to set up wireshark tracing and save them to files. Unfortunately we get so many calls that this uses up drive space incredibly quickly and we will not be able to run long enough to capture what we need before we run out of space.</p><p>Is there a way to apply multiple filters, ie: SIP and RTP only, and put ONLY those packets into the automatically created files?</p><p>If we could find a way to do that then we might be able to filter down to just what we need (maybe) and have the space to save those files.</p><p>The key is to apply the filter BEFORE any data gets saved.</p></div><div id="question-tags" class="tags-container tags">filter sip rtp file</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '15, 08:01</strong></p><img src="https://secure.gravatar.com/avatar/2c796223426577bdbfc1608dd4c40311?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sandy%20Murdock&#39;s gravatar image" /><p>Sandy Murdock<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sandy Murdock has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Feb '15, 08:48</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-39670" class="comments-container"></div><div id="comment-tools-39670" class="comment-tools"></div><div class="clear"></div><div id="comment-39670-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39671"></span>

<div id="answer-container-39671" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39671-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Been asked a few times before, e.g. <a href="https://ask.wireshark.org/questions/4470/how-can-i-only-capture-sip-packets">here</a></p><p>There's a discussion of a SIP\RTP capture filter <a href="http://www.dk-projects.org/windows/wireshark-tshark-capture-sip-rtp/">here</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Feb '15, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-39671" class="comments-container"></div><div id="comment-tools-39671" class="comment-tools"></div><div class="clear"></div><div id="comment-39671-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

