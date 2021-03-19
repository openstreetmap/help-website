+++
type = "question"
title = "Can Wireshark get around AP isolation?"
description = '''If a network router has been set to isolate every client (clients cannot see or communicate with each other) like in a VPN, will Wireshark be able to read the packets of other computers on the network?'''
date = "2013-04-08T07:18:00Z"
lastmod = "2013-04-08T07:38:00Z"
weight = 20177
keywords = [ "access", "accesspoint" ]
aliases = [ "/questions/20177" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Can Wireshark get around AP isolation?](/questions/20177/can-wireshark-get-around-ap-isolation)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20177-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20177-score" class="post-score" title="current number of votes">0</div><span id="post-20177-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>If a network router has been set to isolate every client (clients cannot see or communicate with each other) like in a VPN, will Wireshark be able to read the packets of other computers on the network?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-access" rel="tag" title="see questions tagged &#39;access&#39;">access</span> <span class="post-tag tag-link-accesspoint" rel="tag" title="see questions tagged &#39;accesspoint&#39;">accesspoint</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Apr '13, 07:18</strong></p><img src="https://secure.gravatar.com/avatar/7b4efaaccee9b7c05099987a675abd7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Charlie%20Kucukterzi&#39;s gravatar image" /><p><span>Charlie Kucu...</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Charlie Kucukterzi has no accepted answers">0%</span></p></div></div><div id="comments-container-20177" class="comments-container"></div><div id="comment-tools-20177" class="comment-tools"></div><div class="clear"></div><div id="comment-20177-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20179"></span>

<div id="answer-container-20179" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20179-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20179-score" class="post-score" title="current number of votes">2</div><span id="post-20179-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Charlie Kucukterzi has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Your question title is:</p><blockquote><p>Can Wireshark get around <strong>AP</strong> isolation?</p></blockquote><p>You question is:</p><blockquote><p>If a <strong>network router</strong> has been set to isolate every</p></blockquote><p>Are we talking about a wifi/wlan AP/router or a 'standard router' with a built-in switch?</p><p>As for the wifi/wlan AP: Wireshark will see the <strong>whole</strong> WLAN traffic if your capturing device operates in monitor mode. Client isolation is just a filter within the AP. So, in this case the answer would be: Yes you can get around client isolation, as you will see the whole WLAN traffic.</p><p>As for a 'standard router' with a built-in switch: If there is a feature called 'client isolation' at all (I have never seen such a thing), I would assume that this will prevent packets of device A to be seen by device B. As both are connected to the internal switch of the router, the switch will implement a filter to prevent packets from device B to be sent to the port of device A and vice versa. In that case, the answer is NO, you can't get around client isolation unless you tap into both (all) physical lines of device A and device B.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Apr '13, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Apr '13, 07:25</strong> </span></p></div></div><div id="comments-container-20179" class="comments-container"><span id="20180"></span><div id="comment-20180" class="comment"><div id="post-20180-score" class="comment-score"></div><div class="comment-text"><p>Yes I meant the Wifi router. Thanks. People keep mentioning the "monitor mode" but I only have the promiscuous mode and I'm assuming it means the same thing.</p></div><div id="comment-20180-info" class="comment-info"><span class="comment-age">(08 Apr '13, 07:36)</span> <span class="comment-user userinfo">Charlie Kucu...</span></div></div><span id="20181"></span><div id="comment-20181" class="comment"><div id="post-20181-score" class="comment-score">1</div><div class="comment-text"><blockquote><p>but I only have the promiscuous mode and I'm assuming it means the same thing.</p></blockquote><p>no, it's not the same thing on a wifi/wlan network.</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN#Monitor_mode">http://wiki.wireshark.org/CaptureSetup/WLAN#Monitor_mode</a></p></blockquote></div><div id="comment-20181-info" class="comment-info"><span class="comment-age">(08 Apr '13, 07:38)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-20179" class="comment-tools"></div><div class="clear"></div><div id="comment-20179-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

