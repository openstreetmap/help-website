+++
type = "question"
title = "can&#x27;t see any tcp/udp/icmp traffic"
description = '''i’m update wireshark to 2.2.4 version on my mac os (10.12.2)   i can’t see any tcp/udp/icmp traffice when i using capture packet in monitor and promiscuous mode , but i can see the 802.11 and eap frame . i’m uninstall the Wireshark 2.2.4 back to 1.12.12 , the issue is still. open my computer other f...'''
date = "2017-02-23T21:54:00Z"
lastmod = "2017-02-24T03:00:00Z"
weight = 59652
keywords = [ "software" ]
aliases = [ "/questions/59652" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [can't see any tcp/udp/icmp traffic](/questions/59652/cant-see-any-tcpudpicmp-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59652-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59652-score" class="post-score" title="current number of votes">0</div><span id="post-59652-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i’m update wireshark to 2.2.4 version on my mac os (10.12.2) i can’t see any tcp/udp/icmp traffice when i using capture packet in monitor and promiscuous mode , but i can see the 802.11 and eap frame . i’m uninstall the Wireshark 2.2.4 back to 1.12.12 , the issue is still. open my computer other file also can't see any tcp/udp/icmp traffice. <img src="https://osqa-ask.wireshark.org/upfiles/p22_eE7DRMb.png" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-software" rel="tag" title="see questions tagged &#39;software&#39;">software</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Feb '17, 21:54</strong></p><img src="https://secure.gravatar.com/avatar/8c6817d0d35d3558d66ce198a3a4dba5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daniel%20wang&#39;s gravatar image" /><p><span>daniel wang</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daniel wang has no accepted answers">0%</span></p></img></div></div><div id="comments-container-59652" class="comments-container"></div><div id="comment-tools-59652" class="comment-tools"></div><div class="clear"></div><div id="comment-59652-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59656"></span>

<div id="answer-container-59656" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59656-score" class="post-score" title="current number of votes">1</div><span id="post-59656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To see the layer 3+ information in 802.11 captures you need two things, at a minimum:</p><ol><li>Data frames</li><li>Decryption capability if the data is encrypted (good practice says it should be...)</li></ol><p>For item 2, here is a good link: <a href="https://wiki.wireshark.org/HowToDecrypt802.11">https://wiki.wireshark.org/HowToDecrypt802.11</a></p><p>I bring up item 1 because it is a common cause of issue when working with wireless packet captures. The data frames tend to go at higher data rates so require better capture capability to match the modulation capabilities of the AP and the client. In particular, I do not see data frames in your picture but do see ACKs. With no more information than this picture, it appears you are not able to capture data frames; however, MAC laptops are known to be excellent capture tools. Something does not look right. You sill have to solve this problem first before working on decryption.</p><p>As a test, you may be able to reduce the AP's capabilities so it uses lower data rates and then it will be easier to capture data frames. Otherwise, provide more information on the setup of the system you are analyzing - it could be you are just out of range to capture the high speed frames, etc.</p><p>I use this free tool on my MAC to speed up capture setup:</p><p><a href="https://www.adriangranados.com/apps/airtool">https://www.adriangranados.com/apps/airtool</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Feb '17, 03:00</strong></p><img src="https://secure.gravatar.com/avatar/0a47ef51dd9c9996d194a4983295f5a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bob%20Jones&#39;s gravatar image" /><p><span>Bob Jones</span><br />
<span class="score" title="1014 reputation points"><span>1.0k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bob Jones has 19 accepted answers">21%</span></p></div></div><div id="comments-container-59656" class="comments-container"></div><div id="comment-tools-59656" class="comment-tools"></div><div class="clear"></div><div id="comment-59656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

