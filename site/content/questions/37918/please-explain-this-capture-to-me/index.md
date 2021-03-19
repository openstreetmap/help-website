+++
type = "question"
title = "Please explain this capture to me"
description = '''Capturing Interface When I choose the wifi interface in capturing, I get a list of TCPs and I have no idea what they mean. Most importantly, it says ethernet frame check sequence incorrect and I get no UDPs at all.  This is a photo of what the screen shows http://postimg.org/image/6xzgbfq7r/ Thank y...'''
date = "2014-11-17T14:31:00Z"
lastmod = "2014-11-17T16:46:00Z"
weight = 37918
keywords = [ "interface", "capture" ]
aliases = [ "/questions/37918" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Please explain this capture to me](/questions/37918/please-explain-this-capture-to-me)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37918-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Capturing Interface</p><p>When I choose the wifi interface in capturing, I get a list of TCPs and I have no idea what they mean. Most importantly, it says ethernet frame check sequence incorrect and I get no UDPs at all.</p><p>This is a photo of what the screen shows <a href="http://postimg.org/image/6xzgbfq7r/">http://postimg.org/image/6xzgbfq7r/</a></p><p>Thank you very much FOR ANYONE'S HELP.</p></div><div id="question-tags" class="tags-container tags">interface capture</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Nov '14, 14:31</strong></p><img src="https://secure.gravatar.com/avatar/1059cafb10cc39c170c46dbffbae2711?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Davis&#39;s gravatar image" /><p>Davis<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Davis has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Nov '14, 16:37</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-37918" class="comments-container"></div><div id="comment-tools-37918" class="comment-tools"></div><div class="clear"></div><div id="comment-37918-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37924"></span>

<div id="answer-container-37924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-37924-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>"TLSv1.2" means that a protocol called "Transport Layer Security" is being used on the connection; it's the successor to SSL, for "Secure Sockets Layer", and provides encryption services for protocols such as HTTP, SMTP, etc. that run over TCP. Its main use is for HTTP; that's what "https" traffic is. "https" traffic usually goes to or from TCP port 443, so that's probably what this is.</p><p>Unfortunately, because it's encrypted, it would need to be decrypted to see what's actually happening. <a href="http://wiki.wireshark.org/SSL">The Wireshark Wiki page on SSL</a> discusses, to some extent, how to do decryption, <strong><em>IF</em></strong> possible, but it's complicated, and not always possible.</p><p>Is there some reason to expect UDP traffic on your network? For example, is there any audio or video player traffic, which might use RTP running on top of UDP?</p><p>And as for the Ethernet frame check sequence, that's probably because, for whatever reason, Wireshark thinks the packets include the frame check sequence at the end of the packet when, in fact, they don't include it. Could you show us one of the packets where Wireshark reports that the Ethernet frame check sequence is incorrect, <em>after</em> opening up the display of the Ethernet and IP headers?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Nov '14, 16:46</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-37924" class="comments-container"></div><div id="comment-tools-37924" class="comment-tools"></div><div class="clear"></div><div id="comment-37924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

