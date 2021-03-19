+++
type = "question"
title = "Voip capture on a Grandstream GXP2000"
description = '''I want to capture SIP packets from a Grandstream GXP2000. All the tutorials I see is to capture local packets on a local machine, is it possible to capture the data if I know the local ip of the unit and the port used?'''
date = "2013-04-06T10:26:00Z"
lastmod = "2013-04-06T10:53:00Z"
weight = 20136
keywords = [ "gxp2000", "voip" ]
aliases = [ "/questions/20136" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Voip capture on a Grandstream GXP2000](/questions/20136/voip-capture-on-a-grandstream-gxp2000)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20136-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to capture SIP packets from a Grandstream GXP2000. All the tutorials I see is to capture local packets on a local machine, is it possible to capture the data if I know the local ip of the unit and the port used?</p></div><div id="question-tags" class="tags-container tags">gxp2000 voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Apr '13, 10:26</strong></p><img src="https://secure.gravatar.com/avatar/9c78f4a6f75e84e231798f6c3fd1021a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="irishbiker&#39;s gravatar image" /><p>irishbiker<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="irishbiker has no accepted answers">0%</span></p></div></div><div id="comments-container-20136" class="comments-container"></div><div id="comment-tools-20136" class="comment-tools"></div><div class="clear"></div><div id="comment-20136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20138"></span>

<div id="answer-container-20138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-20138-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If the machine on which you're running Wireshark is on the same Ethernet segment as the phone, and if that segment either uses a hub rather than a switch (note that <a href="http://wiki.wireshark.org/HubReference">some devices claim to be hubs but are actually switches</a>) or <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet#Switched_Ethernet">you can arrange to capture traffic going through the switch from the phone</a>, you should be able to capture traffic going to and from the phone. The Ethernet interface on the machine running Wireshark will have to run in promiscuous mode; use a capture filter such as "host XXX.XXX.XXX.XXX" where "XXX.XXX.XXX.XXX" is the IP address of the phone, or, if you don't want to capture traffic other than SIP traffic, and you know the port being used for SIP, use "host XXX.XXX.XXX.XXX and port PPP", where "PPP" is the port being used.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Apr '13, 10:53</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-20138" class="comments-container"></div><div id="comment-tools-20138" class="comment-tools"></div><div class="clear"></div><div id="comment-20138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

