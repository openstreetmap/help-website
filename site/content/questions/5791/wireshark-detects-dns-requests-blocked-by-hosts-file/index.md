+++
type = "question"
title = "Wireshark Detects DNS Requests Blocked by Hosts File"
description = '''I have Wireshark running on Windows 7 x64. I created a Hosts file that maps specific domains to 127.0.0.1. I then &#x27;ping&#x27;-ed each domain to make sure it returned 127.0.0.1. Nevertheless, Wireshark is capturing DNS requests and responses from my ISP&#x27;s DNS server for these domains. How is that possible...'''
date = "2011-08-21T21:24:00Z"
lastmod = "2011-08-24T08:31:00Z"
weight = 5791
keywords = [ "hosts", "dns" ]
aliases = [ "/questions/5791" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Detects DNS Requests Blocked by Hosts File](/questions/5791/wireshark-detects-dns-requests-blocked-by-hosts-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5791-score" class="post-score" title="current number of votes">0</div><span id="post-5791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have Wireshark running on Windows 7 x64. I created a Hosts file that maps specific domains to 127.0.0.1. I then 'ping'-ed each domain to make sure it returned 127.0.0.1. Nevertheless, Wireshark is capturing DNS requests and responses from my ISP's DNS server for these domains. How is that possible?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-hosts" rel="tag" title="see questions tagged &#39;hosts&#39;">hosts</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '11, 21:24</strong></p><img src="https://secure.gravatar.com/avatar/9c3cf8b5d86f53e2413356c53daece54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Farmisht&#39;s gravatar image" /><p><span>Farmisht</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Farmisht has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Aug '11, 21:53</strong> </span></p></div></div><div id="comments-container-5791" class="comments-container"></div><div id="comment-tools-5791" class="comment-tools"></div><div class="clear"></div><div id="comment-5791-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="5793"></span>

<div id="answer-container-5793" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5793-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5793-score" class="post-score" title="current number of votes">0</div><span id="post-5793-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you see forward or reverse DNS lookups to your ISP's DNS server? Wireshark itself will do reverse DNS lookups unless you explicitly tell it not to by disabling name resolution.</p><p>You can disable name resolution in Wireshark by going to "View -&gt; Name Resolution" and then uncheck "Enable for Network layer".</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Aug '11, 22:36</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5793" class="comments-container"><span id="5795"></span><div id="comment-5795" class="comment"><div id="post-5795-score" class="comment-score"></div><div class="comment-text"><p>In particular, Wireshark, if built with <a href="http://www.gnu.org/s/adns/">adns</a> or <a href="http://c-ares.haxx.se/">c-ares</a>, will itself do reverse DNS lookups <em>without going through the operating system's own host name/host address lookup code</em>, so it might not pay attention to your hosts file.</p></div><div id="comment-5795-info" class="comment-info"><span class="comment-age">(21 Aug '11, 22:50)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="5816"></span><div id="comment-5816" class="comment"><div id="post-5816-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help. Wireshark is recording Type A (Host Address) queries, which I believe are forward lookups.</p><p>Something suspicious is going on. It's always the same hostnames being queried, and they are queried in a specific order. Each hostname used to be queried thousands of times every day, until I added these domains to my hosts file. Now there are drastically fewer queries, but there should be none at all. Every malware scanner I've tried says I'm clean, but I'm not convinced of that.</p></div><div id="comment-5816-info" class="comment-info"><span class="comment-age">(22 Aug '11, 20:35)</span> <span class="comment-user userinfo">Farmisht</span></div></div><span id="5817"></span><div id="comment-5817" class="comment"><div id="post-5817-score" class="comment-score"></div><div class="comment-text"><p>The type A lookups that you still see, are they for fully qualified domain names that are also present in the hosts file? Is there a relation between the type A lookups and the domain search list that you have configured in your DNS settings?</p></div><div id="comment-5817-info" class="comment-info"><span class="comment-age">(22 Aug '11, 22:15)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-5793" class="comment-tools"></div><div class="clear"></div><div id="comment-5793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5844"></span>

<div id="answer-container-5844" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5844-score" class="post-score" title="current number of votes">0</div><span id="post-5844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I am seeing requests for FQDNs that are also in the hosts file, and these domains are being queried in numerical order every time. I truly appreciate your help, however, despite what the malware scanners say, I strongly suspect that I am bot-ted. There were over 153,000 DNS lookups yesterday alone, and I am losing my internet connection frequently (which I believe is my ISP's response to all this.). I have asked for help from the good folks at Bleeping Computer, and may have to format if I can't stay on the internet long enough to benefit from their advice.</p><p>EDIT: My ISP has assured me that they would not interfere with my internet connection without contacting me. I still believe my computer is compromised. I was able to use my router to block outbound access to the domains in question, and that apparently is working.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Aug '11, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/9c3cf8b5d86f53e2413356c53daece54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Farmisht&#39;s gravatar image" /><p><span>Farmisht</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Farmisht has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Aug '11, 19:05</strong> </span></p></div></div><div id="comments-container-5844" class="comments-container"></div><div id="comment-tools-5844" class="comment-tools"></div><div class="clear"></div><div id="comment-5844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

