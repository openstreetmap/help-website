+++
type = "question"
title = "Capturing Bluetooth on Windows or has anyone actually succeeded on Linux?"
description = '''Does it actually work on Windows? http://wiki.wireshark.org/CaptureSetup/NetworkMedia says the only thing that&#x27;ll work is Linux w/Affix stack. http://affix.sourceforge.net/ looks hopelessly outdated. The last update to that appears to be from 2005 and the highest Linux kernel mentioned is 2.6. I cou...'''
date = "2013-06-22T18:53:00Z"
lastmod = "2015-01-10T08:11:00Z"
weight = 22250
keywords = [ "windows", "capture", "audio", "linux", "bluetooth" ]
aliases = [ "/questions/22250" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Capturing Bluetooth on Windows or has anyone actually succeeded on Linux?](/questions/22250/capturing-bluetooth-on-windows-or-has-anyone-actually-succeeded-on-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22250-score" class="post-score" title="current number of votes">1</div><span id="post-22250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Does it actually work on Windows? <a href="http://wiki.wireshark.org/CaptureSetup/NetworkMedia">http://wiki.wireshark.org/CaptureSetup/NetworkMedia</a> says the only thing that'll work is Linux w/Affix stack. <a href="http://affix.sourceforge.net/">http://affix.sourceforge.net/</a> looks hopelessly outdated. The last update to that appears to be from 2005 and the highest Linux kernel mentioned is 2.6.</p><p>I couldn't get Wireshark to capture anything on the BT interface on my Lenovo T61p running Windows 7. It sees the interface but captures nothing when playing audio successfully (via hands-free audio) to a Bluetooth headset.<br />
</p><p>I'm mainly interested in capturing the traffic between my BT-enabled machine and headsets/headphones. If it supposedly works on Linux, has anyone actually succeeded in getting audio to work w/BT headsets and capturing the traffic? Is it easy to get working on major Linux distributions (e.g. Ubuntu)? I'd rather not waste a whole bunch of time on a dead-end (e.g. handsfree audio broken or BT capturing doesn't work).</p><p>If Wireshark can't capture from BT on Windows, is there another free Windows packet sniffer that will?</p><p>(I tried to comment on an existing Bluetooth capture thread, but this forum kept rejecting my comment as "spam" and throwing my work away!)</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-capture" rel="tag" title="see questions tagged &#39;capture&#39;">capture</span> <span class="post-tag tag-link-audio" rel="tag" title="see questions tagged &#39;audio&#39;">audio</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span> <span class="post-tag tag-link-bluetooth" rel="tag" title="see questions tagged &#39;bluetooth&#39;">bluetooth</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Jun '13, 18:53</strong></p><img src="https://secure.gravatar.com/avatar/6eb3a01550d89bb02e2d74b28373f869?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cwerdna&#39;s gravatar image" /><p><span>cwerdna</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cwerdna has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Jun '13, 18:54</strong> </span></p></div></div><div id="comments-container-22250" class="comments-container"><span id="38102"></span><div id="comment-38102" class="comment"><div id="post-38102-score" class="comment-score"></div><div class="comment-text"><p>This is a very good question. I'd love to capture Bluetooth traffic on a PC and/or mobile device running a Windows OS. And, I'd like to do so from Wireshark, and from a an app created by the software dev team to which I belong. Does anyone out there know what it would take to make this happen?</p></div><div id="comment-38102-info" class="comment-info"><span class="comment-age">(24 Nov '14, 07:16)</span> <span class="comment-user userinfo">DeepSnow</span></div></div></div><div id="comment-tools-22250" class="comment-tools"></div><div class="clear"></div><div id="comment-22250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39026"></span>

<div id="answer-container-39026" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39026-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39026-score" class="post-score" title="current number of votes">0</div><span id="post-39026-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is no support for capturing for Windows. Only Linux. I do not have/use Windows, so not I am not really interested to have that, but I have a plan to add this feature for others. I am not sure if Windows API is able to capturing Bluetooth, but I know that it is possible on CSR dongles.</p><p>There is second option: if you have USB dongle you can try USBPcap [1] and try to capturing Bluetooth traffic over USB.</p><p>[1] <a href="http://desowin.org/usbpcap/">http://desowin.org/usbpcap/</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jan '15, 08:11</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p><span>Michał Łabędzki</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></div></div><div id="comments-container-39026" class="comments-container"></div><div id="comment-tools-39026" class="comment-tools"></div><div class="clear"></div><div id="comment-39026-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

