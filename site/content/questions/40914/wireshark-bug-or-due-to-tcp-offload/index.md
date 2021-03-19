+++
type = "question"
title = "Wireshark Bug or due to TCP offload?"
description = '''It seems I&#x27;ve found a discrepancy between reported bytes captured, TCP/IP and data length as well as calculation of &quot;Next Sequence Number&quot;. Below is a &quot;good&quot; example where the &quot;61558 bytes captured&quot; corresponds with the TCP/IP and Data Length.  ...and here is a &quot;bad&quot; example where the &quot;65654 bytes c...'''
date = "2015-03-26T12:20:00Z"
lastmod = "2015-03-26T19:58:00Z"
weight = 40914
keywords = [ "length", "bytes", "sequencenumber" ]
aliases = [ "/questions/40914" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark Bug or due to TCP offload?](/questions/40914/wireshark-bug-or-due-to-tcp-offload)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40914-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It seems I've found a discrepancy between reported bytes captured, TCP/IP and data length as well as calculation of "Next Sequence Number".</p><p>Below is a "good" example where the "61558 bytes captured" corresponds with the TCP/IP and Data Length.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/good_example.png" alt="alt text" /></p><p>...and here is a "bad" example where the "65654 bytes captured" does <em>not</em> correspond with the TCP/IP and Data Length. Also visible here is the fact that Wirehark reports bad FCS - which I also doubt is correct.</p><p>What's more important though, is that the "Next Sequence Number" is also seemingly wrong. This field is calculated by Wireshark and aids greatly in my troubleshooting, but less so when it's incorrect :-)</p><p>The question is whether my finding is indeed due to a bug in Wireshark or due to the fact that TCP Offload is enabled on the server where these captures are taken?</p><p>Wireshark version used: 1.10.10 and 1.12.4 on Windows 7 and Windows Server 2008 R2</p><p>Best Regards, Niels</p><p><img src="https://osqa-ask.wireshark.org/upfiles/bad_example.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">length bytes sequencenumber</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '15, 12:20</strong></p><img src="https://secure.gravatar.com/avatar/5a55fd7d0ca800a3b0724f350dbfec0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="NJL&#39;s gravatar image" /><p>NJL<br />
<span class="score" title="21 reputation points">21</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="NJL has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 26 Mar '15, 12:50</p></div></div><div id="comments-container-40914" class="comments-container"><span id="40915"></span><div id="comment-40915" class="comment"><div id="post-40915-score" class="comment-score"></div><div class="comment-text"><p>Can you share a capture in a publicly accessible spot, e.g. <a href="http://cloudshark.org">CloudShark</a>?</p></div><div id="comment-40915-info" class="comment-info"><span class="comment-age">(26 Mar '15, 13:15)</span> Jaap ♦</div></div><span id="40916"></span><div id="comment-40916" class="comment"><div id="post-40916-score" class="comment-score"></div><div class="comment-text"><p>sanitize using TraceWrangler if necessary (<a href="https://www.tracewrangler.com">https://www.tracewrangler.com</a>)</p></div><div id="comment-40916-info" class="comment-info"><span class="comment-age">(26 Mar '15, 13:28)</span> Jasper ♦♦</div></div><span id="40931"></span><div id="comment-40931" class="comment"><div id="post-40931-score" class="comment-score"></div><div class="comment-text"><p>I tried using TraceWrangler but after several tries it still messed up the important details. Most likely user error, but I gave up and used screenshots instead.</p></div><div id="comment-40931-info" class="comment-info"><span class="comment-age">(26 Mar '15, 23:38)</span> NJL</div></div></div><div id="comment-tools-40914" class="comment-tools"></div><div class="clear"></div><div id="comment-40914-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40926"></span>

<div id="answer-container-40926" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40926-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>This does not look like a Wireshark bug to me.</p><p>In the first example, you have a TCP calculated length of 61504 bytes, with a relative sequence number of 2697841. Wireshark correctly calculates the next expected sequence number to be: 2636337 + 61504 = 2697841. Although it's not shown, the IP total length field is almost certainly 61544, which is 61504 + 20 (standard IP header) + 20 (standard TCP header). And if you add 14 bytes for the Ethernet framing, you get 61558, which matches the number of bytes captured. All is good, as you already know.</p><p>On to the second example then ... The number of bytes captured is indicated as being 65654. Subtracting the 14 bytes for the Ethernet header means that the IP total length field would have to be 65640; however, that number is bigger than the largest value that the field can handle, which happens to be 65535, since the field is an unsigned short (2-byte) field. If you convert 65640 to hexadecimal, you get 0x10068, and when you try to stuff that number into an unsigned short field, you lose the upper 0x10000, leaving you with only 0x0068. In decimal, 0x0068 is 104. So, I think you will find that the IP total length field is set to 104. When you subtract 20 bytes for a standard IP header and another 20 bytes for a standard TCP header, you end up with a TCP payload of 64 bytes. Wireshark then correctly calculates the next expected sequence number of 2699553 from the current relative sequence number of 2699489 + 64. Because there's a lot of extra "padding" following the 64 byte TCP payload (as indicated by the data in the IP total length) field, Wireshark interprets the last 4 bytes of that "extra" data as an invalid Ethernet FCS, which of course it isn't, but that won't stop Wireshark from trying to validate it whenever the Ethernet dissector's "Validate the Ethernet checksum if possible" preference is enabled.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '15, 19:58</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></img></div></div><div id="comments-container-40926" class="comments-container"><span id="40930"></span><div id="comment-40930" class="comment"><div id="post-40930-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your in-depth explanation which of course makes perfect sense. :-)</p></div><div id="comment-40930-info" class="comment-info"><span class="comment-age">(26 Mar '15, 23:37)</span> NJL</div></div></div><div id="comment-tools-40926" class="comment-tools"></div><div class="clear"></div><div id="comment-40926-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

