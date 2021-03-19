+++
type = "question"
title = "Query about combining capture filter"
description = '''Hello all, I am new to wireshark and wireshark community. I am preparing for wcna exam and have the below query. I am right now studying packet capture filters and I am successfully able to write this filter  tcp[1] == 80 , while i want to also to do the filter tcp[1]== 80 &amp;amp; tcp[2] == 443, wires...'''
date = "2012-09-16T21:13:00Z"
lastmod = "2012-09-16T22:27:00Z"
weight = 14310
keywords = [ "capture", "filters", "query" ]
aliases = [ "/questions/14310" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Query about combining capture filter](/questions/14310/query-about-combining-capture-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14310-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am new to wireshark and wireshark community. I am preparing for wcna exam and have the below query. I am right now studying packet capture filters and I am successfully able to write this filter</p><p>tcp[1] == 80 , while i want to also to do the filter tcp[1]== 80 &amp; tcp[2] == 443, wireshark is not accepting the filter, while wireshark is accepting tcp[1]==80 &amp; tcp[2]</p><p>Anything that I am missing or misunderstood about 'anding'</p><p>Thank you Rakesh M</p></div><div id="question-tags" class="tags-container tags">capture filters query</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '12, 21:13</strong></p><img src="https://secure.gravatar.com/avatar/a993e0775b541840d488c64697f9bf65?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rakesh&#39;s gravatar image" /><p>rakesh<br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rakesh has no accepted answers">0%</span></p></div></div><div id="comments-container-14310" class="comments-container"><span id="14311"></span><div id="comment-14311" class="comment"><div id="post-14311-score" class="comment-score"></div><div class="comment-text"><p>Hello ,</p><p>I have realized that i should have used 'and' instead of '&amp;' :).</p><p>Thanks</p></div><div id="comment-14311-info" class="comment-info"><span class="comment-age">(16 Sep '12, 21:29)</span> rakesh</div></div><span id="14314"></span><div id="comment-14314" class="comment"><div id="post-14314-score" class="comment-score">1</div><div class="comment-text"><p>You can use:<br />
- and<br />
- &amp;&amp;<br />
<br />
You can find more information about combining expressions in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html#id36163501">Wireshark User's Guide</a>.</p></div><div id="comment-14314-info" class="comment-info"><span class="comment-age">(16 Sep '12, 22:37)</span> joke</div></div></div><div id="comment-tools-14310" class="comment-tools"></div><div class="clear"></div><div id="comment-14310-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14312"></span>

<div id="answer-container-14312" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14312-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, you should have used 'and' or '&amp;&amp;' instead of '&amp;', but there's more that needs to be corrected with this filter.</p><p>It looks like you're trying to filter on TCP port numbers. The TCP source port is a 2-byte field that starts at tcp[0]. tcp[1] is the second byte of the source port field. So "tcp[1]=80" will capture traffic whose source port is 80 (0x0050), but it will also capture traffic whose source port is 53,840 (0xD250). It will capture all traffic where the second byte of the source port field is 80. You want "tcp[0:2]==80" so that you're comparing the value '80' against the entire two-byte field.</p><p>Same for "tcp[2]==443". tcp[2] is the first byte of the 2-byte destination port field. You want "tcp[2:2]==443".</p><p>Putting all this together, we get "tcp[0:2]==80 &amp;&amp; tcp[2:2]==443". This is a syntactically valid capture filter that Wireshark will accept, but it's very unlikely to capture any traffic. In plain English, this filter means "capture all traffic where the source port is 80 and the destination port is 443."</p><p>In a web browsing session, the web server would likely be using port 80 if the traffic is HTTP, <em>or</em> port 443 if the traffic is HTTPS. Both of these ports are in the "well-known port range." However, the client would be using an ephemeral port that would be a higher number. Exactly what range is used for ephemeral ports depends on the operating system, but it certainly would be above 1,024. You're probably never going to see port 80 AND port 443 as source and destination in the same TCP packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '12, 22:27</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span> </br></br></p></div></div><div id="comments-container-14312" class="comments-container"><span id="14315"></span><div id="comment-14315" class="comment"><div id="post-14315-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much joke. And Jim, you have cleared the last bit of doubt in my mind. Actually to speak with i was worried rather not understood the length reading the book. Now it confirms exactly what is that field. I should have used an OR as I have realized later that the filter with 'and' operation should not / Do not make any sense. Thank you very much</p><p>I initially felt bad asking this question , but now i made a right thing. No matter how silly the question there is always more we learn :)</p></div><div id="comment-14315-info" class="comment-info"><span class="comment-age">(16 Sep '12, 23:42)</span> rakesh</div></div><span id="14329"></span><div id="comment-14329" class="comment"><div id="post-14329-score" class="comment-score"></div><div class="comment-text"><p>How about "tcp[0:2]==80 || tcp[0:2]==443 || tcp[2:2]==80 || tcp[2:2]==443" to capture all HTTP and HTTPS traffic in both directions?</p></div><div id="comment-14329-info" class="comment-info"><span class="comment-age">(17 Sep '12, 11:33)</span> Jim Aragon</div></div></div><div id="comment-tools-14312" class="comment-tools"></div><div class="clear"></div><div id="comment-14312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

