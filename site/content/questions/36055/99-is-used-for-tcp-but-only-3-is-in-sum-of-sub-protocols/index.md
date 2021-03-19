+++
type = "question"
title = "99% is used for TCP but only 3% is in sum of sub-protocols!"
description = '''Actually our server is using 30Mb/s right now, we captured current flow with wireshark, however what we saw is suprising, in Protocol Hierachy Statistics, it shows that 99% of this huge traffic is from TCP section but when I click on the + sign to see sub-protocols, it just shows 3% of it is in HTTP...'''
date = "2014-09-07T05:12:00Z"
lastmod = "2014-09-07T10:17:00Z"
weight = 36055
keywords = [ "ack", "dup-ack", "ddos" ]
aliases = [ "/questions/36055" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [99% is used for TCP but only 3% is in sum of sub-protocols!](/questions/36055/99-is-used-for-tcp-but-only-3-is-in-sum-of-sub-protocols)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36055-score" class="post-score" title="current number of votes">0</div><span id="post-36055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Actually our server is using 30Mb/s right now, we captured current flow with wireshark, however what we saw is suprising, in Protocol Hierachy Statistics, it shows that 99% of this huge traffic is from TCP section but when I click on the + sign to see sub-protocols, it just shows 3% of it is in HTTP and other protocols and 96% source of remaining traffic is not shown at all.</p><p>I suspect ACK packets as they are the most packets in the capture, So what can cause this and how can we fix it?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-dup-ack" rel="tag" title="see questions tagged &#39;dup-ack&#39;">dup-ack</span> <span class="post-tag tag-link-ddos" rel="tag" title="see questions tagged &#39;ddos&#39;">ddos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '14, 05:12</strong></p><img src="https://secure.gravatar.com/avatar/3e9fd7f18de149592f70b85b744e24ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CIT%20Developer&#39;s gravatar image" /><p><span>CIT Developer</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CIT Developer has no accepted answers">0%</span></p></div></div><div id="comments-container-36055" class="comments-container"></div><div id="comment-tools-36055" class="comment-tools"></div><div class="clear"></div><div id="comment-36055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36057"></span>

<div id="answer-container-36057" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36057-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36057-score" class="post-score" title="current number of votes">0</div><span id="post-36057-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The protocol hierarchy shows all protocols that Wireshark could determine, so e.g. for 99% TCP it determined 3% to be HTTP. You're right saying that ACK packets are not classified as HTTP (even if they are part of a HTTP communication) since they do not carry a HTTP payload. If you download a huge file over HTTP Wireshark may label the packets transporting the segments as TCP instead of HTTP since there are no HTTP headers/keywords in that payload.</p><p>What you could do if you wonder about the protocols being used in that 99% is to use the Conversations Statistic to see what ports are used, and filter on conversations to see what content the TCP packets have. The protocol column of the packet list will tell you what protocol Wireshark determined, so if it says "TCP" it didn't find anything more specific.</p><p>Maybe you have standard protocols like HTTP running on non-standard ports, which may prevent Wireshark from determining what the conversations contain. For HTTP you can add more ports in the protocol preference setting to help Wireshark detect it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '14, 08:51</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36057" class="comments-container"><span id="36059"></span><div id="comment-36059" class="comment"><div id="post-36059-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your help, Actually it was related to netlimiter application there was something related to it, After I uninstalled netlimiter the ack packets just gone</p></div><div id="comment-36059-info" class="comment-info"><span class="comment-age">(07 Sep '14, 10:17)</span> <span class="comment-user userinfo">CIT Developer</span></div></div></div><div id="comment-tools-36057" class="comment-tools"></div><div class="clear"></div><div id="comment-36057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

