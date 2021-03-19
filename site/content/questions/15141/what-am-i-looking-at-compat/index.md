+++
type = "question"
title = "what am i looking at &amp; compat"
description = '''i was wondering if someone can clear up what these digits are. i can understand the traffic info in portion and i can read the information about send/recieve and addresses in portion but i have no idea what these values indicate: 0000 b8 e6 25 30 57 89 74 e5 43 9f 6d 16 08 06 00 01 ..%0W.t. C.m........'''
date = "2012-10-21T22:35:00Z"
lastmod = "2012-10-21T23:00:00Z"
weight = 15141
keywords = [ "info", "compatability", "packet" ]
aliases = [ "/questions/15141" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [what am i looking at & compat](/questions/15141/what-am-i-looking-at-compat)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15141-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15141-score" class="post-score" title="current number of votes">0</div><span id="post-15141-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i was wondering if someone can clear up what these digits are. i can understand the traffic info in portion and i can read the information about send/recieve and addresses in portion but i have no idea what these values indicate:</p><p>0000 b8 e6 25 30 57 89 74 e5 43 9f 6d 16 08 06 00 01 ..%0W.t. C.m.....</p><p>this line is followed by sequentially numbered lies 0010, 0020 and similar values across the board. I wouldmuch appreciate a crash course on that info.</p><p>Secondly I wondered if I could expect wireshark to continue to function once Windows 8 is released and to what degree. Thanks!!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-compatability" rel="tag" title="see questions tagged &#39;compatability&#39;">compatability</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '12, 22:35</strong></p><img src="https://secure.gravatar.com/avatar/733bcaeeaecee4ed9fa44a764922c4a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adnmance&#39;s gravatar image" /><p><span>adnmance</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adnmance has no accepted answers">0%</span></p></div></div><div id="comments-container-15141" class="comments-container"></div><div id="comment-tools-15141" class="comment-tools"></div><div class="clear"></div><div id="comment-15141-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15142"></span>

<div id="answer-container-15142" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15142-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15142-score" class="post-score" title="current number of votes">0</div><span id="post-15142-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark is all about interpreting the hex data for you. If you look in the packet detail pane you will see the different protocol layers of the packet. Assuming this was an ethernet-frame, you will see the ethernet and arp layer, as the hex data can be interpreted as:</p><pre><code>0000 -&gt; offset
b8 e6 25 30 57 89 -&gt; destination mac-address
74 e5 43 9f 6d 16 -&gt; source mac-address
08 06 -&gt; ethertype for ARP
00 01 -&gt; First bytes of the ARP protocol header

..%0W.t. C.m..... -&gt; ascii representation of the above bytes</code></pre><p>But again, that is what Wireshark does for you already :-)</p><p>Regarding windows 8 compatability, see <a href="https://ask.wireshark.org/questions/12956/install-on-windows-8-winpcap-issue">https://ask.wireshark.org/questions/12956/install-on-windows-8-winpcap-issue</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '12, 23:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-15142" class="comments-container"></div><div id="comment-tools-15142" class="comment-tools"></div><div class="clear"></div><div id="comment-15142-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

