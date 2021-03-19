+++
type = "question"
title = "filter the response to a matched HTTP request"
description = '''I&#x27;m trying to get wireshark to only capture requests that I&#x27;m sending to wildfly via my test suite, I&#x27;ve gotten everything filtered but the responses to the http request contains. (tcp.dstport == 8080 || tcp.srcport == 8080 ) &amp;amp;&amp;amp; http &amp;amp;&amp;amp; ! http.request.uri contains &quot;/test/&quot;  not sure ...'''
date = "2014-03-19T13:44:00Z"
lastmod = "2014-03-20T12:08:00Z"
weight = 30972
keywords = [ "filter", "http.response", "capture-filter", "http" ]
aliases = [ "/questions/30972" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [filter the response to a matched HTTP request](/questions/30972/filter-the-response-to-a-matched-http-request)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30972-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to get wireshark to only capture requests that I'm sending to wildfly via my test suite, I've gotten everything filtered but the responses to the http request contains.</p><pre><code>(tcp.dstport == 8080 || tcp.srcport == 8080 ) &amp;&amp; http &amp;&amp; ! http.request.uri contains &quot;/test/&quot;</code></pre><p>not sure what I need to look at to get it to match only the responses to the requests that contained test.</p></div><div id="question-tags" class="tags-container tags">filter http.response capture-filter http</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Mar '14, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/e990c7cdac81e570939c4d5b17303b42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xenoterracide&#39;s gravatar image" /><p>xenoterracide<br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xenoterracide has no accepted answers">0%</span></p></div></div><div id="comments-container-30972" class="comments-container"></div><div id="comment-tools-30972" class="comment-tools"></div><div class="clear"></div><div id="comment-30972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="31007"></span>

<div id="answer-container-31007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31007-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>not sure what I need to look at to get it to match only the responses to the requests that contained test.</p></blockquote><p>you can do this:</p><ol><li>Filter for the request: <strong>http.request.uri contains "/test"</strong><br />
</li><li>Get the TCP stream number(s) of those frames (tcp.stream)<br />
</li><li>Then filter for: <strong>tcp.stream eq xxx and frame contains "HTTP/1.1 200 OK"</strong> (or HTTP/1.0)</li></ol><p>You can automate that with tshark and some scripting.</p><ol><li>tshark -nr input.pcap -R 'http.request.uri contains "/test"' -T fields -e tcp.stream</li><li>Read the tcp streams with a script and create new filters based on them</li><li>tshark -nr input.pcap -R 'tcp.stream eq xxx and frame contains "HTTP/1.1 200 OK"'</li></ol><p>See also my answer to a similar question</p><blockquote><p><a href="http://ask.wireshark.org/questions/27616/follow-http-redirects-automatically-http-status-codes-301302">http://ask.wireshark.org/questions/27616/follow-http-redirects-automatically-http-status-codes-301302</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 12:08</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Mar '14, 12:10</p></div></div><div id="comments-container-31007" class="comments-container"></div><div id="comment-tools-31007" class="comment-tools"></div><div class="clear"></div><div id="comment-31007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30973"></span>

<div id="answer-container-30973" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30973-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think that that is possible with just one single filter, because the answer packet does not contain the request (unlike in DNS answers, for example).</p><p>Wireshark can only filter on some packets depending on other packets if the dissector transfers the relevant details to the answer packet. An example for that would be the "http.request_in" which can be used to find packets that are a response to another packet, but that packet has to be specified by number. You can't use a uri filter for this.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Mar '14, 14:09</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span> </br></p></div></div><div id="comments-container-30973" class="comments-container"></div><div id="comment-tools-30973" class="comment-tools"></div><div class="clear"></div><div id="comment-30973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31000"></span>

<div id="answer-container-31000" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31000-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This is the kind of thing <a href="http://wiki.wireshark.org/Mate">MATE</a> is good for.</p><p>Unfortunately it's not documented very well and can be tricky to use, but it is almost certainly possible to do what you want with it...</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 10:17</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-31000" class="comments-container"></div><div id="comment-tools-31000" class="comment-tools"></div><div class="clear"></div><div id="comment-31000-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

