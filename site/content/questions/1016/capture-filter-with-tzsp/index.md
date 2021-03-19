+++
type = "question"
title = "Capture Filter with TZSP"
description = '''Hi Wiresharkers! I am streaming TZSP from my router to my wireshark server, the problem happens when I set the capture filter, it sees the src ip of the router only, I want to filter according to the host ip which is encapsulated within the TZSP packet. any ideas please Mike'''
date = "2010-11-18T14:28:00Z"
lastmod = "2010-11-20T03:49:00Z"
weight = 1016
keywords = [ "tzsp" ]
aliases = [ "/questions/1016" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Capture Filter with TZSP](/questions/1016/capture-filter-with-tzsp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1016-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Wiresharkers!</p><p>I am streaming TZSP from my router to my wireshark server, the problem happens when I set the capture filter, it sees the src ip of the router only, I want to filter according to the host ip which is encapsulated within the TZSP packet.</p><p>any ideas please</p><p>Mike</p></div><div id="question-tags" class="tags-container tags">tzsp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Nov '10, 14:28</strong></p><img src="https://secure.gravatar.com/avatar/f45520ae40c6385a788dde258e149223?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike&#39;s gravatar image" /><p>Mike<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike has no accepted answers">0%</span></p></div></div><div id="comments-container-1016" class="comments-container"></div><div id="comment-tools-1016" class="comment-tools"></div><div class="clear"></div><div id="comment-1016-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1034"></span>

<div id="answer-container-1034" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1034-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I have no tracefile to work with, but I expect something like <code>"udp[xx:4]==0xYYYYYY"</code> would do the trick. Can you upload a sample capture somewhere (<a href="http://www.pcapr.net/home">www.pcapr.net</a> or <a href="http://www.cloudshark.org/">www.cloudshark.org</a> for example)?</p><p>UPDATE: I took a look at <a href="http://en.wikipedia.org/wiki/TZSP">Wikipedia</a> and I see that TSZP is using variable length fields <em>before</em> the encapsulated data. That makes the approach from above useless, <em>unless</em> every packet in your stream has the same TZSP header length.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Nov '10, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Nov '10, 03:53</p></div></div><div id="comments-container-1034" class="comments-container"><span id="1035"></span><div id="comment-1035" class="comment"><div id="post-1035-score" class="comment-score"></div><div class="comment-text"><p>Can I filter based on some html code inside the original packet?</p><p>I found the following filter that captures packets with "get" html script:</p><p>port 80 and tcp[((tcp[12:1] &amp; 0xf0) &gt;&gt; 2):4] = 0x47455420</p><p>it works, but when I apply the same for TZSP encapsolated packet it fails</p><p>Any ideas</p><p>Mike</p></div><div id="comment-1035-info" class="comment-info"><span class="comment-age">(20 Nov '10, 04:20)</span> Mike</div></div><span id="1036"></span><div id="comment-1036" class="comment"><div id="post-1036-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a comment to my answer, that more in line with the nature of this Q&amp;A site.</p><p>Your filter works for unencapsulated packets. The TSZP adds a new IP and UDP header before the packets to forward them to the capturing host. This messes up the indices into the packets where the IP header or HTTP request method can be found.</p><p>We need to determine if all packets have the length for the uncapsulating header and if so, how many bytes we need to skip. Can you post a sample capture? Or mail it to me (address is on my user-profile)?</p></div><div id="comment-1036-info" class="comment-info"><span class="comment-age">(20 Nov '10, 04:25)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1034" class="comment-tools"></div><div class="clear"></div><div id="comment-1034-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

