+++
type = "question"
title = "decoding timestamp in rtp header"
description = '''Hello, I&#x27;m running wireshark on debian Wheezy on x86_64 machine. I&#x27;ve found that when wireshark is decoding UDP as RTP packets, it&#x27;s decoding timestamp in RTP header incorrectly according to RFC3550 page 12: 4. Byte Order, Alignment, and Time Format  All integer fields are carried in network byte or...'''
date = "2015-06-03T10:13:00Z"
lastmod = "2015-06-03T12:42:00Z"
weight = 42854
keywords = [ "timestamps", "decode_rtp", "rtp" ]
aliases = [ "/questions/42854" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [decoding timestamp in rtp header](/questions/42854/decoding-timestamp-in-rtp-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42854-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm running wireshark on debian Wheezy on x86_64 machine. I've found that when wireshark is decoding UDP as RTP packets, it's decoding timestamp in RTP header incorrectly according to <a href="https://www.ietf.org/rfc/rfc3550.txt">RFC3550</a> page 12:</p><p><em>4. Byte Order, Alignment, and Time Format All integer fields are carried in network byte order, that is, most significant byte (octet) first. This byte order is commonly known as big-endian.</em></p><p>and page 76:</p><pre><code>    /*
    * RTP data header
    */
   typedef struct {
       unsigned int version:2;   /* protocol version */
       unsigned int p:1;         /* padding flag */
       unsigned int x:1;         /* header extension flag */
       unsigned int cc:4;        /* CSRC count */
       unsigned int m:1;         /* marker bit */
       unsigned int pt:7;        /* payload type */
       unsigned int seq:16;      /* sequence number */
       u_int32 ts;               /* timestamp */
       u_int32 ssrc;             /* synchronization source */
       u_int32 csrc[1];          /* optional CSRC list */
   } rtp_hdr_t;</code></pre><p>As you can see on the <a href="https://yadi.sk/i/OcEyTV_xh4ZX8">screenshot</a>, wireshark decodes timestamp "as is", without translating it from big-endian to little-endian for x86_64 arch.</p><p>Which way is correct?</p><p>I would like to check this fact in wireshark's source code and maybe fix it, but I don't have enough free time to read developers manual.</p><p>Could anybody please answer, where to find RTP-header parser source code in wireshark's sources ?</p><p>How to report about this MAY BE bug?</p></div><div id="question-tags" class="tags-container tags">timestamps decode_rtp rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '15, 10:13</strong></p><img src="https://secure.gravatar.com/avatar/50477ff991732c02ac2c07e8a93b40d8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yucacodec&#39;s gravatar image" /><p>yucacodec<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yucacodec has no accepted answers">0%</span></p></div></div><div id="comments-container-42854" class="comments-container"></div><div id="comment-tools-42854" class="comment-tools"></div><div class="clear"></div><div id="comment-42854-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="42855"></span>

<div id="answer-container-42855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42855-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your picture shows that Wireshark is decoding the field in big endian (network order): 1c6b89db in hexadecimal is equal to 476809691 in decimal. So there is nothing to fix here (what you see in the byte panel is what is transmitted over the wire, and does not represent the memory of your little endian machine).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '15, 12:42</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-42855" class="comments-container"><span id="42875"></span><div id="comment-42875" class="comment"><div id="post-42875-score" class="comment-score"></div><div class="comment-text"><p>yes, that's right. Thanks.</p></div><div id="comment-42875-info" class="comment-info"><span class="comment-age">(04 Jun '15, 01:59)</span> yucacodec</div></div><span id="42876"></span><div id="comment-42876" class="comment"><div id="post-42876-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-42876-info" class="comment-info"><span class="comment-age">(04 Jun '15, 02:17)</span> grahamb ♦</div></div></div><div id="comment-tools-42855" class="comment-tools"></div><div class="clear"></div><div id="comment-42855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

