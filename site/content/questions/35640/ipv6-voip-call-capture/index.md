+++
type = "question"
title = "IPv6 VoIP call capture"
description = '''Hello! I&#x27;ve set up a VoIP call over IPv6 and I&#x27;m trying to capture it with wireshark (very basic live capture, no filters applied, just clicked on the right interface) but I can&#x27;t see any SIP packets. The call is between 2 machines and the sniffer works on a 3rd separate one - they are all in the sa...'''
date = "2014-08-20T13:04:00Z"
lastmod = "2014-08-20T13:04:00Z"
weight = 35640
keywords = [ "sip", "voip", "ipv6" ]
aliases = [ "/questions/35640" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IPv6 VoIP call capture](/questions/35640/ipv6-voip-call-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35640-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello!</p><p>I've set up a VoIP call over IPv6 and I'm trying to capture it with wireshark (very basic live capture, no filters applied, just clicked on the right interface) but I can't see any SIP packets.</p><p>The call is between 2 machines and the sniffer works on a 3rd separate one - they are all in the same local network.</p><p>If I switch to IPv4 I can capture the call. Is this an IPv6 security feature or a wireshark bug ?</p><p>Thanks !</p><p>J.</p></div><div id="question-tags" class="tags-container tags">sip voip ipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '14, 13:04</strong></p><img src="https://secure.gravatar.com/avatar/3c3a6e6e1a4055c20679be53ab916054?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="qub&#39;s gravatar image" /><p>qub<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="qub has no accepted answers">0%</span></p></div></div><div id="comments-container-35640" class="comments-container"><span id="35647"></span><div id="comment-35647" class="comment"><div id="post-35647-score" class="comment-score">1</div><div class="comment-text"><p>Wireshark should capture the packets whether it's IPv4 or IPv6, especially with no filters applied.</p><p>Assuming it's not confidential, could you upload the trace file when IPv6 is attempted for the SIP call and post the link (<a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a> )?</p><p>Also, how is the third (capturing) machine receiving the data stream? Is the switch in the middle doing port-mirroring, and what is the logic controlling that (eg: one obvious cause would be if you were forwarding to the analyser based on IPv4 subnet range, preventing the IPv6 traffic from reaching the analyzer).</p></div><div id="comment-35647-info" class="comment-info"><span class="comment-age">(20 Aug '14, 19:17)</span> Quadratic</div></div></div><div id="comment-tools-35640" class="comment-tools"></div><div class="clear"></div><div id="comment-35640-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

