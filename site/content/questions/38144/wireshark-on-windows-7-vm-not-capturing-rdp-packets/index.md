+++
type = "question"
title = "Wireshark on Windows 7 VM not capturing RDP packets?"
description = '''I am investigating an issue where my Windows 7 VM host is suddenly resetting RDP connections after about 20 minutes. I set up Wireshark captures on both the Client and the VM simultaneously. The captures taken from the client are showing the behavior I expected to see, however when I look at the cap...'''
date = "2014-11-25T15:31:00Z"
lastmod = "2014-11-25T15:58:00Z"
weight = 38144
keywords = [ "windows7", "rdp", "virtual" ]
aliases = [ "/questions/38144" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark on Windows 7 VM not capturing RDP packets?](/questions/38144/wireshark-on-windows-7-vm-not-capturing-rdp-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38144-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38144-score" class="post-score" title="current number of votes">0</div><span id="post-38144-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am investigating an issue where my Windows 7 VM host is suddenly resetting RDP connections after about 20 minutes. I set up Wireshark captures on both the Client and the VM simultaneously. The captures taken from the client are showing the behavior I expected to see, however when I look at the captures from the VM no RDP traffic is present in the capture at all. If I ping from the client to the VM, the ICMP packets are captured by wireshark. I can also see from netstat command that there is an active TCP connection between my client port and port 3398 on the VM but still no RDP packets appearing in the packet capture.</p><p>My suspicion is that the VMs NIC is not passing the RDP packets up to winpcap, would this be an appropriate explanation? Or could something else be going on? Also curious to see if anyone has experienced the sudden resetting of RCP streams by a VM host.<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows7" rel="tag" title="see questions tagged &#39;windows7&#39;">windows7</span> <span class="post-tag tag-link-rdp" rel="tag" title="see questions tagged &#39;rdp&#39;">rdp</span> <span class="post-tag tag-link-virtual" rel="tag" title="see questions tagged &#39;virtual&#39;">virtual</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Nov '14, 15:31</strong></p><img src="https://secure.gravatar.com/avatar/e8c97d07ed513234e46d7fe5bd3e4cbc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nick-14&#39;s gravatar image" /><p><span>Nick-14</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nick-14 has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Nov '14, 15:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span></p></div></div><div id="comments-container-38144" class="comments-container"></div><div id="comment-tools-38144" class="comment-tools"></div><div class="clear"></div><div id="comment-38144-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38145"></span>

<div id="answer-container-38145" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38145-score" class="post-score" title="current number of votes">3</div><span id="post-38145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using RDP to connect to the VM in order to run Wireshark? Wireshark attempts to determine if you have a remote connection to the machine you're running Wireshark on, and if so, it automatically applies a capture filter to block the remote session traffic.</p><p>You can read about this <a href="http://wiki.wireshark.org/CaptureFilters">here on the Wireshark Wiki</a>. Scroll down to the heading "Default Capture Filters." You'll see that when Wireshark detects an RDP session, at applies a capture filter of "not tcp port 3389". If this is what's happening, you'll need to go to the Capture Options dialog and clear the capture filter before you start capturing in order to see the RDP traffic.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Nov '14, 15:44</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-38145" class="comments-container"><span id="38146"></span><div id="comment-38146" class="comment"><div id="post-38146-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot Jim, this is exactly what has been happening, cheers.</p></div><div id="comment-38146-info" class="comment-info"><span class="comment-age">(25 Nov '14, 15:58)</span> <span class="comment-user userinfo">Nick-14</span></div></div></div><div id="comment-tools-38145" class="comment-tools"></div><div class="clear"></div><div id="comment-38145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

