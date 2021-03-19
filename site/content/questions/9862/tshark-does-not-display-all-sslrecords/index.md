+++
type = "question"
title = "Tshark does not display all ssl.records"
description = '''Hi, According to the post here: http://www.wireshark.org/lists/wireshark-users/200909/msg00254.html there was a feature request for printing all occurances of a field when there are multiple occurances in a single packet (in my case it&#x27;s ssl.record and all other fields related to ssl).  Is it alread...'''
date = "2012-03-30T06:36:00Z"
lastmod = "2012-03-30T07:34:00Z"
weight = 9862
keywords = [ "ssl", "occurances", "multiple", "bug", "field" ]
aliases = [ "/questions/9862" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Tshark does not display all ssl.records](/questions/9862/tshark-does-not-display-all-sslrecords)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9862-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>According to the post here:</p><p><a href="http://www.wireshark.org/lists/wireshark-users/200909/msg00254.html">http://www.wireshark.org/lists/wireshark-users/200909/msg00254.html</a></p><p>there was a feature request for printing all occurances of a field when there are multiple occurances in a single packet (in my case it's ssl.record and all other fields related to ssl). Is it already implemented?</p><p>Best Regards</p></div><div id="question-tags" class="tags-container tags">ssl occurances multiple bug field</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Mar '12, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/ec65992495e12c0bd594fc502152920c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="korczyn&#39;s gravatar image" /><p>korczyn<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="korczyn has no accepted answers">0%</span></p></div></div><div id="comments-container-9862" class="comments-container"></div><div id="comment-tools-9862" class="comment-tools"></div><div class="clear"></div><div id="comment-9862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9863"></span>

<div id="answer-container-9863" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9863-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes indeed this has been implemented:</p><pre><code>  -E&lt;fieldsoption&gt;=&lt;value&gt; set options for output when -Tfields selected:
     header=y|n            switch headers on and off
     separator=/t|/s|&lt;char&gt; select tab, space, printable character as separator
     occurrence=f|l|a      print first, last or all occurrences of each field
     aggregator=,|/s|&lt;char&gt; select comma, space, printable character as
                           aggregator
     quote=d|s|n           select double, single, no quotes for values</code></pre><p>(from "tshark -h")</p><p>You might need to upgrade to 1.6.x</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Mar '12, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-9863" class="comments-container"><span id="9864"></span><div id="comment-9864" class="comment"><div id="post-9864-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your response. In deed I was using an older version!</p><p>Regards, korczyn</p></div><div id="comment-9864-info" class="comment-info"><span class="comment-age">(30 Mar '12, 08:20)</span> korczyn</div></div><span id="9870"></span><div id="comment-9870" class="comment"><div id="post-9870-score" class="comment-score"></div><div class="comment-text"><p>@korczyn, I've converted your "answer" to a comment as that is how this site works, see the <a href="http://ask.wireshark.org/faq/">FAQ</a> for details. If SYN-bit has answered your question, please accept it by clicking the check mark icon.</p></div><div id="comment-9870-info" class="comment-info"><span class="comment-age">(30 Mar '12, 12:40)</span> grahamb ♦</div></div></div><div id="comment-tools-9863" class="comment-tools"></div><div class="clear"></div><div id="comment-9863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

