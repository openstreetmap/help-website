+++
type = "question"
title = "Broadcast Packet? why?"
description = '''hi there, i am new to wireshark and as i was learning it, i noticed that my smc router is sending packets to itself every second. under the protocol column, wireshark shows 0xffff. not sure why this is happening but maybe someone can explain it to me? is this normal? thanks in advance for any explai...'''
date = "2011-05-18T21:29:00Z"
lastmod = "2011-05-19T03:16:00Z"
weight = 4130
keywords = [ "broadcast", "smc" ]
aliases = [ "/questions/4130" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Broadcast Packet? why?](/questions/4130/broadcast-packet-why)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4130-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4130-score" class="post-score" title="current number of votes">0</div><span id="post-4130-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi there, i am new to wireshark and as i was learning it, i noticed that my smc router is sending packets to itself every second. under the protocol column, wireshark shows 0xffff. not sure why this is happening but maybe someone can explain it to me? is this normal? thanks in advance for any explainations.</p><p>Ethernet II, Src: SmcNetwo_0e:46:12 (12:26:f3:0e:46:12), Dst: SmcNetwo_0e:46:12 (00:26:f3:0e:46:12)</p><p>Destination: SmcNetwo_0e:46:12 (00:26:f3:0e:46:12) Address: SmcNetwo_0e:46:12 (00:26:f3:0e:46:12) .... ...0 .... .... .... .... = IG bit: Individual address (unicast) .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default)</p><p>Source: SmcNetwo_0e:46:12 (12:26:f3:0e:46:12) Address: SmcNetwo_0e:46:12 (12:26:f3:0e:46:12) .... ...1 .... .... .... .... = IG bit: Group address (multicast/broadcast) .... ..0. .... .... .... .... = LG bit: Globally unique address (factory default) Type: Unknown (0xffff)</p><p>Data (46 bytes) Data: 802814180580040000000000000000000000000000000000...</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-broadcast" rel="tag" title="see questions tagged &#39;broadcast&#39;">broadcast</span> <span class="post-tag tag-link-smc" rel="tag" title="see questions tagged &#39;smc&#39;">smc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '11, 21:29</strong></p><img src="https://secure.gravatar.com/avatar/e74a04e3d0ffd527c470255c6eb2f6a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="learner&#39;s gravatar image" /><p><span>learner</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="learner has no accepted answers">0%</span></p></div></div><div id="comments-container-4130" class="comments-container"></div><div id="comment-tools-4130" class="comment-tools"></div><div class="clear"></div><div id="comment-4130-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4135"></span>

<div id="answer-container-4135" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4135-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4135-score" class="post-score" title="current number of votes">1</div><span id="post-4135-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How very interesting. If a person constantly talks to himself he will soon be committed.</p><p>The packets that you see are most likely the SMC way to identify a loop caused by 2 ports connected to each other.</p><p>Other vendors implement loop detection in one way or other. For example, Wireshark nicely decodes the Loop packets send by Cisco switches. The vendor independent feature would be the Spanning Tree Protocol or Rapid Spanning Tree.</p><p>Happy learning!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 May '11, 03:16</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p><span>packethunter</span><br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-4135" class="comments-container"></div><div id="comment-tools-4135" class="comment-tools"></div><div class="clear"></div><div id="comment-4135-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

