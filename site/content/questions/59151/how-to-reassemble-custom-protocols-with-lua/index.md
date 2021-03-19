+++
type = "question"
title = "How to reassemble custom protocols with Lua?"
description = '''I have a custom protocol which combines to make a higher level protocol. It is analogous to HTTP over TCP but it is NOT either of those. I have implemented a custom dissector for the lower level custom protocol. I used one of the DLT_USER linktypes to register the protocol in my lua plugin. I manage...'''
date = "2017-01-30T08:31:00Z"
lastmod = "2017-01-30T10:36:00Z"
weight = 59151
keywords = [ "linktype", "reassembly", "custom", "dissector", "lua" ]
aliases = [ "/questions/59151" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to reassemble custom protocols with Lua?](/questions/59151/how-to-reassemble-custom-protocols-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59151-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59151-score" class="post-score" title="current number of votes">0</div><span id="post-59151-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have a custom protocol which combines to make a higher level protocol. It is analogous to HTTP over TCP but it is NOT either of those.</p><p>I have implemented a custom dissector for the lower level custom protocol. I used one of the DLT_USER linktypes to register the protocol in my lua plugin. I managed to successfully dissect all of the fields required in this "subprotocol".</p><p>Now, I would like to "reassemble" or combine packets of this subprotocol to display the higher level protocol. I am struggling to figure out how to do this. I have found some documentation relating to TCP reassembly, but I am not sure reassembly will work with my custom protocol since it is not TCP and it has its own custom linktype.</p><p>I am wondering if a tap is the right solution for me?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-linktype" rel="tag" title="see questions tagged &#39;linktype&#39;">linktype</span> <span class="post-tag tag-link-reassembly" rel="tag" title="see questions tagged &#39;reassembly&#39;">reassembly</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jan '17, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/86e107d43c8198a9eb0490a92dc3988d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GTOET_half_full&#39;s gravatar image" /><p><span>GTOET_half_full</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GTOET_half_full has no accepted answers">0%</span></p></div></div><div id="comments-container-59151" class="comments-container"><span id="59156"></span><div id="comment-59156" class="comment"><div id="post-59156-score" class="comment-score"></div><div class="comment-text"><p>Can anybody confirm the validity of this answer on stackoverflow?</p><p><a href="http://stackoverflow.com/questions/38630416/wireshark-lua-dissector-reassembly-dissector-not-called-with-previous-tvbs-da">http://stackoverflow.com/questions/38630416/wireshark-lua-dissector-reassembly-dissector-not-called-with-previous-tvbs-da</a></p></div><div id="comment-59156-info" class="comment-info"><span class="comment-age">(30 Jan '17, 10:36)</span> <span class="comment-user userinfo">GTOET_half_full</span></div></div></div><div id="comment-tools-59151" class="comment-tools"></div><div class="clear"></div><div id="comment-59151-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="59152"></span>

<div id="answer-container-59152" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-59152-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-59152-score" class="post-score" title="current number of votes">0</div><span id="post-59152-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would recommend visiting the Wireshark <a href="https://wiki.wireshark.org/Lua/Examples">Lua/Examples</a> wiki page and reviewing some of the example Lua files provided there. In particular, <a href="https://wiki.wireshark.org/Lua/Examples?action=AttachFile&amp;do=get&amp;target=fpm.lua">fpm.lua</a>, which performs reassembly of packets. It's TCP-based, but hopefully it provides a nice starting point for you. I'm not sure, but I don't <em>think</em> the technique employed is limited to only TCP-based protocols.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>30 Jan '17, 08:50</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-59152" class="comments-container"><span id="59153"></span><div id="comment-59153" class="comment"><div id="post-59153-score" class="comment-score"></div><div class="comment-text"><p>Thank you for your response. I have delved into that file already and it is hard to tell whether or not the techniques in it can work with non-TCP based protocols. I have tried playing with the pinfo.desegment_len but to no avail so far...</p></div><div id="comment-59153-info" class="comment-info"><span class="comment-age">(30 Jan '17, 09:15)</span> <span class="comment-user userinfo">GTOET_half_full</span></div></div></div><div id="comment-tools-59152" class="comment-tools"></div><div class="clear"></div><div id="comment-59152-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

