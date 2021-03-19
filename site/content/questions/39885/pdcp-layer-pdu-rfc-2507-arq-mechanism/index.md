+++
type = "question"
title = "PDCP layer PDU RFC 2507 ARQ Mechanism"
description = '''Hi , Iam developing a custom dissector on top of UDP which uses PDCP layer PDU RFC 2507 Selective Repeat ARQ Mechanism for segmentation and Reassembly. My message contains   Beginning of Message   continuation of message and   end of message  Messages are not coming in sequence and based on sequence...'''
date = "2015-02-16T02:17:00Z"
lastmod = "2015-02-17T03:23:00Z"
weight = 39885
keywords = [ "pdcp", "layer", "pdu" ]
aliases = [ "/questions/39885" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PDCP layer PDU RFC 2507 ARQ Mechanism](/questions/39885/pdcp-layer-pdu-rfc-2507-arq-mechanism)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39885-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>Iam developing a custom dissector on top of UDP which uses PDCP layer PDU RFC 2507 Selective Repeat ARQ Mechanism for segmentation and Reassembly.</p><p>My message contains</p><pre><code>          Beginning of Message

          continuation of message and

          end of message</code></pre><p>Messages are not coming in sequence and based on sequence number and message id i need to reassemble.</p><p>I dont know whether i should use</p><pre><code>          conversation or

          add_fragment_seq_next or

          add_fragment_seq_check</code></pre><p>Please suggest. I got stuck with this for long time.</p></div><div id="question-tags" class="tags-container tags">pdcp layer pdu</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '15, 02:17</strong></p><img src="https://secure.gravatar.com/avatar/1339589a92af9455063c09e56bfc6299?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="umar&#39;s gravatar image" /><p>umar<br />
<span class="score" title="26 reputation points">26</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="umar has no accepted answers">0%</span></p></div></div><div id="comments-container-39885" class="comments-container"><span id="39890"></span><div id="comment-39890" class="comment"><div id="post-39890-score" class="comment-score"></div><div class="comment-text"><p>You are giving to little information for us to be able to help you. Wireshark has a dissector for 3GPP TS 36.323 PDCP googling there is also 3GPP TS 25.323. The RFC you reference deals only with header compression... If the messages are not comming in sequence there should be a sequence number in them I suppose and of course you need to use that for reassembly.</p></div><div id="comment-39890-info" class="comment-info"><span class="comment-age">(16 Feb '15, 07:08)</span> Anders ♦</div></div><span id="39892"></span><div id="comment-39892" class="comment"><div id="post-39892-score" class="comment-score"></div><div class="comment-text"><p>Hi anders thank you very much for your reply. Actually iam using sequence number for reassembly. my fragment table is always returning NULL value. I have posted my code here and yet to get reply. Can you have a look please. I have gone through many example code in epan library but could not find anything. Don't know why my frag_head is empty. Please help . Thanks</p><p><a href="https://ask.wireshark.org/questions/39824/fragmentation-error-status-access-violation">https://ask.wireshark.org/questions/39824/fragmentation-error-status-access-violation</a></p></div><div id="comment-39892-info" class="comment-info"><span class="comment-age">(16 Feb '15, 08:34)</span> umar</div></div></div><div id="comment-tools-39885" class="comment-tools"></div><div class="clear"></div><div id="comment-39885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39909"></span>

<div id="answer-container-39909" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39909-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>For reference, the answer was given in this wireshark-dev mailing list <a href="https://www.wireshark.org/lists/wireshark-dev/201502/msg00119.html">thread</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '15, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-39909" class="comments-container"></div><div id="comment-tools-39909" class="comment-tools"></div><div class="clear"></div><div id="comment-39909-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

