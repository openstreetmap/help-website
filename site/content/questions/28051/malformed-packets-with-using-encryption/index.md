+++
type = "question"
title = "Malformed packets with using encryption?"
description = '''Hello, I sent a document with IPP - using https://address:631/printers/XXX or with IPP+TLS - using ipp://address:631/printers/XXX??encryption=required. Then I looked into capture file and IPP packets were malformed (printer output was correct). Is it normal (because of TLS) or is something wrong wit...'''
date = "2013-12-12T05:59:00Z"
lastmod = "2013-12-27T08:14:00Z"
weight = 28051
keywords = [ "tls", "ipp", "cups", "packet", "malformed" ]
aliases = [ "/questions/28051" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Malformed packets with using encryption?](/questions/28051/malformed-packets-with-using-encryption)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28051-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I sent a document with IPP - using <a href="https://address:631/printers/XXX">https://address:631/printers/XXX</a> or with IPP+TLS - using <span>ipp://address:631/printers/XXX??encryption=required.</span> Then I looked into capture file and IPP packets were malformed (printer output was correct). Is it normal (because of TLS) or is something wrong with it? When I try normal <span>ipp://address:631/printers/XXX</span> everything is OK.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">tls ipp cups packet malformed</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Dec '13, 05:59</strong></p><img src="https://secure.gravatar.com/avatar/be20005a55b5334aa5e61e2faeee32c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andyn&#39;s gravatar image" /><p>Andyn<br />
<span class="score" title="6 reputation points">6</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andyn has no accepted answers">0%</span></p></div></div><div id="comments-container-28051" class="comments-container"><span id="28389"></span><div id="comment-28389" class="comment"><div id="post-28389-score" class="comment-score"></div><div class="comment-text"><p>nobody? :)</p></div><div id="comment-28389-info" class="comment-info"><span class="comment-age">(25 Dec '13, 10:49)</span> Andyn</div></div><span id="28390"></span><div id="comment-28390" class="comment"><div id="post-28390-score" class="comment-score"></div><div class="comment-text"><p>Well, can you provide a capture file?</p></div><div id="comment-28390-info" class="comment-info"><span class="comment-age">(25 Dec '13, 12:21)</span> Kurt Knochner ♦</div></div><span id="28413"></span><div id="comment-28413" class="comment"><div id="post-28413-score" class="comment-score"></div><div class="comment-text"><p>Here it is: <a href="http://leteckaposta.cz/877815894">http://leteckaposta.cz/877815894</a> (I can't add a comment - akismet thinks it's spam)</p></div><div id="comment-28413-info" class="comment-info"><span class="comment-age">(26 Dec '13, 13:08)</span> Andyn</div></div><span id="28430"></span><div id="comment-28430" class="comment"><div id="post-28430-score" class="comment-score"></div><div class="comment-text"><p>can you please add the frame number(s) of the "malformed packets".</p></div><div id="comment-28430-info" class="comment-info"><span class="comment-age">(27 Dec '13, 04:07)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28051" class="comment-tools"></div><div class="clear"></div><div id="comment-28051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28441"></span>

<div id="answer-container-28441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28441-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark tries to dissect the TLS packets as IPP protocol.</p><p>You need to "decode as" the tcp.port 631 traffic and map it to SSL after HTTP/1.1 101 Switching Protocols message has flown. From then on it's all TLS</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Dec '13, 08:14</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p>mrEEde<br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-28441" class="comments-container"></div><div id="comment-tools-28441" class="comment-tools"></div><div class="clear"></div><div id="comment-28441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

