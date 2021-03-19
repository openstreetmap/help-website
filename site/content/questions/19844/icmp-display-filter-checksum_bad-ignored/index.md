+++
type = "question"
title = "ICMP display filter checksum_bad ignored"
description = '''I was searching for icmp.checksum_bad==1 and found no matches, which was seemingly a good thing; however, when I changed the filter to icmp.checksum_bad==0, I also got no matches. My conclusion is that Wireshark is not computing checksum_bad either way, and is ignoring the display filter specificati...'''
date = "2013-03-26T09:30:00Z"
lastmod = "2013-03-26T11:19:00Z"
weight = 19844
keywords = [ "checksum", "icmp" ]
aliases = [ "/questions/19844" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [ICMP display filter checksum\_bad ignored](/questions/19844/icmp-display-filter-checksum_bad-ignored)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19844-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was searching for icmp.checksum_bad==1 and found no matches, which was seemingly a good thing; however, when I changed the filter to icmp.checksum_bad==0, I also got no matches. My conclusion is that Wireshark is not computing checksum_bad either way, and is ignoring the display filter specification.<br />
</p><p>My question is thus: is there a way to get Wireshark to calculate icmp.checksum_bad properly, so that I can rely on it to locate icmp checksum errors?</p><p>I did confirm that I had plenty of captured icmp packets.</p><p>A similar mechanism on ip header checksums, using ip.checksum_bad produced the expected results where ip.checksum_bad==1 produced no results, but ip.checksum_bad==0 matched every packet.</p><p>Another difference I noted was in the expansion of the ip header in a captured packet vs. the expansion of the ICMP packet: there was no checksum_bad field under checksum for ICMP but there was for IP.</p></div><div id="question-tags" class="tags-container tags">checksum icmp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Mar '13, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/8dc3c1d8b364b8f52c6d2b833851fe72?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="alank25&#39;s gravatar image" /><p>alank25<br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="alank25 has one accepted answer">100%</span> </br></p></div></div><div id="comments-container-19844" class="comments-container"></div><div id="comment-tools-19844" class="comment-tools"></div><div class="clear"></div><div id="comment-19844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="19846"></span>

<div id="answer-container-19846" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19846-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>The icmp.checksum_bad was only being added to the tree, thus was only filterable, in the case of a bad checksum, i.e., "icmp.checksum_bad==1" would match those ICMP packets with bad ICMP checksums; however, "icmp.checksum_bad==0" would not have worked, as you've discovered.</p><p>I committed a change in <a href="http://anonsvn.wireshark.org/viewvc?revision=48563&amp;view=revision">r48563</a> to fix that, and I've <a href="http://wiki.wireshark.org/Development/Roadmap">scheduled</a> the change to be backported to both 1.8.7 and 1.6.15.</p><p>Note that in some cases, such as when a snaplen is applied and not all packet bytes are available, the ICMP checksum can't be verified. In this case, "icmp.checksum_bad" will not be set either way as it's simply unknown.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '13, 11:19</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-19846" class="comments-container"><span id="19888"></span><div id="comment-19888" class="comment"><div id="post-19888-score" class="comment-score"></div><div class="comment-text"><p>I confirmed that with the display filter icmp.checksum_bad==1, Wireshark did display an offending packet.</p></div><div id="comment-19888-info" class="comment-info"><span class="comment-age">(27 Mar '13, 15:34)</span> alank25</div></div></div><div id="comment-tools-19846" class="comment-tools"></div><div class="clear"></div><div id="comment-19846-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

