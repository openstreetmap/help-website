+++
type = "question"
title = "Packets originated from my network card are not being captured in wireshark"
description = '''I have installed wireshark on my computer running windows 7 and have seen the following problem: When I try to ping any ip addresses on my network (ex: my gateway), I can only see ECHO REPLY packets from the gateway to my machine. I don´t see the ECHO REQUESTS. (ping is responsive) When I try to ope...'''
date = "2015-04-14T14:53:00Z"
lastmod = "2015-04-15T06:52:00Z"
weight = 41440
keywords = [ "source", "packets" ]
aliases = [ "/questions/41440" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Packets originated from my network card are not being captured in wireshark](/questions/41440/packets-originated-from-my-network-card-are-not-being-captured-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41440-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41440-score" class="post-score" title="current number of votes">0</div><span id="post-41440-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed wireshark on my computer running windows 7 and have seen the following problem:</p><p>When I try to ping any ip addresses on my network (ex: my gateway), I can only see ECHO REPLY packets from the gateway to my machine. I don´t see the ECHO REQUESTS. (ping is responsive)</p><p>When I try to open any web page I see only packets from the webserver to my machine. I don´t see the ACK frame, only the SYN-ACK. I also see various TCP packets from the http request, but none originated from my ip address.</p><p>If I try to access any server via telnet or ssh, I still don´t see packets with my ip address as source. I only see packets sent BACK to me as destination.</p><p>If I try to ping my OWN ip address, I get a response but NO packets captured in wireshark It´s as if wireshark is capturing BEFORE packets go out of my network card.</p><p>I double checked and have no filters configured.</p><p>Any ideas on what I´m doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-source" rel="tag" title="see questions tagged &#39;source&#39;">source</span> <span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '15, 14:53</strong></p><img src="https://secure.gravatar.com/avatar/298156224b9fed6085d7ff22631f7b05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fredpohl&#39;s gravatar image" /><p><span>fredpohl</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fredpohl has no accepted answers">0%</span></p></div></div><div id="comments-container-41440" class="comments-container"></div><div id="comment-tools-41440" class="comment-tools"></div><div class="clear"></div><div id="comment-41440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="41442"></span>

<div id="answer-container-41442" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41442-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41442-score" class="post-score" title="current number of votes">1</div><span id="post-41442-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Likely that some AV or Endpoint Protection or VPN software on the client is preventing capture of the locally originated packets.</p><p>Fairly frequent question here, see the answer by <span>@Kurt Knochner</span> to this <a href="http://ask.wireshark.org/questions/33597/wireshark-on-win7-machine-not-capturing-all-traffic">question</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '15, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-41442" class="comments-container"><span id="41455"></span><div id="comment-41455" class="comment"><div id="post-41455-score" class="comment-score"></div><div class="comment-text"><p>Nailed it! It was my VPN agent (Citrix Netscaler). After removing it, it worked fine.</p></div><div id="comment-41455-info" class="comment-info"><span class="comment-age">(15 Apr '15, 06:47)</span> <span class="comment-user userinfo">fredpohl</span></div></div><span id="41457"></span><div id="comment-41457" class="comment"><div id="post-41457-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41457-info" class="comment-info"><span class="comment-age">(15 Apr '15, 06:52)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41442" class="comment-tools"></div><div class="clear"></div><div id="comment-41442-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41441"></span>

<div id="answer-container-41441" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41441-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41441-score" class="post-score" title="current number of votes">0</div><span id="post-41441-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would recommend looking at layer 2 packets using your MAC address rather than looking for IP addresses.</p><p>In particular, look for ARP requests without replies. This often happens if you have your Default Gateway setup incorretly.</p><p>Also look to see if your PC is attempting to send out DHCP requests because your IP address isn't configured correctly or other possible problem such as duplex mismatch, etc.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '15, 23:02</strong></p><img src="https://secure.gravatar.com/avatar/08ceaa93ec93bcecf429815ccc39e803?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Walter%20Benton&#39;s gravatar image" /><p><span>Walter Benton</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Walter Benton has no accepted answers">0%</span></p></div></div><div id="comments-container-41441" class="comments-container"></div><div id="comment-tools-41441" class="comment-tools"></div><div class="clear"></div><div id="comment-41441-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

