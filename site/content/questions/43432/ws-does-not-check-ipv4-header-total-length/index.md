+++
type = "question"
title = "WS does not check Ipv4-Header-Total-Length?"
description = '''I&#x27;m working for years with WS and am really pleased with it, but now, I&#x27;ve found something astonishing, which I can not believe to be bug after all these years, it must be misconfiguration on my side (I hope): PROBLEM: Wireshark seems not to check the &#x27;Total-Length&#x27; field of an IPv4 header! DETAILS:...'''
date = "2015-06-21T23:50:00Z"
lastmod = "2015-06-22T04:50:00Z"
weight = 43432
keywords = [ "header", "validate", "ipv4", "totallength" ]
aliases = [ "/questions/43432" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [WS does not check Ipv4-Header-Total-Length?](/questions/43432/ws-does-not-check-ipv4-header-total-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43432-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm working for years with WS and am really pleased with it, but now, I've found something astonishing, which I can not believe to be bug after all these years, it must be misconfiguration on my side (I hope):</p><h3 id="problem">PROBLEM:</h3><p>Wireshark seems not to check the 'Total-Length' field of an IPv4 header!</p><h3 id="details">DETAILS:</h3><p>A kind of conformancetest sends ethernet frames with always the same IPv4/UDP payload. For test purpose, the testtool changes single fields of the IP header only, e.g. the IP-HDR-CRC (which is detected by WS). But if the 'Total Length' field of the IPv4 Header s varied (too-small/too-big), WS tells nothing - although WS should be able to detect it with the help of the overall content of the ethernet frames. Please note, that under Preferences/Protocols/IPv4 all options are enabled (although nothing applies to the header field 'total length'). I'm using WS Version 1.12.5.</p><h3 id="test-frames">TEST FRAMES:</h3><p>I uploaded a <a href="https://www.cloudshark.org/captures/7c36ec0ec8f6">capture with 7 corrupted testframes</a>, where #4 + #6 are the relevant ones:</p><ul><li>no.4 - IP-Header-Total-Length set to 197 (instead of 192)</li><li>no.6 - IP-Header-Total-Length set to 224 (instead of 192)</li></ul><p><em>(Note: 'Validation' seems to disabled in CloudShare, so please download and open it in WS to see the corruptions (in Cloudshare/more info../File/Download.)</em></p><h3 id="question">QUESTION:</h3><p>Might this be a bug in WS - or do I only use wrong settings or assumptions?</p></div><div id="question-tags" class="tags-container tags">header validate ipv4 totallength</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jun '15, 23:50</strong></p><img src="https://secure.gravatar.com/avatar/9cda1b2e882533ded78af7471c874f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ralf%20S&#39;s gravatar image" /><p>Ralf S<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ralf S has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jun '15, 23:51</p></div></div><div id="comments-container-43432" class="comments-container"></div><div id="comment-tools-43432" class="comment-tools"></div><div class="clear"></div><div id="comment-43432-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43437"></span>

<div id="answer-container-43437" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43437-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=epan/dissectors/packet-ip.c;h=5a785207ad083b58f9314cc01cfb3a8011554dbf;hb=c52dc98563db07f0bb152ca63304bf6e40682422#l2078">The code</a> has checking for various situations build in:</p><ol><li>Shorter than header size</li><li>0 (i.c.o. TSO)</li><li>Adjustment of buffer</li></ol><p>and a remark on what could cause the total header length to be larger than what's in the packet. This could have legitimate reasons, so an all-out error would be wrong. Reasons being:</p><ol><li>IP header in an ICMP packet</li><li>frame cut short during capture.</li><li>others?</li></ol><p>Specific code would have to be added to differentiate these situations. A bug? Maybe, for sure an option for enhancement.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jun '15, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-43437" class="comments-container"><span id="43439"></span><div id="comment-43439" class="comment"><div id="post-43439-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jaap for that fast reply and glance into WS sources.</p><p>None three situations mentioned by you above (and implemented in WS) apply to the corrupted testframes. So it's currently not supported. And of course I understand the complexity of validation (reasons above).</p><p>As WS development is widely out of my focus and as I really like to trigger this as a WS enhancement - whom could I give a '+1' for this proposal?</p></div><div id="comment-43439-info" class="comment-info"><span class="comment-age">(22 Jun '15, 06:23)</span> Ralf S</div></div><span id="43440"></span><div id="comment-43440" class="comment"><div id="post-43440-score" class="comment-score"></div><div class="comment-text"><p>See the wiki page <a href="https://wiki.wireshark.org/ReportingBugs">Reporting Bugs</a> for info on how to submit a bug (or enhancement request).</p></div><div id="comment-43440-info" class="comment-info"><span class="comment-age">(22 Jun '15, 07:37)</span> grahamb ♦</div></div><span id="43442"></span><div id="comment-43442" class="comment"><div id="post-43442-score" class="comment-score"></div><div class="comment-text"><p>Ok, I added this as an enhancement to the WS Bug Tracker,</p><p>see <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11296">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=11296</a></p></div><div id="comment-43442-info" class="comment-info"><span class="comment-age">(22 Jun '15, 08:04)</span> Ralf S</div></div></div><div id="comment-tools-43437" class="comment-tools"></div><div class="clear"></div><div id="comment-43437-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

