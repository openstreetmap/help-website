+++
type = "question"
title = "How do I get the acknowledgement number for a packet in Wireshark using Lua?"
description = '''I am writing a Lua dissector for a protocol on top of the TCP protocol. It needs to store the acknowledgment number of request packets, in order to determine which is the corresponding response packet. For example I can get the packet number with pinfo.number, is there any similar way I can access t...'''
date = "2012-05-07T03:20:00Z"
lastmod = "2012-05-07T06:57:00Z"
weight = 10723
keywords = [ "pinfo", "dissector", "acknowledgement", "tcp", "lua" ]
aliases = [ "/questions/10723" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I get the acknowledgement number for a packet in Wireshark using Lua?](/questions/10723/how-do-i-get-the-acknowledgement-number-for-a-packet-in-wireshark-using-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10723-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10723-score" class="post-score" title="current number of votes">0</div><span id="post-10723-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a Lua dissector for a protocol on top of the TCP protocol. It needs to store the acknowledgment number of request packets, in order to determine which is the corresponding response packet.</p><p>For example I can get the packet number with pinfo.number, is there any similar way I can access the acknowledgement number?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pinfo" rel="tag" title="see questions tagged &#39;pinfo&#39;">pinfo</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-acknowledgement" rel="tag" title="see questions tagged &#39;acknowledgement&#39;">acknowledgement</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 May '12, 03:20</strong></p><img src="https://secure.gravatar.com/avatar/ada08bfd6a970cd432d168e40d89737e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ville&#39;s gravatar image" /><p><span>Ville</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ville has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '12, 03:55</strong> </span></p></div></div><div id="comments-container-10723" class="comments-container"><span id="10724"></span><div id="comment-10724" class="comment"><div id="post-10724-score" class="comment-score"></div><div class="comment-text"><p>What protocol are you dissecting?</p></div><div id="comment-10724-info" class="comment-info"><span class="comment-age">(07 May '12, 03:37)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="10725"></span><div id="comment-10725" class="comment"><div id="post-10725-score" class="comment-score"></div><div class="comment-text"><p>A special protocol on top of the TCP protocol.</p></div><div id="comment-10725-info" class="comment-info"><span class="comment-age">(07 May '12, 03:56)</span> <span class="comment-user userinfo">Ville</span></div></div></div><div id="comment-tools-10723" class="comment-tools"></div><div class="clear"></div><div id="comment-10723-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="10731"></span>

<div id="answer-container-10731" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10731-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10731-score" class="post-score" title="current number of votes">0</div><span id="post-10731-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can define the desired fields with Field.new() and then use the field definitions in the dissector function.</p><blockquote><p><code>-- define the fields</code><br />
<code>tcp_srcp_f = Field.new("tcp.srcport")</code><br />
<code>tcp_dstp_f = Field.new("tcp.dstport")</code><br />
<strong><code>tcp_ack_f = Field.new("tcp.ack")</code></strong><br />
<code>tcp_seq_f = Field.new("tcp.seq")</code><br />
</p><p><code>function tcp_test_proto.dissector(buffer,pinfo,tree)</code><br />
<code>-- use the fields in the dissector</code><br />
<code>local sport = tcp_srcp_f()</code><br />
<code>local dport = tcp_dstp_f()</code><br />
<strong><code>local ack = tcp_ack_f()</code></strong><br />
<code>local seq = tcp_seq_f()</code><br />
<code>...</code><br />
<code>end</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 May '12, 06:57</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 May '12, 06:58</strong> </span></p></div></div><div id="comments-container-10731" class="comments-container"></div><div id="comment-tools-10731" class="comment-tools"></div><div class="clear"></div><div id="comment-10731-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

