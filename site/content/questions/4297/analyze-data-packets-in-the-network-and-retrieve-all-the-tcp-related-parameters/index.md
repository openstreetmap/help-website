+++
type = "question"
title = "Analyze data packets in the network and retrieve all the TCP related parameters"
description = '''Hi, I want to analyze data packets in the network and retrieve all the TCP related parameters of a particular device and capture them into a file.'''
date = "2011-05-31T13:25:00Z"
lastmod = "2011-05-31T13:33:00Z"
weight = 4297
keywords = [ "analyzedata" ]
aliases = [ "/questions/4297" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Analyze data packets in the network and retrieve all the TCP related parameters](/questions/4297/analyze-data-packets-in-the-network-and-retrieve-all-the-tcp-related-parameters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4297-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I want to analyze data packets in the network and retrieve all the TCP related parameters of a particular device and capture them into a file.</p></div><div id="question-tags" class="tags-container tags">analyzedata</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '11, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/5b3d6cf175710e532eb8185521ba364a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kumar&#39;s gravatar image" /><p>Kumar<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kumar has no accepted answers">0%</span></p></div></div><div id="comments-container-4297" class="comments-container"></div><div id="comment-tools-4297" class="comment-tools"></div><div class="clear"></div><div id="comment-4297-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4298"></span>

<div id="answer-container-4298" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4298-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Okay, that sounds exactly like what you can do with Wireshark: first, capture TCP packet data, second, analyze it. Or did you mean that you want to get stack parameters that are configured in the OS of a device? You might be able to extract or deduct some of them from packets you see (like TCP window scaling settings, with more or less accurate results/guesses), but it won't be the same like looking at the Windows registry or similar *nix stack parameter files.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 May '11, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-4298" class="comments-container"><span id="4299"></span><div id="comment-4299" class="comment"><div id="post-4299-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your prompt reply. I have some more questions. Can you please provide me your mail id so that i can post them to your mail id.</p></div><div id="comment-4299-info" class="comment-info"><span class="comment-age">(31 May '11, 13:44)</span> Kumar</div></div><span id="4300"></span><div id="comment-4300" class="comment"><div id="post-4300-score" class="comment-score"></div><div class="comment-text"><p>Why not post them here? Others might be interested, too, and more users might add their ideas/wisdom to your questions :-)</p></div><div id="comment-4300-info" class="comment-info"><span class="comment-age">(31 May '11, 13:47)</span> Jasper ♦♦</div></div><span id="4301"></span><div id="comment-4301" class="comment"><div id="post-4301-score" class="comment-score"></div><div class="comment-text"><p>For the captured "Modbus/TCP" packets, other details like "Frame 2976", "Internel Protocol"....etc are also displayed in the same "Modbus/TCP" packet. But i only need certain data in a packet. So is there any mechanism to modify source code of this dissector and capture only required parameters ?</p></div><div id="comment-4301-info" class="comment-info"><span class="comment-age">(31 May '11, 14:35)</span> Kumar</div></div><span id="4302"></span><div id="comment-4302" class="comment"><div id="post-4302-score" class="comment-score"></div><div class="comment-text"><p>I guess you could download the Wireshark source code and modify the ModBus/TCP dissector to skip displaying fields you do not like to be displayed. Capturing only required parameters is not an option since the capture process always records complete frames, including all checksums etc.</p><p>On the other hand - displaying more data than needed is usually not a problem - you might also try to display only the wanted details as additonal columns of the file list (right click on the according fields and select "appy as column").</p></div><div id="comment-4302-info" class="comment-info"><span class="comment-age">(31 May '11, 14:42)</span> Jasper ♦♦</div></div></div><div id="comment-tools-4298" class="comment-tools"></div><div class="clear"></div><div id="comment-4298-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

