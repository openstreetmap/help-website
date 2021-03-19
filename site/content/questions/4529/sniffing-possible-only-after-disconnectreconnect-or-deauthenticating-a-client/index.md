+++
type = "question"
title = "Sniffing possible only after disconnect/reconnect or deauthenticating a client"
description = '''Hi all, I&#x27;m just doing some expeiments at my own WLAN (it is encrypted with WPA-PSK and I know the passphrase), I&#x27;m trying to sniff some traffic with Wireshark (on Backtrack 5) with a usb device (linksys wusb54gc), I entered the passphrase in the Wireshark preferences and there are 2 clients connect...'''
date = "2011-06-12T13:33:00Z"
lastmod = "2011-06-13T11:28:00Z"
weight = 4529
keywords = [ "sniffing", "disconnect", "deauthentication", "reconnect" ]
aliases = [ "/questions/4529" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Sniffing possible only after disconnect/reconnect or deauthenticating a client](/questions/4529/sniffing-possible-only-after-disconnectreconnect-or-deauthenticating-a-client)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4529-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4529-score" class="post-score" title="current number of votes">0</div><span id="post-4529-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all, I'm just doing some expeiments at my own WLAN (it is encrypted with WPA-PSK and I know the passphrase), I'm trying to sniff some traffic with Wireshark (on Backtrack 5) with a usb device (linksys wusb54gc), I entered the passphrase in the Wireshark preferences and there are 2 clients connected to the net, (my laptop with its own wifi card and another laptop with its wifi card) but I realize that I can see traffic only after I disconnect/reconnect my laptop from the net (using windows) I'm trying to sniff and, similarly, I can see the other pc's traffic only when I send it a deauthentication packet with aireplay. The steps I perform are:</p><ul><li>airmon-ng start wlan0 8 (8 is the net channel)</li><li>run wireshark</li><li>start a new live capture</li></ul><p>If I don't perform any disconnection from the net (or send a deauth packet to the other client) I'm only able to see 802.11 traffic packets (encrypted), but if I disconnect/reconnect (from Windows), "magically" in wireshark I can see my traffic decyphered. I don't understand if this is a normal situation (but I believe not), I think the normal situation is just putting the interface in monitor mode and start capturing through wireshark. Can you help me please?</p><p>Thank you in advance,</p><p>Mark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-disconnect" rel="tag" title="see questions tagged &#39;disconnect&#39;">disconnect</span> <span class="post-tag tag-link-deauthentication" rel="tag" title="see questions tagged &#39;deauthentication&#39;">deauthentication</span> <span class="post-tag tag-link-reconnect" rel="tag" title="see questions tagged &#39;reconnect&#39;">reconnect</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Jun '11, 13:33</strong></p><img src="https://secure.gravatar.com/avatar/f2249566881a84857cc1e1746d712c4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Markus&#39;s gravatar image" /><p><span>Markus</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Markus has no accepted answers">0%</span></p></div></div><div id="comments-container-4529" class="comments-container"></div><div id="comment-tools-4529" class="comment-tools"></div><div class="clear"></div><div id="comment-4529-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="4539"></span>

<div id="answer-container-4539" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4539-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4539-score" class="post-score" title="current number of votes">1</div><span id="post-4539-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Markus has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, this is normal behavior for WPA-PSK. WPA-PSK uses the preshared key to negotiate a session key each time a client connects to the access point. This negotiation consists of 4 EAPOL packets. When these packets are in your tracefile for a pacticular client and wireshark has the PSK, then it can decrypt the negotiation and catch the session key to decrypt the traffic. If the 4 EAPOL packets are not in the trace (as you started capturing <strong>after</strong> the client connected to the AP) you are not able to decrypt the traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '11, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4539" class="comments-container"></div><div id="comment-tools-4539" class="comment-tools"></div><div class="clear"></div><div id="comment-4539-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="4541"></span>

<div id="answer-container-4541" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4541-score" class="post-score" title="current number of votes">0</div><span id="post-4541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you very much SYNbit, I fully understand, very useful! Thanks again!</p><p>Mark</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '11, 11:28</strong></p><img src="https://secure.gravatar.com/avatar/f2249566881a84857cc1e1746d712c4b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Markus&#39;s gravatar image" /><p><span>Markus</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Markus has no accepted answers">0%</span></p></div></div><div id="comments-container-4541" class="comments-container"></div><div id="comment-tools-4541" class="comment-tools"></div><div class="clear"></div><div id="comment-4541-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

