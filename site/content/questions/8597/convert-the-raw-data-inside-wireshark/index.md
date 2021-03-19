+++
type = "question"
title = "Convert the raw data inside Wireshark ?"
description = '''We are planning to make a solution on our Telecom system, that would monitor the signalling messages (e.g. RANAP/CC/MM/SMS, BICC, H..248, MAP, ISUP, INAP/CAP, etc.), which belongs to specific transactions and after post-processing those would be checked in Wireshark. The raw monitoring data will be ...'''
date = "2012-01-25T00:52:00Z"
lastmod = "2012-01-25T02:29:00Z"
weight = 8597
keywords = [ "filter", "capture", "conversion", "dissector" ]
aliases = [ "/questions/8597" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Convert the raw data inside Wireshark ?](/questions/8597/convert-the-raw-data-inside-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8597-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are planning to make a solution on our Telecom system, that would monitor the signalling messages (e.g. RANAP/CC/MM/SMS, BICC, H..248, MAP, ISUP, INAP/CAP, etc.), which belongs to specific transactions and after post-processing those would be checked in Wireshark.</p><p>The raw monitoring data will be stored in the form as they captured from the system, which means</p><p>• all the type of signaling data that were involved in the transaction would be in the same monitoring file;</p><p>• The monitoring will contain the signaling messages on application layer level, thus all of the layer below the application layer shall be dummy layer, meaning that layer 2 – layer 4 headers and data shall be faked.</p><p>My question related to this are the following:</p><ul><li>Is it a requirement in Wireshark that the messages shall be first sorted out by protocol type into separate files or there could be one file, which contains all the protocol messages ?</li><li>Could the conversion of raw data into pcap format - and faking the underlayers - be implemented in Wireshark - e.g. as an add-in or part of the dissector ?</li></ul><p>Thanks !</p></div><div id="question-tags" class="tags-container tags">filter capture conversion dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jan '12, 00:52</strong></p><img src="https://secure.gravatar.com/avatar/07543cd721cba4254edea1bb5929efe8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BEGINNER&#39;s gravatar image" /><p>BEGINNER<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BEGINNER has no accepted answers">0%</span></p></div></div><div id="comments-container-8597" class="comments-container"></div><div id="comment-tools-8597" class="comment-tools"></div><div class="clear"></div><div id="comment-8597-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8602"></span>

<div id="answer-container-8602" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8602-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>Wireshark can work out protocol types on its own. Fire it up on your desktop network connection and see the mayhem of mixed protocol message flows. Not a problem.</li><li>There are two options to import raw data into Wireshark. There's the command line tool text2pcap, and the GUI import feature. Both can do the same, faking the lower layers. Make sure to read the text2pcap manual page to get an idea of the required input format.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jan '12, 02:29</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-8602" class="comments-container"><span id="8652"></span><div id="comment-8652" class="comment"><div id="post-8652-score" class="comment-score"></div><div class="comment-text"><p>Thank you !</p><p>Still I have further questions:</p><p>As the encapsulation type is common - and at at least in the GUI it is not optional - that means that still the protocol types in a source file shall be separated by the type of lower layer used. Is it correct ?</p><p>And as I see the dummy layers can be added only for IP, but not for SS7 for example. Has Wireshark solution for faking the lower layers in case of SS7 ?</p><p>Thanks !</p></div><div id="comment-8652-info" class="comment-info"><span class="comment-age">(27 Jan '12, 04:32)</span> BEGINNER</div></div></div><div id="comment-tools-8602" class="comment-tools"></div><div class="clear"></div><div id="comment-8602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

