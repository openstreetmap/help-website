+++
type = "question"
title = "Automating extraction of UDP payload from pcap file"
description = '''Hey, Was wondering if it&#x27;s possible to point Wireshark, or a Wireshark utility, at an existing pcap UDP capture file and have it do the equivalent of:  * Follow UDP Stream  * Save As (Raw format) to a specified output file ...from the command line. Is this doable? Thanks! -phil matthews'''
date = "2015-01-09T06:55:00Z"
lastmod = "2015-01-10T04:55:00Z"
weight = 38998
keywords = [ "commandline", "export", "payload" ]
aliases = [ "/questions/38998" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Automating extraction of UDP payload from pcap file](/questions/38998/automating-extraction-of-udp-payload-from-pcap-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38998-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>Was wondering if it's possible to point Wireshark, or a Wireshark utility, at an existing pcap UDP capture file and have it do the equivalent of: * Follow UDP Stream * Save As (Raw format) to a specified output file ...from the command line.</p><p>Is this doable?</p><p>Thanks!</p><p>-phil matthews</p></div><div id="question-tags" class="tags-container tags">commandline export payload</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jan '15, 06:55</strong></p><img src="https://secure.gravatar.com/avatar/a6bad2698d688c02954130adfba2d7ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philbo_m&#39;s gravatar image" /><p>philbo_m<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philbo_m has no accepted answers">0%</span></p></div></div><div id="comments-container-38998" class="comments-container"></div><div id="comment-tools-38998" class="comment-tools"></div><div class="clear"></div><div id="comment-38998-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39021"></span>

<div id="answer-container-39021" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39021-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please read the scripting part of my answer to a similar question.</p><blockquote><p><a href="https://ask.wireshark.org/questions/35353/exporting-payload-data-in-binary-file">https://ask.wireshark.org/questions/35353/exporting-payload-data-in-binary-file</a><br />
</p></blockquote><p>As an alternative, you can run tshark with the options -V and -x, or -T dpml and then and extract whatever you need from that output.</p><blockquote><p>tshark -nr input.pcap -V -x | your_script<br />
tshark -nr input.pcap -T pdml | your_script<br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '15, 04:55</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-39021" class="comments-container"><span id="39160"></span><div id="comment-39160" class="comment"><div id="post-39160-score" class="comment-score"></div><div class="comment-text"><p>Hey Kurt,</p><p>Using '-T pdml' + a little bit of post-processing on the data.data element - works like a charm.<br />
</p><p>Thanks!</p><p>-phil</p></div><div id="comment-39160-info" class="comment-info"><span class="comment-age">(15 Jan '15, 06:49)</span> philbo_m</div></div></div><div id="comment-tools-39021" class="comment-tools"></div><div class="clear"></div><div id="comment-39021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

