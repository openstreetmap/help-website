+++
type = "question"
title = "Wireless N losing internet access"
description = '''Have a strange problem.  Using a Intel N 2230 and connecting 802.11n to a router, I lose access to the network at various times.  I&#x27;m still shown as connected but I can&#x27;t reach any part of the internal network or external internet etc.  Performed a packet capture of the moment it drops, traffic does...'''
date = "2013-08-24T14:05:00Z"
lastmod = "2013-08-25T11:43:00Z"
weight = 24012
keywords = [ "wireless" ]
aliases = [ "/questions/24012" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless N losing internet access](/questions/24012/wireless-n-losing-internet-access)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24012-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24012-score" class="post-score" title="current number of votes">0</div><span id="post-24012-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Have a strange problem.</p><p>Using a Intel N 2230 and connecting 802.11n to a router, I lose access to the network at various times.</p><p>I'm still shown as connected but I can't reach any part of the internal network or external internet etc.</p><p>Performed a packet capture of the moment it drops, traffic doesn't seem to strange to me (albeit I'm new to this) apart from a series of packets with SACK_PERM=1. (??)</p><p>Anyone able to take a look at the attached and see what's happening? I'm starting to think its a driver issue....</p><p><a href="http://sdrv.ms/16uKhsb">Packet Capture</a> <a href="http://sdrv.ms/16uKhsb">http://sdrv.ms/16uKhsb</a></p><p>thanks</p><p>Richard</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Aug '13, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/c115eff93d2ff05f66f0ca88ee38e17a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rcarter15&#39;s gravatar image" /><p><span>rcarter15</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rcarter15 has no accepted answers">0%</span></p></div></div><div id="comments-container-24012" class="comments-container"></div><div id="comment-tools-24012" class="comment-tools"></div><div class="clear"></div><div id="comment-24012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24030"></span>

<div id="answer-container-24030" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24030-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24030-score" class="post-score" title="current number of votes">0</div><span id="post-24030-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Fram 26 contains the last inbound packet coming in from your router. After that, only outbound packets were traced, among those even ARP request which should trigger an immediate reply from your default gateway. Assuming that your Win7 is the only one suffering and the other users on the WLAN are still happily communicating at this time, you're probably with your guess. dumpcap doesn't trace the lower WLAN protocols though to find out who is failing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '13, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/5500bd1decb766660522dfb347eedc49?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrEEde&#39;s gravatar image" /><p><span>mrEEde</span><br />
<span class="score" title="3892 reputation points"><span>3.9k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="70 badges"><span class="bronze">●</span><span class="badgecount">70</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrEEde has 48 accepted answers">20%</span></p></div></div><div id="comments-container-24030" class="comments-container"><span id="24031"></span><div id="comment-24031" class="comment"><div id="post-24031-score" class="comment-score"></div><div class="comment-text"><p>Thanks mrEEde, I've been playing with this all day.</p><p>I have a second Dell laptop which runs a different wireless card, so far this does not seem to display the same problem.</p><p>I have also now installed linux on the machine with the issue.<br />
</p><p>I'd start to think its hardware related, except 802.11g works fine and stable. Its only when I switch to the 802.11n that the problems appear (even with forcing 20mhz channel)</p><p>I've dropped a mail to dell but that might take some time ;-)</p><p>thanks for checking I hadn't missed anything in the packet capture.</p><p>Richard</p></div><div id="comment-24031-info" class="comment-info"><span class="comment-age">(25 Aug '13, 10:52)</span> <span class="comment-user userinfo">rcarter15</span></div></div><span id="24032"></span><div id="comment-24032" class="comment"><div id="post-24032-score" class="comment-score"></div><div class="comment-text"><blockquote><p>dumpcap doesn't trace the lower WLAN protocols though to find out who is failing.</p></blockquote><p>It'll do that <em>if</em> you're capturing in monitor mode, which you can do on OS X, Linux (although you might have to use <a href="http://www.aircrack-ng.org/doku.php?id=airmon-ng">airmon-ng</a>, rather than the Wireshark checkbox or TShark/dumpcap/tcpdump <code>-I</code> flag, to turn monitor mode on), and *BSD, but which you can't do on Windows. Turning on monitor mode on a Wi-Fi adapter might disassociate it from the network, so you might need a separate machine from the machine having the problems - and that machine will obviously need 802.11n support on its Wi-Fi adapter. For protocols above the 802.11 layer, and possibly 802.11 management frames, you may have to worry about <a href="http://wiki.wireshark.org/HowToDecrypt802.11">decrypting protected network (WEP or WPA/WPA2) traffic</a>.</p></div><div id="comment-24032-info" class="comment-info"><span class="comment-age">(25 Aug '13, 11:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="24035"></span><div id="comment-24035" class="comment"><div id="post-24035-score" class="comment-score"></div><div class="comment-text"><p>I can fire up linux on my work laptop, which is also 802.11n and working fine.<br />
</p><p>I'll run a capture from there and see what happens.<br />
</p><p>I'll repost it once I get a failure. ;-)</p><p>thanks</p><p>Richard</p></div><div id="comment-24035-info" class="comment-info"><span class="comment-age">(25 Aug '13, 11:43)</span> <span class="comment-user userinfo">rcarter15</span></div></div></div><div id="comment-tools-24030" class="comment-tools"></div><div class="clear"></div><div id="comment-24030-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

