+++
type = "question"
title = "No packets are being detected on outgoing traffic"
description = '''I have a device which is set to automatically report to an external site. This device also had a web interface that I can log into by navigating to its ip address. When I navigate to the device&#x27;s IP address, it is lighting up wireshark, and there is lots of activity.  However, I detect no other pack...'''
date = "2012-08-01T17:18:00Z"
lastmod = "2012-08-01T18:27:00Z"
weight = 13303
keywords = [ "packets", "no" ]
aliases = [ "/questions/13303" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [No packets are being detected on outgoing traffic](/questions/13303/no-packets-are-being-detected-on-outgoing-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13303-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a device which is set to automatically report to an external site. This device also had a web interface that I can log into by navigating to its ip address. When I navigate to the device's IP address, it is lighting up wireshark, and there is lots of activity.</p><p>However, I detect no other packets. So if I don't go to the web interface and let wireshark sit there for a few hours, there are literally no packets detected with that ip address as the source.</p><p>I know that the device is reporting because I am seeing the data on the external server showing up. Unfortunately, I do not have access that the external server's address.</p></div><div id="question-tags" class="tags-container tags">packets no</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Aug '12, 17:18</strong></p><img src="https://secure.gravatar.com/avatar/44121030a2e0fbc808cfff8231d0d442?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="genesismachine&#39;s gravatar image" /><p>genesismachine<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="genesismachine has no accepted answers">0%</span></p></div></div><div id="comments-container-13303" class="comments-container"></div><div id="comment-tools-13303" class="comment-tools"></div><div class="clear"></div><div id="comment-13303-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="13304"></span>

<div id="answer-container-13304" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13304-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm guessing that you are running Wireshark on your PC and that both the PC and the device are connected to a switch of some sort.</p><p>So; Wireshark will see traffic to/from your PC (and the device). It will not see traffic between the device and the server since (basically) that traffic isn't (doesn't need to be) sent by the switch to your PC.</p><p>See <a href="http://wiki.wireshark.org/CaptureSetup/Ethernet?action=show&amp;redirect=CaptureSetup_2fEthernet">Capture Setup - Ethernet</a> for more detailed info.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Aug '12, 18:27</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p>Bill Meier ♦♦<br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Aug '12, 18:34</p></div></div><div id="comments-container-13304" class="comments-container"><span id="13330"></span><div id="comment-13330" class="comment"><div id="post-13330-score" class="comment-score"></div><div class="comment-text"><p>Thanks, I'm buying a hub right now. I will plug the hub into the switch and my device+computer into the hub. In theory, that should work, right?</p><p>I'm pretty new to networking, but willing to learn (My background is EE).</p></div><div id="comment-13330-info" class="comment-info"><span class="comment-age">(02 Aug '12, 16:11)</span> genesismachine</div></div><span id="13331"></span><div id="comment-13331" class="comment"><div id="post-13331-score" class="comment-score"></div><div class="comment-text"><p>Yes: assuming the "hub" really acts as a hub.</p><p>(I expect you've already read <a href="http://wiki.wireshark.org/HubReference,">http://wiki.wireshark.org/HubReference,</a> but if not, please review same).</p></div><div id="comment-13331-info" class="comment-info"><span class="comment-age">(02 Aug '12, 17:04)</span> Bill Meier ♦♦</div></div></div><div id="comment-tools-13304" class="comment-tools"></div><div class="clear"></div><div id="comment-13304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

