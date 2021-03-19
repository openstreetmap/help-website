+++
type = "question"
title = "DHCP offer, reject etc"
description = '''Hi not sure for the life of me what I&#x27;ve done as this was working, basically when entering &quot;bootp&quot; filter to capture DHCP data I get nothing, the data is shown as ARP as opposed to offer, ACK etc and I believe this is why it&#x27;s not being shown with a bootp filter, if I run a trace from another PC thi...'''
date = "2011-10-21T06:18:00Z"
lastmod = "2013-06-13T23:32:00Z"
weight = 7021
keywords = [ "ack", "dhcp" ]
aliases = [ "/questions/7021" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [DHCP offer, reject etc](/questions/7021/dhcp-offer-reject-etc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7021-score" class="post-score" title="current number of votes">0</div><span id="post-7021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi not sure for the life of me what I've done as this was working, basically when entering "bootp" filter to capture DHCP data I get nothing, the data is shown as ARP as opposed to offer, ACK etc and I believe this is why it's not being shown with a bootp filter, if I run a trace from another PC this is shown correctly as offer, ACK etc.</p><p>I have uninstalled the application including personal settings and reinstalled but this has not cleared the issue not sure if this is a red herring but if I "Analyze" the packet and "Decode as" I don't get the same options (tabs) as on a working machine, my operationg system is windows 7.</p><p>Any help would be greatly appreciated.</p><p>28 16.703822 Dell_85:3a:78 Netgear_3e:eb:44 ARP 42 192.168.254.8 is at f0:4d:a2:85:3a:78</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-dhcp" rel="tag" title="see questions tagged &#39;dhcp&#39;">dhcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Oct '11, 06:18</strong></p><img src="https://secure.gravatar.com/avatar/1664bec52b70c018d7128921f8a263e3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="livewired&#39;s gravatar image" /><p><span>livewired</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="livewired has no accepted answers">0%</span></p></div></div><div id="comments-container-7021" class="comments-container"></div><div id="comment-tools-7021" class="comment-tools"></div><div class="clear"></div><div id="comment-7021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

4 Answers:

</div>

</div>

<span id="7027"></span>

<div id="answer-container-7027" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7027-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7027-score" class="post-score" title="current number of votes">0</div><span id="post-7027-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Do you have capture filters applied?</p><p>Are you sure your machine does get an offer at all? There may be an IP address conflict preventing the DHCP server to offer you anything. Hence the ARPs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '11, 07:34</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7027" class="comments-container"><span id="7028"></span><div id="comment-7028" class="comment"><div id="post-7028-score" class="comment-score"></div><div class="comment-text"><p>Hi thank you for your answer, I have no filters applied (unless when trying to apply the bootp one)I am not trying to capture my PC obtaining DHCP and through the logs I can read that there is an offer confirming the IP Address is correct and that there are no conflicts, it's just that in the Protocol description it is identified as "ARP" as opposed to DHCP "Offer" or "ACK".</p><p>Just to explain myself better this is not a network issue I'm having but a wireshark issue.</p></div><div id="comment-7028-info" class="comment-info"><span class="comment-age">(21 Oct '11, 08:01)</span> <span class="comment-user userinfo">livewired</span></div></div><span id="7029"></span><div id="comment-7029" class="comment"><div id="post-7029-score" class="comment-score"></div><div class="comment-text"><p>i.e. the bellow should have DHCP XXXX instead of ARP</p><p>28 16.703822 Dell_85:3a:78 Netgear_3e:eb:44 ARP 42 192.168.254.8 is at f0:4d:a2:85:3a:78</p></div><div id="comment-7029-info" class="comment-info"><span class="comment-age">(21 Oct '11, 08:04)</span> <span class="comment-user userinfo">livewired</span></div></div><span id="7032"></span><div id="comment-7032" class="comment"><div id="post-7032-score" class="comment-score"></div><div class="comment-text"><p>The packet in question says ARP because it's an ARP packet. It's not a DHCP packet. Trust me.</p><p>Yes, this is either a network issue or a Wireshark capturing issue wherein it is somehow not capturing the DHCP packets. It is not an issue of Wireshark misidentifying DHCP packets as ARP packets.</p><p>On the machine where you are capturing the DHCP packets, are they being sent to or from the machine that's not seeing the DHCP packets, are they being sent as broadcasts or multicasts from some other machine, or are they being sent between other machines?</p></div><div id="comment-7032-info" class="comment-info"><span class="comment-age">(21 Oct '11, 13:03)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-7027" class="comment-tools"></div><div class="clear"></div><div id="comment-7027-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7030"></span>

<div id="answer-container-7030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7030-score" class="post-score" title="current number of votes">0</div><span id="post-7030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>are you entering the filter in the capture options dialog or the filter box once you have started the capture?. if its the first one, clear the capture filter box in the capture options dialog and then enter bootp in the filter textbox just below the menu &amp; buttons and hit apply.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '11, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/e495b06a4bc732e3eaa676408285777f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tobbe&#39;s gravatar image" /><p><span>tobbe</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tobbe has no accepted answers">0%</span></p></div></div><div id="comments-container-7030" class="comments-container"><span id="7031"></span><div id="comment-7031" class="comment"><div id="post-7031-score" class="comment-score"></div><div class="comment-text"><p>Hi sorry there's some confusion here the above example is with no filter applied, as stated on another PC the trace shows DHCP XXXXX instead of ARP, as the trace shows ARP instead of the various DHCP offer, accept, reject etc it fails to show if a bootp filter is applied.</p><p>It's a shame I can't screen capture on here picture paints a thousand words etc</p></div><div id="comment-7031-info" class="comment-info"><span class="comment-age">(21 Oct '11, 08:40)</span> <span class="comment-user userinfo">livewired</span></div></div></div><div id="comment-tools-7030" class="comment-tools"></div><div class="clear"></div><div id="comment-7030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="7035"></span>

<div id="answer-container-7035" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7035-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7035-score" class="post-score" title="current number of votes">0</div><span id="post-7035-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>As Guy states, it <em>is</em> an ARP packet what you see.</p><p>What you don't see is the DHCP offer being <strong>unicast</strong> to the requesting host. That is caused by your capture setup that only exposes broadcast, some multicast and link local frames. This is what switching is all about. You'll need to use the monitor port to see it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Oct '11, 14:18</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-7035" class="comments-container"></div><div id="comment-tools-7035" class="comment-tools"></div><div class="clear"></div><div id="comment-7035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22038"></span>

<div id="answer-container-22038" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22038-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22038-score" class="post-score" title="current number of votes">0</div><span id="post-22038-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Are you sure your machine does get an offer at all? There may be an IP address conflict preventing the DHCP server to offer you anything. Hence the ARPs.</p><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote><blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote></blockquote><p>IP address conflict occurs when two or more computers on the same LAN network end up with the same IP address. When this occurs, both computers end up not being able to connect to network.There are a few ways in which this problem can be fixed.If it is Static IP request your ISP for a change of IP.If it is a Dynamic IP you can try resetting your modem by switching ON and OFF the modem or open the command prompt and type "ipconfig /release," which dumps the automatic address it had, and then "ipconfig /renew," which gets a new address.To check for the change in IP you can visit <a href="http://www.ip-details.com"></a><a href="http://www.ip-details.com">http://www.ip-details.com</a> which gives your public IP when you visit the site.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jun '13, 23:32</strong></p><img src="https://secure.gravatar.com/avatar/94c3b1ebf70df030934c156b893da3a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="frozengal&#39;s gravatar image" /><p><span>frozengal</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="frozengal has no accepted answers">0%</span></p></div></div><div id="comments-container-22038" class="comments-container"></div><div id="comment-tools-22038" class="comment-tools"></div><div class="clear"></div><div id="comment-22038-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

