+++
type = "question"
title = "PMIPv6 with UDP encapsulation not decoded properly by Wireshark"
description = '''Hi Experts, I&#x27;m just wondering if there&#x27;s a way to manually configure Wireshark for it to be able to properly decode PMIPv6 with UDP encapsulation over IPv4 transport. I&#x27;m using the latest Wireshark version 2.0.3 and noticed that the data payload (original data before PMIPv6 tunnel encapsulation) is...'''
date = "2016-05-12T08:32:00Z"
lastmod = "2016-05-12T08:32:00Z"
weight = 52473
keywords = [ "pmipv6" ]
aliases = [ "/questions/52473" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PMIPv6 with UDP encapsulation not decoded properly by Wireshark](/questions/52473/pmipv6-with-udp-encapsulation-not-decoded-properly-by-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-52473-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Experts, I'm just wondering if there's a way to manually configure Wireshark for it to be able to properly decode PMIPv6 with UDP encapsulation over IPv4 transport. I'm using the latest Wireshark version 2.0.3 and noticed that the data payload (original data before PMIPv6 tunnel encapsulation) is decoded by Wireshark as "Binding Refresh Request" (mobility header type) and the data Payload protocol is reported by Wireshark as "SATNET Monitoring". Due to this, I wasn't able to see the original data packet. Is this a bug or an unsupported feature or is there a way to configure Wireshark to tell it how to properly decode PMIPv6 packets? Thanks!</p></div><div id="question-tags" class="tags-container tags">pmipv6</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 May '16, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/32de10b52e39c8a85f95140b64a8d840?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ger&#39;s gravatar image" /><p>Ger<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ger has no accepted answers">0%</span></p></div></div><div id="comments-container-52473" class="comments-container"><span id="54165"></span><div id="comment-54165" class="comment"><div id="post-54165-score" class="comment-score"></div><div class="comment-text"><p>Do you have a capture file you could provide so someone could take a look at this? Or if you suspect it's a bug, open a Wireshark bug report and attach the capture file to it.</p></div><div id="comment-54165-info" class="comment-info"><span class="comment-age">(19 Jul '16, 09:42)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-52473" class="comment-tools"></div><div class="clear"></div><div id="comment-52473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

