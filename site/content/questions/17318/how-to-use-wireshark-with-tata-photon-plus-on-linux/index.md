+++
type = "question"
title = "how to use wireshark with Tata Photon Plus on Linux?"
description = '''Hello, I have a Tata photon plus (EC1260) device. How can I use wireshark in combination with this device Thank you'''
date = "2012-12-30T05:01:00Z"
lastmod = "2013-07-24T14:21:00Z"
weight = 17318
keywords = [ "linux", "tataphoton+", "wireshark" ]
aliases = [ "/questions/17318" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [how to use wireshark with Tata Photon Plus on Linux?](/questions/17318/how-to-use-wireshark-with-tata-photon-plus-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17318-score" class="post-score" title="current number of votes">0</div><span id="post-17318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a Tata photon plus (EC1260) device. How can I use wireshark in combination with this device</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-tataphoton+" rel="tag" title="see questions tagged &#39;tataphoton+&#39;">tataphoton+</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Dec '12, 05:01</strong></p><img src="https://secure.gravatar.com/avatar/dd1c285e36e9992162ab478234fcc0ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bharathi&#39;s gravatar image" /><p><span>Bharathi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bharathi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jul '13, 12:34</strong> </span></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-17318" class="comments-container"></div><div id="comment-tools-17318" class="comment-tools"></div><div class="clear"></div><div id="comment-17318-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="17324"></span>

<div id="answer-container-17324" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-17324-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-17324-score" class="post-score" title="current number of votes">0</div><span id="post-17324-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As you did not mention your OS, I assume Windows, as there is only Tata Photon software for Windows.</p><p>Well, on Windows, you can only capture traffic of that device, if WinPcap is able to identify ('see') the USB device. That really depends on the driver of the device.</p><p>So, please try this:</p><ul><li>Plug in the USB device<br />
</li><li>Install Wireshark</li><li>the WinPcap service should be started now. Please check with the following command:</li></ul><blockquote><p><code>sc query npf</code><br />
</p></blockquote><p>You should see</p><blockquote><p><code>STATE              : 4  RUNNING</code><br />
</p></blockquote><ul><li>Connect to the internet with the Tata Dialer software</li><li>Run <strong>dumpcap</strong> in a DOS window</li></ul><blockquote><p><code>dumpcap -D -M</code><br />
</p></blockquote><p>If you can see the device in the output of dumpcap (identify it by its IP address), then you can (most certainly) capture traffic on it (read the Wirshark Wiki how to do that).</p><p>If you can't see the device, and the NPF service is running (sc command above), then you are (most certainly) out of luck, as WinPcap does not detect that kind of device.</p><p>BTW: Please also read the USB Capture wiki.</p><blockquote><p><code>http://wiki.wireshark.org/CaptureSetup/USB</code><br />
</p></blockquote><p><strong>UPDATE</strong>: On <strong>Ubuntu</strong> the USB 3G modem will be used as a serial connection /dev/ttyUSB0. So, you should be able to capture traffic on it, as mentioned in the <a href="http://wiki.wireshark.org/CaptureSetup/USB">USB sniffing wiki</a> for Linux.</p><p>If that does not work, you can still try one of the serial port sniffers (<strong>no</strong> pcap output!).</p><blockquote><p><code>http://linux.die.net/man/1/slsnif</code><br />
<code>http://jpnevulator.snarl.nl/</code><br />
<code>http://freecode.com/projects/linuxserialsniffer</code><br />
<code>http://code.google.com/p/uscmon/</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Dec '12, 14:56</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Dec '12, 01:55</strong> </span></p></div></div><div id="comments-container-17324" class="comments-container"><span id="17327"></span><div id="comment-17327" class="comment"><div id="post-17327-score" class="comment-score"></div><div class="comment-text"><p>Thank You. I should have specified that I am using Ubuntu 12.04 as my OS. Im sorry about not having done that.</p></div><div id="comment-17327-info" class="comment-info"><span class="comment-age">(31 Dec '12, 01:20)</span> <span class="comment-user userinfo">Bharathi</span></div></div><span id="17329"></span><div id="comment-17329" class="comment"><div id="post-17329-score" class="comment-score"></div><div class="comment-text"><p>well, are you able to connect to the internet with that device on Ubuntu? If so, do you see any new ethernet interface (eth1, eth2)? If yes, then just capture on eth1,eth2. If there is no new ethernet device, you can still try to capture data on the USB bus. Please read the USB wiki I already mentioned.</p><p>If you cannot connect to the internet on Ubuntu, then there is no need to capture data, as there will be none ;-)</p></div><div id="comment-17329-info" class="comment-info"><span class="comment-age">(31 Dec '12, 01:30)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="17334"></span><div id="comment-17334" class="comment"><div id="post-17334-score" class="comment-score"></div><div class="comment-text"><p>see my <strong>UPDATE</strong> in the answer.</p></div><div id="comment-17334-info" class="comment-info"><span class="comment-age">(31 Dec '12, 01:56)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-17324" class="comment-tools"></div><div class="clear"></div><div id="comment-17324-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="23346"></span>

<div id="answer-container-23346" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23346-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23346-score" class="post-score" title="current number of votes">0</div><span id="post-23346-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>On Linux, if your 3G modem is connected to the Internet, there will probably be a PPP device of some sort for it. You can capture on that.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jul '13, 14:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span> </br></br></p></div></div><div id="comments-container-23346" class="comments-container"></div><div id="comment-tools-23346" class="comment-tools"></div><div class="clear"></div><div id="comment-23346-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

