+++
type = "question"
title = "UDP heuristic dissector to be invoked only when UDP checksum is zero"
description = '''I am building a heuristic dissector for the UDP protocol and would like it to be activated only when the UDP checksum of a packet is 0 (zero). How shall I approach that? At the moment, the tvb passed to my UDP heuristic dissector only contains the bytes starting after the UDP header so I cannot chec...'''
date = "2015-03-02T05:51:00Z"
lastmod = "2015-03-02T12:29:00Z"
weight = 40184
keywords = [ "heuristic", "dissector" ]
aliases = [ "/questions/40184" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [UDP heuristic dissector to be invoked only when UDP checksum is zero](/questions/40184/udp-heuristic-dissector-to-be-invoked-only-when-udp-checksum-is-zero)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40184-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am building a heuristic dissector for the UDP protocol and would like it to be activated only when the UDP checksum of a packet is 0 (zero).</p><p>How shall I approach that?</p><p>At the moment, the tvb passed to my UDP heuristic dissector only contains the bytes starting <em>after</em> the UDP header so I cannot check the checksum anymore. Is the checksum value part of pinfo maybe?</p><p>I initially tried to set up the dissector with the following command but it did not work: dissector_add_uint("udp.checksum", 0x0000, udp_handle);</p></div><div id="question-tags" class="tags-container tags">heuristic dissector</div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Mar '15, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/258615514217bb9b718d4738b80328c8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxvirrozeito&#39;s gravatar image" /><p>maxvirrozeito<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxvirrozeito has no accepted answers">0%</span></p></div></div><div id="comments-container-40184" class="comments-container"></div><div id="comment-tools-40184" class="comment-tools"></div><div class="clear"></div><div id="comment-40184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40190"></span>

<div id="answer-container-40190" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40190-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is no mechanism to support that. Subdissectors don't get passed the headers for the containing protocol, the checksum is not provided in any other fashion, and <code>dissector_add_uint()</code> does not take an arbitrary field as an argument, it takes the name of a dissector table registered by the containing protocol's dissector, and the only table the UDP dissector provides is one for the port number.</p><p>Either you'll have to make a hacked version of Wireshark or you'll have to figure out some <em>other</em> way of identifying your protocol's packets (which you should probably do anyway, as there's no guarantee that a zero checksum means it's your protocol).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Mar '15, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-40190" class="comments-container"><span id="40222"></span><div id="comment-40222" class="comment"><div id="post-40222-score" class="comment-score"></div><div class="comment-text"><p>I will add all the relevant UDP ports to the dissector table - it will be a better way of detecting my protocol. I initially wanted to avoid that as it involves a few thousands ports.</p></div><div id="comment-40222-info" class="comment-info"><span class="comment-age">(03 Mar '15, 09:41)</span> maxvirrozeito</div></div></div><div id="comment-tools-40190" class="comment-tools"></div><div class="clear"></div><div id="comment-40190-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

