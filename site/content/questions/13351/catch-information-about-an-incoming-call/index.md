+++
type = "question"
title = "Catch information about an incoming call"
description = '''Hi guys, i&#x27;m develoing a software for my business and one of the features is to identify the incoming call, search in data base and show client&#x27;s information. Well, we&#x27;re using a NEC Aspire central with 4 RDSI lines. Yesterday I shutted down all pc&#x27;s and capture all traffic with Wireshark while I ca...'''
date = "2012-08-03T07:42:00Z"
lastmod = "2012-08-04T04:19:00Z"
weight = 13351
keywords = [ "catch", "capture", "connection", "telephony" ]
aliases = [ "/questions/13351" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Catch information about an incoming call](/questions/13351/catch-information-about-an-incoming-call)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13351-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys, i'm develoing a software for my business and one of the features is to identify the incoming call, search in data base and show client's information.</p><p>Well, we're using a NEC Aspire central with 4 RDSI lines. Yesterday I shutted down all pc's and capture all traffic with Wireshark while I called myself (mobile phone to NEC Aspire), but apparently no information was captured when I pick up, hang or call... I've capture something but I think isn't from the NEC.</p><p>Another day I tried to write the rule "src 192.168.1.150" which is the NEC IP, and I capture information about the phone, time... ut I need real time, not just when call finished.</p><p>Yesterday I didn't capture even that information.</p><p>Any suggest?</p><p>Thank you buddies,</p><p>Adán</p></div><div id="question-tags" class="tags-container tags">catch capture connection telephony</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Aug '12, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/2286c35cbf9c68127e1eb473943ee723?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoudan&#39;s gravatar image" /><p>Zoudan<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoudan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Sep '12, 08:26</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-13351" class="comments-container"></div><div id="comment-tools-13351" class="comment-tools"></div><div class="clear"></div><div id="comment-13351-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13362"></span>

<div id="answer-container-13362" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13362-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hm... are you sure you want to do this with a sniffer?</p><p>NEC already offers that kind of software (<a href="http://www.necaspire.com/necaspire/pc_applications/pc_assistant.php">PC Assistant</a>) and I'm sure they also offer an API to get the required information about incoming calls much easier than extracting everything from a captured session.</p><p>Maybe I'm on the wrong track. If so, please update your question with more details.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '12, 04:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-13362" class="comments-container"><span id="13366"></span><div id="comment-13366" class="comment"><div id="post-13366-score" class="comment-score"></div><div class="comment-text"><p>Well, it's a great idea, I've seen NEC programas but they are just for clients, not developers. Maybe, looking his software and surfing the web I can get something about an API to get the information.</p><p>I'm trying this, if not get result, I repeat Wireshark testing because between NEC and my PC there is a switch, and it's possible I am not capturing the required information because NEC send different information per interface.</p><p>Thank you all,</p><p>Adán</p></div><div id="comment-13366-info" class="comment-info"><span class="comment-age">(04 Aug '12, 11:42)</span> Zoudan</div></div></div><div id="comment-tools-13362" class="comment-tools"></div><div class="clear"></div><div id="comment-13362-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

