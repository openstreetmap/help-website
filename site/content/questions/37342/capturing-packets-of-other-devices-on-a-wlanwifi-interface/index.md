+++
type = "question"
title = "capturing packets of other devices on a wlan/wifi interface"
description = '''In wireshark we can capture packets of only our devices in TCP protocol while packets of other devices are captured as broadcast packets in ARP protocol. Is there any way to capture packets of other devices in TCP protocol. I heard we should do some changes in the wi-fi settings. If it is the way in...'''
date = "2014-10-24T17:44:00Z"
lastmod = "2014-10-26T15:27:00Z"
weight = 37342
keywords = [ "packets", "capturing" ]
aliases = [ "/questions/37342" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [capturing packets of other devices on a wlan/wifi interface](/questions/37342/capturing-packets-of-other-devices-on-a-wlanwifi-interface)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37342-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37342-score" class="post-score" title="current number of votes">0</div><span id="post-37342-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In wireshark we can capture packets of only our devices in TCP protocol while packets of other devices are captured as broadcast packets in ARP protocol. Is there any way to capture packets of other devices in TCP protocol. I heard we should do some changes in the wi-fi settings. If it is the way in this case, let me know how can we do that or any other ways.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packets" rel="tag" title="see questions tagged &#39;packets&#39;">packets</span> <span class="post-tag tag-link-capturing" rel="tag" title="see questions tagged &#39;capturing&#39;">capturing</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '14, 17:44</strong></p><img src="https://secure.gravatar.com/avatar/e35c18b4fe32a6eb0aa4b21c55dff6d5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Harish%20Vaibhav&#39;s gravatar image" /><p><span>Harish Vaibhav</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Harish Vaibhav has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Oct '14, 15:28</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-37342" class="comments-container"></div><div id="comment-tools-37342" class="comment-tools"></div><div class="clear"></div><div id="comment-37342-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="37355"></span>

<div id="answer-container-37355" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37355-score" class="post-score" title="current number of votes">0</div><span id="post-37355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I heard we should do some changes in the <strong>wi-fi settings</strong>.</p></blockquote><p>wifi-settings? O.K. so, I 'guess' you are trying to capture wifi/wlan traffic of other machines. If so, please read the <strong>WLAN capture setup</strong> wiki, especially the part about monitor mode!</p><blockquote><p><a href="http://wiki.wireshark.org/CaptureSetup/WLAN">http://wiki.wireshark.org/CaptureSetup/WLAN</a></p></blockquote><p>If you are running Wireshark on Windows, please read my answer to a similar question.</p><blockquote><p><a href="https://ask.wireshark.org/questions/33354/cannot-see-traffic-between-tablet-and-speakers">https://ask.wireshark.org/questions/33354/cannot-see-traffic-between-tablet-and-speakers</a><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Oct '14, 15:27</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-37355" class="comments-container"></div><div id="comment-tools-37355" class="comment-tools"></div><div class="clear"></div><div id="comment-37355-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

