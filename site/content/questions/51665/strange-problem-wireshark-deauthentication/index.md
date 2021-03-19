+++
type = "question"
title = "Strange problem (wireshark, deauthentication)"
description = '''Hello,  This question is not actually for wireshark but a more general one in case someone has the same problem. Consider the following scenario. 2 wireless cards, 1 sniffing with wireshark and 1 send deauth packets to a device (consider all set on the same channel). The sniffing device does not sni...'''
date = "2016-04-14T03:06:00Z"
lastmod = "2016-04-14T03:06:00Z"
weight = 51665
keywords = [ "deauthentication" ]
aliases = [ "/questions/51665" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Strange problem (wireshark, deauthentication)](/questions/51665/strange-problem-wireshark-deauthentication)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51665-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>This question is not actually for wireshark but a more general one in case someone has the same problem. Consider the following scenario.</p><p>2 wireless cards, 1 sniffing with wireshark and 1 send deauth packets to a device (consider all set on the same channel). The sniffing device does not sniff any deuthentication packets, neither does the device, but if i start wireshark on the deauthing device I normally see the packets as being sent. I tested it enough to be sure that the deauth packets are not being send. Why is the deauthenticating card seeing the packets normally and what exactly might be the problem?</p><p>Any answers would be really appreciated!</p></div><div id="question-tags" class="tags-container tags">deauthentication</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '16, 03:06</strong></p><img src="https://secure.gravatar.com/avatar/1fc4f29b27e759eb494bc5ccfce75e47?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="biteme&#39;s gravatar image" /><p>biteme<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="biteme has no accepted answers">0%</span></p></div></div><div id="comments-container-51665" class="comments-container"><span id="51670"></span><div id="comment-51670" class="comment"><div id="post-51670-score" class="comment-score"></div><div class="comment-text"><p>I would guess the difference is that Wireshark shows you what was sent down the stack, but if the driver won't put it on the air, it won't go. It's an assumption, usually a good one, that if you see it in Wireshark it makes onto the network. But not always, with a notable example being a firewall. Did you check the aircrack-ng forum? That suite of software has some standard injection tests that you can try to see if you wireless card will inject the frame into the air.</p></div><div id="comment-51670-info" class="comment-info"><span class="comment-age">(14 Apr '16, 08:57)</span> Bob Jones</div></div></div><div id="comment-tools-51665" class="comment-tools"></div><div class="clear"></div><div id="comment-51665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

