+++
type = "question"
title = "Tshark, missing answer domain name in display filter for PTR records"
description = '''OS: Ubuntu 10.04.4 LTS Tshark: 1.2.7 I&#x27;m trying to sniff all DNS traffic and output queries and answers to a text file for parsing. All queries for &#x27;A&#x27; records return the needed information: response name, address and ttl. Queries for PTR records do not display all fields (the fields dns.resp.addr, ...'''
date = "2012-11-21T09:21:00Z"
lastmod = "2012-11-21T10:28:00Z"
weight = 16167
keywords = [ "ptr", "dns", "tshark" ]
aliases = [ "/questions/16167" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Tshark, missing answer domain name in display filter for PTR records](/questions/16167/tshark-missing-answer-domain-name-in-display-filter-for-ptr-records)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16167-score" class="post-score" title="current number of votes">0</div><span id="post-16167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>OS: Ubuntu 10.04.4 LTS Tshark: 1.2.7</p><p>I'm trying to sniff all DNS traffic and output queries and answers to a text file for parsing. All queries for 'A' records return the needed information: response name, address and ttl. Queries for PTR records do not display all fields (the fields dns.resp.addr, dns.resp.name, and dns.resp.primaryname return no values).</p><p>What can be done to output the info to a text file? Specifying fields with Tshark is great but missing the domain name returned from the PTR query is odd. An oversight/bug?</p><p>Any help is appreciated.</p><p>---OUTPUT---</p><p>sudo tshark -n -s0 -i eth4 port 53<br />
0.000000 [host] -&gt; [dnsSRV] DNS Standard query A <a href="http://wireshark.com">wireshark.com</a><br />
0.000508 [dnsSRV] -&gt; [host] DNS Standard query response A 184.172.141.116<br />
2.868755 [host] -&gt; [dnsSRV] DNS Standard query PTR <a href="http://116.141.172.184.in-addr.arpa">116.141.172.184.in-addr.arpa</a><br />
2.869270 [dnsSRV] -&gt; [host] DNS Standard query response PTR <a href="http://wir.wireshark.com">wir.wireshark.com</a><br />
</p><p>sudo tshark -n -s0 -i eth4 port 53 -T fields -E separator=\, -e frame.time -e ip.src -e ip.dst -e dns.qry.name -e dns.resp.name -e dns.resp.addr -e dns.resp.ttl<br />
Nov 21, 2012 17:05:29.113891000,[host],[dnsSRV],<a href="http://wireshark.com">wireshark.com</a>,,,<br />
Nov 21, 2012 17:05:29.114397000,[dnsSRV],[host],<a href="http://wireshark.com">wireshark.com</a>,<a href="http://wireshark.com">wireshark.com</a>,,4632<br />
Nov 21, 2012 17:05:45.270631000,[host],[dnsSRV],<a href="http://116.141.172.184.in-addr.arpa">116.141.172.184.in-addr.arpa</a>,,,<br />
Nov 21, 2012 17:05:45.271134000,[dnsSRV],[host],<a href="http://116.141.172.184.in-addr.arpa">116.141.172.184.in-addr.arpa</a>,<a href="http://116.141.172.184.in-addr.arpa">116.141.172.184.in-addr.arpa</a>,,12039<br />
</p><p>---ADDITION---<br />
It also appears that this is failing for 'A' records (see above). The 'A' record dns.resp.addr is populated correctly with Tshark1.6.7 running on Ubuntu12.04.1LTS but 'PTR' records still do not show the dns.resp.addr or dns.resp.name fields (interesting).</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ptr" rel="tag" title="see questions tagged &#39;ptr&#39;">ptr</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '12, 09:21</strong></p><img src="https://secure.gravatar.com/avatar/5d768cc77fa0cef79231c2374bb8ab00?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twhisnant&#39;s gravatar image" /><p><span>twhisnant</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twhisnant has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '12, 09:34</strong> </span></p></div></div><div id="comments-container-16167" class="comments-container"></div><div id="comment-tools-16167" class="comment-tools"></div><div class="clear"></div><div id="comment-16167-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16172"></span>

<div id="answer-container-16172" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16172-score" class="post-score" title="current number of votes">0</div><span id="post-16172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no filter for the PTR response in the current release.</p><p>You can run tshark with option -V and then parse the full output of the DNS response.</p><blockquote><p><code>tshark -r input.cap -V</code><br />
</p></blockquote><p>or parse the 'text' field of the DNS responses.</p><blockquote><p><code>tshark -r input.cap -R "dns.resp.len" -T fields -e text</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '12, 10:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Nov '12, 10:35</strong> </span></p></div></div><div id="comments-container-16172" class="comments-container"></div><div id="comment-tools-16172" class="comment-tools"></div><div class="clear"></div><div id="comment-16172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

