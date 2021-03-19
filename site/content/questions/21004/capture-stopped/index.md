+++
type = "question"
title = "capture stopped"
description = '''when i was using wireshark capturing on an ethernet the capture suddenly stopped and showed me this message: the network adapter on which capture was being done is no longer running . The capture stopped.'''
date = "2013-05-07T09:40:00Z"
lastmod = "2013-05-08T14:05:00Z"
weight = 21004
keywords = [ "capture", "stopped" ]
aliases = [ "/questions/21004" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capture stopped](/questions/21004/capture-stopped)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21004-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>when i was using wireshark capturing on an ethernet the capture suddenly stopped and showed me this message: the network adapter on which capture was being done is no longer running . The capture stopped.</p></div><div id="question-tags" class="tags-container tags">capture stopped</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '13, 09:40</strong></p><img src="https://secure.gravatar.com/avatar/583b809745fa45690fa8b950c5d28714?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ashraf&#39;s gravatar image" /><p>Ashraf<br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ashraf has no accepted answers">0%</span></p></div></div><div id="comments-container-21004" class="comments-container"><span id="21025"></span><div id="comment-21025" class="comment"><div id="post-21025-score" class="comment-score"></div><div class="comment-text"><blockquote><p>the capture <strong>suddenly</strong> stopped</p></blockquote><p>what exactly is <strong>suddenly</strong>? 1 second, 1 minute, 1 hour?</p><p>If this an onboard nic or some USB dongle or a PCCARD nic?</p></div><div id="comment-21025-info" class="comment-info"><span class="comment-age">(08 May '13, 06:16)</span> Kurt Knochner ♦</div></div><span id="21029"></span><div id="comment-21029" class="comment"><div id="post-21029-score" class="comment-score"></div><div class="comment-text"><p>it is a NIC and the capture was running for two hours and it stopped . then when i start capture again it capture for short time about 10 min and it stopped again.</p></div><div id="comment-21029-info" class="comment-info"><span class="comment-age">(08 May '13, 07:29)</span> Ashraf</div></div><span id="21893"></span><div id="comment-21893" class="comment"><div id="post-21893-score" class="comment-score"></div><div class="comment-text"><p>I forget to tell you that i am using a notebook(toshiba laptop) may this problem due to over heat in the NIC card or it does not affected by the heavy traffic ?</p></div><div id="comment-21893-info" class="comment-info"><span class="comment-age">(10 Jun '13, 12:03)</span> Ashraf</div></div></div><div id="comment-tools-21004" class="comment-tools"></div><div class="clear"></div><div id="comment-21004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="21007"></span>

<div id="answer-container-21007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21007-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>This means the link on the capture interface went down during capturing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '13, 13:01</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-21007" class="comments-container"><span id="21017"></span><div id="comment-21017" class="comment"><div id="post-21017-score" class="comment-score"></div><div class="comment-text"><p>So how to solve it??</p></div><div id="comment-21017-info" class="comment-info"><span class="comment-age">(08 May '13, 01:40)</span> Ashraf</div></div><span id="21018"></span><div id="comment-21018" class="comment"><div id="post-21018-score" class="comment-score"></div><div class="comment-text"><p>Does this happen every time? Do you have logging on your switch? Does it show link-up/link-down messages? Is your cable OK? Did you plug the cable in firmly?</p></div><div id="comment-21018-info" class="comment-info"><span class="comment-age">(08 May '13, 01:51)</span> SYN-bit ♦♦</div></div><span id="21030"></span><div id="comment-21030" class="comment"><div id="post-21030-score" class="comment-score"></div><div class="comment-text"><p>i don't have a logging on that switch the cable is ok and every thing else is ok</p></div><div id="comment-21030-info" class="comment-info"><span class="comment-age">(08 May '13, 07:30)</span> Ashraf</div></div><span id="21056"></span><div id="comment-21056" class="comment"><div id="post-21056-score" class="comment-score"></div><div class="comment-text"><p>Be very careful with such statement, without logging on the switch you cannot be sure the lower layer did not go down, renegotiated, then came up again. Replace your cable.</p></div><div id="comment-21056-info" class="comment-info"><span class="comment-age">(09 May '13, 07:36)</span> Jaap ♦</div></div><span id="21895"></span><div id="comment-21895" class="comment"><div id="post-21895-score" class="comment-score"></div><div class="comment-text"><p>I forget to tell you that i am using a notebook(toshiba laptop) may this problem due to over heat in the NIC card or it does not affected by the heavy traffic ?</p></div><div id="comment-21895-info" class="comment-info"><span class="comment-age">(10 Jun '13, 12:03)</span> Ashraf</div></div></div><div id="comment-tools-21007" class="comment-tools"></div><div class="clear"></div><div id="comment-21007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21039"></span>

<div id="answer-container-21039" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21039-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>it is a NIC and the capture was running for two hours and it stopped . then when i start capture again it capture for short time about 10 min and it stopped again.</p></blockquote><p>Did you check the power setting options of the NIC driver? Some drivers allow to disable an interface if the computer goes into power save state. Something similar to this:</p><blockquote><p><a href="http://postimg.org/image/5dtjopdgh/">http://postimg.org/image/5dtjopdgh/</a></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 May '13, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-21039" class="comments-container"><span id="21053"></span><div id="comment-21053" class="comment"><div id="post-21053-score" class="comment-score"></div><div class="comment-text"><p>i did but nothing happened, and this time it is captured only 20MB it is about 10 min</p></div><div id="comment-21053-info" class="comment-info"><span class="comment-age">(09 May '13, 04:52)</span> Ashraf</div></div><span id="21062"></span><div id="comment-21062" class="comment"><div id="post-21062-score" class="comment-score"></div><div class="comment-text"><p>Then either your NIC (or your switch) may be faulty/broken <strong>or</strong> some other software (e.g. Network Profile Changer) on your system disables the NIC for some reason.</p></div><div id="comment-21062-info" class="comment-info"><span class="comment-age">(09 May '13, 09:47)</span> Kurt Knochner ♦</div></div><span id="21894"></span><div id="comment-21894" class="comment"><div id="post-21894-score" class="comment-score"></div><div class="comment-text"><p>I forget to tell you that i am using a notebook(toshiba laptop) may this problem due to over heat in the NIC card or it does not affected by the heavy traffic ?</p></div><div id="comment-21894-info" class="comment-info"><span class="comment-age">(10 Jun '13, 12:03)</span> Ashraf</div></div><span id="21914"></span><div id="comment-21914" class="comment"><div id="post-21914-score" class="comment-score"></div><div class="comment-text"><p>maybe. The system could be configured to switch off system components to prevent damage caused by over heating. However, then I would expect a longer disconnect than just a few seconds and some information in the system logs about that event.</p></div><div id="comment-21914-info" class="comment-info"><span class="comment-age">(11 Jun '13, 03:20)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-21039" class="comment-tools"></div><div class="clear"></div><div id="comment-21039-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

