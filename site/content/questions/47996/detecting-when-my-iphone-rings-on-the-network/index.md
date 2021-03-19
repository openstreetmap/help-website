+++
type = "question"
title = "Detecting when my iPhone rings on the network..."
description = '''I would like to know if you think it is doable to sense on a network when an iPhone is ringing (as it communicates this fact to other iOS devices somehow) - and then script this on a PC using something like AutoIT to make a web call to a web service... Does anyone know about this type of apple-devic...'''
date = "2015-11-25T14:43:00Z"
lastmod = "2015-11-26T08:33:00Z"
weight = 47996
keywords = [ "iphone" ]
aliases = [ "/questions/47996" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Detecting when my iPhone rings on the network...](/questions/47996/detecting-when-my-iphone-rings-on-the-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47996-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47996-score" class="post-score" title="current number of votes">0</div><span id="post-47996-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know if you think it is doable to sense on a network when an iPhone is ringing (as it communicates this fact to other iOS devices somehow) - and then script this on a PC using something like AutoIT to make a web call to a web service...</p><p>Does anyone know about this type of apple-device communication? Is one able to determine which packets are 'rings' vs. other traffic? Or, as I suspect, is there some sort of secure comm channel set up between devices such that you can't tell what the traffic type is...</p><p>In case you're curious, the longer story is that My father is very hard of hearing... In spite of many ringer tones / visual ring settings / etc, he misses more calls than he makes. I put a lighting control system in his place and could flicker the lights from a computer program if I am able to know when the phone is ringing...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-iphone" rel="tag" title="see questions tagged &#39;iphone&#39;">iphone</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '15, 14:43</strong></p><img src="https://secure.gravatar.com/avatar/0ec29213afa3ba09e08429890d959ca6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy123&#39;s gravatar image" /><p><span>andy123</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy123 has no accepted answers">0%</span></p></div></div><div id="comments-container-47996" class="comments-container"><span id="48000"></span><div id="comment-48000" class="comment"><div id="post-48000-score" class="comment-score"></div><div class="comment-text"><blockquote><p>(as it communicates this fact to other iOS devices somehow)</p></blockquote><p>What indicates that it does so? Are you referring to the <a href="https://support.apple.com/en-us/HT204681">"iPhone Cellular Calls"</a> feature of Continuity?</p></div><div id="comment-48000-info" class="comment-info"><span class="comment-age">(25 Nov '15, 23:21)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-47996" class="comment-tools"></div><div class="clear"></div><div id="comment-47996-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="48002"></span>

<div id="answer-container-48002" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48002-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48002-score" class="post-score" title="current number of votes">1</div><span id="post-48002-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="andy123 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I doubt that the iPhone just broadcasts a simple and easily identifiable packet, I'd expect that the communication is not only encrypted but that the Apple devices in the group have to register and authorize themselves to the iPhone, so your emulator would have to do the same unless you've got another apple device so that you could just monitor packets running between the two Apple devices (and possibly guess by their size).</p><p>So in your situation, I would probably rather look for a Bluetooth handsfree that could be hacked at hardware level to behave similar to <a href="http://the-gadgeteer.com/2013/05/08/renny-is-the-original-bluetooth-home-ringer-for-your-cellular-phone/">this one</a>, i.e. to control your light beacon system.</p><p>If the Bluetooth range is insufficient (but as vibrating alert of the iPhone is not a solution, your father probably doesn't carry it with him around the house, so range should not be an issue), an alternative would be some arrangement at telephony service level. The simplest way is to set up an account with some SIP (VoIP) service and run a kind of command line VoIP client at the PC, which would indicate the incoming calls to an application controlling the light beacons (<a href="http://sipp.sourceforge.net/">SIPp</a> is not a VoIP client but it is a good candidate as it can invoke arbitrary executables). It then depends on arrangement with the telephony operator whether the call would be forked to both numbers or whether it would be forwarded from iPhone's number to the VoIP number and your father would have to pick the calls up on the PC (for that case, SIPp is not applicable!) or would call back from the iPhone. The call forwarding trigger would have to be "no answer" with a short timeout so that the calling number would be registered at the iPhone to allow calling back but then the call would move to the power ringer quickly.</p><p>Instead of a VoIP service, you could use another mobile number assigned to some kind of "alarm system mobile communicator board", as devices of this kind are usually equipped with dry contacts allowing to control external electrical circuits.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '15, 01:29</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48002" class="comments-container"></div><div id="comment-tools-48002" class="comment-tools"></div><div class="clear"></div><div id="comment-48002-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="48008"></span>

<div id="answer-container-48008" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-48008-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-48008-score" class="post-score" title="current number of votes">1</div><span id="post-48008-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think that the iPhone will send any signal to the local network when it receives a call. Maybe through <strong>Continuity</strong> as <span><span>@Guy Harris</span></span> indicated. But that communication will be encrypted, so nothing to analyze with Wireshark.</p><p>Maybe you should think about alternative ways to detect a phone call. Maybe the following project is what you are looking for.</p><blockquote><p><a href="http://mad-science.wonderhowto.com/how-to/trigger-anything-from-anywhere-with-just-phone-call-0135369/">http://mad-science.wonderhowto.com/how-to/trigger-anything-from-anywhere-with-just-phone-call-0135369/</a><br />
</p></blockquote><p>You can certainly extend this to "listen" to the sound of the ringing phone to trigger an action, instead of using the light detector. Although detecting a certain 'sound wave' is not that easy!!</p><blockquote><p><a href="https://www.google.com/#q=arduino+trigger+based+on+sound">https://www.google.com/#q=arduino+trigger+based+on+sound</a><br />
<a href="https://www.google.com/#q=micro+controller+trigger+based+on+sound">https://www.google.com/#q=micro+controller+trigger+based+on+sound</a><br />
</p><p><a href="http://hellomico.com/getting-started/">http://hellomico.com/getting-started/</a><br />
<a href="http://interface.khm.de/index.php/lab/interfaces-advanced/radio-signal-strength-sensor/">http://interface.khm.de/index.php/lab/interfaces-advanced/radio-signal-strength-sensor/</a><br />
</p></blockquote><p>Just an idea ....</p><p>Or you <strong>just buy a proven commercial solution</strong> for this type of problem....</p><blockquote><p><a href="http://bellman.com/sensor/">http://bellman.com/sensor/</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Nov '15, 08:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Nov '15, 08:58</strong> </span></p></div></div><div id="comments-container-48008" class="comments-container"></div><div id="comment-tools-48008" class="comment-tools"></div><div class="clear"></div><div id="comment-48008-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

