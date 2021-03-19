+++
type = "question"
title = "How can you tell if a DNS Response has the Message compressed in Wireshark?"
description = '''DNS Experts, How can you tell by looking at the DNS Response, if the response message was compressed? Example: http://pastebin.com/taF8kDui Showing Response 1 with message compression and Response 2 without Message compression Diff https://www.diffchecker.com/zjmrf8xi Thank you PPcap'''
date = "2015-12-21T08:35:00Z"
lastmod = "2015-12-21T15:31:00Z"
weight = 48663
keywords = [ "dns" ]
aliases = [ "/questions/48663" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How can you tell if a DNS Response has the Message compressed in Wireshark?](/questions/48663/how-can-you-tell-if-a-dns-response-has-the-message-compressed-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48663-score" class="post-score" title="current number of votes">0</div><span id="post-48663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>DNS Experts,</p><p>How can you tell by looking at the DNS Response, if the response message was compressed?</p><p>Example: <a href="http://pastebin.com/taF8kDui">http://pastebin.com/taF8kDui</a></p><p>Showing Response 1 with message compression and Response 2 without Message compression</p><p>Diff <a href="https://www.diffchecker.com/zjmrf8xi">https://www.diffchecker.com/zjmrf8xi</a></p><p>Thank you PPcap</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dns" rel="tag" title="see questions tagged &#39;dns&#39;">dns</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Dec '15, 08:35</strong></p><img src="https://secure.gravatar.com/avatar/5002cb544de33c526f994599d3ae391f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ppcap&#39;s gravatar image" /><p><span>ppcap</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ppcap has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Dec '15, 08:41</strong> </span></p></div></div><div id="comments-container-48663" class="comments-container"></div><div id="comment-tools-48663" class="comment-tools"></div><div class="clear"></div><div id="comment-48663-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48665"></span>

<div id="answer-container-48665" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48665-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48665-score" class="post-score" title="current number of votes">1</div><span id="post-48665-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="ppcap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>When a domain name appears in a DNS packet more than once and DNS compression is in use, the second and subsequent appearances of the domain name can be replaced by a pointer to the earlier occurrence of the name. The name isn't actually compressed, it's removed altogether and replaced by the pointer.</p><p>Normal DNS encoding separates the domain name into "labels" (the parts separated by periods) and encodes the name by listing the number of characters in each label, followed by the actual characters, with the whole thing terminated with zero. So "www.google.com" would be encoded as as "3www6google3com0".</p><p>When a pointer is used instead of the literal domain name, the pointer will be only two bytes. The first two bits of the first byte will be "11" which indicates that it is a pointer, not a literal domain name. The remaining bits are the actual value of the pointer, as an offset from the beginning of the DNS portion of the packet, which is normally the transaction ID.</p><p>There is no flag in the DNS packet that will tell you that DNS compression was used. Instead, you'll simply have to highlight each domain name in the packet in the Packet Details pane and then look in the Packet Bytes pane to see whethher you see the literal domain name or if you see a two-byte pointer.</p><p>See <a href="http://www.ccs.neu.edu/home/amislove/teaching/cs4700/fall09/handouts/project1-primer.pdf">this link</a> for a reasonably concise explanation of how domain names can be represented in a DNS packet. Scroll down to section 5 "DNS Packet Compression."</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Dec '15, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-48665" class="comments-container"></div><div id="comment-tools-48665" class="comment-tools"></div><div class="clear"></div><div id="comment-48665-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

