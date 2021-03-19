+++
type = "question"
title = "Missing SIP Packets"
description = '''I have a Polycom phone that is on the public internet, and is registered SIP/UDP to my Metaswitch. Wiresharking a mirrored port was showing normal SIP and RTP traffic. THEN- someone got into the phone via web, deleted the SIP Info so the phone was no longer registered, and started blasting the IP wi...'''
date = "2015-03-24T08:28:00Z"
lastmod = "2015-03-24T13:16:00Z"
weight = 40803
keywords = [ "sipcapture" ]
aliases = [ "/questions/40803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing SIP Packets](/questions/40803/missing-sip-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a Polycom phone that is on the public internet, and is registered SIP/UDP to my Metaswitch. Wiresharking a mirrored port was showing normal SIP and RTP traffic.</p><p>THEN- someone got into the phone via web, deleted the SIP Info so the phone was no longer registered, and started blasting the IP with TLS traffic, TLSv1 Client Hello packets, change sipher, and app data packets.</p><p>I updated the SIP reg info, got the phone registered again and updated the web PW, the phone does work, however now all I see on wireshark is the TLS traffic, I dont see any SIP or RTP traffic.</p><p>Why can't I see the SIP/RTP traffic??</p></div><div id="question-tags" class="tags-container tags">sipcapture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '15, 08:28</strong></p><img src="https://secure.gravatar.com/avatar/8fe607750a0ac093c31e4fff77aac15d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GAS&#39;s gravatar image" /><p>GAS<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GAS has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Mar '15, 19:03</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-40803" class="comments-container"></div><div id="comment-tools-40803" class="comment-tools"></div><div class="clear"></div><div id="comment-40803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40816"></span>

<div id="answer-container-40816" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40816-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Probably the "someone" has also enabled SSL/TLS on the phone. Maybe you'd better factory default it and reinstall firmware in case the "someone" installed a custom firmware version.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '15, 13:16</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40816" class="comments-container"><span id="40819"></span><div id="comment-40819" class="comment"><div id="post-40819-score" class="comment-score"></div><div class="comment-text"><p>I looked at the phone, TLS is not enabled, it still has the Polycom firmware on it. I can run a call trace(in my switch) on the call to the phone and see SIP traffic to and from the phone, but its not showing up on wireshark.</p><p>Thanks</p></div><div id="comment-40819-info" class="comment-info"><span class="comment-age">(24 Mar '15, 13:39)</span> GAS</div></div><span id="40830"></span><div id="comment-40830" class="comment"><div id="post-40830-score" class="comment-score"></div><div class="comment-text"><p>Still looks like the attacker tried to do more than just 'delete the SIP info', especially since they followed up with specific TLS traffic. Doesn't sound like some random script kiddie to me.</p><p>Also you didn't specify which 'IP' was blasted with TLS traffic. Be specific on your interfaces please.</p></div><div id="comment-40830-info" class="comment-info"><span class="comment-age">(25 Mar '15, 04:04)</span> Jaap ♦</div></div><span id="40833"></span><div id="comment-40833" class="comment"><div id="post-40833-score" class="comment-score"></div><div class="comment-text"><p>The public IP of the phone is getting all the TLS traffic, from a Europena IP address. I guess whats odd to me is that the phone is working (they made a 1.5 hour call yesterday), I see SIP traffic in the call trace in my switch, but no SIP or RTP traffic on wireshark.</p><p>I restarted wireshark, made sure it in promisc mode, etc.</p></div><div id="comment-40833-info" class="comment-info"><span class="comment-age">(25 Mar '15, 06:44)</span> GAS</div></div><span id="40847"></span><div id="comment-40847" class="comment"><div id="post-40847-score" class="comment-score"></div><div class="comment-text"><p>What do you see on the Wireshark capture? Any other SIP clients, just not yours? Nothing at all? A different VLAN? Is the mirror still intact, correctly configured? How long ago did you have a working SIP/RTP traffic capture of your phone?</p></div><div id="comment-40847-info" class="comment-info"><span class="comment-age">(25 Mar '15, 09:39)</span> Jaap ♦</div></div></div><div id="comment-tools-40816" class="comment-tools"></div><div class="clear"></div><div id="comment-40816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

