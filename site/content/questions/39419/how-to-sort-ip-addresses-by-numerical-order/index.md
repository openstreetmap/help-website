+++
type = "question"
title = "How to sort IP addresses by numerical order?"
description = '''I want to sort IP addresses so that in ascending order, I get 10.0.0.1, 10.0.0.2, 10.0.0.3, etc. Currently wireshark sorts by default to lexicographical order, i.e 10.0.0.1, 10.0.0.11, 10.0.0.12, 10.0.0.2, etc. Is this possible in wireshark currently? Google and poking around in preferences yielded ...'''
date = "2015-01-26T18:43:00Z"
lastmod = "2015-01-31T13:57:00Z"
weight = 39419
keywords = [ "ordering", "ip", "sorting" ]
aliases = [ "/questions/39419" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to sort IP addresses by numerical order?](/questions/39419/how-to-sort-ip-addresses-by-numerical-order)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39419-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to sort IP addresses so that in ascending order, I get 10.0.0.1, 10.0.0.2, 10.0.0.3, etc.</p><p>Currently wireshark sorts by default to lexicographical order, i.e 10.0.0.1, 10.0.0.11, 10.0.0.12, 10.0.0.2, etc.</p><p>Is this possible in wireshark currently? Google and poking around in preferences yielded nothing.</p><p>Currently using wireshark 1.10.6.</p></div><div id="question-tags" class="tags-container tags">ordering ip sorting</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Jan '15, 18:43</strong></p><img src="https://secure.gravatar.com/avatar/f94457aed80c398e4355dd7d2f69a780?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fruglemonkey&#39;s gravatar image" /><p>fruglemonkey<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fruglemonkey has no accepted answers">0%</span></p></div></div><div id="comments-container-39419" class="comments-container"></div><div id="comment-tools-39419" class="comment-tools"></div><div class="clear"></div><div id="comment-39419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39525"></span>

<div id="answer-container-39525" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39525-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>You can script this with <a href="https://www.wireshark.org/docs/man-pages/tshark.html"><code>tshark</code></a> and <a href="http://man7.org/linux/man-pages/man1/sort.1.html"><code>sort</code></a>. For example:</p><pre><code>tshark -r file.pcap -T fields -e ip.src | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4</code></pre><p>EDIT: Using <em>"Statistics -&gt; Endpoint List -&gt; IPv4"</em> or <em>"Statistics -&gt; Endpoints -&gt; IPv4"</em> works as expected, but the behavior is wrong when sorting by the Packet Details "Source" or "Destination" IP address columns. You may want to <a href="https://bugs.wireshark.org/bugzilla/">open a bug report</a> for that incorrect sort behavior.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Jan '15, 13:57</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Feb '15, 09:42</p></div></div><div id="comments-container-39525" class="comments-container"></div><div id="comment-tools-39525" class="comment-tools"></div><div class="clear"></div><div id="comment-39525-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

