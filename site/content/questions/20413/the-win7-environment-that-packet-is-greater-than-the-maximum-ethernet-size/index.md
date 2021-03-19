+++
type = "question"
title = "The win7 environment that packet is greater than the maximum Ethernet size"
description = '''During the data analysis process, the client packet greater than the size of the Ethernet standard. Can help explain why. https://www.cloudshark.org/captures/8e164cd10b06 thank you.'''
date = "2013-04-15T04:39:00Z"
lastmod = "2013-04-15T19:22:00Z"
weight = 20413
keywords = [ "analysis", "tcp" ]
aliases = [ "/questions/20413" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The win7 environment that packet is greater than the maximum Ethernet size](/questions/20413/the-win7-environment-that-packet-is-greater-than-the-maximum-ethernet-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20413-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20413-score" class="post-score" title="current number of votes">0</div><span id="post-20413-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>During the data analysis process, the client packet greater than the size of the Ethernet standard. Can help explain why. <a href="https://www.cloudshark.org/captures/8e164cd10b06">https://www.cloudshark.org/captures/8e164cd10b06</a> thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-analysis" rel="tag" title="see questions tagged &#39;analysis&#39;">analysis</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Apr '13, 04:39</strong></p><img src="https://secure.gravatar.com/avatar/c66d8077ef5f4d265694332542e2fbd4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mengsunny&#39;s gravatar image" /><p><span>mengsunny</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mengsunny has no accepted answers">0%</span></p></div></div><div id="comments-container-20413" class="comments-container"></div><div id="comment-tools-20413" class="comment-tools"></div><div class="clear"></div><div id="comment-20413-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="20414"></span>

<div id="answer-container-20414" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-20414-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-20414-score" class="post-score" title="current number of votes">1</div><span id="post-20414-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You captured on the PC with the IP address 21.235.28.153, which had "TCP large send offloading" activated in the network card driver. That means that the CPU will push large chunks of data to the network card, where it will be segmented into valid sizes - but that only happens <strong>after</strong> Wireshark already recording it.</p><p>Capture on the other system to see that valid packets arrive, or turn of network card acceleration settings like Large Send Offload and CRC calculation (which means slowing down your PC, which is usually not a good idea).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Apr '13, 04:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-20414" class="comments-container"><span id="20415"></span><div id="comment-20415" class="comment"><div id="post-20415-score" class="comment-score"></div><div class="comment-text"><p>Adjust the MTU value of the client, the problem has been resolved, but the large size of the package still exists, but does not need to be fragmented. Can you help explain why？ <a href="https://www.cloudshark.org/captures/ba5845e9e8c7">https://www.cloudshark.org/captures/ba5845e9e8c7</a></p></div><div id="comment-20415-info" class="comment-info"><span class="comment-age">(15 Apr '13, 04:53)</span> <span class="comment-user userinfo">mengsunny</span></div></div><span id="20416"></span><div id="comment-20416" class="comment"><div id="post-20416-score" class="comment-score"></div><div class="comment-text"><p>This has <strong>nothing</strong> to do with MTU. This is TCP segmentation, so on a totally different layer.</p></div><div id="comment-20416-info" class="comment-info"><span class="comment-age">(15 Apr '13, 04:55)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div><span id="20439"></span><div id="comment-20439" class="comment"><div id="post-20439-score" class="comment-score">1</div><div class="comment-text"><p>I.e., if you want to see the packets as they appear on the network, rather than as they are supplied to Wireshark by the system on which you're running Wireshark, you would either need to capture on another machine (so that you see packets captured from the wire rather than packets wrapped around to Wireshark in software) or turn off the TCP segmentation offload (so that the packets that get wrapped around to Wireshark in software look more like packets as they'll be transmitted on the wire).</p><p>Nothing you did with the MTU would have any effect on that.</p></div><div id="comment-20439-info" class="comment-info"><span class="comment-age">(15 Apr '13, 15:18)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="20441"></span><div id="comment-20441" class="comment"><div id="post-20441-score" class="comment-score"></div><div class="comment-text"><p>Capturing packets do not see this on the server side. Thank you very much help.</p></div><div id="comment-20441-info" class="comment-info"><span class="comment-age">(15 Apr '13, 19:22)</span> <span class="comment-user userinfo">mengsunny</span></div></div></div><div id="comment-tools-20414" class="comment-tools"></div><div class="clear"></div><div id="comment-20414-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

