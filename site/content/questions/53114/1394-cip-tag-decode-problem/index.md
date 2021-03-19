+++
type = "question"
title = "1394 CIP Tag decode problem?"
description = '''I&#x27;m looking at an Ethernet capture from a BroadR Reach camera using 1722 to send MJPEG video. I am confused by the wireshark output and wonder if there is a decoding issue or, more likely, a misunderstanding on my part. The IEEE 1394 spec indicates that the Tag value 00 indicates No CIP header inclu...'''
date = "2016-06-01T10:19:00Z"
lastmod = "2016-06-01T15:02:00Z"
weight = 53114
keywords = [ "ieee1722", "ieee1394" ]
aliases = [ "/questions/53114" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [1394 CIP Tag decode problem?](/questions/53114/1394-cip-tag-decode-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53114-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm looking at an Ethernet capture from a BroadR Reach camera using 1722 to send MJPEG video. I am confused by the wireshark output and wonder if there is a decoding issue or, more likely, a misunderstanding on my part. The IEEE 1394 spec indicates that the Tag value 00 indicates No CIP header included. The trace I have captured has a Tag value of 00 <img src="https://osqa-ask.wireshark.org/upfiles/1722.png" alt="Screen shot" /> However wireshark goes on to decode a CIP header. The values in the header are largely garbage from a comparison with the standard. For example Format ID in the screen shot is 0x0d which is not listed as a valid code in 1394. The values are pretty random landing in the reserved range for several elements. This suggests to me that Wireshark is decoding 1394 incorrectly.</p><p>Associated with this is the fact that it seems to be ignoring the 1394 Header CRC between the 1394 Header and the CIP header.</p><p>I'm totally confused as to whats going on. Is Wireshark throwing a wobble or is it me?</p><p>Here is the pcap file <a href="https://www.dropbox.com/s/jmfr7f5mpetiett/1722.pcap?dl=0">1722.pcap</a></p></div><div id="question-tags" class="tags-container tags">ieee1722 ieee1394</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '16, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/93fcd0e57fcd4123e08295cf23f5685d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paulrbarnard&#39;s gravatar image" /><p>paulrbarnard<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paulrbarnard has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jun '16, 10:24</p></div></div><div id="comments-container-53114" class="comments-container"></div><div id="comment-tools-53114" class="comment-tools"></div><div class="clear"></div><div id="comment-53114-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53118"></span>

<div id="answer-container-53118" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53118-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The 1394 dissection is part of the 1722 dissection, which does assume the 1394 fields are all there all the time. If this is in error a <a href="https://bugs.wireshark.org">bug report</a> should be filed, with your capture attached and a reference to the <a href="http://grouper.ieee.org/groups/1722/">protocol working group</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '16, 15:02</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53118" class="comments-container"><span id="53130"></span><div id="comment-53130" class="comment"><div id="post-53130-score" class="comment-score"></div><div class="comment-text"><p>Thank you Jaap. Having slept on it I'm pretty sure this is a bug so I have raised a ticket <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12490">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=12490</a> to track this problem.</p></div><div id="comment-53130-info" class="comment-info"><span class="comment-age">(02 Jun '16, 01:34)</span> paulrbarnard</div></div></div><div id="comment-tools-53118" class="comment-tools"></div><div class="clear"></div><div id="comment-53118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

