+++
type = "question"
title = "Spanning tree for bridges"
description = '''18 2012-11-08 07:58:03.331868 3comEuro_6c:a0:2c Spanning-tree-(for-bridges)_00 STP 120 MST. Root = 32768/0/00:1e:c1:6c:9f:fa Cost = 0 Port = 0x8032  Why does this appear/occur every 2 seconds on my network? Is it really necessary for it to occur every 2 seconds?'''
date = "2013-01-29T09:18:00Z"
lastmod = "2013-01-29T19:44:00Z"
weight = 18042
keywords = [ "spanningtree", "stp" ]
aliases = [ "/questions/18042" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Spanning tree for bridges](/questions/18042/spanning-tree-for-bridges)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18042-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><pre><code>18  2012-11-08 07:58:03.331868  3comEuro_6c:a0:2c   Spanning-tree-(for-bridges)_00  STP 120 MST. Root = 32768/0/00:1e:c1:6c:9f:fa  Cost = 0  Port = 0x8032</code></pre><p>Why does this appear/occur every 2 seconds on my network? Is it really necessary for it to occur every 2 seconds?</p></div><div id="question-tags" class="tags-container tags">spanningtree stp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jan '13, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/ab34e9a43e48b9cb007396154d2c7436?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cherokee&#39;s gravatar image" /><p>cherokee<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cherokee has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jan '13, 09:22</p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-18042" class="comments-container"></div><div id="comment-tools-18042" class="comment-tools"></div><div class="clear"></div><div id="comment-18042-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="18043"></span>

<div id="answer-container-18043" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18043-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you need <a href="http://en.wikipedia.org/wiki/Spanning_Tree_Protocol">spanning-tree</a> in your network depends on your network topology. If you only have one switch (or a switch-stack), then you probably don't need it (unless you are afraid people will connect two ports by accident). You can configure your switches to not use spanning-tree to get rid of these packets.</p><p>But if you do need spanning-tree because you have multiple paths between switches, then yes, you need these messages in your network to do the loop detection and automatic reconfiguration of your switches in case a link fails.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 09:26</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-18043" class="comments-container"><span id="18047"></span><div id="comment-18047" class="comment"><div id="post-18047-score" class="comment-score"></div><div class="comment-text"><p>not to forget - "every 2 seconds" is an eternity in today's networks, so apart from sometimes being annoying in the packet list, BPDU frames do not hurt the network bandwidth.</p></div><div id="comment-18047-info" class="comment-info"><span class="comment-age">(29 Jan '13, 10:03)</span> Jasper ♦♦</div></div><span id="18072"></span><div id="comment-18072" class="comment"><div id="post-18072-score" class="comment-score"></div><div class="comment-text"><p>It's like car insurance. You don't need it until you need it! So don't disable spanning tree. It's so insignificant that it's not even a packet....it's just a frame! :)</p></div><div id="comment-18072-info" class="comment-info"><span class="comment-age">(29 Jan '13, 19:41)</span> hansangb</div></div></div><div id="comment-tools-18043" class="comment-tools"></div><div class="clear"></div><div id="comment-18043-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="18073"></span>

<div id="answer-container-18073" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18073-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>By the way, Spanning Tree was developed to prevent layer 2 loops from occurring. In IP world, the TTL field can be used to prevent packets from looping around forever. However, there is no such field in an Ethernet frame. As a result, if you create a L2 loop, the frames will fly around infinitely. Creating a L2 loop is a great way to test the "real throughput" of any switch! :)<br />
</p><p>Spanning tree's job is to make sure that there is only one path to the root bridge (king of the hill). this way, even if you have redundant uplinks (not part of etherchannel) you are guaranteed <em>not</em> to have loops at layer 2. That's the sole purpose of spanning tree. Insuring that your L2 network is loop free.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jan '13, 19:44</strong></p><img src="https://secure.gravatar.com/avatar/63805f079ac429902641cad9d7cd69e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="hansangb&#39;s gravatar image" /><p>hansangb<br />
<span class="score" title="791 reputation points">791</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="hansangb has 7 accepted answers">12%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 30 Jan '13, 00:07</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-18073" class="comments-container"><span id="18141"></span><div id="comment-18141" class="comment"><div id="post-18141-score" class="comment-score"></div><div class="comment-text"><p>oops! Thanks Graham! I left the <em>not</em> out, I take it? :)</p></div><div id="comment-18141-info" class="comment-info"><span class="comment-age">(30 Jan '13, 16:23)</span> hansangb</div></div><span id="18146"></span><div id="comment-18146" class="comment"><div id="post-18146-score" class="comment-score"></div><div class="comment-text"><p>I changed a "look" into "loop".</p></div><div id="comment-18146-info" class="comment-info"><span class="comment-age">(30 Jan '13, 23:47)</span> grahamb ♦</div></div></div><div id="comment-tools-18073" class="comment-tools"></div><div class="clear"></div><div id="comment-18073-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

