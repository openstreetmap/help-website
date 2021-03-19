+++
type = "question"
title = "Incorrect Header checksum for all outbound packets from Ethernet adapter"
description = '''Hi, I captured all the packets from my computer for Ethernet card. I noticed for all the packets with source IP as my ethernet card IP got Header checksum error. I tried disabling the Checksum offload on my NIC. Also tried updating the NIC driver. Even on Wireshark the TCP prefernce is disabled for ...'''
date = "2011-04-14T04:23:00Z"
lastmod = "2011-04-15T09:55:00Z"
weight = 3495
keywords = [ "badchecksum" ]
aliases = [ "/questions/3495" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Incorrect Header checksum for all outbound packets from Ethernet adapter](/questions/3495/incorrect-header-checksum-for-all-outbound-packets-from-ethernet-adapter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3495-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3495-score" class="post-score" title="current number of votes">0</div><span id="post-3495-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I captured all the packets from my computer for Ethernet card.</p><p>I noticed for all the packets with source IP as my ethernet card IP got Header checksum error. I tried disabling the Checksum offload on my NIC. Also tried updating the NIC driver. Even on Wireshark the TCP prefernce is disabled for "Validate TCP checksum if possible". Still getting the capture with incorrect header checksum even for ICMP and all other traffic from my Ethernet IP. Also tried capturing using Ethereal. Got the same bad checksum.</p><p>Please help me to identify the problem.. Is it with my NIC or where I have to check the .. What could be the problem.</p><p>Regards, Sarav</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-badchecksum" rel="tag" title="see questions tagged &#39;badchecksum&#39;">badchecksum</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Apr '11, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/23b4ae29f81b03b17a485fa9e6d5e92a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sarav&#39;s gravatar image" /><p><span>Sarav</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sarav has no accepted answers">0%</span></p></div></div><div id="comments-container-3495" class="comments-container"></div><div id="comment-tools-3495" class="comment-tools"></div><div class="clear"></div><div id="comment-3495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3497"></span>

<div id="answer-container-3497" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3497-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3497-score" class="post-score" title="current number of votes">1</div><span id="post-3497-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Did you also disable "Validate the IP checksum if possible"?<br />
Please check:<br />
- Edit<br />
- Preferences<br />
- Protocols<br />
- IP</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Apr '11, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/fac200552b0c24be2bc93a740bd54d0d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="joke&#39;s gravatar image" /><p><span>joke</span><br />
<span class="score" title="1278 reputation points"><span>1.3k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="34 badges"><span class="bronze">●</span><span class="badgecount">34</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="joke has 6 accepted answers">9%</span> </br></br></p></div></div><div id="comments-container-3497" class="comments-container"><span id="3513"></span><div id="comment-3513" class="comment"><div id="post-3513-score" class="comment-score">1</div><div class="comment-text"><p>(What this means is that your adapter is probably doing IP and TCP checksum offloading, so that the IP and TCP implementations aren't computing the checksums and inserting them into the packet before handing them to the adapter - or to the capture mechanism and thus to tcpdump/Ethereal/Wireshark/etc. - so the application capturing the traffic sees packets with bad checksums. You need to turn off checksum validation to suppress the complaints.)</p></div><div id="comment-3513-info" class="comment-info"><span class="comment-age">(15 Apr '11, 09:55)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-3497" class="comment-tools"></div><div class="clear"></div><div id="comment-3497-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

