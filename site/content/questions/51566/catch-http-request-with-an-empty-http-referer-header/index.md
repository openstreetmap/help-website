+++
type = "question"
title = "Catch HTTP request with an empty HTTP Referer header"
description = '''The filter  http.referer == &quot;&quot;  will catch both HTTP requests without Referer header and HTTP requests whose Referer header are empty (see this pcap file). Is there a way to catch the case where the Referer header is present, but it&#x27;s empty? Thanks.'''
date = "2016-04-11T15:41:00Z"
lastmod = "2016-04-11T18:02:00Z"
weight = 51566
keywords = [ "wireshark" ]
aliases = [ "/questions/51566" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Catch HTTP request with an empty HTTP Referer header](/questions/51566/catch-http-request-with-an-empty-http-referer-header)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51566-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The filter</p><pre><code>http.referer == &quot;&quot;</code></pre><p>will catch both HTTP requests without Referer header and HTTP requests whose Referer header are empty (see this <a href="https://www.dropbox.com/s/uw56sd0bl5424u5/Http_referer_empty.pcap">pcap file</a>).</p><p>Is there a way to catch the case where the Referer header is present, but it's empty?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags">wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Apr '16, 15:41</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p>pktUser1001<br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></div></div><div id="comments-container-51566" class="comments-container"><span id="51573"></span><div id="comment-51573" class="comment"><div id="post-51573-score" class="comment-score"></div><div class="comment-text"><p>Thanks @jim-aragon for the answer. I think I am wrong in making the assumption without testing.</p></div><div id="comment-51573-info" class="comment-info"><span class="comment-age">(11 Apr '16, 19:16)</span> pktUser1001</div></div></div><div id="comment-tools-51566" class="comment-tools"></div><div class="clear"></div><div id="comment-51566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51572"></span>

<div id="answer-container-51572" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-51572-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>When I apply that filter (http.referer==""), it does not show requests without a Referer header. I've tested it with v2.0.2, v2.0.2 Legacy, v1.12.8, and v1.10.14. The file you linked to appears to have only one request in it; a request with an empty Referer header. The file does not have a request without a Referer header in it to test against. I used a different file to test if the filter would show requests without a Referer header. It did not. It only showed packets with an empty Referer header.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Apr '16, 18:02</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p>Jim Aragon<br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-51572" class="comments-container"></div><div id="comment-tools-51572" class="comment-tools"></div><div class="clear"></div><div id="comment-51572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

