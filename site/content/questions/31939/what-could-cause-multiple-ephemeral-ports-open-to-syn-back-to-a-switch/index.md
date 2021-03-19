+++
type = "question"
title = "What could cause multiple ephemeral ports open to SYN back to a switch ?"
description = '''Situation: I have two identical Netgear GS748Tv3 switches in the same location connected to each other through one port. As of three days both stopped allowing management though the HTTP interface. After pulling the power and restarting I have access to the HTTP interface. One of the switches is beh...'''
date = "2014-04-17T11:51:00Z"
lastmod = "2014-04-19T14:58:00Z"
weight = 31939
keywords = [ "http", "multiple", "syn", "port" ]
aliases = [ "/questions/31939" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [What could cause multiple ephemeral ports open to SYN back to a switch ?](/questions/31939/what-could-cause-multiple-ephemeral-ports-open-to-syn-back-to-a-switch)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31939-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Situation: I have two identical Netgear GS748Tv3 switches in the same location connected to each other through one port. As of three days both stopped allowing management though the HTTP interface. After pulling the power and restarting I have access to the HTTP interface. One of the switches is behaving slugglishly at responding to HTTP to manage it through its interface. This has been occuring to three additional switches of the same type in our domain within the last month. I know it is possible for switches to go bad, and capcitors to fail, but for all five to go bad within a month of each other and three within a week seems unlikely.</p><p>So I began a capture of what was occuring from my management station to the switch and of the backbone traffic to the switches. The only thing that seems to be out of the ordinary on the one sluggish switch is that when I open the HTTP management page it is opening additional ephemeral ports in sequence to send SYN messages and getting no response before finally cycling back to the orginal ephemeral port that began opening the page and finally sending an ACK message. This has been checked from multiple PCs.</p><p>Questions: Has anyone experience this before? If they have what is/was the common cause? Could this be an electrical issue causing a bit shift? Or could there be something else at play like HTTP pipelining gone arry or TCP SYN attack? or are we most likely experiencing devices failing around the same time?</p></div><div id="question-tags" class="tags-container tags">http multiple syn port</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Apr '14, 11:51</strong></p><img src="https://secure.gravatar.com/avatar/3179a2e857857fc32eb5d30f074546b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cptamericajd&#39;s gravatar image" /><p>cptamericajd<br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cptamericajd has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Apr '14, 12:04</p></div></div><div id="comments-container-31939" class="comments-container"><span id="32333"></span><div id="comment-32333" class="comment"><div id="post-32333-score" class="comment-score"></div><div class="comment-text"><p>Anyone know if there is CLI for these switches that can be accessed to poke around for issues? I found nothing in the manual.</p></div><div id="comment-32333-info" class="comment-info"><span class="comment-age">(30 Apr '14, 19:45)</span> cptamericajd</div></div></div><div id="comment-tools-31939" class="comment-tools"></div><div class="clear"></div><div id="comment-31939-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31996"></span>

<div id="answer-container-31996" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31996-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Could this be an electrical issue causing a bit shift?</p></blockquote><p>rather unlikely on all 5 switches, as you mentioned yourself in the capacitor example.</p><blockquote><p>or are we most likely experiencing devices failing around the same time?</p></blockquote><p>a fimware bug. Did you try to upgrade?</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '14, 14:58</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31996" class="comments-container"><span id="32332"></span><div id="comment-32332" class="comment"><div id="post-32332-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, I agree the bit shift was unlikely. Firmware already has been at latest version for about a year with no problems. We have reset all settings back to default on two of our switches at a primary site to see if they go down again, not like this determines what is wrong, but maybe a feature that was set was buggy. So far so good. If it occurs again we are planing to reflash the firmware. Luckily we have an order for some enterprise switches on the way as a replacement, but I am still bothered that there may be something on the network causing the failure.</p></div><div id="comment-32332-info" class="comment-info"><span class="comment-age">(30 Apr '14, 19:45)</span> cptamericajd</div></div><span id="32367"></span><div id="comment-32367" class="comment"><div id="post-32367-score" class="comment-score"></div><div class="comment-text"><blockquote><p>but I am still bothered that there may be something on the network causing the failure.</p></blockquote><p>did you consider (or check) an IP address conflict? Again: Unlikely on 5 different switches, but you'll never know...</p></div><div id="comment-32367-info" class="comment-info"><span class="comment-age">(01 May '14, 16:21)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-31996" class="comment-tools"></div><div class="clear"></div><div id="comment-31996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

