+++
type = "question"
title = "Can&#x27;t sniff wifi"
description = '''I want to sniff wifi packets with wireshark but monitor mode seems to fail. I&#x27;m using backtrack 5 and an alpha AWUS036H wifi usb card, i try to sniff my own box without encryption. Here is what i&#x27;m doing to activate monitor mode :  root@root:~# airmon-ng start wlan0  wich seems to be working :  root...'''
date = "2012-02-05T05:16:00Z"
lastmod = "2012-02-07T00:39:00Z"
weight = 8832
keywords = [ "broadcast", "wifi" ]
aliases = [ "/questions/8832" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Can't sniff wifi](/questions/8832/cant-sniff-wifi)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8832-score" class="post-score" title="current number of votes">0</div><span id="post-8832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to sniff wifi packets with wireshark but monitor mode seems to fail. I'm using backtrack 5 and an alpha AWUS036H wifi usb card, i try to sniff my own box without encryption.</p><p>Here is what i'm doing to activate monitor mode :</p><blockquote><p><span class="__cf_email__" data-cfemail="ccbea3a3b88cbea3a3b8">[email protected]</span>:~# airmon-ng start wlan0</p></blockquote><p>wich seems to be working :</p><blockquote><p><span class="__cf_email__" data-cfemail="addfc2c2d9eddfc2c2d9">[email protected]</span>:~# iwconfig mon0<br />
mon0 IEEE 802.11bg Mode:Monitor Tx-Power=20 dBm<br />
Retry long limit:7 RTS thr:off Fragment thr:off<br />
Power Management:on</p></blockquote><p>However when i start capturing on mon0 in wireshark i'm only getting broadcast packets. In capture options the "capture packets in monitor mode" option is grayed out.</p><p>I do not understand what's going on. Any Ideas ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-wifi" rel="tag" title="see questions tagged &#39;wifi&#39;">wifi</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Feb '12, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/0ed6886a56f1c415f49c38ac4cf89762?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kyori&#39;s gravatar image" /><p><span>kyori</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kyori has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-8832" class="comments-container"><span id="8844"></span><div id="comment-8844" class="comment"><div id="post-8844-score" class="comment-score"></div><div class="comment-text"><p>use airodump-ng and look at the tracefile saved from it, if thats working it might be a wireshark issue, if not make sure your wlan0 device is NOT used to connect to a wireless network, which might corrupt your monitor mode settings on mon0</p></div><div id="comment-8844-info" class="comment-info"><span class="comment-age">(06 Feb '12, 05:02)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="8852"></span><div id="comment-8852" class="comment"><div id="post-8852-score" class="comment-score"></div><div class="comment-text"><p>At least with some versions of Linux and some devices and drivers, you can run in monitor mode when connected to a wireless network. Given the <code>wlan0</code> and <code>mon0</code>, the driver for the adapter is probably a mac80211 driver, so I wouldn't be surprised if it supported running in monitor mode when connected to a wireless network.</p></div><div id="comment-8852-info" class="comment-info"><span class="comment-age">(06 Feb '12, 09:06)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="8870"></span><div id="comment-8870" class="comment"><div id="post-8870-score" class="comment-score"></div><div class="comment-text"><p>Right, that <em>should</em> work - I was just suggesting there might be a conflict if the card already seems to be in mon. mode but the issues appear it might be a conflict where normally there shouldn't be one</p></div><div id="comment-8870-info" class="comment-info"><span class="comment-age">(07 Feb '12, 00:39)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-8832" class="comment-tools"></div><div class="clear"></div><div id="comment-8832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

