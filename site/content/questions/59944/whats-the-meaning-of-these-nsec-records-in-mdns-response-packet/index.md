+++
type = "question"
title = "what&#x27;s the meaning of these NSEC records in mDNS response packet?"
description = '''I got a mDNS response like this, can&#x27;t understand the NSEC records in additional records section. According to rfc 6762, NSEC record in the Additional Section indicates nonexistence of record, but in the Answers Section, it does exist. So what does this mean? Multicast Domain Name System (response) ...'''
date = "2017-03-08T21:40:00Z"
lastmod = "2017-03-09T17:48:00Z"
weight = 59944
keywords = [ "mdns", "multicast", "dns" ]
aliases = [ "/questions/59944" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [what's the meaning of these NSEC records in mDNS response packet?](/questions/59944/whats-the-meaning-of-these-nsec-records-in-mdns-response-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59944-score" class="post-score" title="current number of votes">0</div><span id="post-59944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I got a mDNS response like this, can't understand the NSEC records in additional records section. According to rfc 6762, NSEC record in the Additional Section indicates nonexistence of record, but in the Answers Section, it does exist. So what does this mean?</p><pre><code>Multicast Domain Name System (response)
    Transaction ID: 0x0000
    Flags: 0x8400 Standard query response, No error
    Questions: 0
    Answer RRs: 2
    Authority RRs: 0
    Additional RRs: 3
    Answers
        6.2.9.E.3.F.4.E.9.6.9.3.D.6.0.1.0.0.0.0.0.0.0.0.0.0.0.0.0.8.E.F.ip6.arpa: type PTR, class IN, cache flush, R-er.local
        104.1.168.192.in-addr.arpa: type PTR, class IN, cache flush, R-er.local
            Name: 104.1.168.192.in-addr.arpa
            Type: PTR (domain name PoinTeR) (12)
            .000 0000 0000 0001 = Class: IN (0x0001)
            1... .... .... .... = Cache flush: True
            Time to live: 120
            Data length: 2
            Domain Name: R-er.local
    Additional records
        6.2.9.E.3.F.4.E.9.6.9.3.D.6.0.1.0.0.0.0.0.0.0.0.0.0.0.0.0.8.E.F.ip6.arpa: type NSEC, class IN, cache flush, next domain name 6.2.9.E.3.F.4.E.9.6.9.3.D.6.0.1.0.0.0.0.0.0.0.0.0.0.0.0.0.8.E.F.ip6.arpa
        104.1.168.192.in-addr.arpa: type NSEC, class IN, cache flush, next domain name 104.1.168.192.in-addr.arpa
            Name: 104.1.168.192.in-addr.arpa
            Type: NSEC (47)
            .000 0000 0000 0001 = Class: IN (0x0001)
            1... .... .... .... = Cache flush: True
            Time to live: 120
            Data length: 6
            Next Domain Name: 104.1.168.192.in-addr.arpa
            RR type in bit map: PTR (domain name PoinTeR)
        &lt;Root&gt;: type OPT</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mdns" rel="tag" title="see questions tagged &#39;mdns&#39;">mdns</span> <span class="post-tag tag-link-multicast" rel="tag" title="see questions tagged &#39;multicast&#39;">multicast</span> <span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Mar '17, 21:40</strong></p><img src="https://secure.gravatar.com/avatar/75de90cd2dddc1467b3f3db8d49dfb30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jfly&#39;s gravatar image" /><p><span>jfly</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jfly has no accepted answers">0%</span></p></div></div><div id="comments-container-59944" class="comments-container"></div><div id="comment-tools-59944" class="comment-tools"></div><div class="clear"></div><div id="comment-59944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59972"></span>

<div id="answer-container-59972" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59972-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59972-score" class="post-score" title="current number of votes">2</div><span id="post-59972-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jfly has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello jfly</p><p>It looks like the mDNS responder has implemented an option from RFC6762:</p><pre><code>   On receipt of a question for a particular name, rrtype, and rrclass,
   for which a responder does have one or more unique answers, the
   responder MAY also include an NSEC record in the Additional Record
   Section indicating the nonexistence of other rrtypes for that name
   and rrclass.</code></pre><p>Since the mDNS message holds two responses, the additional NSEC record informs the client, that there are no further responses available.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '17, 13:50</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-59972" class="comments-container"><span id="59974"></span><div id="comment-59974" class="comment"><div id="post-59974-score" class="comment-score"></div><div class="comment-text"><p>Thanks! I miss this while reading rfc.</p></div><div id="comment-59974-info" class="comment-info"><span class="comment-age">(09 Mar '17, 17:48)</span> <span class="comment-user userinfo">jfly</span></div></div></div><div id="comment-tools-59972" class="comment-tools"></div><div class="clear"></div><div id="comment-59972-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

