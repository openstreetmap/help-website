+++
type = "question"
title = "How to force RTP &quot;Payload type&quot; to AMR ?"
description = '''Hi I have a application for monitoring the network. This application has a button to start Wireshark to display the captured traffic. Sometime the RTP payload type is well recognized (AMR-WB) by Wireshark and I can use use the use &quot;RTP -&amp;gt; Stream Analysis&quot;. Sometime it&#x27;s &quot;Unknown&quot; and I can&#x27;t use ...'''
date = "2017-02-24T04:24:00Z"
lastmod = "2017-02-24T04:24:00Z"
weight = 59659
keywords = [ "rtp" ]
aliases = [ "/questions/59659" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to force RTP "Payload type" to AMR ?](/questions/59659/how-to-force-rtp-payload-type-to-amr)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-59659-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi</p><p>I have a application for monitoring the network. This application has a button to start Wireshark to display the captured traffic.</p><p>Sometime the RTP payload type is well recognized (AMR-WB) by Wireshark and I can use use the use "RTP -&gt; Stream Analysis".</p><p>Sometime it's "Unknown" and I can't use the Stream Analysis (the graph is empty). I changed the Preferences-&gt;Protocol-&gt;AMR-&gt;AMR Dynamic Payload Type, this add a new tree "AMR-WB" in the protocol layers, but the RTP payload type remains "Unknown" and I still can't use the Stream Analysis.</p><p>Also if I save the pcap (the one with RTP type well recognized AMR-WB) and open it again, Wireshark loses the information and display "DynamicRTP", so I can't use the Stream Analysis anymore.</p><p>That means our monitoring application, when launching Wireshark, probably loads a profil to set the RTP payload type to AMR-WB. Is it possible to do that with Wireshark ?</p><p>How can I force the RTP Payload Type to AMR ?</p><p>See attachement. It's exactly the same flow (but monitored at 2 different places).</p><p>Thank you!!</p><p>rtp amr <img src="https://osqa-ask.wireshark.org/upfiles/rtp_amr_aAf54B5.png" alt="rtp amr" /></p><hr /><p>rtp not recognized <img src="https://osqa-ask.wireshark.org/upfiles/rtp_unknown_fe9TXE6.png" alt="rtp not recognized" /></p></div><div id="question-tags" class="tags-container tags">rtp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '17, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/bb815b46a2b20bbb4a8bea157207b394?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nico128&#39;s gravatar image" /><p>Nico128<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nico128 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-59659" class="comments-container"></div><div id="comment-tools-59659" class="comment-tools"></div><div class="clear"></div><div id="comment-59659-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

