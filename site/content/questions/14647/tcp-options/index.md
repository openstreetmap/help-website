+++
type = "question"
title = "TCP options"
description = '''What will cause the TCP options such as scaling and SACK not to show during the handshake? Would a router or firewall do this? A message of NOP 4 NOP row a router may have removed is reported by Wireshark.'''
date = "2012-10-02T15:00:00Z"
lastmod = "2012-10-07T09:33:00Z"
weight = 14647
keywords = [ "tcp-options" ]
aliases = [ "/questions/14647" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [TCP options](/questions/14647/tcp-options)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14647-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14647-score" class="post-score" title="current number of votes">0</div><span id="post-14647-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>What will cause the TCP options such as scaling and SACK not to show during the handshake? Would a router or firewall do this? A message of NOP 4 NOP row a router may have removed is reported by Wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tcp-options" rel="tag" title="see questions tagged &#39;tcp-options&#39;">tcp-options</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Oct '12, 15:00</strong></p><img src="https://secure.gravatar.com/avatar/9d629f265392eaf7b61f921e25f9f730?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ws2006&#39;s gravatar image" /><p><span>ws2006</span><br />
<span class="score" title="1 reputation points">1</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ws2006 has no accepted answers">0%</span></p></div></div><div id="comments-container-14647" class="comments-container"></div><div id="comment-tools-14647" class="comment-tools"></div><div class="clear"></div><div id="comment-14647-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14648"></span>

<div id="answer-container-14648" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14648-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14648-score" class="post-score" title="current number of votes">5</div><span id="post-14648-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you don't see a TCP option in the handshake packet(s), then the option wasn't there when Wireshark saw the packet. It is possible that the system sending the packet included an option and then an intermediate router, firewall, or other security device stripped out the option and replaced it with a NOP.</p><p>When options are used, the TCP header is expanded in multiples of four bytes to make room for the option(s). If the options do not take all four bytes, then zeroes (NOPs) fill the unused bytes. A sending system will never put four NOPs in a row. If it had no options for that four-byte area, it simply wouldn't add the four bytes at all. As Wireshark is telling you, four NOPs in a row is a strong indication that some intermediate device has removed one or more options and substituted NOPs.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Oct '12, 18:57</strong></p><img src="https://secure.gravatar.com/avatar/071fe61f64868d98bdf4eb060b63b6ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jim%20Aragon&#39;s gravatar image" /><p><span>Jim Aragon</span><br />
<span class="score" title="7187 reputation points"><span>7.2k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="118 badges"><span class="bronze">●</span><span class="badgecount">118</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jim Aragon has 70 accepted answers">24%</span></p></div></div><div id="comments-container-14648" class="comments-container"><span id="14651"></span><div id="comment-14651" class="comment"><div id="post-14651-score" class="comment-score">1</div><div class="comment-text"><p><a href="http://ask.wireshark.org/users/7/lchappell">Laura Chappell</a> suggested this feature during <a href="https://blog.wireshark.org/2010/06/sharkfest-10-recap/">Sharkfest '10</a> and <a href="http://ask.wireshark.org/users/8/stig">Stig Bjørlykke</a> implemented it in <a href="http://anonsvn.wireshark.org/viewvc?view=revision&amp;revision=33265">r33265</a>. Some additional information: <a href="https://www.lcuportal2.com/index.php?option=com_easyblog&amp;view=entry&amp;id=1&amp;Itemid=73">https://www.lcuportal2.com/index.php?option=com_easyblog&amp;view=entry&amp;id=1&amp;Itemid=73</a>.</p></div><div id="comment-14651-info" class="comment-info"><span class="comment-age">(02 Oct '12, 19:27)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="14751"></span><div id="comment-14751" class="comment"><div id="post-14751-score" class="comment-score"></div><div class="comment-text"><p>So with no options with scaling or sack, the window size advertised was 47K. I would assume performance of the application will suffer with these options removed.</p></div><div id="comment-14751-info" class="comment-info"><span class="comment-age">(06 Oct '12, 18:12)</span> <span class="comment-user userinfo">ws2006</span></div></div><span id="14756"></span><div id="comment-14756" class="comment"><div id="post-14756-score" class="comment-score"></div><div class="comment-text"><p>SACK is always good to have, because it is usually the best way to recover from packet loss and has no known downsides if used.</p><p>Window scaling is a different cup of tea: a window too small can be bad, because you can't utilize the available bandwith if the line has high bandwitdh coming with high latency. BUT a window too big is bad, too, since it can lead to buffer overload in routers and switches, leading to packet drops and thus retransmissions.</p></div><div id="comment-14756-info" class="comment-info"><span class="comment-age">(07 Oct '12, 09:33)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-14648" class="comment-tools"></div><div class="clear"></div><div id="comment-14648-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

