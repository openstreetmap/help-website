+++
type = "question"
title = "Decoding ANSI standard protocols"
description = '''I am using Wireshark version 1.6.5 to decode captured RANAP and SCCP packets over M3UA with ANSI configuration point codes. I could observe that only 2 bytes are being considered for point code decoding. Moreover the order of subsystem number and point code seems to be the other way when compared wi...'''
date = "2012-03-03T20:30:00Z"
lastmod = "2012-03-06T07:47:00Z"
weight = 9336
keywords = [ "ansi_sccp" ]
aliases = [ "/questions/9336" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Decoding ANSI standard protocols](/questions/9336/decoding-ansi-standard-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9336-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9336-score" class="post-score" title="current number of votes">0</div><span id="post-9336-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using Wireshark version 1.6.5 to decode captured RANAP and SCCP packets over M3UA with ANSI configuration point codes. I could observe that only 2 bytes are being considered for point code decoding. Moreover the order of subsystem number and point code seems to be the other way when compared with the ANSI SCCP standard (T1.112.3). This problem is observed only for connectionless SCCP messages like UDT and XUDT. Whole purpose of my testing is XUDT messaging (segmentation and reassembly). In preferences, under MTP3, I have changed the variant to ANSI and SLS to be 5 bits. I am missing some configuration or is this not supported with the current release of Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ansi_sccp" rel="tag" title="see questions tagged &#39;ansi_sccp&#39;">ansi_sccp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '12, 20:30</strong></p><img src="https://secure.gravatar.com/avatar/b17b7761931303886b0932e9001e0477?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nsvijay&#39;s gravatar image" /><p><span>nsvijay</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nsvijay has no accepted answers">0%</span></p></div></div><div id="comments-container-9336" class="comments-container"><span id="9363"></span><div id="comment-9363" class="comment"><div id="post-9363-score" class="comment-score"></div><div class="comment-text"><p>Hmm, it should work fine in 1.6.5. I just tried it out and it looked okay to me.</p><p>What does the Protocol column say? If it's decoding up to SCCP it should say "SCCP (ANSI)" if it is successfully using the ANSI preference. If it doesn't say ANSI then double check the preference setting.</p></div><div id="comment-9363-info" class="comment-info"><span class="comment-age">(05 Mar '12, 09:49)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="9365"></span><div id="comment-9365" class="comment"><div id="post-9365-score" class="comment-score"></div><div class="comment-text"><p>When it decoded SCCP layer, it still shows as SCCP (Intl ITU). In preferences, I just set the MTP3 variant as ANSI. Am I missing any other settings? Can you provide a snapshot of your preferences and output pcap file?</p></div><div id="comment-9365-info" class="comment-info"><span class="comment-age">(05 Mar '12, 10:41)</span> <span class="comment-user userinfo">nsvijay</span></div></div><span id="9394"></span><div id="comment-9394" class="comment"><div id="post-9394-score" class="comment-score"></div><div class="comment-text"><p>Just setting the MTP3 standard to ANSI works for me. Are you decoding the RFC version of M3UA? Not that I think that should matter. Is this SCTP/M3UA/SCTP/IP/Ethernet?</p></div><div id="comment-9394-info" class="comment-info"><span class="comment-age">(06 Mar '12, 06:48)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="9396"></span><div id="comment-9396" class="comment"><div id="post-9396-score" class="comment-score"></div><div class="comment-text"><p>Yes, I am trying SCCP/M3UA/SCTP/IP/Ethernet. And I have configured RFC3332 version of M3UA.</p></div><div id="comment-9396-info" class="comment-info"><span class="comment-age">(06 Mar '12, 07:47)</span> <span class="comment-user userinfo">nsvijay</span></div></div></div><div id="comment-tools-9336" class="comment-tools"></div><div class="clear"></div><div id="comment-9336-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

