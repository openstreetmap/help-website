+++
type = "question"
title = "IP Addr. Generating the Most Traffic"
description = '''On our network, we noticed a spike in network utilization on a specific date at a specific time. Ever since then the network utilization is extemely high. I want to sniff the network and determine what IP addresses are generating all of the activity. How do I do that? '''
date = "2011-10-11T13:11:00Z"
lastmod = "2011-10-11T14:29:00Z"
weight = 6850
keywords = [ "question", "network", "analysis" ]
aliases = [ "/questions/6850" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [IP Addr. Generating the Most Traffic](/questions/6850/ip-addr-generating-the-most-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6850-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>On our network, we noticed a spike in network utilization on a specific date at a specific time. Ever since then the network utilization is extemely high. I want to sniff the network and determine what IP addresses are generating all of the activity. How do I do that?<br />
</p></div><div id="question-tags" class="tags-container tags">question network analysis</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Oct '11, 13:11</strong></p><img src="https://secure.gravatar.com/avatar/3187e63ea376c874d8fa4baa5406503e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Netguru&#39;s gravatar image" /><p>Netguru<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Netguru has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-6850" class="comments-container"></div><div id="comment-tools-6850" class="comment-tools"></div><div class="clear"></div><div id="comment-6850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6855"></span>

<div id="answer-container-6855" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6855-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>For me, a good start is always a look at the network topology. You do have a recent topology, don't you?</p><p>If you notice a peak in the utilization you either want to record traffic at a choke point, like a router or a firewall; or you capture traffic for a whole network segment.</p><p>If you capture traffic at a choke point you need to mirror the traffic from the choke point to an analysis port. Unless you have a low-end switch the switch manual/website should explain how to do this. Look for SPAN ports, analysis ports or monitor ports. If you have an unmanaged switch check out the <a href="http://www.dual-comm.com/" title="Dualcomm">Dualcomm</a> portable tap.</p><p>Capturing traffic for "the whole segment" can be very difficult, if it spans over several switches. If you can focus on one switch you might get away with mirroring a whole VLAN.</p><p>Once the mirror port is defined install and fire up Wireshark. I prefer using a dedicated device for Wireshark and try not to install Wireshark on a server. To avoid any interference from my analysis device I disable all bindings, esp. IP.</p><p>The rest is easy: Capture away until you have your spike recorded. <strong>Statistics -&gt; Endpoints -&gt; IP</strong> reveals your top talkers and listener.</p><p>More ideas on can be found in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/" title="Wireshark User&#39;s Guide">Wireshark User's Guide</a> and the <a href="http://wiki.wireshark.org/" title="Wireshark Wiki">Wireshark Wiki</a>.</p><p>Be sure to try <strong>Statistics -&gt; IO-Graphs</strong> to visualize the spike.</p><p>Good hunting!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '11, 14:29</strong></p><img src="https://secure.gravatar.com/avatar/3b60e92020a427bb24332efc0b560943?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="packethunter&#39;s gravatar image" /><p>packethunter<br />
<span class="score" title="2137 reputation points"><span>2.1k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="48 badges"><span class="bronze">●</span><span class="badgecount">48</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="packethunter has 8 accepted answers">8%</span></p></div></div><div id="comments-container-6855" class="comments-container"></div><div id="comment-tools-6855" class="comment-tools"></div><div class="clear"></div><div id="comment-6855-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

