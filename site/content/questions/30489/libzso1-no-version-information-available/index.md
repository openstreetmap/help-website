+++
type = "question"
title = "libz.so.1: no version information available"
description = '''I am using wireshark 1.10.x in Linux. If running the following command:  tshark -r test.pcap -V &amp;gt;&amp;gt; test.txt The command passed. But if I call the command in my software, the error is: tshark: /home/my software/bin/libz.so.1: no version information available (required by /usr/local/lib/libwiret...'''
date = "2014-03-06T12:04:00Z"
lastmod = "2014-03-06T13:33:00Z"
weight = 30489
keywords = [ "available", "information", "version", "1.10", "no" ]
aliases = [ "/questions/30489" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [libz.so.1: no version information available](/questions/30489/libzso1-no-version-information-available)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30489-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark 1.10.x in Linux. If running the following command: tshark -r test.pcap -V &gt;&gt; test.txt The command passed.</p><p>But if I call the command in my software, the error is: tshark: /home/my software/bin/libz.so.1: no version information available (required by /usr/local/lib/libwiretap.so.3) libz.so.1 exists in both /lib/libz.so.1 and /home/my software/bin/libz.so.1, and they have the same version number.</p><p>Any possible reason for the failure? And how to let tshark call /lib/libz.so.1, not /home/my software/bin/libz.so.1?</p><p>The error did not happen when using wirehshark 1.6.x.</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">available information version 1.10 no</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '14, 12:04</strong></p><img src="https://secure.gravatar.com/avatar/5428a0ee14871ca6db736dcf6099b4fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huang-shi&#39;s gravatar image" /><p>huang-shi<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huang-shi has no accepted answers">0%</span></p></div></div><div id="comments-container-30489" class="comments-container"></div><div id="comment-tools-30489" class="comment-tools"></div><div class="clear"></div><div id="comment-30489-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30502"></span>

<div id="answer-container-30502" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30502-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Any possible reason for the failure?</p></blockquote><p>Yes. The way you called tshark in your software/application. As you did not say anything about that, it's impossible to help you.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '14, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-30502" class="comments-container"><span id="30506"></span><div id="comment-30506" class="comment"><div id="post-30506-score" class="comment-score"></div><div class="comment-text"><p>Thank you. I modified PATH and the problem was solved.</p></div><div id="comment-30506-info" class="comment-info"><span class="comment-age">(06 Mar '14, 14:51)</span> huang-shi</div></div></div><div id="comment-tools-30502" class="comment-tools"></div><div class="clear"></div><div id="comment-30502-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

