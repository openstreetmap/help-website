+++
type = "question"
title = "tshark -z rtp,streams packet loss"
description = '''When using tshark command option –z rtp,streams should it detect packet loss as indicated in the thsark html description for –z rtp,streams.  -z rtp,streams Collect statistics for all RTP streams and calculate max. delta, max. and mean jitter and packet loss percentages If I force RTP holes using ne...'''
date = "2014-07-03T14:09:00Z"
lastmod = "2014-07-03T14:09:00Z"
weight = 34392
keywords = [ "streams", "rtp", "tshark", "-z" ]
aliases = [ "/questions/34392" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark -z rtp,streams packet loss](/questions/34392/tshark-z-rtpstreams-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34392-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When using tshark command option –z rtp,streams should it detect packet loss as indicated in the thsark html description for –z rtp,streams.</p><p>-z rtp,streams Collect statistics for all RTP streams and calculate max. delta, max. and mean jitter and packet loss percentages If I force RTP holes using network tools the belwo command still returns 0 packet loss but clearly displays time deltas and jitter.</p><p>tshark –i 3 –q –d udp.port==7534 –z rtp,streams</p><p>If I force RTP holes using network tools the below command still returns 0 packet loss, clearly displays time deltas and jitter but if I open test.pcap in Wireshark,decode as RTP and run RTP analysis it shows sequence errors.</p><p>tshark –i 3 –q –d udp.port==7534 –z rtp,streams –w test.pcap</p><p>Is there any tshark commands that will summarize rtp sequence errors similar to Wireshark RTP analysis?</p></div><div id="question-tags" class="tags-container tags">streams rtp tshark -z</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '14, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/0d7f474517de065f0e9017fc5fcf39ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bb411h&#39;s gravatar image" /><p>bb411h<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bb411h has no accepted answers">0%</span></p></div></div><div id="comments-container-34392" class="comments-container"></div><div id="comment-tools-34392" class="comment-tools"></div><div class="clear"></div><div id="comment-34392-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

