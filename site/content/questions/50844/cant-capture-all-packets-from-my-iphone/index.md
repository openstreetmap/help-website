+++
type = "question"
title = "can&#x27;t capture all packets from my iPhone"
description = '''I have been capturing packets in my subnet and was particularly interested to monitor traffic from my iPhone. However I didn&#x27;t capture any packets excerpt for those with MDNS and IGMPv2 protocols. I was browsing, using apps on my iPhone and didn&#x27;t monitor any activity. But when I monitor my laptop I...'''
date = "2016-03-12T11:14:00Z"
lastmod = "2016-03-12T11:30:00Z"
weight = 50844
keywords = [ "sniffing", "packets", "iphone", "wireshark" ]
aliases = [ "/questions/50844" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [can't capture all packets from my iPhone](/questions/50844/cant-capture-all-packets-from-my-iphone)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50844-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been capturing packets in my subnet and was particularly interested to monitor traffic from my iPhone. However I didn't capture any packets excerpt for those with MDNS and IGMPv2 protocols. I was browsing, using apps on my iPhone and didn't monitor any activity. But when I monitor my laptop I get all types of packets including TCP and UDP. Why do I see only two types of packets from my iPhone?</p></div><div id="question-tags" class="tags-container tags">sniffing packets iphone wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Mar '16, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/a2622c3619c19aa56a9290471185430b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leek&#39;s gravatar image" /><p>Leek<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leek has no accepted answers">0%</span></p></div></div><div id="comments-container-50844" class="comments-container"></div><div id="comment-tools-50844" class="comment-tools"></div><div class="clear"></div><div id="comment-50844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50845"></span>

<div id="answer-container-50845" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50845-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Not enough information in your question, so I have to I guess that you are using <em>promiscuous</em> mode on your laptop's wireless network adaptor, which means you can see only broadcast packets from your iPhone (and unicast packets towards your laptop if any would be sent). To see unicast packets from your iPhone, you need to use <em>monitoring</em> mode on your laptop. This is currently only possible with Linux or OS X; on Windows, you need the AirPcap hardware and its corresponding drivers to do that.</p><p>See details regarding difference between promiscuous and monitoring mode and possibilities and limitations on various OSes <a href="https://wiki.wireshark.org/CaptureSetup/WLAN">here</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Mar '16, 11:30</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-50845" class="comments-container"><span id="50846"></span><div id="comment-50846" class="comment"><div id="post-50846-score" class="comment-score"></div><div class="comment-text"><p>Yes, I did use promiscuous mode and I have Windows. Thank you for clarification!</p></div><div id="comment-50846-info" class="comment-info"><span class="comment-age">(12 Mar '16, 11:38)</span> Leek</div></div><span id="50847"></span><div id="comment-50847" class="comment"><div id="post-50847-score" class="comment-score"></div><div class="comment-text"><p>If you don't care about the local traffic of the iPhone and it would be enough for you to capture its communication to the internet, a workaround could be to run the capture at the WiFi router itself or, if there is more than a single box between your CATV/telephone line and the WiFi antenna, using one of the capturing methods applicable at wired Ethernet between the access point / router / CATV/ADSL modem.</p></div><div id="comment-50847-info" class="comment-info"><span class="comment-age">(12 Mar '16, 11:54)</span> sindy</div></div></div><div id="comment-tools-50845" class="comment-tools"></div><div class="clear"></div><div id="comment-50845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

