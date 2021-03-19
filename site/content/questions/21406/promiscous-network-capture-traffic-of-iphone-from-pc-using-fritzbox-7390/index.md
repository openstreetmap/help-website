+++
type = "question"
title = "Promiscous network: capture traffic of iPhone from pc using Fritzbox 7390"
description = '''Hello, I am new at these things and i need help. I have a Fritzbox 7390. My PC is conencted by a switch to the lan and my iPhone is conencted through wifi.  From Wireshark, that i installed on my pc, i cannot see the iPhone interface. Can someone help me how to do it? thanks'''
date = "2013-05-23T07:03:00Z"
lastmod = "2013-05-23T07:44:00Z"
weight = 21406
keywords = [ "fritzbox", "promiscous" ]
aliases = [ "/questions/21406" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Promiscous network: capture traffic of iPhone from pc using Fritzbox 7390](/questions/21406/promiscous-network-capture-traffic-of-iphone-from-pc-using-fritzbox-7390)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21406-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21406-score" class="post-score" title="current number of votes">0</div><span id="post-21406-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I am new at these things and i need help.</p><p>I have a Fritzbox 7390. My PC is conencted by a switch to the lan and my iPhone is conencted through wifi.</p><p>From Wireshark, that i installed on my pc, i cannot see the iPhone interface.</p><p>Can someone help me how to do it?</p><p>thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fritzbox" rel="tag" title="see questions tagged &#39;fritzbox&#39;">fritzbox</span> <span class="post-tag tag-link-promiscous" rel="tag" title="see questions tagged &#39;promiscous&#39;">promiscous</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 May '13, 07:03</strong></p><img src="https://secure.gravatar.com/avatar/fd4f609caf084a6f4eb71f82e93709f0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tecnologie&#39;s gravatar image" /><p><span>tecnologie</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tecnologie has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '13, 07:45</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-21406" class="comments-container"></div><div id="comment-tools-21406" class="comment-tools"></div><div class="clear"></div><div id="comment-21406-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="21409"></span>

<div id="answer-container-21409" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21409-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21409-score" class="post-score" title="current number of votes">1</div><span id="post-21409-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I have a <strong>Fritzbox</strong> 7390. My PC is conencted by a switch to the lan and my iPhone is conencted through wifi.</p></blockquote><p>For your case, you need to capture the traffic of the iPhone either via a <a href="http://wiki.wireshark.org/CaptureSetup/WLAN">WLAN capture</a> (rather hard for a novice) <strong>or</strong> on the Fritzbox itself.</p><p>See the following tutorial:</p><blockquote><p><a href="http://linuxundich.de/de/software/netzwerk-traffic-direkt-mit-der-fritzbox-aufzeichnen-und-mit-wireshark-auswerten/">http://linuxundich.de/de/software/netzwerk-traffic-direkt-mit-der-fritzbox-aufzeichnen-und-mit-wireshark-auswerten/</a></p></blockquote><p>The site is in german. Please use <strong>google translate</strong> for your language.</p><p>There are other methods to capture directly on a Fritz!Box. Please google for: <strong>fritzbox tcpdump</strong></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 07:35</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '13, 07:35</strong> </span></p></div></div><div id="comments-container-21409" class="comments-container"></div><div id="comment-tools-21409" class="comment-tools"></div><div class="clear"></div><div id="comment-21409-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21407"></span>

<div id="answer-container-21407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21407-score" class="post-score" title="current number of votes">0</div><span id="post-21407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure what you mean by "cannot see the iPhone interface"? Wireshark on the PC can only capture traffic that comes into the network card(s) on the PC.</p><p>Assuming you actually want to capture the iPhone traffic, this is unlikely to be easy.</p><p>I'm assuming you have a network as shown below, possibly with the WiFi Access Point (AP) and switch combined?</p><pre><code>       Internet
          ||
PC ==== SWITCH === AP \/\/ IPhone</code></pre><p>If so, then unless you can persuade the switch to mirror the traffic from the AP port to the port used for your PC you'll be out of luck. Most consumer\home switches can't do this. See the switched section of the Wiki page on <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet">Ethernet networks</a> and many similar questions in this site such as <a href="http://ask.wireshark.org/questions/10946/switched-network">this</a> one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-21407" class="comments-container"></div><div id="comment-tools-21407" class="comment-tools"></div><div class="clear"></div><div id="comment-21407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="21410"></span>

<div id="answer-container-21410" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21410-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21410-score" class="post-score" title="current number of votes">0</div><span id="post-21410-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The Fritzbox 7390 provides an undocumented(?) option to capture network traffic. You can access it via the Webinterface of the fritz, using this link: <a href="http://fritz.box/cgi-bin/webcm?getpage=../html/capture.html">http://fritz.box/cgi-bin/webcm?getpage=../html/capture.html</a></p><p>You can then capture the traffic you would like to and analyze it afterwards in wireshark. I'm not sure if you can limit to the WLAN-Interface traffic only, as I don't have a Fritzbox available for testing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 May '13, 07:42</strong></p><img src="https://secure.gravatar.com/avatar/7141e1bec61c168ead9f00d304b75859?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pfuender&#39;s gravatar image" /><p><span>pfuender</span><br />
<span class="score" title="56 reputation points">56</span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pfuender has no accepted answers">0%</span></p></div></div><div id="comments-container-21410" class="comments-container"><span id="21411"></span><div id="comment-21411" class="comment"><div id="post-21411-score" class="comment-score"></div><div class="comment-text"><p>looks like that I was a bit too slow, see the more detailed answer of 'Kurt Knochner'..</p></div><div id="comment-21411-info" class="comment-info"><span class="comment-age">(23 May '13, 07:44)</span> <span class="comment-user userinfo">pfuender</span></div></div></div><div id="comment-tools-21410" class="comment-tools"></div><div class="clear"></div><div id="comment-21410-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

