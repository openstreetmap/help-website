+++
type = "question"
title = "wireshark 1.12.4 on windows, reports dst multicast 224.0.0.9 as being IGMPv2"
description = '''I&#x27;m seeing that 224.0.0.9 is detected as IGMPv2 by wireshark and not RIP as it shouold be .  i checked the IGMPv2 RFC but it never indicates that this 224.0.0.9 is used by the protocol .Only RIP does .  ftp://mood.ateme.com/Clement/IGMPv2.jpg do you know why wireshark is seeing this ?'''
date = "2015-04-29T07:21:00Z"
lastmod = "2015-04-29T12:35:00Z"
weight = 41943
keywords = [ "igmpv2", "224.0.0.9", "rip" ]
aliases = [ "/questions/41943" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [wireshark 1.12.4 on windows, reports dst multicast 224.0.0.9 as being IGMPv2](/questions/41943/wireshark-1124-on-windows-reports-dst-multicast-224009-as-being-igmpv2)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41943-score" class="post-score" title="current number of votes">0</div><span id="post-41943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm seeing that 224.0.0.9 is detected as IGMPv2 by wireshark and not RIP as it shouold be .</p><p>i checked the IGMPv2 RFC but it never indicates that this 224.0.0.9 is used by the protocol .Only RIP does .<br />
</p><p><a href="ftp://mood.ateme.com/Clement/IGMPv2.jpg">ftp://mood.ateme.com/Clement/IGMPv2.jpg</a></p><p>do you know why wireshark is seeing this ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-igmpv2" rel="tag" title="see questions tagged &#39;igmpv2&#39;">igmpv2</span> <span class="post-tag tag-link-224.0.0.9" rel="tag" title="see questions tagged &#39;224.0.0.9&#39;">224.0.0.9</span> <span class="post-tag tag-link-rip" rel="tag" title="see questions tagged &#39;rip&#39;">rip</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Apr '15, 07:21</strong></p><img src="https://secure.gravatar.com/avatar/8e6dd7c871572d92dd7f45f2b07cc330?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Clement%20Duval&#39;s gravatar image" /><p><span>Clement Duval</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Clement Duval has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-41943" class="comments-container"><span id="41944"></span><div id="comment-41944" class="comment"><div id="post-41944-score" class="comment-score"></div><div class="comment-text"><p>What is the protocol field value in your IP header?</p></div><div id="comment-41944-info" class="comment-info"><span class="comment-age">(29 Apr '15, 08:03)</span> <span class="comment-user userinfo">Pascal Quantin</span></div></div></div><div id="comment-tools-41943" class="comment-tools"></div><div class="clear"></div><div id="comment-41943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41950"></span>

<div id="answer-container-41950" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41950-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41950-score" class="post-score" title="current number of votes">1</div><span id="post-41950-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's not the destination address that defines this packet as IGMP, it's the IP protocol number which identifies this as IGMP. RIP(2) is running over UDP, a different IP protocol.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Apr '15, 12:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41950" class="comments-container"></div><div id="comment-tools-41950" class="comment-tools"></div><div class="clear"></div><div id="comment-41950-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

