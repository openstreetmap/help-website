+++
type = "question"
title = "UDP checksum error on IPv4 frame with loose source route."
description = '''I have a captured IPv4 frame with a few options in the header. One is a loose source route. The current pointer is not at the end. The frame has a UDP payload. Wireshark states the UDP checksum is incorrect. It appears it calculates the checksum based on the L3 IP destination address. Shouldn&#x27;t it b...'''
date = "2011-11-08T09:53:00Z"
lastmod = "2011-11-08T09:53:00Z"
weight = 7284
keywords = [ "checksum", "udp", "loose", "ipv4", "source" ]
aliases = [ "/questions/7284" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [UDP checksum error on IPv4 frame with loose source route.](/questions/7284/udp-checksum-error-on-ipv4-frame-with-loose-source-route)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7284-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a captured IPv4 frame with a few options in the header. One is a loose source route. The current pointer is not at the end. The frame has a UDP payload. Wireshark states the UDP checksum is incorrect. It appears it calculates the checksum based on the L3 IP destination address. Shouldn't it be calculated based on the last route in the loose source route table as long as the pointer hasn't gone past the table?</p></div><div id="question-tags" class="tags-container tags">checksum udp loose ipv4 source</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Nov '11, 09:53</strong></p><img src="https://secure.gravatar.com/avatar/a7ebcfc9938ca262a77295f0cc716985?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mayn&#39;s gravatar image" /><p>mayn<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mayn has no accepted answers">0%</span></p></div></div><div id="comments-container-7284" class="comments-container"></div><div id="comment-tools-7284" class="comment-tools"></div><div class="clear"></div><div id="comment-7284-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

