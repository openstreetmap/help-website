+++
type = "question"
title = "DG gryphon protocol"
description = '''Hi. I&#x27;m not an expert with Wireshark by any means.. but have come across DG Gryphon Protocol whilst capturing information. I can&#x27;t find any information on Wireshark about this so I would very much appreciate it if anyone can give me some information on this. I have tried the FAQs etc and tried the u...'''
date = "2012-08-20T19:35:00Z"
lastmod = "2014-02-25T11:14:00Z"
weight = 13786
keywords = [ "gryphon" ]
aliases = [ "/questions/13786" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [DG gryphon protocol](/questions/13786/dg-gryphon-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13786-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. I'm not an expert with Wireshark by any means.. but have come across DG Gryphon Protocol whilst capturing information. I can't find any information on Wireshark about this so I would very much appreciate it if anyone can give me some information on this. I have tried the FAQs etc and tried the user guide.. but nothing. Google gives a certain amount of information, but I'd really like to hear from someone from Wireshark as to what this is.</p></div><div id="question-tags" class="tags-container tags">gryphon</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Aug '12, 19:35</strong></p><img src="https://secure.gravatar.com/avatar/f362ed5efa32fe1f2a1951ec84a6b6ac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ghost&#39;s gravatar image" /><p>Ghost<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ghost has no accepted answers">0%</span></p></div></div><div id="comments-container-13786" class="comments-container"></div><div id="comment-tools-13786" class="comment-tools"></div><div class="clear"></div><div id="comment-13786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13788"></span>

<div id="answer-container-13788" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13788-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What is it that you wish to know ? A shot in the dark: Are you seeing some traffic on TCP port 7000 which is being dissected as gryphon but which may not really be gryphon ?</p><p>The README associated with the gryphon dissector source says:</p><blockquote><p>Dearborn Group Technology has released under GPL this plugin for Wireshark. It decodes the protocol used by their Gryphon automotive network tool.</p><p>The plugin decodes the communication protocol, but not any vehicle network messages.</p><p>Dearborn Group Technology can be found at <a href="http://www.dgtech.com/">http://www.dgtech.com/</a> The author is Steve Limkemann [email protected]</p></blockquote><p>The gryphon dissector was originally added to Ethereal (now known as Wireshark) in 1999.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Aug '12, 20:51</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Aug '12, 20:57</p></div></div><div id="comments-container-13788" class="comments-container"><span id="13800"></span><div id="comment-13800" class="comment"><div id="post-13800-score" class="comment-score"></div><div class="comment-text"><p>In particular, <a href="http://www.dgtech.com/product/gryphon/gryphon.php">Gryphon</a> "is a hardware adapter that provides remote connectivity for multiplexed automation and automotive communication networks. GRYPHON doesn't require any programming and is ready to run out-of-the-box as a stand-alone product. It uses an Ethernet connection to provide a high-speed user interface." Plug Gryphon into a car or truck and into an Ethernet, and do diagnostics on the vehicle from a personal computer running the Gryphon control software controlling the Gryphon box.</p></div><div id="comment-13800-info" class="comment-info"><span class="comment-age">(21 Aug '12, 13:38)</span> Guy Harris ♦♦</div></div><span id="13801"></span><div id="comment-13801" class="comment"><div id="post-13801-score" class="comment-score"></div><div class="comment-text"><p>...and Bill's guess in the first paragraph is probably the answer, especially if it shows a lot of the traffic as malformed. Unless you're working in an car/truck repair shop, you probably have nothing using the Gryphon protocol.</p></div><div id="comment-13801-info" class="comment-info"><span class="comment-age">(21 Aug '12, 13:39)</span> Guy Harris ♦♦</div></div><span id="13830"></span><div id="comment-13830" class="comment"><div id="post-13830-score" class="comment-score"></div><div class="comment-text"><p>Hi. Yes, one thing I was curious about was why, after visiting a certain site for so long, I am just recently seeing Gryphon Protocol, and the other thing I was curious about is what you mentioned..in the protocol column it shows as Gryphor and in the Info column it shows as invalid. Thank you for your replies.. much appreciated. Not so easy when I am learning this by myself.</p></div><div id="comment-13830-info" class="comment-info"><span class="comment-age">(22 Aug '12, 16:32)</span> Ghost</div></div></div><div id="comment-tools-13788" class="comment-tools"></div><div class="clear"></div><div id="comment-13788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30189"></span>

<div id="answer-container-30189" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30189-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Late entry, but posted for the benefit of those who might come after:</p><p>TCP7000/7001/7002 are associated with the Cisco Unified Communications/Call Manager (CUCM), either the Tomcat resource, and/or the Trace Collection Tool Service, and/or the Trace Collection servlet. I observe TCP7000 consistently on my network, and we have a LOT of Cisco VoIP and associated CUCM servers.</p><p>Here is the snip from my spreadsheet collection of protocols/ports:</p><p>"This port is used for communication between Cisco Trace Collection Tool Service and Cisco Trace Collection servlet."</p><p>HTH Ray, University of Wyoming</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '14, 11:14</strong></p><img src="https://secure.gravatar.com/avatar/9777ec9cd4e7ecd1c518183812b1358d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RD%20Monasmith&#39;s gravatar image" /><p>RD Monasmith<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RD Monasmith has no accepted answers">0%</span></p></div></div><div id="comments-container-30189" class="comments-container"></div><div id="comment-tools-30189" class="comment-tools"></div><div class="clear"></div><div id="comment-30189-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

