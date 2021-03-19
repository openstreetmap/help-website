+++
type = "question"
title = "tshark analysis question"
description = '''I have a requirement to produce a report that lists all outgoing destinations and their ports from the a given pcap file. I am using tshark to analyze the pcap file and in the past used the simple -z hosts option. I do not know how to get the ports to show up as well. Does anyone know how to make th...'''
date = "2014-06-14T11:39:00Z"
lastmod = "2014-06-14T22:20:00Z"
weight = 33803
keywords = [ "reporting", "tshark" ]
aliases = [ "/questions/33803" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark analysis question](/questions/33803/tshark-analysis-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33803-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a requirement to produce a report that lists all outgoing destinations and their ports from the a given pcap file. I am using tshark to analyze the pcap file and in the past used the simple -z hosts option. I do not know how to get the ports to show up as well. Does anyone know how to make this work? My initial code is below.</p><p>tshark -r file.pcap -q -z hosts &gt; output.txt Thanks</p><p>Sean</p></div><div id="question-tags" class="tags-container tags">reporting tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Jun '14, 11:39</strong></p><img src="https://secure.gravatar.com/avatar/96931104cd81bb95200423cb211b3cb7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sean_hoo&#39;s gravatar image" /><p>sean_hoo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sean_hoo has no accepted answers">0%</span></p></div></div><div id="comments-container-33803" class="comments-container"></div><div id="comment-tools-33803" class="comment-tools"></div><div class="clear"></div><div id="comment-33803-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="33811"></span>

<div id="answer-container-33811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-33811-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>tshark -r input.cap.pcapng -q -z conv,tcp &gt; output.txt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jun '14, 22:20</strong></p><img src="https://secure.gravatar.com/avatar/6f9cdab5081b4272d1abf703a2689372?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kishan%20pandey&#39;s gravatar image" /><p>kishan pandey<br />
<span class="score" title="221 reputation points">221</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="silver">●</span><span class="badgecount">29</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kishan pandey has 2 accepted answers">28%</span></p></div></div><div id="comments-container-33811" class="comments-container"><span id="33813"></span><div id="comment-33813" class="comment"><div id="post-33813-score" class="comment-score"></div><div class="comment-text"><p>@kishan pandey: I converted your comment to an answer, as it is a valid answer. Please <a href="http://ask.wireshark.org/faq/">read the FAQ</a> for how this site works ;-)</p></div><div id="comment-33813-info" class="comment-info"><span class="comment-age">(15 Jun '14, 02:54)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-33811" class="comment-tools"></div><div class="clear"></div><div id="comment-33811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

