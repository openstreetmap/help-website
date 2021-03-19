+++
type = "question"
title = "When to use tvb_reported_length?"
description = '''I am aware that tvb_captured_length describes the available data for dissection, and tvb_reported_length the data that was available in the real world (snaplen). tvb_captured_length should be used when:  A new dissector needs to return a value to indicate acceptance of packet data.  When should tvb_...'''
date = "2014-07-04T04:08:00Z"
lastmod = "2014-07-04T07:14:00Z"
weight = 34404
keywords = [ "tvb_length" ]
aliases = [ "/questions/34404" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [When to use tvb\_reported\_length?](/questions/34404/when-to-use-tvb_reported_length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34404-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am aware that <code>tvb_captured_length</code> describes the available data for dissection, and <code>tvb_reported_length</code> the data that was available in the real world (snaplen).</p><p><code>tvb_captured_length</code> should be used when:</p><ul><li>A new dissector needs to return a value to indicate acceptance of packet data.</li></ul><p>When should <code>tvb_reported_length</code> be used? Please provide some examples that clearly demonstrate the difference between <code>tvb_captured_length()</code> and <code>tvb_reported_length()</code>. I am especially interested in the "correct" behavior of reassembly.</p><p>If a dissector needs (for example) 8 bytes that describe the following data (type, variable length). What value should be used for comparing? This:</p><pre><code>int dissect_example(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data) {
    if (tvb_captured_length(tvb) &lt; 8) {
        return -1;
    }
    // ...
    return tvb_captured_length(tvb);
}</code></pre><p>or this?</p><pre><code>int dissect_example(tvbuff_t *tvb, packet_info *pinfo, proto_tree *tree, void *data) {
    if (tvb_reported_length(tvb) &lt; 8) {
        return -1;
    }
    // ...
    return tvb_captured_length(tvb);
}</code></pre><p>I guess it is the former, since a dissector is interested in data, but data that is not captured cannot be checked.</p><p>Is the assumption <code>tvb_captured_length() &lt;= tvb_reported_length()</code> also always valid? What is the lower bound of <code>tvb_captured_length()</code> when the two values are not equal?</p></div><div id="question-tags" class="tags-container tags">tvb_length</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Jul '14, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lekensteyn has 32 accepted answers">30%</span></p></div></div><div id="comments-container-34404" class="comments-container"></div><div id="comment-tools-34404" class="comment-tools"></div><div class="clear"></div><div id="comment-34404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34415"></span>

<div id="answer-container-34415" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34415-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I think you'll always have to work with tvb_captured_length when dissecting packets</p></blockquote><p>No "normal" dissection should use <code>tvb_reported_length()</code> as it should try to dissect the reported data and run into an exception when the available (captured) data is exhausted generating the automatic output <code>[malformed packet - data may have been cut short]</code> (or something like that).</p><p>The only time to use <code>tvb_captured_length()</code> is when you don't want the exception like in heuristic dissectors when determining whether this is the right dissector or not or possibly in reassembly, decompression and the like. So reported length should be the normal case and captured length only used in special cases.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '14, 07:14</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Jul '14, 14:16</p><img src="https://secure.gravatar.com/avatar/285b1f0f4caadc088a38c40aea22feba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lekensteyn&#39;s gravatar image" /><p>Lekensteyn<br />
<span class="score" title="2213 reputation points"><span>2.2k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="24 badges"><span class="bronze">●</span><span class="badgecount">24</span></span></p></div></div><div id="comments-container-34415" class="comments-container"><span id="34416"></span><div id="comment-34416" class="comment"><div id="post-34416-score" class="comment-score"></div><div class="comment-text"><p>Thanks Anders, that is helpful. Would you mind adding an answer and touch some points from my question? The more distinct cases with examples, the better.</p></div><div id="comment-34416-info" class="comment-info"><span class="comment-age">(04 Jul '14, 08:07)</span> Lekensteyn</div></div><span id="34417"></span><div id="comment-34417" class="comment"><div id="post-34417-score" class="comment-score"></div><div class="comment-text"><p>Comment converted to answer</p></div><div id="comment-34417-info" class="comment-info"><span class="comment-age">(04 Jul '14, 08:25)</span> grahamb ♦</div></div><span id="34470"></span><div id="comment-34470" class="comment"><div id="post-34470-score" class="comment-score"></div><div class="comment-text"><p>Anders, to clarify, <code>tvb_captured_length()</code> should only be used as return value or when used for heuristics checks, and <code>tvb_reported_length()</code> for all other cases? Or are there other cases where <code>tvb_captured_length()</code> should be used?</p></div><div id="comment-34470-info" class="comment-info"><span class="comment-age">(08 Jul '14, 09:16)</span> Lekensteyn</div></div><span id="34477"></span><div id="comment-34477" class="comment"><div id="post-34477-score" class="comment-score"></div><div class="comment-text"><p>It's impossible to give a straight answer but basically-yes. As Guy said, tvb_captured _length should only be used in rare cases.</p></div><div id="comment-34477-info" class="comment-info"><span class="comment-age">(08 Jul '14, 12:45)</span> Anders ♦</div></div><span id="39893"></span><div id="comment-39893" class="comment"><div id="post-39893-score" class="comment-score"></div><div class="comment-text"><p><code>doc/packet-PROTOABBREV.c</code> suggests to use <code>tvb_captured_length()</code> in a new-style dissector routine. You want to do this when you have successfully dissected (most) of the message, when the length is not known in advance (for example, when used in combination with <code>tcp_dissect_pdus</code> or a protocol such as SMTP which has no explicit message length).</p></div><div id="comment-39893-info" class="comment-info"><span class="comment-age">(16 Feb '15, 10:13)</span> Lekensteyn</div></div></div><div id="comment-tools-34415" class="comment-tools"></div><div class="clear"></div><div id="comment-34415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34412"></span>

<div id="answer-container-34412" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34412-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you'll always have to work with tvb_captured_length when dissecting packets, because - as you already said - it's what you have. tvb_reported_length is necessary for statistics and for some expert analysis topics, e.g. when calculating next sequence number for TCP.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Jul '14, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-34412" class="comments-container"><span id="34413"></span><div id="comment-34413" class="comment"><div id="post-34413-score" class="comment-score"></div><div class="comment-text"><p>Consider <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-ms-mms.c#l376"><code>dissect_msmms_command()</code> in packet-ms-mms.c</a>. Is that proper use of <code>tvb_reported_length_remaining()</code>?</p></div><div id="comment-34413-info" class="comment-info"><span class="comment-age">(04 Jul '14, 06:22)</span> Lekensteyn</div></div><span id="34421"></span><div id="comment-34421" class="comment"><div id="post-34421-score" class="comment-score">1</div><div class="comment-text"><p>No. As Anders said, dissectors should attempt to dissect based on the reported length, because they should throw an exception if they run out of data, so the user knows that the packet really is bigger than what Wireshark is showing, the capture was just cut off with a snapshot length/slice length.</p><p>For example, a "dissect until the end of the packet" loop should use <code>tvb_reported_length()</code>, not <code>tvb_captured_length()</code>.</p><p><code>tvb_captured_length()</code> should only be used in some rare circumstances. For example, if the packet has a checksum that the dissector checks, it should use <code>tvb_captured_length()</code> - or <code>tvb_bytes_exist()</code> - to make sure all the data over which the checksum should be calculated was captured, and not attempt to check the checksum if not all the data was captured.</p></div><div id="comment-34421-info" class="comment-info"><span class="comment-age">(04 Jul '14, 12:39)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-34412" class="comment-tools"></div><div class="clear"></div><div id="comment-34412-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

