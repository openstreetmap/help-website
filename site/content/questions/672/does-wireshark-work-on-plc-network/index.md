+++
type = "question"
title = "Does Wireshark Work on PLC Network?"
description = '''Hi, I am new to PLCs. Actually we have a network of PLCs and we wanted to analyze the traffic on the network which is on Thicknet. We have no vendor support and we dont know the protocol even. Some special nic cards having AUI port were came with PLC. These nics are ISA-slot based cards. These nics ...'''
date = "2010-10-26T10:24:00Z"
lastmod = "2010-10-26T10:50:00Z"
weight = 672
keywords = [ "plc", "analyze", "data" ]
aliases = [ "/questions/672" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Does Wireshark Work on PLC Network?](/questions/672/does-wireshark-work-on-plc-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-672-score" class="post-score" title="current number of votes">0</div><span id="post-672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I am new to PLCs. Actually we have a network of PLCs and we wanted to analyze the traffic on the network which is on Thicknet. We have no vendor support and we dont know the protocol even. Some special nic cards having AUI port were came with PLC. These nics are ISA-slot based cards. These nics are installed on the PC and a program written in C language is run to capture the data. This program was given by the vendor.</p><p>I request all of you to kindly share your expertise. Can Wireshark anaylze the traffic on this network. IF possible then how? Secondly is it possible to change the network from Thicknet to UTP cable with normal ethernet card.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-plc" rel="tag" title="see questions tagged &#39;plc&#39;">plc</span> <span class="post-tag tag-link-analyze" rel="tag" title="see questions tagged &#39;analyze&#39;">analyze</span> <span class="post-tag tag-link-data" rel="tag" title="see questions tagged &#39;data&#39;">data</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Oct '10, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/cc262b90e22365938a0544574756298a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssamir&#39;s gravatar image" /><p><span>ssamir</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssamir has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Oct '10, 10:51</strong> </span></p><img src="https://secure.gravatar.com/avatar/9b4bb3984350b45aee3eda5cc1c90d36?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lchappell&#39;s gravatar image" /><p><span>lchappell ♦</span><br />
<span class="score" title="1206 reputation points"><span>1.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span></p></div></div><div id="comments-container-672" class="comments-container"><span id="677"></span><div id="comment-677" class="comment"><div id="post-677-score" class="comment-score"></div><div class="comment-text"><p>I'd just install Wireshark on one of the systems and look at the start page to see if Wireshark can recognize the adapter on that system. From there start capturing the traffic. If Wireshark has a dissector for the protocol in use you will know it as it will break apart packets based on their field values.</p></div><div id="comment-677-info" class="comment-info"><span class="comment-age">(26 Oct '10, 10:50)</span> <span class="comment-user userinfo">lchappell ♦</span></div></div></div><div id="comment-tools-672" class="comment-tools"></div><div class="clear"></div><div id="comment-672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="673"></span>

<div id="answer-container-673" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-673-score" class="post-score" title="current number of votes">0</div><span id="post-673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Without knowing the protocol(s) in use, there's really no way to answer your questions...can you give us a bit more information?</p><p>Look in your Windows configuration (Control Panel-&gt;Network Connections) and open the Properties for the network connection. A dialog box will open, and one of the items displayed is "This connection uses the following items." If one of those items is "Internet Protocol (TCP/IP)", Wireshark should be able to capture/analyze data from those adapters. If you'll post the full list of those items, we can tell you if Wireshark will "do more" than basic TCP/IP analysis for you.</p><p>--Wes</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '10, 10:30</strong></p><img src="https://secure.gravatar.com/avatar/11ea89c2fd5a5830c69d0574a51b8142?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wesmorgan1&#39;s gravatar image" /><p><span>wesmorgan1</span><br />
<span class="score" title="411 reputation points">411</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wesmorgan1 has 2 accepted answers">4%</span></p></div></div><div id="comments-container-673" class="comments-container"></div><div id="comment-tools-673" class="comment-tools"></div><div class="clear"></div><div id="comment-673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

