+++
type = "question"
title = "How to calculate SNR values?"
description = '''Hello, I have difficulties in calculating SNR values using wireshark. Software Network Stumbler can do it but I can&#x27;t save those values into file. Can I do it using Wireshark? Please I need your help. Thank you.'''
date = "2012-12-02T18:27:00Z"
lastmod = "2012-12-02T23:22:00Z"
weight = 16489
keywords = [ "snr" ]
aliases = [ "/questions/16489" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to calculate SNR values?](/questions/16489/how-to-calculate-snr-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16489-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have difficulties in calculating SNR values using wireshark. Software Network Stumbler can do it but I can't save those values into file. Can I do it using Wireshark? Please I need your help. Thank you.</p></div><div id="question-tags" class="tags-container tags">snr</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '12, 18:27</strong></p><img src="https://secure.gravatar.com/avatar/a3291ae3aa2fd3100059945d1afa121c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tyanium&#39;s gravatar image" /><p>Tyanium<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tyanium has no accepted answers">0%</span></p></div></div><div id="comments-container-16489" class="comments-container"></div><div id="comment-tools-16489" class="comment-tools"></div><div class="clear"></div><div id="comment-16489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16492"></span>

<div id="answer-container-16492" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16492-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>see this similar question:</p><blockquote><p><code>http://ask.wireshark.org/questions/3330/get-snr-from-wlan-capture</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '12, 23:22</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16492" class="comments-container"><span id="16494"></span><div id="comment-16494" class="comment"><div id="post-16494-score" class="comment-score"></div><div class="comment-text"><p>But I can't find how to show signal and noise values as columns as you said. Please tell me how to.</p></div><div id="comment-16494-info" class="comment-info"><span class="comment-age">(02 Dec '12, 23:44)</span> Tyanium</div></div><span id="16500"></span><div id="comment-16500" class="comment"><div id="post-16500-score" class="comment-score"></div><div class="comment-text"><p>Quote from the answer:</p><blockquote><p><code>Wireshark doesn't currently calculate an SNR from signal and noise values, so it can't directly display the SNR.</code><br />
</p></blockquote><p>To show the signal and noise values of the PPI header (if it's in the capture file!), use these filters for the columns (add a <strong>custom</strong> column):</p><blockquote><p><code>ppi.80211-common.dbm.antsignal</code><br />
<code>ppi.80211-common.dbm.antnoise</code><br />
</p></blockquote><p>column Tutorial</p><blockquote><p><code>www.lovemytool.com/blog/2009/10/chris_greer_10.html</code></p></blockquote></div><div id="comment-16500-info" class="comment-info"><span class="comment-age">(03 Dec '12, 04:55)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16492" class="comment-tools"></div><div class="clear"></div><div id="comment-16492-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

