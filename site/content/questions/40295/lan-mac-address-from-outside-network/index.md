+++
type = "question"
title = "Lan Mac Address from outside network"
description = '''HI, To start with, lets say I&#x27;m a novice, Im a coder but not a hacker, I have read a few articles that mentioned wreshark but cannot find an answer to the following : Can Wireshark sniff out a Lan mac address from outside that network ? Thanks, Mark'''
date = "2015-03-05T10:12:00Z"
lastmod = "2015-03-06T08:41:00Z"
weight = 40295
keywords = [ "sniffing", "mac", "wlan" ]
aliases = [ "/questions/40295" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lan Mac Address from outside network](/questions/40295/lan-mac-address-from-outside-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40295-score" class="post-score" title="current number of votes">0</div><span id="post-40295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>HI,</p><p>To start with, lets say I'm a novice, Im a coder but not a hacker, I have read a few articles that mentioned wreshark but cannot find an answer to the following :</p><p>Can Wireshark sniff out a Lan mac address from outside that network ? Thanks, Mark</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sniffing" rel="tag" title="see questions tagged &#39;sniffing&#39;">sniffing</span> <span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span> <span class="post-tag tag-link-wlan" rel="tag" title="see questions tagged &#39;wlan&#39;">wlan</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '15, 10:12</strong></p><img src="https://secure.gravatar.com/avatar/160d71de03c433deead030c6a80651bb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="22oakdene&#39;s gravatar image" /><p><span>22oakdene</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="22oakdene has no accepted answers">0%</span></p></div></div><div id="comments-container-40295" class="comments-container"></div><div id="comment-tools-40295" class="comment-tools"></div><div class="clear"></div><div id="comment-40295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40296"></span>

<div id="answer-container-40296" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40296-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40296-score" class="post-score" title="current number of votes">0</div><span id="post-40296-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Short answer: no (almost). A little more background: when you say "outside the network" I interpret that as "behind a router". This router limits where Ethernet frames can go, hence behind a router the node's MAC address is no longer visible.</p><p>But I also say 'almost'. Sometimes a MAC address comes up in an higher layer protocol, for instance if the router also functions as DHCP relay. Or if you use certain types of IPv6 addresses.</p><p>Have a look at the online <a href="http://tcpipguide.com">TCPIP guide</a> if you would like to know more.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 10:57</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-40296" class="comments-container"><span id="40327"></span><div id="comment-40327" class="comment"><div id="post-40327-score" class="comment-score"></div><div class="comment-text"><p>Hi Jaap, Thanks for the response, allow me to add more info. I have recently read an article online that there is a keygen for "Sky" routers [Incase you are outwith the UK, Sky is one of if not, the largest ISP providers here] Meaning the keygen requires the SSID and MAC address and this uses the same algorithm that Sky used to create the password - meaning if someone can sniff your MAC address, they can generate the password that it was shipped with !!</p><p>Of course, I can change the Password, SSID and hide the network but I'm curious if this is actually possible ?, i.e. is this a real threat ??</p><p>So, How does someone sniff a MAC address if they are not in the network. Follow ?</p></div><div id="comment-40327-info" class="comment-info"><span class="comment-age">(06 Mar '15, 08:41)</span> <span class="comment-user userinfo">22oakdene</span></div></div></div><div id="comment-tools-40296" class="comment-tools"></div><div class="clear"></div><div id="comment-40296-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

