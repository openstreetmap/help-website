+++
type = "question"
title = "Wireshark packet loss"
description = '''Hi, My VoIP application is running on a windows PC at 1 end and on a android device at the other over a wifi network. My usecase needs the windows side to only send data and android side to only receive. I am running wireshark on windows PC and tcpdump on android device to capture all the voip data....'''
date = "2012-07-16T02:59:00Z"
lastmod = "2012-07-23T06:49:00Z"
weight = 12741
keywords = [ "packetloss" ]
aliases = [ "/questions/12741" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark packet loss](/questions/12741/wireshark-packet-loss)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12741-score" class="post-score" title="current number of votes">0</div><span id="post-12741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>My VoIP application is running on a windows PC at 1 end and on a android device at the other over a wifi network. My usecase needs the windows side to only send data and android side to only receive. I am running wireshark on windows PC and tcpdump on android device to capture all the voip data. I am getting to see some packet drops in the android side dump. But the windows side pcap dump does not indicate any packet drops. I have verified that my code is not missing any packets and is sucessfully calling sendto() for all the packets. Does this mean -<br />
1. The packets are dropped in the wifi network OR 2. The packets are dropped in the stack layer on the windows side and is never sent to the network / the packets are received by the android device but is dropped in the stack layer?</p><p>I would greatly appreciate any help on this. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Jul '12, 02:59</strong></p><img src="https://secure.gravatar.com/avatar/b8d5a27b2f8b20402faf470468bf2ec9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="abhiram&#39;s gravatar image" /><p><span>abhiram</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="abhiram has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-12741" class="comments-container"></div><div id="comment-tools-12741" class="comment-tools"></div><div class="clear"></div><div id="comment-12741-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="12913"></span>

<div id="answer-container-12913" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-12913-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-12913-score" class="post-score" title="current number of votes">0</div><span id="post-12913-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It is possible, though unlikely, that the packets are being dropped in the Windows stack below where Wireshark (actually WinPCAP) captures the packets. More likely is that they are being dropped in the network or possibly on the Android device. To further diagnose you'll probably need additional monitoring points (e.g., another computer connected to a HUB--not a switch--between the Windows PC and the wifi network).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>23 Jul '12, 06:49</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-12913" class="comments-container"></div><div id="comment-tools-12913" class="comment-tools"></div><div class="clear"></div><div id="comment-12913-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

