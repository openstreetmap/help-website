+++
type = "question"
title = "Packet in Binary file but not showing in wireshark gui"
description = '''Hi, i have a strange issue that i hope someone can help me with. I am trying to alleviate network issues for my app. i have 2 traces going one client side and 1 monitoring firewall and server side. I see the packet in the client side but not in the server side. i decided to check the binary file and...'''
date = "2011-04-18T20:40:00Z"
lastmod = "2011-04-18T23:49:00Z"
weight = 3595
keywords = [ "binary", "gui", "traces", "streams" ]
aliases = [ "/questions/3595" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Packet in Binary file but not showing in wireshark gui](/questions/3595/packet-in-binary-file-but-not-showing-in-wireshark-gui)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3595-score" class="post-score" title="current number of votes">0</div><span id="post-3595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i have a strange issue that i hope someone can help me with. I am trying to alleviate network issues for my app. i have 2 traces going one client side and 1 monitoring firewall and server side. I see the packet in the client side but not in the server side. i decided to check the binary file and there is an entry on the server side for this packet as it has a unique http cookie. the only problem i have is that i cannot see it in the gui which means i cannot see the conversation and see if any errors are relted to that particular stream.</p><p>Any help on why this happens would be greatly appreciated.</p><p>Mick</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-binary" rel="tag" title="see questions tagged &#39;binary&#39;">binary</span> <span class="post-tag tag-link-gui" rel="tag" title="see questions tagged &#39;gui&#39;">gui</span> <span class="post-tag tag-link-traces" rel="tag" title="see questions tagged &#39;traces&#39;">traces</span> <span class="post-tag tag-link-streams" rel="tag" title="see questions tagged &#39;streams&#39;">streams</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Apr '11, 20:40</strong></p><img src="https://secure.gravatar.com/avatar/2ff42af4239c7d9eccf458f590828946?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmmchippy&#39;s gravatar image" /><p><span>mmmchippy</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmmchippy has no accepted answers">0%</span></p></div></div><div id="comments-container-3595" class="comments-container"><span id="3598"></span><div id="comment-3598" class="comment"><div id="post-3598-score" class="comment-score"></div><div class="comment-text"><p>If you can see it in tyhe binary pcap file there should be a packet in the GUI with the corresponding content, not necessary a http packet though. What happens if you filter with "frame contains" and the pattern?</p></div><div id="comment-3598-info" class="comment-info"><span class="comment-age">(18 Apr '11, 23:09)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-3595" class="comment-tools"></div><div class="clear"></div><div id="comment-3595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3599"></span>

<div id="answer-container-3599" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3599-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3599-score" class="post-score" title="current number of votes">0</div><span id="post-3599-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Please try the following. Go to the protocol preferences of TCP and then disable "Allow subdissector to reassemble TCP streams". When doing that, the HTTP dissector will not try to reassemble all data into a full HTTP request and response. There can be several causes for the HTTP dissector to fail reassembling and thus showing only "[TCP segment of a reassembled PDU]" packets. Disabling the reassembly will make Wireshark dissect all TCP packets on it's own.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Apr '11, 23:49</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-3599" class="comments-container"></div><div id="comment-tools-3599" class="comment-tools"></div><div class="clear"></div><div id="comment-3599-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

