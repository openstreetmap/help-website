+++
type = "question"
title = "Some SIP request/response messages are missing for calls in a live traffic trace"
description = '''Hi, I have been trying to capture trace for SIP and RTP to my vendor for live traffic. The problem is, some SIP request/response messages are missing for particular calls. For example, for a particular successful call, I am getting only INVITE and ACK messages by filtering using sip.To contains or s...'''
date = "2015-04-10T23:15:00Z"
lastmod = "2015-04-10T23:15:00Z"
weight = 41373
keywords = [ "sip", "rtp", "missing_packets" ]
aliases = [ "/questions/41373" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Some SIP request/response messages are missing for calls in a live traffic trace](/questions/41373/some-sip-requestresponse-messages-are-missing-for-calls-in-a-live-traffic-trace)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41373-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have been trying to capture trace for SIP and RTP to my vendor for live traffic. The problem is, some SIP request/response messages are missing for particular calls. For example, for a particular successful call, I am getting only INVITE and ACK messages by filtering using sip.To contains or sip.From contains, sip.Call-ID, sip.Via filters. Result for all those filters are same. I have tried Call flow from Telephoney&gt; VoIP Calls, same result.</p><p>Any help regarding this situation would be much appreciated.</p></div><div id="question-tags" class="tags-container tags">sip rtp missing_packets</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Apr '15, 23:15</strong></p><img src="https://secure.gravatar.com/avatar/07986727b2a1d71b46fd0e036f626bad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sentinel&#39;s gravatar image" /><p>Sentinel<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sentinel has no accepted answers">0%</span></p></div></div><div id="comments-container-41373" class="comments-container"><span id="41380"></span><div id="comment-41380" class="comment"><div id="post-41380-score" class="comment-score"></div><div class="comment-text"><p>can you provide a sample capture file? If so, please upload it to google drive, dropbox or cloudshark.org and post the link here.</p></div><div id="comment-41380-info" class="comment-info"><span class="comment-age">(11 Apr '15, 05:43)</span> Kurt Knochner ♦</div></div><span id="41400"></span><div id="comment-41400" class="comment"><div id="post-41400-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt, The capture I am talking about is really large as it was live traffic trace. So I am facing difficulties uploading it.</p><p>Can you give me any clue regarding this missing message scenario,why this might be occuring ? As I am totally blank on this right now !</p></div><div id="comment-41400-info" class="comment-info"><span class="comment-age">(12 Apr '15, 23:57)</span> Sentinel</div></div><span id="41401"></span><div id="comment-41401" class="comment"><div id="post-41401-score" class="comment-score"></div><div class="comment-text"><p>What is the packet rate? Perhaps you have packet drops on your capturing interface. What OS and version, which wireshark version?</p><p>If TCP are used perhaps reassembly fails, try frame contains.</p></div><div id="comment-41401-info" class="comment-info"><span class="comment-age">(13 Apr '15, 01:42)</span> Anders ♦</div></div></div><div id="comment-tools-41373" class="comment-tools"></div><div class="clear"></div><div id="comment-41373-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

