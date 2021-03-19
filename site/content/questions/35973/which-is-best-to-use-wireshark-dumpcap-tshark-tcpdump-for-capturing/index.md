+++
type = "question"
title = "Which is best to use, Wireshark, DUMPCAP, TSHARK, TCPDUMP for capturing?"
description = '''Everyday between 230PM and 4PM Network gets slow apps get disconnected... We do not drop internet connection from site... We drop Drive mapping back to HQ up North, We Drop Outlook Exchange Connection back to HQ up North.  Users can still access web browser to external sites... We have checked that ...'''
date = "2014-09-03T14:34:00Z"
lastmod = "2014-09-03T16:20:00Z"
weight = 35973
keywords = [ "timeouts", "outlook", "drops", "network", "2010" ]
aliases = [ "/questions/35973" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Which is best to use, Wireshark, DUMPCAP, TSHARK, TCPDUMP for capturing?](/questions/35973/which-is-best-to-use-wireshark-dumpcap-tshark-tcpdump-for-capturing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35973-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35973-score" class="post-score" title="current number of votes">0</div><span id="post-35973-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Everyday between 230PM and 4PM Network gets slow apps get disconnected... We do not drop internet connection from site... We drop Drive mapping back to HQ up North, We Drop Outlook Exchange Connection back to HQ up North.</p><p>Users can still access web browser to external sites... We have checked that no replication is happening, we have checked server logs for DC's here and at HQ up North... There internet connection does not drop either. The VPN between the sites does not show any issues when checking the Sonicwalls at both sites... We are thinking of sniffing the networking internal at our site to see what would cause the drop or slow throughput.</p><p>Which is best to use, Wireshark, DUMPCAP, TSHARK, TCPDUMP for capturing?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timeouts" rel="tag" title="see questions tagged &#39;timeouts&#39;">timeouts</span> <span class="post-tag tag-link-outlook" rel="tag" title="see questions tagged &#39;outlook&#39;">outlook</span> <span class="post-tag tag-link-drops" rel="tag" title="see questions tagged &#39;drops&#39;">drops</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span> <span class="post-tag tag-link-2010" rel="tag" title="see questions tagged &#39;2010&#39;">2010</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '14, 14:34</strong></p><img src="https://secure.gravatar.com/avatar/6eddde40186257f0aabb72ae40ef90c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ITSupportMorrisvilleNC&#39;s gravatar image" /><p><span>ITSupportMor...</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ITSupportMorrisvilleNC has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Sep '14, 16:19</strong> </span></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span></p></div></div><div id="comments-container-35973" class="comments-container"></div><div id="comment-tools-35973" class="comment-tools"></div><div class="clear"></div><div id="comment-35973-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35976"></span>

<div id="answer-container-35976" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35976-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35976-score" class="post-score" title="current number of votes">0</div><span id="post-35976-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>TCPDump is fine, dumpcap is fine, too. Wireshark and tshark are both using dumpcap to do the capture for them, so it is usually best to use dumpcap directly without the overhead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '14, 16:20</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-35976" class="comments-container"></div><div id="comment-tools-35976" class="comment-tools"></div><div class="clear"></div><div id="comment-35976-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

