+++
type = "question"
title = "Identify an unknown ip address on a different network"
description = '''I have found this IP address and I was wondering is there a way I can arp the IP address to find its Mac address? The IP address is on a different network, but I still want to be able to find it&#x27;s mac address. Please help as I am new to wireshark.'''
date = "2016-06-03T13:00:00Z"
lastmod = "2016-06-06T13:13:00Z"
weight = 53186
keywords = [ "arp", "unknownipaddress", "ipaddress", "mac-address", "location" ]
aliases = [ "/questions/53186" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Identify an unknown ip address on a different network](/questions/53186/identify-an-unknown-ip-address-on-a-different-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53186-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53186-score" class="post-score" title="current number of votes">0</div><span id="post-53186-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have found this IP address and I was wondering is there a way I can arp the IP address to find its Mac address? The IP address is on a different network, but I still want to be able to find it's mac address. Please help as I am new to wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-arp" rel="tag" title="see questions tagged &#39;arp&#39;">arp</span> <span class="post-tag tag-link-unknownipaddress" rel="tag" title="see questions tagged &#39;unknownipaddress&#39;">unknownipaddress</span> <span class="post-tag tag-link-ipaddress" rel="tag" title="see questions tagged &#39;ipaddress&#39;">ipaddress</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span> <span class="post-tag tag-link-location" rel="tag" title="see questions tagged &#39;location&#39;">location</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '16, 13:00</strong></p><img src="https://secure.gravatar.com/avatar/ab6e6cb4fe847f7280ef0312b875fe69?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lucy&#39;s gravatar image" /><p><span>Lucy</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lucy has no accepted answers">0%</span></p></div></div><div id="comments-container-53186" class="comments-container"></div><div id="comment-tools-53186" class="comment-tools"></div><div class="clear"></div><div id="comment-53186-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53252"></span>

<div id="answer-container-53252" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-53252-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-53252-score" class="post-score" title="current number of votes">0</div><span id="post-53252-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>MAC Addresses are unique, but meaningful locally within a broadcast domain, so you will need access to a device within the same broadcast domain.</p><p>If the device is not on your network, why do you need the MAC? If it's to help someone on that network, have them try to ping it, then run look at their ARP cache (arp -a).</p><p>If you have admin privileges on a remote windows PC and you are on a Windows 7 or higher PC, you can also run getmac /s computername and get back the MAC address.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Jun '16, 13:13</strong></p><img src="https://secure.gravatar.com/avatar/3f2f87a6a68e4c51c3851c20b6c56a1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CMH_Tim&#39;s gravatar image" /><p><span>CMH_Tim</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CMH_Tim has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jun '16, 13:14</strong> </span></p></div></div><div id="comments-container-53252" class="comments-container"></div><div id="comment-tools-53252" class="comment-tools"></div><div class="clear"></div><div id="comment-53252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

