+++
type = "question"
title = "Help understanding DNS packet data"
description = '''Hello all, I am going through my DNS data and I keep seeing some odd Hex values within the query. I&#x27;m new to all of this so I am hoping someone can help me figure out what it means, what it&#x27;s used for and that purpose it has within the DNS packet data.  When I run a dump on port 53 I am seeing a bun...'''
date = "2016-03-10T12:52:00Z"
lastmod = "2016-03-21T09:52:00Z"
weight = 50806
keywords = [ "dnsquery" ]
aliases = [ "/questions/50806" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help understanding DNS packet data](/questions/50806/help-understanding-dns-packet-data)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50806-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50806-score" class="post-score" title="current number of votes">0</div><span id="post-50806-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I am going through my DNS data and I keep seeing some odd Hex values within the query. I'm new to all of this so I am hoping someone can help me figure out what it means, what it's used for and that purpose it has within the DNS packet data.<br />
</p><p>When I run a dump on port 53 I am seeing a bunch of queries with values within brackets [ ] for example:</p><pre><code>[C00C](3)www(6)google(3)com(0)</code></pre><p>Here is another example with part of the payload - see the [C00C] shows up again below in the ANSWER section. I'm also seeing a few other Hex values within the brackets [ ] but not sure what they are for or how they are used. Any help understanding would be greatly appreciated.</p><pre><code>ANSWER SECTION:
Offset = 0x0030, RR count = 0
Name      &quot;[C00C](14)5-01-2cd3-001f(3)lex(6)google(3)com(0)&quot;
  TYPE   CNAME  (5)
  CLASS  1
  TTL    14
  DLEN   30
  DATA</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dnsquery" rel="tag" title="see questions tagged &#39;dnsquery&#39;">dnsquery</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Mar '16, 12:52</strong></p><img src="https://secure.gravatar.com/avatar/8e28cea791864f402c6aa62b2b4f417a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mike_vu&#39;s gravatar image" /><p><span>mike_vu</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mike_vu has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-50806" class="comments-container"></div><div id="comment-tools-50806" class="comment-tools"></div><div class="clear"></div><div id="comment-50806-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50807"></span>

<div id="answer-container-50807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50807-score" class="post-score" title="current number of votes">2</div><span id="post-50807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>What tool are you using to view the packet data? That doesn't look like a Wireshark display. Nevertheless:</p><p>Domain names in a DNS packet are encoded. "www.google.com" for example, is actually stored in the packet as "3www6novell3com0". It's the number of characters followed by the characters and the whole thing terminated by zero.</p><p>The domain name that is in the query portion of the packet is repeated in the answer portion. However, instead of repeating the whole domain name, only a pointer to the first occurrence of the name is stored in the packet. C00C is the hex value of the pointer. The first two bits are 1's, which indicates that it is a pointer, and the remaining bits are the actual value of the pointer.</p><p>C00C in binary is 11000000 00001100. The first two bits indicate that it is a pointer. The remaining bits (000000 00001100) are the actual value of the pointer. The equivalent decimal value is 12. Start at the very first field in the DNS portion of the packet, which is the transaction ID, and count down 12 bytes. That will take you right to the first occurrence of the name, the one that is in the query portion of the packet.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '16, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-50807" class="comments-container"><span id="50811"></span><div id="comment-50811" class="comment"><div id="post-50811-score" class="comment-score"></div><div class="comment-text"><p>If you're curious about the gory details, see sections 3.1 "Name space definitions" and 4.1.4 "Message compression" of <a href="http://tools.ietf.org/html/rfc1035">RFC 1035</a>, "DOMAIN NAMES - IMPLEMENTATION AND SPECIFICATION".</p></div><div id="comment-50811-info" class="comment-info"><span class="comment-age">(10 Mar '16, 17:06)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="51067"></span><div id="comment-51067" class="comment"><div id="post-51067-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that was a great explanation.<br />
</p></div><div id="comment-51067-info" class="comment-info"><span class="comment-age">(21 Mar '16, 08:43)</span> <span class="comment-user userinfo">mike_vu</span></div></div><span id="51070"></span><div id="comment-51070" class="comment"><div id="post-51070-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-51070-info" class="comment-info"><span class="comment-age">(21 Mar '16, 09:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-50807" class="comment-tools"></div><div class="clear"></div><div id="comment-50807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

