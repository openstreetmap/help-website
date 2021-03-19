+++
type = "question"
title = "PDU reassembly over UDP within a lua dissector"
description = '''Hi, I&#x27;m willing to build a dissector able to reassemble PDUs spanned accross multiple UDP packets. My protocol have sequence/fragment IDs/total length, so there&#x27;s everything needed to reassemble properly. If i&#x27;m not mistaken there&#x27;s no automated assembly mechanism like for TCP within the API ( pinfo...'''
date = "2013-12-13T05:39:00Z"
lastmod = "2013-12-13T06:40:00Z"
weight = 28076
keywords = [ "lua", "dissector", "reassembly" ]
aliases = [ "/questions/28076" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [PDU reassembly over UDP within a lua dissector](/questions/28076/pdu-reassembly-over-udp-within-a-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28076-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28076-score" class="post-score" title="current number of votes">1</div><span id="post-28076-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm willing to build a dissector able to reassemble PDUs spanned accross multiple UDP packets. My protocol have sequence/fragment IDs/total length, so there's everything needed to reassemble properly.</p><p>If i'm not mistaken there's no automated assembly mechanism like for TCP within the API ( pinfo.desegment_len etc). So I take it I would have to implement a manual re-assembly.</p><p>But how can I pass data between 2 frames / dissector calls ? Tvb can only be declared/used in a dissector so can't store my fragment in a tvb variable. I tried to store it in a ByteArray and then use bytearray&lt;-&gt;tvb conversions methods with no luck, wireshark crashes, probably because of ByteArray's maximum sizes (overflow)</p><p>Also, whilst a manual re-assembly might work on a first pass, how about random access when clicking ?</p><p>Any suggestions ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Dec '13, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/e4e8bc4618a9948a893ae407b22e8160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lepolac&#39;s gravatar image" /><p><span>lepolac</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lepolac has no accepted answers">0%</span></p></div></div><div id="comments-container-28076" class="comments-container"></div><div id="comment-tools-28076" class="comment-tools"></div><div class="clear"></div><div id="comment-28076-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28077"></span>

<div id="answer-container-28077" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28077-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28077-score" class="post-score" title="current number of votes">0</div><span id="post-28077-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Basically you will need to implement the same re-assembly routines in your protocol dissector as are implemented in the IP and the TCP dissector. Have a look at the support functions for reassmbly that can be found in "epan/reassemble.h" and how they are used in the IP and TCP dissector.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Dec '13, 06:39</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-28077" class="comments-container"><span id="28078"></span><div id="comment-28078" class="comment"><div id="post-28078-score" class="comment-score"></div><div class="comment-text"><p>Oops, just realized you are using Lua instead of C. Not sure how many support routines there are in Lua regarding reassembly...</p></div><div id="comment-28078-info" class="comment-info"><span class="comment-age">(13 Dec '13, 06:40)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-28077" class="comment-tools"></div><div class="clear"></div><div id="comment-28077-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

