+++
type = "question"
title = "How to set capture-filter for l2tp control packets"
description = '''Hello I&#x27;m newbie to Wireshark, not sure if it&#x27;s known question or issue. I use &quot;l2tp.sid==0&quot; to set display-filter to filter l2tp control packets and work well. but it was failed to work w/ capture-filter w/ syntax error. Could anybody to let me know if it&#x27;s possible to set such capture-filter and h...'''
date = "2014-02-13T21:39:00Z"
lastmod = "2014-02-17T22:34:00Z"
weight = 29853
keywords = [ "capture-filter", "l2tp" ]
aliases = [ "/questions/29853" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to set capture-filter for l2tp control packets](/questions/29853/how-to-set-capture-filter-for-l2tp-control-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29853-score" class="post-score" title="current number of votes">0</div><span id="post-29853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello</p><p>I'm newbie to Wireshark, not sure if it's known question or issue. I use "l2tp.sid==0" to set display-filter to filter l2tp control packets and work well. but it was failed to work w/ capture-filter w/ syntax error. Could anybody to let me know if it's possible to set such capture-filter and how if the answer is yes, thanks in advance!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-filter" rel="tag" title="see questions tagged &#39;capture-filter&#39;">capture-filter</span> <span class="post-tag tag-link-l2tp" rel="tag" title="see questions tagged &#39;l2tp&#39;">l2tp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '14, 21:39</strong></p><img src="https://secure.gravatar.com/avatar/3540a8ef2d9764d4e0ad88b01abed52c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="guyin&#39;s gravatar image" /><p><span>guyin</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="guyin has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Sep '16, 12:14</strong> </span></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p><span>sindy</span><br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-29853" class="comments-container"></div><div id="comment-tools-29853" class="comment-tools"></div><div class="clear"></div><div id="comment-29853-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29863"></span>

<div id="answer-container-29863" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29863-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29863-score" class="post-score" title="current number of votes">0</div><span id="post-29863-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Actually L2TP control messages are identified by the control flag in the L2TP header.</p><p>Display filter for control messages</p><blockquote><p>l2tp.type == 1</p></blockquote><p>The same in capture filter syntax (highest bit in the first byte of the UDP payload is the control flag)</p><blockquote><p>udp[8]&gt;&gt;7=1<br />
tcpdump -ni eth0 'udp[8]&gt;&gt;7=1'</p></blockquote><p>If you want to filter for the SID, the following capture filter will work</p><blockquote><p>tcpdump -ni eth0 'udp[14:2]=0'</p></blockquote><p><strong>HINT:</strong> there can be control messages with a SID != 0, so if you only filter for the SID, you might miss some control messages.</p><p>You can obviously also combine the two</p><blockquote><p>tcpdump -ni eth0 'udp[8]&gt;&gt;7=1 and udp[14:2]=0'</p></blockquote><p>which will filter for frames with the control flag set and SID == 0.</p><p><strong>++ UPDATE ++</strong></p><p>For L2TPv3 directly at the IP level (see your comment about DOCSIS), the whole thing works like this:</p><p>According to your screenshot, you can identify L2TPv3 frames in the IP frame with</p><blockquote><p>ip[9]=115</p></blockquote><p>and then you can use the same filters I mentioned above, just adjusted to the new location in the IP frame. The 'limitations' regarding the control message flag and the SID are the <strong>same</strong>.</p><p>So, the full filter would be</p><blockquote><p>tcpdump -ni eth0 'ip[9]=115 and ip[24]&gt;&gt;7=1'</p></blockquote><p>or with the SID</p><blockquote><p>tcpdump -ni eth0 'ip[9]=115 and ip[24]&gt;&gt;7=1 and ip[20:4]=0'</p></blockquote><p><del>I'm not sure regarding the SID (ip[20:4] or ip[20:2] ip[22:2]), as I can't determine that from the screenshot. I <strong>guess</strong> it's ip[20:4].</del></p><p>According to the capture files at bugs.wireshark.org, it is ip[20:4] for the SID (display field: l2tp.sid).</p><p><strong>Hint</strong>: This will only work, if there are no additional IP options. If there are, you need to adjust the offset in the IP frame according to the IP options length.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '14, 02:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>16 Feb '14, 05:20</strong> </span></p></div></div><div id="comments-container-29863" class="comments-container"><span id="29889"></span><div id="comment-29889" class="comment"><div id="post-29889-score" class="comment-score"></div><div class="comment-text"><p>Hi, Kurt</p><p>Thanks for your info. Actually my case is to capture DOCSIS DEPI control packets whihch is L2TPv3 over IP. since there is no UDP and also can't use type flag but control session id to identify the control packets. How can I revise the filters you offered in such case?</p></div><div id="comment-29889-info" class="comment-info"><span class="comment-age">(15 Feb '14, 08:38)</span> <span class="comment-user userinfo">guyin</span></div></div><span id="29893"></span><div id="comment-29893" class="comment"><div id="post-29893-score" class="comment-score"></div><div class="comment-text"><p>can you post a small sample capture file somewhere (google drive, dropbox, cloudshark.org)?</p></div><div id="comment-29893-info" class="comment-info"><span class="comment-age">(15 Feb '14, 10:51)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29899"></span><div id="comment-29899" class="comment"><div id="post-29899-score" class="comment-score"></div><div class="comment-text"><p>Hi, Kurt Pls refer to following link for a screen capture of one DEPI control packets. you can see the l2tp header right next to IP header and session id is 0. I think we can use something like ip[x:y] to represent the session id field but not sure the exact syntax. <a href="https://dl.dropboxusercontent.com/u/83185044/Screen%20Shot%202014-02-16%20at%2010.58.23%20AM.png">https://dl.dropboxusercontent.com/u/83185044/Screen%20Shot%202014-02-16%20at%2010.58.23%20AM.png</a></p></div><div id="comment-29899-info" class="comment-info"><span class="comment-age">(15 Feb '14, 19:04)</span> <span class="comment-user userinfo">guyin</span></div></div><span id="29910"></span><div id="comment-29910" class="comment"><div id="post-29910-score" class="comment-score">1</div><div class="comment-text"><p>see the <strong>++ UPDATE ++</strong> in my answer.</p></div><div id="comment-29910-info" class="comment-info"><span class="comment-age">(16 Feb '14, 03:03)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="29948"></span><div id="comment-29948" class="comment"><div id="post-29948-score" class="comment-score"></div><div class="comment-text"><p>Hi, Kurt</p><p>Thanks a lot for your help! the "ip proto l2tp &amp;&amp; ip[20:4]==0" works fine w/ my case. of course it's not complete just simple to match my specific case. thanks again for your help!</p></div><div id="comment-29948-info" class="comment-info"><span class="comment-age">(17 Feb '14, 19:16)</span> <span class="comment-user userinfo">guyin</span></div></div><span id="29952"></span><div id="comment-29952" class="comment not_top_scorer"><div id="post-29952-score" class="comment-score"></div><div class="comment-text"><p>Of course that's a bit easier to read ;-))</p><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up)</p></div><div id="comment-29952-info" class="comment-info"><span class="comment-age">(17 Feb '14, 22:34)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-29863" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-29863-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

