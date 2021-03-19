+++
type = "question"
title = "what could be the possible reasons for rapid DNS requests on the same hostname"
description = '''In a malware pcap file, saw a client keep doing DNS requests on the same hostname, wonder what could be happening? Any theories? Here is the pcap: https://www.dropbox.com/s/3a43pp28t067lyy/consecutiveDnsReqs.pcap?dl=0 '''
date = "2016-05-02T10:08:00Z"
lastmod = "2016-05-02T11:27:00Z"
weight = 52156
keywords = [ "wireshark" ]
aliases = [ "/questions/52156" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [what could be the possible reasons for rapid DNS requests on the same hostname](/questions/52156/what-could-be-the-possible-reasons-for-rapid-dns-requests-on-the-same-hostname)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52156-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52156-score" class="post-score" title="current number of votes">0</div><span id="post-52156-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In a malware pcap file, saw a client keep doing DNS requests on the same hostname, wonder what could be happening? Any theories?</p><p>Here is the pcap: <a href="https://www.dropbox.com/s/3a43pp28t067lyy/consecutiveDnsReqs.pcap?dl=0">https://www.dropbox.com/s/3a43pp28t067lyy/consecutiveDnsReqs.pcap?dl=0</a></p><p><img src="https://osqa-ask.wireshark.org/upfiles/2b_mLNzTEJ.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 May '16, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/7bb7310612573625abd07a67f22724ad?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pktUser1001&#39;s gravatar image" /><p><span>pktUser1001</span><br />
<span class="score" title="201 reputation points">201</span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pktUser1001 has one accepted answer">12%</span></p></img></div></div><div id="comments-container-52156" class="comments-container"></div><div id="comment-tools-52156" class="comment-tools"></div><div class="clear"></div><div id="comment-52156-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="52157"></span>

<div id="answer-container-52157" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52157-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52157-score" class="post-score" title="current number of votes">0</div><span id="post-52157-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="pktUser1001 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Most likely caused by a program that doesn't cache results, or which is simply coded to check for this name all the time (for whatever reason, but it ain't for stealth).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 May '16, 11:00</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-52157" class="comments-container"><span id="52158"></span><div id="comment-52158" class="comment"><div id="post-52158-score" class="comment-score"></div><div class="comment-text"><p>That's possible, but my problem is why the client didn't do anything (for example, start a new TCP connection) after getting the DNS response, instead it immediately sent the same DNS request.</p></div><div id="comment-52158-info" class="comment-info"><span class="comment-age">(02 May '16, 11:18)</span> <span class="comment-user userinfo">pktUser1001</span></div></div><span id="52159"></span><div id="comment-52159" class="comment"><div id="post-52159-score" class="comment-score"></div><div class="comment-text"><p>Maybe the DNS reply is a signal and the malware will only communicate when a certain IP is returned. This sometimes happens to avoid putting suspicious TCP/UDP traffic on the internet link when there's nothing the C&amp;C servers want to tell their bots. Mostly they return loopback IPs for those DNS queries, though (or used to), but loopback answers are suspicious enough on their own.</p><p>In the end, you can't tell without reverse engineering the binary that did the name lookups.</p><p>Again, asking for the same thing in such a quick way is stupid.</p></div><div id="comment-52159-info" class="comment-info"><span class="comment-age">(02 May '16, 11:27)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-52157" class="comment-tools"></div><div class="clear"></div><div id="comment-52157-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

