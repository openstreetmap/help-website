+++
type = "question"
title = "Recommended capture computers"
description = '''I recently had Riverbed tech support inform me that using their Pilot software burst bandwidth report is not going to be accurate unless I use a Linux based computer with a Turbocap card installed.  So that seems to rule out laptops. What computers are people out there dragging around to their clien...'''
date = "2011-04-19T16:33:00Z"
lastmod = "2011-04-19T16:36:00Z"
weight = 3625
keywords = [ "computer" ]
aliases = [ "/questions/3625" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Recommended capture computers](/questions/3625/recommended-capture-computers)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3625-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I recently had Riverbed tech support inform me that using their Pilot software burst bandwidth report is not going to be accurate unless I use a Linux based computer with a Turbocap card installed.</p><p>So that seems to rule out laptops. What computers are people out there dragging around to their clients networks?</p><p>Can anyone recommend a prebuilt Linux system and/or Windows system that is particularly well suited for the Turbocap card and accurate timestamps?</p><p>What are you folks out there using?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">computer</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Apr '11, 16:33</strong></p><img src="https://secure.gravatar.com/avatar/7df3f9a4b16eae9f77feb6eabe92919e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eelarry&#39;s gravatar image" /><p>eelarry<br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eelarry has no accepted answers">0%</span></p></div></div><div id="comments-container-3625" class="comments-container"></div><div id="comment-tools-3625" class="comment-tools"></div><div class="clear"></div><div id="comment-3625-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3626"></span>

<div id="answer-container-3626" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3626-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Here is Riverbed's reply to my issue with their burst bandwidth report on a Dell laptop:</p><p>This is a follow-up to our phone conversation regarding the Burst Bandwidth 1ms (max and average) views in Pilot. We can see the bandwidth reported on the 1ms views seem to exceed the linkspeed, which should not be possible.</p><p>The problem is not so much a bug with Pilot as it has to do with the way time-stamping is performed when packets are received. In Windows, using a normal NIC, the OS handles time-stamping the arriving packets. Depending on what else the OS is handling, there can be some delay in the time-stamping process and several packets collected in the buffer may be recorded with the same time-stamp. When analyzed with a program like Pilot, it appears that more data was received that is physically possible.<br />
</p><p>On our specialty TurboCap capture card, when installed in a Linux box, time stamping can be made more accurate by assigning one of the CPU's processor cores the sole task of time-stamping (a driver parameter). This will result in much greater accuracy for the sub-second burst views.</p><p>It is therefore recommended to use the normal Bandwidth Over Time view when using a regular NIC in Windows when the problem is encountered. Discrepancies will be averaged out when calculating over the much longer interval (1sec vs 1ms). Another suggestion is to run Pilot on a workstation dedicated to perform captures only, all other non-essential programs or utilities should be turned off. This should help to minimize delays in performing the time stamping function.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Apr '11, 16:36</strong></p><img src="https://secure.gravatar.com/avatar/7df3f9a4b16eae9f77feb6eabe92919e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="eelarry&#39;s gravatar image" /><p>eelarry<br />
<span class="score" title="36 reputation points">36</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="eelarry has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-3626" class="comments-container"></div><div id="comment-tools-3626" class="comment-tools"></div><div class="clear"></div><div id="comment-3626-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

