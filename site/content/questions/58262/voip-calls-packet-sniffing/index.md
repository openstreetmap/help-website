+++
type = "question"
title = "Voip calls packet sniffing"
description = '''hello all, i am running a voip call beetween 2 user in a private network, each user are connected with wifi and also the server. i was trying to sniff from other computer (other user in the same network) but i can&#x27;t get the voip packet (sip and rtp) from these 2 user that was doing a call. can anyon...'''
date = "2016-12-20T16:33:00Z"
lastmod = "2016-12-20T16:33:00Z"
weight = 58262
keywords = [ "voipcalls", "sniffing", "asterisk", "voip" ]
aliases = [ "/questions/58262" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Voip calls packet sniffing](/questions/58262/voip-calls-packet-sniffing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58262-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hello all,</p><p>i am running a voip call beetween 2 user in a private network, each user are connected with wifi and also the server. i was trying to sniff from other computer (other user in the same network) but i can't get the voip packet (sip and rtp) from these 2 user that was doing a call. can anyone tell me is wireshark actually cannot capture packet like the case above ? because i read from some articles that wireshark can sniff if it connected with the same wireless connection. or is there any additional setting that i've to do to enable wireshark to capture the voip packet sent from other user to another user ?</p><p>NB : I am using asterisk as a server and csipsimple asn a client</p><p>thanks</p></div><div id="question-tags" class="tags-container tags">voipcalls sniffing asterisk voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Dec '16, 16:33</strong></p><img src="https://secure.gravatar.com/avatar/5908f368e76b623cf9ba633022d7cf69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alfit19&#39;s gravatar image" /><p>alfit19<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alfit19 has no accepted answers">0%</span></p></div></div><div id="comments-container-58262" class="comments-container"><span id="58538"></span><div id="comment-58538" class="comment"><div id="post-58538-score" class="comment-score"></div><div class="comment-text"><ol><li><p>Are you able to see other traffic between the users? For example, if you ping one user from the other, do you see the ICMP request and replies?</p></li><li><p>Can you post your WiFi capture (on either Cloudshark or Google Drive)? I am wondering if the VoIP connection is encrypted so the SIP and RTP traffic is not seen.</p></li></ol></div><div id="comment-58538-info" class="comment-info"><span class="comment-age">(05 Jan '17, 08:22)</span> Amato_C</div></div></div><div id="comment-tools-58262" class="comment-tools"></div><div class="clear"></div><div id="comment-58262-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

