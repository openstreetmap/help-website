+++
type = "question"
title = "Wireshark keeps giving a 0 for length."
description = '''Hello. I am analyzing virus through Virtualbox, and am using Wireshark in my real computer (mac) to monitor all of the network connections it makes. I have gotten a lot of network activity from the virus, showing me the IP that it is communicating to, the network protocol that it is using, etc. I al...'''
date = "2012-10-09T22:29:00Z"
lastmod = "2012-10-17T11:08:00Z"
weight = 14850
keywords = [ "follow", "length", "tcp" ]
aliases = [ "/questions/14850" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark keeps giving a 0 for length.](/questions/14850/wireshark-keeps-giving-a-0-for-length)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14850-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14850-score" class="post-score" title="current number of votes">0</div><span id="post-14850-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello. I am analyzing virus through Virtualbox, and am using Wireshark in my real computer (mac) to monitor all of the network connections it makes. I have gotten a lot of network activity from the virus, showing me the IP that it is communicating to, the network protocol that it is using, etc. I always get data inside of my little hex viewer at the bottom of Wireshark, but whenever I click "Follow TCP Stream", nothing shows up. I am almost positive that this is because, inside of the INFO column in Wireshark, I always get a length value of 0 "Len=0". I know that these packets contain data, but it's frustrating how Wireshark always gives me the value of "Len=0", and doesn't let me follow the TCP stream.</p><p>Any help would be appreciated in resolving this issue, thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-follow" rel="tag" title="see questions tagged &#39;follow&#39;">follow</span> <span class="post-tag tag-link-length" rel="tag" title="see questions tagged &#39;length&#39;">length</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Oct '12, 22:29</strong></p><img src="https://secure.gravatar.com/avatar/040ca03d78af0415b2a15631f06e64c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mourginakis&#39;s gravatar image" /><p><span>mourginakis</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mourginakis has no accepted answers">0%</span></p></div></div><div id="comments-container-14850" class="comments-container"><span id="14853"></span><div id="comment-14853" class="comment"><div id="post-14853-score" class="comment-score"></div><div class="comment-text"><p>So does the virus use a modified TCP stack, in which it obfuscates the 'TCP' datastream?</p></div><div id="comment-14853-info" class="comment-info"><span class="comment-age">(09 Oct '12, 23:08)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div><span id="14856"></span><div id="comment-14856" class="comment"><div id="post-14856-score" class="comment-score"></div><div class="comment-text"><p>can you post the capture file at <a href="http://cloudshark.org">cloudshark.org</a>?</p></div><div id="comment-14856-info" class="comment-info"><span class="comment-age">(09 Oct '12, 23:41)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="14907"></span><div id="comment-14907" class="comment"><div id="post-14907-score" class="comment-score"></div><div class="comment-text"><p>"VIrus" was a bit of a misnomer. It's more of a worm, but the point still stands, it's communicating over the internet. Because I can't save my capture file without saving all of the captured packets, i'll just give you an example:</p><p>1078 158.006317000 192.168.0.12 1<strong>.</strong>.**<em>.</em>(dst. ip) TCP 78 50384 &gt; 36 [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=16 TSval=392959107 TSecr=0 SACK_PERM=1</p><p>And in the hex view I get: .=.k..h. m ....E. .<span>@gc</span>@<span class="__cf_email__" data-cfemail="84aac4aa">[email protected]</span> a....... .....$.O l....... ........ ........ ...l.... ......<br />
</p><p>If this data is being obfuscated, is there a way to un-obfusctate it? If so, how? Thanks.</p></div><div id="comment-14907-info" class="comment-info"><span class="comment-age">(10 Oct '12, 17:26)</span> <span class="comment-user userinfo">mourginakis</span></div></div></div><div id="comment-tools-14850" class="comment-tools"></div><div class="clear"></div><div id="comment-14850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15063"></span>

<div id="answer-container-15063" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-15063-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-15063-score" class="post-score" title="current number of votes">0</div><span id="post-15063-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you expand each of the sections (Frame, Ethernet, IP, TCP, etc.) and click the last item in the last section, does it highlight the last "....." section of the bytes? If yes, then there is no data transfer yet.</p><p>The packet output you posted appears to be a TCP SYN packet. The number of bytes you referenced (77 excluding spaces) is about right for a SYN. If you're only seeing SYN packets and no responses, the worm is probably just trying to establish a connection with its Command &amp; Control host.</p><p>If you can post the packet capture, or a screenshot of the expanded protocol information (you can obfuscate the IPs if you want), it can be verified.</p><p>-Greg</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Oct '12, 11:08</strong></p><img src="https://secure.gravatar.com/avatar/6af533edcd07f58511d208454431454d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thechaosmachine&#39;s gravatar image" /><p><span>thechaosmachine</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thechaosmachine has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-15063" class="comments-container"></div><div id="comment-tools-15063" class="comment-tools"></div><div class="clear"></div><div id="comment-15063-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

