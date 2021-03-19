+++
type = "question"
title = "The NPF driver isn&#x27;t running.  You may have trouble capturing or listing interfaces."
description = ''' i just installed in and started it for the first time and it gave me this error  The NPF driver isn&#x27;t running. You may have trouble capturing or listing interfaces. then when i tried to list the available interfaces ..it gave me an error saying There are no interfaces on which a capture can be done...'''
date = "2012-12-24T09:08:00Z"
lastmod = "2015-06-25T13:32:00Z"
weight = 17235
keywords = [ "npf", "driver" ]
aliases = [ "/questions/17235" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [The NPF driver isn't running. You may have trouble capturing or listing interfaces.](/questions/17235/the-npf-driver-isnt-running-you-may-have-trouble-capturing-or-listing-interfaces)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17235-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>            i just installed in and started it for the first time and it gave me this error</code></pre><p>The NPF driver isn't running. You may have trouble capturing or listing interfaces.</p><p>then when i tried to list the available interfaces ..it gave me an error saying There are no interfaces on which a capture can be done.</p><p>please help me i have no idea what to do</p></div><div id="question-tags" class="tags-container tags">npf driver</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Dec '12, 09:08</strong></p><img src="https://secure.gravatar.com/avatar/1a68f115d202720cf37d585a13edd1be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ejaz&#39;s gravatar image" /><p>Ejaz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ejaz has no accepted answers">0%</span></p></div></div><div id="comments-container-17235" class="comments-container"><span id="19337"></span><div id="comment-19337" class="comment"><div id="post-19337-score" class="comment-score"></div><div class="comment-text"><p>Hey,bro. I have met the same question as you did. And my suggestion is find the "windows command processer"(I bet you must know where it is...) Right click it, Choose "Run as Administrator" and type "net start npf". Then restart the wireshark. And you'll find everything is going to be normal. however,for now,I've met a issue, Everytime I reboot the computer,then I need to do the process again,otherwise I'll meet the "The npf ......" problem again.. Realy annoying.</p></div><div id="comment-19337-info" class="comment-info"><span class="comment-age">(10 Mar '13, 00:30)</span> nowitzji</div></div><span id="35076"></span><div id="comment-35076" class="comment"><div id="post-35076-score" class="comment-score"></div><div class="comment-text"><p>I have this same problem. I tried to install WinPcap but the install program tells me an instance is already running and it must be stopped. How can this be? I'm using a home computer that has never had this program installed. When I look at current running programs I don't see any WinPcap at all. Please help.</p></div><div id="comment-35076-info" class="comment-info"><span class="comment-age">(01 Aug '14, 14:12)</span> Brian</div></div></div><div id="comment-tools-17235" class="comment-tools"></div><div class="clear"></div><div id="comment-17235-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="17236"></span>

<div id="answer-container-17236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-17236-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Did you install WinPcap with Wireshark? And did you install it with elevated privileges (Adminitrator rights)?</p><p>To be able to capture packets, WinPcap needs to have elevated privileges.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Dec '12, 09:24</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 24 Dec '12, 09:24</p></div></div><div id="comments-container-17236" class="comments-container"><span id="30803"></span><div id="comment-30803" class="comment"><div id="post-30803-score" class="comment-score"></div><div class="comment-text"><p>I installed winpcap and its working wonders now!</p><p>Thanks</p></div><div id="comment-30803-info" class="comment-info"><span class="comment-age">(14 Mar '14, 08:20)</span> sandy</div></div></div><div id="comment-tools-17236" class="comment-tools"></div><div class="clear"></div><div id="comment-17236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="41170"></span>

<div id="answer-container-41170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41170-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Typing "net start npf" in PowerShell as Admin worked for me.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Apr '15, 21:22</strong></p><img src="https://secure.gravatar.com/avatar/fb73529da370abdc690009f182dfae7d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmelone&#39;s gravatar image" /><p>mmelone<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmelone has no accepted answers">0%</span></p></div></div><div id="comments-container-41170" class="comments-container"></div><div id="comment-tools-41170" class="comment-tools"></div><div class="clear"></div><div id="comment-41170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="43568"></span>

<div id="answer-container-43568" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43568-score" class="post-score" title="current number of votes">-1</div></div></td><td><div class="item-right"><div class="answer-body"><p>A quick solution that worked for me was to set WireShark to run as administrator (from it's shortcut's settings, Compatibility tab). This way it was able to automatically start the NPF driver by itsef at start up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '15, 13:32</strong></p><img src="https://secure.gravatar.com/avatar/3d472dc3f28a7cd6ee043e04e9463090?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Cosmin%20Plasoianu&#39;s gravatar image" /><p>Cosmin Plaso...<br />
<span class="score" title="5 reputation points">5</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Cosmin Plasoianu has no accepted answers">0%</span></p></div></div><div id="comments-container-43568" class="comments-container"><span id="43576"></span><div id="comment-43576" class="comment"><div id="post-43576-score" class="comment-score"></div><div class="comment-text"><p>This really isn't a great idea, the Wireshark process consists of millions of lines of code that you're allowing unknown packets from the wire to access. Privilege separation between capture and packet analysis was added for a reason, so that only the capture mechanism required elevated privileges.</p><p>Please don't do this, or recommend it to others.</p></div><div id="comment-43576-info" class="comment-info"><span class="comment-age">(25 Jun '15, 17:05)</span> grahamb ♦</div></div></div><div id="comment-tools-43568" class="comment-tools"></div><div class="clear"></div><div id="comment-43568-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

