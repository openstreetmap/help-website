+++
type = "question"
title = "VOIP call recording"
description = '''Hello All,  I am new to this wire shark software. I am in need of a software that would record all phone conversations (Iindividual voip phones by grand stream or call centric) on the network from a centralized computer. I will dedicate this computer for this purpose only. i am planning to get 4-5 p...'''
date = "2011-03-27T15:34:00Z"
lastmod = "2011-03-27T23:16:00Z"
weight = 3166
keywords = [ "recording", "phone", "voip" ]
aliases = [ "/questions/3166" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [VOIP call recording](/questions/3166/voip-call-recording)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3166-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All, I am new to this wire shark software. I am in need of a software that would record all phone conversations (Iindividual voip phones by grand stream or call centric) on the network from a centralized computer. I will dedicate this computer for this purpose only. i am planning to get 4-5 phone lines for my workers which will be directly connected by ethernet cables to my hub/router. I want all conversations to be recorded on my centralized computer, which can be later played back. Please let me know if wire shark can be used for this purpose on windows xp based system.</p><p>thanks Manny</p></div><div id="question-tags" class="tags-container tags">recording phone voip</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '11, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/2a744b2ab75f6538c64761c0589596ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Manny&#39;s gravatar image" /><p>Manny<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Manny has no accepted answers">0%</span></p></div></div><div id="comments-container-3166" class="comments-container"></div><div id="comment-tools-3166" class="comment-tools"></div><div class="clear"></div><div id="comment-3166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3170"></span>

<div id="answer-container-3170" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-3170-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>First of all Wireshark is a packet sniffer and dissection engine. So, theoretically it can grab the data and store them, which you can then process into the form you need.</p><p>Practically this a very manual process, identifying capture files, manipulating them, finding call information and related media streams (which requires protocol insights into call control and media protocols), then extract the media from them (if the codec allows you) and play/store that.</p><p>Without any Wireshark experience under your belt you have a steep learning curve ahead with something that's not a call recorder, the thing you're after.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Mar '11, 23:16</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-3170" class="comments-container"><span id="3188"></span><div id="comment-3188" class="comment"><div id="post-3188-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the input Jaap. I know i have a long way to go, if i have to use this software effectively i tried playing around with it, i could capture a simple voice call from majicjack on my computer using the telephony option. i am not sure how to configure this kind for the entire network of computers from this one computer. this currently shows my ethernet card as the device. but how can i capture all the voice traffic on my router.</p><p>As you menioned, if this is not the software for my purpose, are there other softwares that does this job or may help me for my work. Please let me know. thanks a lot for the reply.</p><p>Regards, Manny</p></div><div id="comment-3188-info" class="comment-info"><span class="comment-age">(28 Mar '11, 18:17)</span> Manny</div></div><span id="3189"></span><div id="comment-3189" class="comment"><div id="post-3189-score" class="comment-score"></div><div class="comment-text"><p>I.e., while you might be able to do that with Wireshark, Wireshark wasn't <em>designed</em> to be a tool for doing that, so it's not as convenient as you'd probably want for that purpose. You might try doing a Web search for "voip call recording software" to see if there are other tools that would do a better job of recording VoIP calls.</p></div><div id="comment-3189-info" class="comment-info"><span class="comment-age">(28 Mar '11, 18:17)</span> Guy Harris ♦♦</div></div><span id="3197"></span><div id="comment-3197" class="comment"><div id="post-3197-score" class="comment-score"></div><div class="comment-text"><p>Well, <a href="http://www.oxid.it/index.html">Cain&amp;Abel</a> come to mind.</p></div><div id="comment-3197-info" class="comment-info"><span class="comment-age">(28 Mar '11, 23:28)</span> Jaap ♦</div></div></div><div id="comment-tools-3170" class="comment-tools"></div><div class="clear"></div><div id="comment-3170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

