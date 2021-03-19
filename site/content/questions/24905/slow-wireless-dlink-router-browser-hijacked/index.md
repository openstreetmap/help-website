+++
type = "question"
title = "Slow Wireless, Dlink router, Browser hijacked"
description = '''Hi, My wireless is very slow although I&#x27;ve standard settings. Wireless router is Dlink dir 655. A  few weeks ago I discovered that my DNS settings on that router had changed (my DNS settings  gone, free dns was enabled on the Dlink).  I &#x27;ve put back my old settings, cleaned my laptop with several an...'''
date = "2013-09-18T05:09:00Z"
lastmod = "2013-09-18T15:39:00Z"
weight = 24905
keywords = [ "wireless", "dlink", "hijacked", "browser" ]
aliases = [ "/questions/24905" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Slow Wireless, Dlink router, Browser hijacked](/questions/24905/slow-wireless-dlink-router-browser-hijacked)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24905-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24905-score" class="post-score" title="current number of votes">0</div><span id="post-24905-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>My wireless is very slow although I've standard settings. Wireless router is Dlink dir 655. A few weeks ago I discovered that my DNS settings on that router had changed (my DNS settings gone, free dns was enabled on the Dlink).</p><p>I 've put back my old settings, cleaned my laptop with several antispyy and malware tools (cleaned lot of weird entry's and I saw my browser was hijacked) and thought it would all be fine, but no way wireless is still very slow.</p><p>I've made some wireshark captures (wireless connection through Dlink) and was wondering what the following entry's mean:</p><p>7 0.000551000 6.274776000 192.168.0.105 224.0.0.252 LLMNR 64 Standard query 0xda6b A wpad 607</p><p><strong>Who or what is ip 224.0.0.252</strong>?</p><p>14 0.248453000 8.064420000 192.168.0.105 192.168.1.35 TCP 74 1564 &gt; 445 [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=4 SACK_PERM=1 TSval=224816 TSecr=0 1174</p><p>Why is my pc (192.168.0.105) asking for my NAS (192.168.1.35),although I have no mappings, flushed dns, deleted arp table, and the NAS isn't at the network at this moment)?</p><p>Hope you can help in trouble shooting my slow wireless,</p><p>Thank you, regards Marco</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-dlink" rel="tag" title="see questions tagged &#39;dlink&#39;">dlink</span> <span class="post-tag tag-link-hijacked" rel="tag" title="see questions tagged &#39;hijacked&#39;">hijacked</span> <span class="post-tag tag-link-browser" rel="tag" title="see questions tagged &#39;browser&#39;">browser</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Sep '13, 05:09</strong></p><img src="https://secure.gravatar.com/avatar/38fcdf7c9733dc854d2545deb14e8dcf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wiredshark&#39;s gravatar image" /><p><span>wiredshark</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wiredshark has no accepted answers">0%</span></p></div></div><div id="comments-container-24905" class="comments-container"></div><div id="comment-tools-24905" class="comment-tools"></div><div class="clear"></div><div id="comment-24905-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24906"></span>

<div id="answer-container-24906" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24906-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24906-score" class="post-score" title="current number of votes">1</div><span id="post-24906-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The first entry is for <a href="http://en.wikipedia.org/wiki/Link-local_Multicast_Name_Resolution">link-local multicast name resolution</a> and is quite normal for windows systems.</p><p>The second is your PC attempting to open a TCP connection to the NAS on port 445, and again is quite normal for windows systems, your PC is trying to do something with a file share on the NAS.</p><p>Unfortunately neither of these is likely to be the cause of your wireless slowdown.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Sep '13, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-24906" class="comments-container"><span id="24928"></span><div id="comment-24928" class="comment"><div id="post-24928-score" class="comment-score"></div><div class="comment-text"><p>Thank you grahamb for the answer,</p><p>I must change the titel of this post..at the moment my wired connection is also very slow :-( I've opened the Interface Details &gt; 802.3 (Ethernet)tab in Wireshark and noticed:</p><p>Statistics</p><p>Packets transmitted with heartbeat failure 16830</p><p>All of the other statistics in that tab are 0</p><p>What are these heartbeat failures?</p><p>regards, marco</p></div><div id="comment-24928-info" class="comment-info"><span class="comment-age">(18 Sep '13, 15:39)</span> <span class="comment-user userinfo">wiredshark</span></div></div></div><div id="comment-tools-24906" class="comment-tools"></div><div class="clear"></div><div id="comment-24906-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

