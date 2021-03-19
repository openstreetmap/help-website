+++
type = "question"
title = "TCP capture filter performance"
description = '''I think it may be a naive question, but I also want to make sure of this; I&#x27;m wondering if this could affect pefromance of a tap or the program speed: I want to filter syn packets using(tcp.flags.syn==1), I know it is implicitly filter the tcp protocal, is there any need to mention the TCP protocol ...'''
date = "2012-12-05T00:56:00Z"
lastmod = "2012-12-05T01:23:00Z"
weight = 16572
keywords = [ "tap", "tcp", "wireshark" ]
aliases = [ "/questions/16572" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TCP capture filter performance](/questions/16572/tcp-capture-filter-performance)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16572-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I think it may be a naive question, but I also want to make sure of this; I'm wondering if this could affect pefromance of a tap or the program speed: I want to filter syn packets using(tcp.flags.syn==1), I know it is implicitly filter the tcp protocal, is there any need to mention the TCP protocol explicitly again inside the filter of the tap??</p></div><div id="question-tags" class="tags-container tags">tap tcp wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Dec '12, 00:56</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p>Leena<br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Dec '12, 04:53</p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-16572" class="comments-container"></div><div id="comment-tools-16572" class="comment-tools"></div><div class="clear"></div><div id="comment-16572-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16573"></span>

<div id="answer-container-16573" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16573-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>You mean, do you need to filter on "tcp.flags.syn==1 and tcp"? No, tcp.flags.syn==1 is enough in itself, it will only look at the packets containing the TCP protocol layer. Speed-wise I don't think it makes much difference to additionally specifiy "tcp" since the filter checks that anyway, so I guess it gets optimized anyway.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Dec '12, 01:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-16573" class="comments-container"><span id="16577"></span><div id="comment-16577" class="comment"><div id="post-16577-score" class="comment-score"></div><div class="comment-text"><p>Thanks alot</p></div><div id="comment-16577-info" class="comment-info"><span class="comment-age">(05 Dec '12, 02:06)</span> Leena</div></div><span id="16741"></span><div id="comment-16741" class="comment"><div id="post-16741-score" class="comment-score"></div><div class="comment-text"><p>@Jasper: I want to be sure of this although I checked on it by trials on wireshark, I need to filter ipv4 and in the filter I have ip address in ipv4(ip.src==172.16.0.0/12),so as the rule above it will implicitly filter the ipv4,right?? no need to write (ip) in the filter? Thanks a alot, and sorry to disturb you.</p></div><div id="comment-16741-info" class="comment-info"><span class="comment-age">(09 Dec '12, 23:06)</span> Leena</div></div><span id="16743"></span><div id="comment-16743" class="comment"><div id="post-16743-score" class="comment-score">1</div><div class="comment-text"><p>no, ip.src is enough to make sure the filter works. And you're not disturbing ;-)</p></div><div id="comment-16743-info" class="comment-info"><span class="comment-age">(10 Dec '12, 01:32)</span> Jasper ♦♦</div></div><span id="16754"></span><div id="comment-16754" class="comment"><div id="post-16754-score" class="comment-score"></div><div class="comment-text"><p>@Jasper:Thanks a lot, but if I use (not ip.src==172.16.0.0/12)to filter inbound traffic I should mention ipv4 in the filter explicitly,right?? I tried it with just a display filter in a pcap and packets with ipv6 still there.</p></div><div id="comment-16754-info" class="comment-info"><span class="comment-age">(10 Dec '12, 12:19)</span> Leena</div></div><span id="16755"></span><div id="comment-16755" class="comment"><div id="post-16755-score" class="comment-score">1</div><div class="comment-text"><p>which makes sense, because all you're saying is "do not show me ipv4 addresses of the network 172.16.0.0/12". You need to add "and not ipv6" to also remove ipv6 traffic. Or just go "ip and not ip.src==172.16.0.0/12" to remove everything that is not IPv4 as well as the network you don't want.</p></div><div id="comment-16755-info" class="comment-info"><span class="comment-age">(10 Dec '12, 12:32)</span> Jasper ♦♦</div></div></div><div id="comment-tools-16573" class="comment-tools"></div><div class="clear"></div><div id="comment-16573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

