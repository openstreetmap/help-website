+++
type = "question"
title = "rtp and sip trafic"
description = '''I sniff the traffic between client machines sip but I click on player decode and then I get no result I do not know where is the problem. knowing that I use sip client installed on a virtual machine and another on the physical machine and the attacker uses a machine back track 4 r1. any one cab help...'''
date = "2014-02-13T13:32:00Z"
lastmod = "2014-02-13T16:08:00Z"
weight = 29842
keywords = [ "rasadab" ]
aliases = [ "/questions/29842" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [rtp and sip trafic](/questions/29842/rtp-and-sip-trafic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29842-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I sniff the traffic between client machines sip but I click on player decode and then I get no result I do not know where is the problem. knowing that I use sip client installed on a virtual machine and another on the physical machine and the attacker uses a machine back track 4 r1. any one cab help me !</p></div><div id="question-tags" class="tags-container tags">rasadab</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '14, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/c0daef753254fda2189e88256b71ec73?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rasdab&#39;s gravatar image" /><p>rasdab<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rasdab has no accepted answers">0%</span></p></div></div><div id="comments-container-29842" class="comments-container"></div><div id="comment-tools-29842" class="comment-tools"></div><div class="clear"></div><div id="comment-29842-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29851"></span>

<div id="answer-container-29851" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29851-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>It should be reasonable straight forward provided you have captured all the necessary packets. Basically you should confirm that you have at least two packets that show up in Wireshark as SIP/SDP. These will be the Invite Request from the Caller IP and the "OK" Status from the Called IP. They will both have SDP message bodies that contain the Media Description that has Media Port, which is the UDP port used for the RTP traffic. Wireshark will then look for UDP packets matching these, and decode them as RTP.</p><p>This is for unencrypted SIP over UDP. If you are using encrypted SIP over TLS you would need to provide Wireshark with the appropriate private key to do the decrypt first (I haven't actually looked at SIP over TLS but that's the theory)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '14, 16:08</strong></p><img src="https://secure.gravatar.com/avatar/57fbbe2a1e14ccc2a681a28886e5a484?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="martyvis&#39;s gravatar image" /><p>martyvis<br />
<span class="score" title="891 reputation points">891</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="martyvis has 5 accepted answers">7%</span></p></div></div><div id="comments-container-29851" class="comments-container"><span id="29873"></span><div id="comment-29873" class="comment"><div id="post-29873-score" class="comment-score"></div><div class="comment-text"><p>i have 7 sip/sdp but when i clic on "telephony" after "voip calls" "player" and decode i have now result empty "graph"<img src="https://osqa-ask.wireshark.org/upfiles/Capture.JPeG" alt="alt text" /></p></div><div id="comment-29873-info" class="comment-info"><span class="comment-age">(14 Feb '14, 13:54)</span> rasdab</div></div><span id="29917"></span><div id="comment-29917" class="comment"><div id="post-29917-score" class="comment-score"></div><div class="comment-text"><p>You probably need to provide more details of the capture (maybe upload to Cloudshark if it is non-sensitive such as phone numbers of the conversation contants). According to the snapshot of your graph, all of your RTP packets (100%) are out of sequence. Also you seem to be showing the voice graph for a time outside the Duration (15.37 and 7.4 secs). Maybe also just confirm for yourself that the samples at <a href="http://wiki.wireshark.org/SampleCaptures#SIP_and_RTP">http://wiki.wireshark.org/SampleCaptures#SIP_and_RTP</a> work in your setup (playback properly)</p></div><div id="comment-29917-info" class="comment-info"><span class="comment-age">(16 Feb '14, 14:08)</span> martyvis</div></div></div><div id="comment-tools-29851" class="comment-tools"></div><div class="clear"></div><div id="comment-29851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

