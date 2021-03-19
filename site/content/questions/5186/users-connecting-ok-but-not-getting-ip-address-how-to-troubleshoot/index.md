+++
type = "question"
title = "Users connecting OK, but not getting IP address: how to troubleshoot?"
description = '''On my network, users connect (a) wirelessly to their own combination bridge, router, and signal amplifier, then from there (b) wirelessly to my secure hardware. Some users can connect to my hardware, but don&#x27;t get an IP address from my DHCP server. Any suggestions on how to troubleshoot this with Wi...'''
date = "2011-07-23T17:53:00Z"
lastmod = "2011-07-24T08:51:00Z"
weight = 5186
keywords = [ "ip", "connection", "address" ]
aliases = [ "/questions/5186" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Users connecting OK, but not getting IP address: how to troubleshoot?](/questions/5186/users-connecting-ok-but-not-getting-ip-address-how-to-troubleshoot)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5186-score" class="post-score" title="current number of votes">0</div><span id="post-5186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On my network, users connect (a) wirelessly to their own combination bridge, router, and signal amplifier, then from there (b) wirelessly to my secure hardware. Some users can connect to my hardware, but don't get an IP address from my DHCP server. Any suggestions on how to troubleshoot this with Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Jul '11, 17:53</strong></p><img src="https://secure.gravatar.com/avatar/f218fd90d1a6784194e941ecf91bf166?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ThatAMan&#39;s gravatar image" /><p><span>ThatAMan</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ThatAMan has no accepted answers">0%</span></p></div></div><div id="comments-container-5186" class="comments-container"></div><div id="comment-tools-5186" class="comment-tools"></div><div class="clear"></div><div id="comment-5186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5187"></span>

<div id="answer-container-5187" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5187-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5187-score" class="post-score" title="current number of votes">0</div><span id="post-5187-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can run Wireshark on a mirroring port close to your DHCP server to see whether the DHCP requests from the clients get to the DHCP server. If they do, you should then look if the DHCP server responds (if not, maybe it ran out of addresses to hand out.</p><p>Depending on the outcome of this first check, you may want to run Wireshark near the Access Point to see whether the DHCP requests and responses are seen there.</p><p>For help on how to setup things in order for Wireshark to be able to see the traffic, have a look at <a href="http://wiki.wireshark.org/CaptureSetup">http://wiki.wireshark.org/CaptureSetup</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '11, 23:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-5187" class="comments-container"><span id="5192"></span><div id="comment-5192" class="comment"><div id="post-5192-score" class="comment-score"></div><div class="comment-text"><p>A thousand thanks, SYNbit! You know your stuff! Another question: How do I troubleshoot this from the client side?</p></div><div id="comment-5192-info" class="comment-info"><span class="comment-age">(24 Jul '11, 08:51)</span> <span class="comment-user userinfo">ThatAMan</span></div></div></div><div id="comment-tools-5187" class="comment-tools"></div><div class="clear"></div><div id="comment-5187-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

