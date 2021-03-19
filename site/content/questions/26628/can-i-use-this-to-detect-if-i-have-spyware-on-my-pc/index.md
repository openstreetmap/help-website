+++
type = "question"
title = "Can I use this to detect if I have spyware on my PC?"
description = '''And if so, can I see exactly what data is being transmitted and to what IP? Also, can I get additional info on the IP, like country and service provider, and have the option to block any further communication?'''
date = "2013-11-03T02:06:00Z"
lastmod = "2013-11-03T02:24:00Z"
weight = 26628
keywords = [ "security" ]
aliases = [ "/questions/26628" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can I use this to detect if I have spyware on my PC?](/questions/26628/can-i-use-this-to-detect-if-i-have-spyware-on-my-pc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26628-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>And if so, can I see exactly what data is being transmitted and to what IP? Also, can I get additional info on the IP, like country and service provider, and have the option to block any further communication?</p></div><div id="question-tags" class="tags-container tags">security</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Nov '13, 02:06</strong></p><img src="https://secure.gravatar.com/avatar/aecef4739b2a43d0d46ab7a58a14f4a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="leebonolo&#39;s gravatar image" /><p>leebonolo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="leebonolo has no accepted answers">0%</span></p></div></div><div id="comments-container-26628" class="comments-container"></div><div id="comment-tools-26628" class="comment-tools"></div><div class="clear"></div><div id="comment-26628-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26629"></span>

<div id="answer-container-26629" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26629-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can use Wireshark to record what your PC is receiving and sending, unless you have a very sophisticated malware infection that manages to either</p><ul><li>prevent Wireshark from running in the first place</li><li>ceases doing its communication while the capture is running</li><li>or hides the packets from Wireshark</li></ul><p>All three are not very likely because most Spyware is too stupid to care. If you capture all communication from your PC you can use GeoIP databases to find the locations of the other system (if it is known).</p><p>You might want to check my blog for the following posts that may help:</p><p><a href="http://blog.packet-foo.com/2013/04/the-packet-analysts-self-check/">http://blog.packet-foo.com/2013/04/the-packet-analysts-self-check/</a></p><p><a href="http://blog.packet-foo.com/2013/05/wireshark-geoip-resolution-setup/">http://blog.packet-foo.com/2013/05/wireshark-geoip-resolution-setup/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Nov '13, 02:24</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-26629" class="comments-container"></div><div id="comment-tools-26629" class="comment-tools"></div><div class="clear"></div><div id="comment-26629-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

