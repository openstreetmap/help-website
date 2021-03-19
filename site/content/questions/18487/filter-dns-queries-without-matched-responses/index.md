+++
type = "question"
title = "Filter DNS queries without matched responses"
description = '''I receive seldom messages during stress test about timed out DNS requests from c-ares used in download manager as part of libcurl. I have huge pcap and need to identify such failed DNS queries. Is it possible with Wireshark&#x27;s expression language?'''
date = "2013-02-11T08:41:00Z"
lastmod = "2017-01-22T21:47:00Z"
weight = 18487
keywords = [ "dns" ]
aliases = [ "/questions/18487" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Filter DNS queries without matched responses](/questions/18487/filter-dns-queries-without-matched-responses)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18487-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18487-score" class="post-score" title="current number of votes">0</div><span id="post-18487-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I receive seldom messages during stress test about timed out DNS requests from c-ares used in download manager as part of libcurl. I have huge pcap and need to identify such failed DNS queries. Is it possible with Wireshark's expression language?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '13, 08:41</strong></p><img src="https://secure.gravatar.com/avatar/ebe0ccc07e8cd45d527cd0c7d743f740?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey%20Starodubtsev&#39;s gravatar image" /><p><span>Andrey Staro...</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey Starodubtsev has no accepted answers">0%</span></p></div></div><div id="comments-container-18487" class="comments-container"></div><div id="comment-tools-18487" class="comment-tools"></div><div class="clear"></div><div id="comment-18487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18498"></span>

<div id="answer-container-18498" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18498-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18498-score" class="post-score" title="current number of votes">3</div><span id="post-18498-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Andrey Starodubtsev has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Perhaps the following as a Wireshark display filter will work:</p><pre><code>dns &amp;&amp; (dns.flags.response == 0) &amp;&amp; ! dns.response_in</code></pre><p>(Hat tip to what I think was a recent ask.wireshark.org answer (that I can't find right now)).</p><p>You can also use <code>tshark -2 -R "dns &amp;&amp; (dns.flags.response == 0) &amp;&amp; ! dns.response_in" ...</code></p><p>(You may have to adjust the quoting depending upon the OS/shell you are using.</p><p>Update: A test using this filter with the latest 1.8 tshark seemed to sort of work. A DNS query without a response was found but, for some reason, the frame number was incorrect. (I.e. the frame found by wireshark using the filter was the same as that found by tshark, but tshark showed a different (incorrect) frame number).</p><p>I've filed <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8316">Bug #8316</a> at bugs.wireshark.org.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '13, 11:04</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Feb '13, 08:56</strong> </span></p></div></div><div id="comments-container-18498" class="comments-container"><span id="18502"></span><div id="comment-18502" class="comment"><div id="post-18502-score" class="comment-score"></div><div class="comment-text"><p>That's it, thank you!</p></div><div id="comment-18502-info" class="comment-info"><span class="comment-age">(11 Feb '13, 11:12)</span> <span class="comment-user userinfo">Andrey Staro...</span></div></div><span id="26892"></span><div id="comment-26892" class="comment"><div id="post-26892-score" class="comment-score"></div><div class="comment-text"><p>added <code>-i eth1</code> arg for listening on interface eth1, worked flawlessly, thank you.</p></div><div id="comment-26892-info" class="comment-info"><span class="comment-age">(12 Nov '13, 05:52)</span> <span class="comment-user userinfo">Mayura</span></div></div></div><div id="comment-tools-18498" class="comment-tools"></div><div class="clear"></div><div id="comment-18498-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58960"></span>

<div id="answer-container-58960" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-58960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-58960-score" class="post-score" title="current number of votes">0</div><span id="post-58960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To troubleshoot unsuccessful DNS query:</p><p>Browse to Domain Name System &gt; Flags, last line is the reply code, the 0 of which means no error. Others are listed down according to iana.org: <a href="http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml">http://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml</a></p><p>RCODE Name Description Reference 0 NoError No Error [RFC1035] 1 FormErr Format Error [RFC1035] 2 ServFail Server Failure [RFC1035] 3 NXDomain Non-Existent Domain [RFC1035] 4 NotImp Not Implemented [RFC1035] 5 Refused Query Refused [RFC1035] 6 YXDomain Name Exists when it should not [RFC2136][RFC6672] 7 YXRRSet RR Set Exists when it should not [RFC2136] 8 NXRRSet RR Set that should exist does not [RFC2136] 9 NotAuth Server Not Authoritative for zone [RFC2136] 9 NotAuth Not Authorized [RFC2845] 10 NotZone Name not contained in zone [RFC2136] 11-15 Unassigned<br />
16 BADVERS Bad OPT Version [RFC6891] 16 BADSIG TSIG Signature Failure [RFC2845] 17 BADKEY Key not recognized [RFC2845] 18 BADTIME Signature out of time window [RFC2845] 19 BADMODE Bad TKEY Mode [RFC2930] 20 BADNAME Duplicate key name [RFC2930] 21 BADALG Algorithm not supported [RFC2930] 22 BADTRUNC Bad Truncation [RFC4635] 23 BADCOOKIE Bad/missing Server Cookie [RFC7873] 24-3840 Unassigned<br />
3841-4095 Reserved for Private Use [RFC6895] 4096-65534 Unassigned<br />
65535 Reserved, can be allocated by Standards Action [RFC6895]</p><p>You can use the expression:</p><p>(!(dns.flags.rcode==0))&amp;&amp;(dns.flags.response==1)</p><p>-- !(dns.flags.rcode==0) means the reply code does not match "no error" -- dns.flags.response==1 means match all the query answer packet.</p><p>Test if this work, start Wireshark capture, open a command window, ping a non exist website, like ping www.gggoogeld.com. Then stop the capture, apply the expression in the display filter, see if the unsuccessful query been listed and only that is listed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '17, 21:47</strong></p><img src="https://secure.gravatar.com/avatar/8c7c45d5a392624fdc6eb0d1779d3abb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FrankTrunk&#39;s gravatar image" /><p><span>FrankTrunk</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FrankTrunk has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-58960" class="comments-container"></div><div id="comment-tools-58960" class="comment-tools"></div><div class="clear"></div><div id="comment-58960-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

