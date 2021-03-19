+++
type = "question"
title = "how to find the maximum segment size"
description = '''I have this wireshark file with a list of traffics. I want to find the maximum segment size of a TCP segment but I can&#x27;t find it. I saw online that this is normally found when you expand the TCP line and under the &quot;Options&quot; line, but I can&#x27;t seem to find the Options line, all it has under TCP is &quot;Fl...'''
date = "2012-05-06T23:29:00Z"
lastmod = "2012-05-07T01:33:00Z"
weight = 10713
keywords = [ "mss" ]
aliases = [ "/questions/10713" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how to find the maximum segment size](/questions/10713/how-to-find-the-maximum-segment-size)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10713-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10713-score" class="post-score" title="current number of votes">0</div><span id="post-10713-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have this wireshark file with a list of traffics. I want to find the maximum segment size of a TCP segment but I can't find it. I saw online that this is normally found when you expand the TCP line and under the "Options" line, but I can't seem to find the Options line, all it has under TCP is "Flags", "Checksum", and "SEQ/ACK Analysis".</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mss" rel="tag" title="see questions tagged &#39;mss&#39;">mss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 May '12, 23:29</strong></p><img src="https://secure.gravatar.com/avatar/f126d43120341d8eff8c980d639fd83c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JenniferJ88&#39;s gravatar image" /><p><span>JenniferJ88</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JenniferJ88 has no accepted answers">0%</span></p></div></div><div id="comments-container-10713" class="comments-container"></div><div id="comment-tools-10713" class="comment-tools"></div><div class="clear"></div><div id="comment-10713-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10714"></span>

<div id="answer-container-10714" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10714-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10714-score" class="post-score" title="current number of votes">1</div><span id="post-10714-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can find the MSS option only in the SYN and SYN/ACK packets. They are set once and will be used for the whole session.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 May '12, 23:54</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-10714" class="comments-container"><span id="10715"></span><div id="comment-10715" class="comment"><div id="post-10715-score" class="comment-score"></div><div class="comment-text"><p>Ya it's an SYN packet but there's still no MSS option...</p></div><div id="comment-10715-info" class="comment-info"><span class="comment-age">(07 May '12, 00:00)</span> <span class="comment-user userinfo">JenniferJ88</span></div></div><span id="10716"></span><div id="comment-10716" class="comment"><div id="post-10716-score" class="comment-score"></div><div class="comment-text"><p>it only has the window size, but I guess that's not the MSS...</p></div><div id="comment-10716-info" class="comment-info"><span class="comment-age">(07 May '12, 00:06)</span> <span class="comment-user userinfo">JenniferJ88</span></div></div><span id="10717"></span><div id="comment-10717" class="comment"><div id="post-10717-score" class="comment-score"></div><div class="comment-text"><p>Then a MSS is not advertised, which means both sides will base the MSS on the MTU of the link they use for sending the traffic.</p><p>Assuming both systems are connected by ethernet, they will use 1500 minus the IP header length minus the TCP header length. So when no additional IP and TCP options are used, they will use an MSS of 1500 - 20 - 20 = 1460.</p></div><div id="comment-10717-info" class="comment-info"><span class="comment-age">(07 May '12, 00:06)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="10718"></span><div id="comment-10718" class="comment"><div id="post-10718-score" class="comment-score"></div><div class="comment-text"><p>So is there a way to find the MTU in wireshark traces?</p></div><div id="comment-10718-info" class="comment-info"><span class="comment-age">(07 May '12, 00:23)</span> <span class="comment-user userinfo">JenniferJ88</span></div></div><span id="10719"></span><div id="comment-10719" class="comment"><div id="post-10719-score" class="comment-score"></div><div class="comment-text"><p>Only by deducting it from the maximum packet length found in a TCP session. The actual MTU value is not sent.</p></div><div id="comment-10719-info" class="comment-info"><span class="comment-age">(07 May '12, 00:27)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="10721"></span><div id="comment-10721" class="comment not_top_scorer"><div id="post-10721-score" class="comment-score"></div><div class="comment-text"><p>@ SYN-Bit: You gotta be careful about that -&gt; I have seen systems using a fallback MSS os 536 (576 min. MTU -20 -20) when no MSS in found in TCP options during handshake</p></div><div id="comment-10721-info" class="comment-info"><span class="comment-age">(07 May '12, 01:33)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-10714" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-10714-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

