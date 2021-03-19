+++
type = "question"
title = "Large fragmented ICMP issue"
description = '''When i request 12000 bytes(ping size) then i see that fragmentation happens  so after fragmentation result shows (1480*8) + 168 bytes = 12000  so last frame size should be 168(data)+20(IP)+8(ICMP)+14(frame header) = 210 Bytes  but as i saw frame length is showing 202 Bytes.. why ICMP packet are not ...'''
date = "2015-03-14T22:24:00Z"
lastmod = "2015-03-15T08:32:00Z"
weight = 40567
keywords = [ "fragment", "icmp" ]
aliases = [ "/questions/40567" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Large fragmented ICMP issue](/questions/40567/large-fragmented-icmp-issue)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40567-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40567-score" class="post-score" title="current number of votes">0</div><span id="post-40567-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When i request 12000 bytes(ping size) then i see that fragmentation happens</p><p>so after fragmentation result shows (1480*8) + 168 bytes = 12000</p><p>so last frame size should be 168(data)+20(IP)+8(ICMP)+14(frame header) = 210 Bytes</p><p>but as i saw frame length is showing 202 Bytes.. why ICMP packet are not added only for fragmented packet.</p><p>for normal 32 bytes ICMP condition it works fine..</p><p>Jasper could you please help me on that<br />
</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-fragment" rel="tag" title="see questions tagged &#39;fragment&#39;">fragment</span> <span class="post-tag tag-link-icmp" rel="tag" title="see questions tagged &#39;icmp&#39;">icmp</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '15, 22:24</strong></p><img src="https://secure.gravatar.com/avatar/69a5598823733e13a51c1a2a0ae4ee9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lvi&#39;s gravatar image" /><p><span>Lvi</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lvi has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> converted to question <strong>15 Mar '15, 03:32</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-40567" class="comments-container"></div><div id="comment-tools-40567" class="comment-tools"></div><div class="clear"></div><div id="comment-40567-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40575"></span>

<div id="answer-container-40575" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40575-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40575-score" class="post-score" title="current number of votes">0</div><span id="post-40575-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Keep in mind that when IP fragments a large ICMP packet (or any packet, actually) only the first will have the ICMP (or other layer 4) header. All others will just have the remaining payload fragments right after the IPv4 header. Check your 9 packets - the first has Ethernet/IP/ICMP/payload, all other 8 packets will only have Ethernet/IP/payload.</p><p>So the 8 byte you're missing is the ICMP header. Also, the first packet only has 1472 bytes ping payload, because of the header (so 1480 is the ICMP header plus payload).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Mar '15, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40575" class="comments-container"></div><div id="comment-tools-40575" class="comment-tools"></div><div class="clear"></div><div id="comment-40575-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

