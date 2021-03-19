+++
type = "question"
title = "capture from other device"
description = '''Hi I have Siemens HiPath PBX connected to my LAN. I want to capture all the traffic going in and out from that PBX on my computer. Can I use wireshark to capture the packets? SNMP is enables on Siemens HiPath system, is that useful for capture full traffic? I cannot install anything on Siemens HiPat...'''
date = "2012-06-30T23:34:00Z"
lastmod = "2012-07-01T10:03:00Z"
weight = 12351
keywords = [ "other", "remote", "devices" ]
aliases = [ "/questions/12351" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capture from other device](/questions/12351/capture-from-other-device)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12351-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12351-score" class="post-score" title="current number of votes">0</div><span id="post-12351-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I have Siemens HiPath PBX connected to my LAN. I want to capture all the traffic going in and out from that PBX on my computer.</p><p>Can I use wireshark to capture the packets?</p><p>SNMP is enables on Siemens HiPath system, is that useful for capture full traffic? I cannot install anything on Siemens HiPath as its not computer but IP-PBX hardware. please let me know what are the ways to capture the packets from it.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-other" rel="tag" title="see questions tagged &#39;other&#39;">other</span> <span class="post-tag tag-link-remote" rel="tag" title="see questions tagged &#39;remote&#39;">remote</span> <span class="post-tag tag-link-devices" rel="tag" title="see questions tagged &#39;devices&#39;">devices</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jun '12, 23:34</strong></p><img src="https://secure.gravatar.com/avatar/1e12f3b74179b6cd58c5ac5d09849f66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanket%20P&#39;s gravatar image" /><p><span>Sanket P</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sanket P has no accepted answers">0%</span></p></div></div><div id="comments-container-12351" class="comments-container"></div><div id="comment-tools-12351" class="comment-tools"></div><div class="clear"></div><div id="comment-12351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12357"></span>

<div id="answer-container-12357" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12357-score" class="post-score" title="current number of votes">0</div><span id="post-12357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm assuming your LAN is an Ethernet LAN. If so, then see <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">the Wireshark Wiki page for capturing on Ethernet</a> for the gory details of ways to capture on a switched Ethernet (if you're <em>not</em> on a switched Ethernet, any machine on the Ethernet should, if its Ethernet adapter can be put in promiscuous mode, be able to see all traffic on the Ethernet, including the PBX's traffic, but I think most Ethernets are switched these days, and that makes it harder).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jul '12, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12357" class="comments-container"></div><div id="comment-tools-12357" class="comment-tools"></div><div class="clear"></div><div id="comment-12357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

