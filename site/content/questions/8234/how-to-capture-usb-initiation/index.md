+++
type = "question"
title = "how to capture USB initiation"
description = '''I&#x27;m trying to debug a linux connection over usb to an embedded controller. The controller is part of a PV inverter and turns itself off when it gets dark. Powering up in the morning does not work properly with the device connected to a Linux box, leaving the embedded controller unable to communicate...'''
date = "2012-01-05T09:42:00Z"
lastmod = "2012-01-06T11:43:00Z"
weight = 8234
keywords = [ "usb" ]
aliases = [ "/questions/8234" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to capture USB initiation](/questions/8234/how-to-capture-usb-initiation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8234-score" class="post-score" title="current number of votes">0</div><span id="post-8234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to debug a linux connection over usb to an embedded controller. The controller is part of a PV inverter and turns itself off when it gets dark. Powering up in the morning does not work properly with the device connected to a Linux box, leaving the embedded controller unable to communicate until it is reset (not a trivial task). All's well with Windows XP.</p><p>So my question is "how do I start the capture from the usb device before the device exists"?: I want to start the capture at night and review the results after sun-up. Using the pseudo device that includes all devices will collect a lot of noise from other interfaces, so I'd prefer not to use that approach.</p><p>regards Tim</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-usb" rel="tag" title="see questions tagged &#39;usb&#39;">usb</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Jan '12, 09:42</strong></p><img src="https://secure.gravatar.com/avatar/a605ed5a360d29e78d5f997c616e235d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tim&#39;s gravatar image" /><p><span>Tim</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tim has no accepted answers">0%</span></p></div></div><div id="comments-container-8234" class="comments-container"></div><div id="comment-tools-8234" class="comment-tools"></div><div class="clear"></div><div id="comment-8234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8245"></span>

<div id="answer-container-8245" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8245-score" class="post-score" title="current number of votes">1</div><span id="post-8245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If by "the pseudo device that includes all devices" you mean the <code>any</code> device, not only will it collect a lot of noise from other interfaces, it won't capture any USB traffic! The <code>any</code> device captures from all regular Linux network interfaces, but doesn't capture, for example, USB or Bluetooth traffic.</p><p>You don't start captures from USB devices, you start captures on USB buses (yes, I know, that should be "on USBs", "USB bus" being like "ATM machine" or "PIN number" :-)) Start a capture on the bus into which you'd plug the controller, before the controller is plugged in, and leave it running. It sounds as if you can't leave the controller plugged in while it's powering up, so I presume you'll plug it in after it powers up; you should see what USB traffic goes to and from it once you plug it in.</p><p>(If "All's well with Windows XP." means that powering up in the morning works fine with the device plugged into a Windows XP system, you might also want to see whether anybody can help you on that.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '12, 21:30</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-8245" class="comments-container"><span id="8252"></span><div id="comment-8252" class="comment"><div id="post-8252-score" class="comment-score">1</div><div class="comment-text"><p>Sounds like a doc error in Wireshark: the words are nearly verbatim from the UI.</p><p>I get wound up by PIN number, but for some reason USB bus doesn't jar so much. I think it's the semantics of B in USB: in my mind it means a specification, rather than a physical bus.</p><p>The device is always plugged in (I want to start recording as soon as possible, rather than after I wake up). My linux box is currently dead, but I see the buses that you mean on another.</p><p>I don't want to use XP as it's not easy to automate a GUI, although I probably do need to capture the traffic to compare it with the linux case.</p></div><div id="comment-8252-info" class="comment-info"><span class="comment-age">(06 Jan '12, 04:05)</span> <span class="comment-user userinfo">Tim</span></div></div><span id="8260"></span><div id="comment-8260" class="comment"><div id="post-8260-score" class="comment-score"></div><div class="comment-text"><p>If "the words" are the text "Pseudo-device that captures on all interfaces", then it's a <em>code</em> error, and it's in libpcap, not in Wireshark. It should probably say "all <em>network</em> interfaces".</p><p>By "plugged in" I mean "plugged into the Linux or Windows box's USB bus" rather than "plugged into the wall socket". I inferred from "Powering up in the morning does not work properly with the device connected to a Linux box" that you can't leave the device plugged into the Linux box's USB bus overnight.</p><p>As for XP, it has a command line, but the problem is WinPcap can't capture on a USB bus.</p></div><div id="comment-8260-info" class="comment-info"><span class="comment-age">(06 Jan '12, 11:43)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-8245" class="comment-tools"></div><div class="clear"></div><div id="comment-8245-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8236"></span>

<div id="answer-container-8236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8236-score" class="post-score" title="current number of votes">0</div><span id="post-8236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Have a look at the <a href="http://ask.wireshark.org/questions/2801/usbmon-captures">usbmon captures</a> question and answers that follow.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Jan '12, 11:34</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-8236" class="comments-container"><span id="8251"></span><div id="comment-8251" class="comment"><div id="post-8251-score" class="comment-score"></div><div class="comment-text"><p>so don't capture with wireshark. use usbmon and analyse with wireshark.</p></div><div id="comment-8251-info" class="comment-info"><span class="comment-age">(06 Jan '12, 03:58)</span> <span class="comment-user userinfo">Tim</span></div></div><span id="8259"></span><div id="comment-8259" class="comment"><div id="post-8259-score" class="comment-score"></div><div class="comment-text"><p>In the page to which Chris Maynard was referring, "usbmon" is <em>not</em> a program that you would use instead of Wireshark, "usbmon" is a capture mechanism that libpcap uses when capturing on USB buses and that, since Wireshark uses libpcap to capture, Wireshark can use.</p><p>I.e., you capture with Wireshark using libpcap using usbmon and then have Wireshark analyze the results.</p></div><div id="comment-8259-info" class="comment-info"><span class="comment-age">(06 Jan '12, 11:29)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-8236" class="comment-tools"></div><div class="clear"></div><div id="comment-8236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

