+++
type = "question"
title = "Different outputs in VoIP Calls Analysis for different versions of Wireshark, why?"
description = '''In version 1.2.9 when I use the VoIP Calls analysis I see only protocol H.323.  In version 1.10.0, the same capture file, when I use VoIP Calls analysis I see not only protocol H.323 in the output, but also another protocol AC_ISDN.  Does anybody know what is different, obviously something changed b...'''
date = "2014-02-28T01:25:00Z"
lastmod = "2014-02-28T08:58:00Z"
weight = 30262
keywords = [ "analysis", "calls", "voip" ]
aliases = [ "/questions/30262" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Different outputs in VoIP Calls Analysis for different versions of Wireshark, why?](/questions/30262/different-outputs-in-voip-calls-analysis-for-different-versions-of-wireshark-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30262-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In version 1.2.9 when I use the VoIP Calls analysis I see only protocol H.323. In version 1.10.0, the same capture file, when I use VoIP Calls analysis I see not only protocol H.323 in the output, but also another protocol AC_ISDN. Does anybody know what is different, obviously something changed between the versions. And why the output of the VoIP Calls analysis is so much different? Where can I find more information? I was not able to upload an image to show you this...</p></div><div id="question-tags" class="tags-container tags">analysis calls voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '14, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/8547af0318c4770dcd05bf80f19b45a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lz1dsb&#39;s gravatar image" /><p>lz1dsb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lz1dsb has no accepted answers">0%</span></p></div></div><div id="comments-container-30262" class="comments-container"><span id="30266"></span><div id="comment-30266" class="comment"><div id="post-30266-score" class="comment-score"></div><div class="comment-text"><p>can you post a sample capture file somewhere (google drive, dropbox, cloudshark.org)?</p></div><div id="comment-30266-info" class="comment-info"><span class="comment-age">(28 Feb '14, 06:59)</span> Kurt Knochner ♦</div></div><span id="30886"></span><div id="comment-30886" class="comment"><div id="post-30886-score" class="comment-score"></div><div class="comment-text"><p>I have a sample capture where this issue is seen... but how can I upload the file?</p></div><div id="comment-30886-info" class="comment-info"><span class="comment-age">(17 Mar '14, 07:29)</span> lz1dsb</div></div><span id="30887"></span><div id="comment-30887" class="comment"><div id="post-30887-score" class="comment-score"></div><div class="comment-text"><p>You can upload it to cloudshark.org, pcapr.net, a public dropbox, or pretty much anywhere that the rest of us can get to it. You can even upload it to <a href="http://wiki.wireshark.org/SampleCaptures">http://wiki.wireshark.org/SampleCaptures</a></p></div><div id="comment-30887-info" class="comment-info"><span class="comment-age">(17 Mar '14, 08:06)</span> Hadriel</div></div></div><div id="comment-tools-30262" class="comment-tools"></div><div class="clear"></div><div id="comment-30262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30278"></span>

<div id="answer-container-30278" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30278-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A lot has changed since 1.2.9, including a bunch of new protocols and changes to dissectors of existing protocols. "AC_ISDN" is a part of the "ACtrace" protocol wireshark supports dissecting/analyzing, and "ACtrace" are basically trace packets from AudioCodes gateways.</p><p>I believe those packets can either appear as the whole payload of a UDP packet, or inside a LAPD message/packet; the latter case is probably what's happening for you. When you look in the protocol details of the packets in wireshark, do you see the "ACtrace" message embedded in there?</p><p>Unfortunately the dissector has a fairly rudimentary heuristic for whether the LAPD's payload is an ACtrace packet or not, so it may be wrong. On the other hand, AudioCodes gateways do H.323 so maybe those really are ACtrace messages in your wireshark capture?</p><p>As Kurt said, a sample capture would really help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '14, 08:58</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30278" class="comments-container"><span id="30880"></span><div id="comment-30880" class="comment"><div id="post-30880-score" class="comment-score"></div><div class="comment-text"><p>Hardiel, Thank you for this info. I haven't got any notification that anyone has answered to my question. Anyway. I'm not able to find any information what so ever about ACtrace? Is this an internal processing in Wireshark? I've uploaded an image showing how the VoIP Calls analysis looks like. Indeed it's the H.323 protocol in question. <img src="https://osqa-ask.wireshark.org/upfiles/Version-1.10.0_VoIPCalls.png" alt="alt text" /></p></div><div id="comment-30880-info" class="comment-info"><span class="comment-age">(17 Mar '14, 05:26)</span> lz1dsb</div></div><span id="30888"></span><div id="comment-30888" class="comment"><div id="post-30888-score" class="comment-score"></div><div class="comment-text"><p>No, it's not a Wireshark internal thing - ACTrace is an AudioCodes thing. The "AC" stands for AudioCodes. The chances are that your capture is capturing an H.323 call from or to an AudioCodes H.323 gateway, and the AudioCodes gateway is sending those ACTrace/AC_ISDN messages.</p></div><div id="comment-30888-info" class="comment-info"><span class="comment-age">(17 Mar '14, 08:08)</span> Hadriel</div></div></div><div id="comment-tools-30278" class="comment-tools"></div><div class="clear"></div><div id="comment-30278-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

