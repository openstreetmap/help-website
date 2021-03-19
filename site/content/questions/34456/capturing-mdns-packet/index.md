+++
type = "question"
title = "Capturing mDNS packet"
description = '''Hi, I have a bunch of Apple devices, printer etc. in my home that all supports Bonjour. The mDNS Watcher app can find all of them. But when I capture with Wireshark, I don’t see any of them.  I followed this thread &amp;amp; applied the display filter ‘dns and udp.port eq 5353’ but I don’t see anything....'''
date = "2014-07-07T22:23:00Z"
lastmod = "2014-07-08T07:33:00Z"
weight = 34456
keywords = [ "mdns" ]
aliases = [ "/questions/34456" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing mDNS packet](/questions/34456/capturing-mdns-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34456-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a bunch of Apple devices, printer etc. in my home that all supports Bonjour. The mDNS Watcher app can find all of them. But when I capture with Wireshark, I don’t see any of them.</p><p>I followed this <a href="http://ask.wireshark.org/questions/23518/mdns-protocol-filtering">thread</a> &amp; applied the display filter ‘dns and udp.port eq 5353’ but I don’t see anything.</p><p>Is there any other way I can look at mDNS packet?</p></div><div id="question-tags" class="tags-container tags">mdns</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jul '14, 22:23</strong></p><img src="https://secure.gravatar.com/avatar/29ccfac7eaba9eaf208c68b22bb256bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lilyhack&#39;s gravatar image" /><p>lilyhack<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lilyhack has no accepted answers">0%</span></p></div></div><div id="comments-container-34456" class="comments-container"></div><div id="comment-tools-34456" class="comment-tools"></div><div class="clear"></div><div id="comment-34456-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="34459"></span>

<div id="answer-container-34459" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34459-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your display filter is correct. Maybe there simply weren't any mDNS packets during the period that you captured traffic. mDNS responses are cached, so it isn't necessary for a network device to issue a mDNS query every time it wants to communicate with another device.</p><p>Try power-cycling one of the Apple devices while you're capturing with Wireshark. You should be able to see mDNS startup probes and service announcements per Section 8 of <a href="http://tools.ietf.org/pdf/rfc6762.pdf">RFC 6762</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '14, 00:15</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-34459" class="comments-container"></div><div id="comment-tools-34459" class="comment-tools"></div><div class="clear"></div><div id="comment-34459-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="34466"></span>

<div id="answer-container-34466" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34466-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>dns and udp.port eq 5353</p></blockquote><p>If you apply that filter on the following sample capture file, do you see any frames?</p><blockquote><p><a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=mDNS1.zip">http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=mDNS1.zip</a></p></blockquote><p>If you see no matching frames, there is something wrong with your Wireshark configuration, maybe some dissectors disabled, or another protocol on port 5353 was set to 'decode as'.</p><p>If you see matching frames, there was either no mDNS traffic while you were capturing or there is something wrong with your capture setup.</p><p>So, here are some questions:</p><ul><li>where/how did you capture (ethernet/wireless)?</li><li>Did you use any capture filters?</li><li>are there VLANs involved?</li><li>what is your OS and OS version?</li><li>what is your Wireshark version?</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jul '14, 07:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-34466" class="comments-container"><span id="34471"></span><div id="comment-34471" class="comment"><div id="post-34471-score" class="comment-score"></div><div class="comment-text"><p>@Kurt-Knochner, Yes I see MDNS packet with your capture. And it seems my windows firewall blocked the port 5353. After disabling the firewall, I see mDNS packets generated my devices.</p></div><div id="comment-34471-info" class="comment-info"><span class="comment-age">(08 Jul '14, 09:44)</span> lilyhack</div></div><span id="34476"></span><div id="comment-34476" class="comment"><div id="post-34476-score" class="comment-score"></div><div class="comment-text"><blockquote><p>After disabling the firewall, I see mDNS packets generated my devices.</p></blockquote><p>good.</p></div><div id="comment-34476-info" class="comment-info"><span class="comment-age">(08 Jul '14, 11:35)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-34466" class="comment-tools"></div><div class="clear"></div><div id="comment-34466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

