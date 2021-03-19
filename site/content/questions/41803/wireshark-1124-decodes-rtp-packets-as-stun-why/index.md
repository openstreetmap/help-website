+++
type = "question"
title = "Wireshark 1.12.4 decodes RTP packets as STUN. Why?"
description = '''Recently I upgraded to Wireshark 1.12.2 and it started decode some RTP packets as STU packets. Why? Upgrade to 1.12.4 showed the same behavior. Now, according to STUN RFC5389, the UDP payload bits 0 and 1 are both 0 and the RTP packets are version 2 so there is no way to misinterpret the two.'''
date = "2015-04-24T14:20:00Z"
lastmod = "2015-04-25T11:36:00Z"
weight = 41803
keywords = [ "stun" ]
aliases = [ "/questions/41803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.12.4 decodes RTP packets as STUN. Why?](/questions/41803/wireshark-1124-decodes-rtp-packets-as-stun-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently I upgraded to Wireshark 1.12.2 and it started decode some RTP packets as STU packets. Why? Upgrade to 1.12.4 showed the same behavior.</p><p>Now, according to STUN RFC5389, the UDP payload bits 0 and 1 are both 0 and the RTP packets are version 2 so there is no way to misinterpret the two.</p></div><div id="question-tags" class="tags-container tags">stun</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '15, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/881a751e071988139643ed8799a92640?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="prorad&#39;s gravatar image" /><p>prorad<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="prorad has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 25 Apr '15, 04:18</p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-41803" class="comments-container"><span id="41805"></span><div id="comment-41805" class="comment"><div id="post-41805-score" class="comment-score"></div><div class="comment-text"><p>Do you have the "Try to decode RTP outside of conversations" preference for RTP set?</p><p>According to RFC 3489, the UDP payload bits 0 and 1 are not necessarily both 0; Wireshark dissects both "classic STUN" (RFC 3489) and "current" STUN (RFC 5389).</p></div><div id="comment-41805-info" class="comment-info"><span class="comment-age">(24 Apr '15, 16:15)</span> Guy Harris ♦♦</div></div><span id="41809"></span><div id="comment-41809" class="comment"><div id="post-41809-score" class="comment-score"></div><div class="comment-text"><p>Yes I do have this set.</p></div><div id="comment-41809-info" class="comment-info"><span class="comment-age">(24 Apr '15, 17:41)</span> prorad</div></div><span id="41810"></span><div id="comment-41810" class="comment"><div id="post-41810-score" class="comment-score"></div><div class="comment-text"><p>So are those packets showing up as "ChannelData TURN Message" packets? Those are described in <a href="https://tools.ietf.org/html/rfc5766#section-11.4">section 11.4 of RFC 5766</a>.</p></div><div id="comment-41810-info" class="comment-info"><span class="comment-age">(24 Apr '15, 17:48)</span> Guy Harris ♦♦</div></div><span id="41811"></span><div id="comment-41811" class="comment"><div id="post-41811-score" class="comment-score"></div><div class="comment-text"><p>According to rfc3489, all supported STUN message types have both bits 0 and 1 equal zero.</p><p>That's why these two bits would be nailed to zero. As such, there should be no collision between the STUN protocol and the RTP version 2.</p><p>That's my understanding.</p></div><div id="comment-41811-info" class="comment-info"><span class="comment-age">(24 Apr '15, 17:50)</span> prorad</div></div><span id="41812"></span><div id="comment-41812" class="comment"><div id="post-41812-score" class="comment-score"></div><div class="comment-text"><p>I was going say "that's why rfc5389 could nail the bits 0 and 1 to zero."</p></div><div id="comment-41812-info" class="comment-info"><span class="comment-age">(24 Apr '15, 17:52)</span> prorad</div></div><span id="41813"></span><div id="comment-41813" class="comment not_top_scorer"><div id="post-41813-score" class="comment-score"></div><div class="comment-text"><p>...and RFC 5766 says that ChannelData messages <em>don't</em> necessarily have both bits 0 and 1 equal zero, so they're <em>not</em> nailed to zero, and there <em>is</em> a risk of collision between TURN and RTP version 2.</p></div><div id="comment-41813-info" class="comment-info"><span class="comment-age">(24 Apr '15, 18:07)</span> Guy Harris ♦♦</div></div><span id="41830"></span><div id="comment-41830" class="comment not_top_scorer"><div id="post-41830-score" class="comment-score"></div><div class="comment-text"><p>Correct, those packets are showing up as "ChannelData TURN Message" packets.</p></div><div id="comment-41830-info" class="comment-info"><span class="comment-age">(25 Apr '15, 09:59)</span> prorad</div></div></div><div id="comment-tools-41803" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-41803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41834"></span>

<div id="answer-container-41834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41834-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark's STUN/TURN dissector is, as indicated, dissecting the RTP packets as TURN packets.</p><p>This would either require a stronger TURN heuristic or a way to disable the TURN heuristic. Please file a bug at <a href="http://bugs.wireshark.org/">the Wireshark Bugzilla</a>, and attach a capture file containing the mis-dissected packets.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Apr '15, 11:36</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-41834" class="comments-container"><span id="41836"></span><div id="comment-41836" class="comment"><div id="post-41836-score" class="comment-score"></div><div class="comment-text"><p>Thank you. Will do.</p></div><div id="comment-41836-info" class="comment-info"><span class="comment-age">(25 Apr '15, 11:43)</span> prorad</div></div><span id="41893"></span><div id="comment-41893" class="comment"><div id="post-41893-score" class="comment-score"></div><div class="comment-text"><p>Created a bugzilla but report "<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11152">Bug 11152</a>"</p></div><div id="comment-41893-info" class="comment-info"><span class="comment-age">(27 Apr '15, 08:33)</span> prorad</div></div></div><div id="comment-tools-41834" class="comment-tools"></div><div class="clear"></div><div id="comment-41834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

