+++
type = "question"
title = "Memcache and TCP"
description = '''When I do a scan on Wireshark. The protocol Memcache comes up at least 100 times every second. Only responding and coming from my PC, none other on the network. Also noticing (my computer only) that a lot of TCP protocols. lots, There are over 270,000 Protocols within 10 minutes, mostly belonging to...'''
date = "2013-09-09T21:46:00Z"
lastmod = "2013-10-16T22:17:00Z"
weight = 24495
keywords = [ "virus", "slow", "memcache", "tcp", "internet" ]
aliases = [ "/questions/24495" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Memcache and TCP](/questions/24495/memcache-and-tcp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24495-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I do a scan on Wireshark. The protocol Memcache comes up at least 100 times every second. Only responding and coming from my PC, none other on the network.</p><p>Also noticing (my computer only) that a lot of TCP protocols. lots, There are over 270,000 Protocols within 10 minutes, mostly belonging to TCP and Memcache.</p><p>Any help to what this could be would be appreciated, I think that this is the reason my network may be slower than it should be.</p><p>I should also add, some of the TCP repeatedly go to a verizon website, I never wen't with Verizon before, nobody in the household has either. possibly a virus?</p></div><div id="question-tags" class="tags-container tags">virus slow memcache tcp internet</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '13, 21:46</strong></p><img src="https://secure.gravatar.com/avatar/2b549b1de3eacbcdbf55c1a2b197b67f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zefeldo&#39;s gravatar image" /><p>Zefeldo<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zefeldo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 09 Sep '13, 21:48</p></div></div><div id="comments-container-24495" class="comments-container"><span id="24506"></span><div id="comment-24506" class="comment"><div id="post-24506-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The <strong>protocol Memcache</strong> comes up at least 100 times every second</p></blockquote><p>TCP or UDP, source port or destination port?</p><blockquote><p>There are over 270,000 Protocols within 10 minutes,</p></blockquote><p>by 'protocols' you mean different TCP/UDP connections or packets?</p></div><div id="comment-24506-info" class="comment-info"><span class="comment-age">(10 Sep '13, 00:01)</span> Kurt Knochner ♦</div></div><span id="24531"></span><div id="comment-24531" class="comment"><div id="post-24531-score" class="comment-score"></div><div class="comment-text"><p>oh, sorry, the protocols, i meant packets but 90% of them are the protocol TCP or Memcache.</p><p>random ports from different packets:</p><pre><code>Memcache - Src port: memcache (11211), dst port: 33929 
TCP - Src port: (10378), Dst Port: bacula-sd (9103) 
TCP - Src port: rbd-dsb-disp (1571), Dst Port: https (443)</code></pre><p>if you need more i can provide, i hope none of these may end up accidentally being myself going to a website, pretty sure none are, pretty new to wireshark (will learn in time) thanks for the help</p></div><div id="comment-24531-info" class="comment-info"><span class="comment-age">(10 Sep '13, 10:22)</span> Zefeldo</div></div><span id="24538"></span><div id="comment-24538" class="comment"><div id="post-24538-score" class="comment-score"></div><div class="comment-text"><blockquote><p>if you need more i can provide,</p></blockquote><p>ports are good, IP addresses are better.</p><blockquote><p>i hope none of these may end up accidentally being myself going to a website,</p></blockquote><p>impossible to tell without the capture file or at least some parts of it.</p></div><div id="comment-24538-info" class="comment-info"><span class="comment-age">(10 Sep '13, 15:09)</span> Kurt Knochner ♦</div></div><span id="24877"></span><div id="comment-24877" class="comment"><div id="post-24877-score" class="comment-score"></div><div class="comment-text"><p>I suppose I will upload a file if somebody would like to view it, i'll make sure my computer is the only computer on the network atleast, other than my game consoles.</p></div><div id="comment-24877-info" class="comment-info"><span class="comment-age">(17 Sep '13, 20:20)</span> Zefeldo</div></div><span id="24882"></span><div id="comment-24882" class="comment"><div id="post-24882-score" class="comment-score"></div><div class="comment-text"><p>Go ahead. I'll check it.</p></div><div id="comment-24882-info" class="comment-info"><span class="comment-age">(18 Sep '13, 00:25)</span> Kurt Knochner ♦</div></div><span id="26094"></span><div id="comment-26094" class="comment not_top_scorer"><div id="post-26094-score" class="comment-score"></div><div class="comment-text"><p>sorry for the long wait for a response, i tried to add a download link, but (can't remember the name of it) marked it as spam (from this website) anyway, here it is <a href="http://www.mediafire.com/download/va1a541mluia55v/Network.pcapng">http://www.mediafire.com/download/va1a541mluia55v/Network.pcapng</a></p></div><div id="comment-26094-info" class="comment-info"><span class="comment-age">(16 Oct '13, 17:53)</span> Zefeldo</div></div></div><div id="comment-tools-24495" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-24495-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="26098"></span>

<div id="answer-container-26098" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-26098-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Looks like BitTorrent traffic to me. Check your bittorrent client to see if it is running while you're capturing data, and if it uses UDP port 11211 as its data port. I guess Wireshark gets confused because it thinks that UDP 11211 is MEMCACHE while it isn't. It's just a coincidence that the other protocol (I guess BitTorrent) is set to use that port. If you want to continue capturing while using that port for protocols other than MEMCACHE you might want to change the port setting of the MEMCACHE protocol decoder in the preferences, or disable it completely (Analyze -&gt; Enabled Protocols -&gt; uncheck "MEMCACHE").</p><p>Regarding the 270,000 protocols in 10 minutes - this is just an interpretation error. Clients use ephemeral ports for communicating with servers, and Wireshark labels them according to the services file. So the client ports get funny protocol labels most of the time even though it is not using the protocol at all. You might want to disable the "resolve transport names" option in the name resolution settings of your preferences to avoid further confusion.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '13, 22:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '13, 22:19</p></div></div><div id="comments-container-26098" class="comments-container"></div><div id="comment-tools-26098" class="comment-tools"></div><div class="clear"></div><div id="comment-26098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

