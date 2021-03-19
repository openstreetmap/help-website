+++
type = "question"
title = "Find unknown static IP address of a device with known MAC address"
description = '''Hi, I have a Lantronix network device that has been returned from a customer which has had a static IP address set in it. I have none of the network details that it was installed in. I do have its MAC address. I have tried connecting the device directly to my laptop and running wire shark but I&#x27;m ne...'''
date = "2016-05-18T10:10:00Z"
lastmod = "2016-05-19T21:59:00Z"
weight = 52739
keywords = [ "ip", "mac-address" ]
aliases = [ "/questions/52739" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Find unknown static IP address of a device with known MAC address](/questions/52739/find-unknown-static-ip-address-of-a-device-with-known-mac-address)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52739-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52739-score" class="post-score" title="current number of votes">0</div><span id="post-52739-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have a Lantronix network device that has been returned from a customer which has had a static IP address set in it. I have none of the network details that it was installed in. I do have its MAC address. I have tried connecting the device directly to my laptop and running wire shark but I'm new to this and I can't work out how to determine its IP address from all the data packets.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ip" rel="tag" title="see questions tagged &#39;ip&#39;">ip</span> <span class="post-tag tag-link-mac-address" rel="tag" title="see questions tagged &#39;mac-address&#39;">mac-address</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '16, 10:10</strong></p><img src="https://secure.gravatar.com/avatar/0c99b74e44116f45dde6d1bc7d999efd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Matthew%20Butcher&#39;s gravatar image" /><p><span>Matthew Butcher</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Matthew Butcher has no accepted answers">0%</span></p></div></div><div id="comments-container-52739" class="comments-container"></div><div id="comment-tools-52739" class="comment-tools"></div><div class="clear"></div><div id="comment-52739-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="52757"></span>

<div id="answer-container-52757" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52757-score" class="post-score" title="current number of votes">1</div><span id="post-52757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>That's not the way to do it. Go to the devices' manual and lookup the reset procedure, usually something like holding some buttons on power on, or setting a loop between some ports. Otherwise you could setup a network scanner to sweep the IP address range you suspect the device to be on (usually a private range address). Unless the device autonomously sends packets (eg. SNMP notifications, or NTP queries) there's little to see.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '16, 01:08</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-52757" class="comments-container"><span id="52760"></span><div id="comment-52760" class="comment"><div id="post-52760-score" class="comment-score"></div><div class="comment-text"><p>Though I agree there is no guarantee that this works, this is always my first stop. It's fast, costs almost nothing, and works often enough for me that probability is in my favor next time the issue comes around.</p><p>I have found many devices (luckily) will actually produce frames for me - like arp requests for the default GW, ARP for some other host as part of the configuration, maybe some LLDP or CDP... The higher end the device, the more likely to get something here. Maybe it even implements RFC5227 for dup IP detection and issues ARP probes/ARP announcements at boot...</p><p>Then, of course, sometimes nothing comes out. Then absolutely - time to get the manual out and do a factory reset.</p></div><div id="comment-52760-info" class="comment-info"><span class="comment-age">(19 May '16, 03:24)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="52775"></span><div id="comment-52775" class="comment"><div id="post-52775-score" class="comment-score"></div><div class="comment-text"><p>Unfortunately there doesn't seem to be a simple way to reset this device...</p><p><a href="https://www.lantronix.com/products/xport-ar/">https://www.lantronix.com/products/xport-ar/</a></p></div><div id="comment-52775-info" class="comment-info"><span class="comment-age">(19 May '16, 08:30)</span> <span class="comment-user userinfo">Matthew Butcher</span></div></div><span id="52776"></span><div id="comment-52776" class="comment"><div id="post-52776-score" class="comment-score"></div><div class="comment-text"><p>Does the software application "Device Installer" from Lantronix not locate it?</p></div><div id="comment-52776-info" class="comment-info"><span class="comment-age">(19 May '16, 08:37)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="52801"></span><div id="comment-52801" class="comment"><div id="post-52801-score" class="comment-score"></div><div class="comment-text"><p>As Grahamb stated above.....Use "Device Installer", which is a software tool provided by Lantronix to locate and configure their devices.</p><p><a href="http://www.lantronix.com/products/deviceinstaller/">http://www.lantronix.com/products/deviceinstaller/</a></p></div><div id="comment-52801-info" class="comment-info"><span class="comment-age">(19 May '16, 21:59)</span> <span class="comment-user userinfo">Rooster_50</span></div></div></div><div id="comment-tools-52757" class="comment-tools"></div><div class="clear"></div><div id="comment-52757-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52758"></span>

<div id="answer-container-52758" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52758-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52758-score" class="post-score" title="current number of votes">0</div><span id="post-52758-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you've connected the two only to each other, all frames (packets) you can see in your capture should have only one of two source MAC addresses: the one of your PC and the one of the blackbox. So apply a display filter <code>(eth.src == bl:ac:kb:ox:ad:dr) and arp</code> and if any packets remain in the list, they must have been sent by the blackbox, and they read, in the info column, <code>Who has X.X.X.X? Tell Y.Y.Y.Y</code>. And <code>Y.Y.Y.Y</code> is the IP of the blackbox.</p><p>For the miracle to happen, you need that the blackbox feels a need to send something somewhere, or read something from somewhere, otherwise you are out of luck because it won't have any reason to send the ARP request you need.</p><p>A hint: don't connect them directly, insert a hub or switch between them, and use the following order of steps:</p><ol><li>connect only the PC to the switch and wait until the interface comes up</li><li>start capturing with no capture filter</li><li>connect the blackbox to the switch (and switch it on of course) and do whatever is necessary so that it would attempt to send or receive data.</li></ol><p>The reason to do it the above way is that you normally cannot start a capture on an interface which is down, and the frames you need might come between the moment the interface came up and the moment you've started the capture if the blackbox doesn't have much to send/receive.</p><p>Knowing the IP address, you'll still have to guess the mask, as it cannot be determined from the ARP requests nor anything else normally seen on the wire. So your best choice is to set <code>Y.Y.Y.(Y+1)/255.255.255.0</code> (except if the last byte would make 255, in that case use 253 instead) as the address/mask of your PC's interface and try to log in.</p><p>If you cannot catch any ARP request, Wireshark cannot help you and you'll have to use some scanning tool which will send arp requests to the device's MAC, asking for all possible IP addresses one by one.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '16, 01:13</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-52758" class="comments-container"><span id="52774"></span><div id="comment-52774" class="comment"><div id="post-52774-score" class="comment-score"></div><div class="comment-text"><p>I have tried this today but unfortunately can't get the device to send/receive anything.</p></div><div id="comment-52774-info" class="comment-info"><span class="comment-age">(19 May '16, 08:26)</span> <span class="comment-user userinfo">Matthew Butcher</span></div></div></div><div id="comment-tools-52758" class="comment-tools"></div><div class="clear"></div><div id="comment-52758-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52779"></span>

<div id="answer-container-52779" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52779-score" class="post-score" title="current number of votes">0</div><span id="post-52779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Not to overlook a potentially simple and easy solution, have you tried simply asking the customer what the static IP address was set to on the device?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '16, 09:15</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-52779" class="comments-container"></div><div id="comment-tools-52779" class="comment-tools"></div><div class="clear"></div><div id="comment-52779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="52780"></span>

<div id="answer-container-52780" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-52780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-52780-score" class="post-score" title="current number of votes">0</div><span id="post-52780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try <a href="http://www.habets.pp.se/synscan/programs.php?prog=arping">arping</a>? Or if you're running Windows, <a href="http://www.elifulkerson.com/projects/arp-ping.php">arp-ping</a>?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '16, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-52780" class="comments-container"></div><div id="comment-tools-52780" class="comment-tools"></div><div class="clear"></div><div id="comment-52780-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

