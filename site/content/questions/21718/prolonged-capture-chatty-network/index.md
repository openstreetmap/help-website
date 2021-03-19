+++
type = "question"
title = "Prolonged Capture / chatty network"
description = '''I want to do a prolonged capture (24 hours) segmented into either 24 or 48 capture files (depending on size). Here is my issue... I&#x27;m scanning an uplink port on a main switch that basically captures all local / inbound /outbound traffic. We don&#x27;t have a huge network (~ 200 workstation/servers + ~50 ...'''
date = "2013-06-03T12:14:00Z"
lastmod = "2013-06-03T14:10:00Z"
weight = 21718
keywords = [ "capture", "filesize" ]
aliases = [ "/questions/21718" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Prolonged Capture / chatty network](/questions/21718/prolonged-capture-chatty-network)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21718-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to do a prolonged capture (24 hours) segmented into either 24 or 48 capture files (depending on size).</p><p>Here is my issue... I'm scanning an uplink port on a main switch that basically captures all local / inbound /outbound traffic.</p><p>We don't have a huge network (~ 200 workstation/servers + ~50 other network devices), but my dump files are pretty huge.<br />
</p><p>30 mins = ~1500000 packets with a file size of 1.175GB</p><p>This size is a little unmanageable to use due to the size but a smaller capture wouldn't be much of a use for statistical reasons.<br />
</p><p>What do big companies do for these types of captures? My network isn't exactly huge.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">capture filesize</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jun '13, 12:14</strong></p><img src="https://secure.gravatar.com/avatar/3591acaff85f26a15e7236604a5e4728?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="CameronW&#39;s gravatar image" /><p>CameronW<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="CameronW has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-21718" class="comments-container"></div><div id="comment-tools-21718" class="comment-tools"></div><div class="clear"></div><div id="comment-21718-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="21719"></span>

<div id="answer-container-21719" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-21719-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you do not want to reduce file size to be manageable by Wireshark (which is understandable in many cases) you'll probably have to look for other solutions, e.g. <a href="http://www.riverbed.com/products-solutions/products/performance-management/network-infrastructure/High-Speed-Packet-Analysis.html">Cace Pilot</a>, OpNet, Wildpackets Omnipeek etc.</p><p>Sometimes, if it's only statistics you're interested in, you can also try to use some kind of NetFlow analysis software.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jun '13, 14:10</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-21719" class="comments-container"></div><div id="comment-tools-21719" class="comment-tools"></div><div class="clear"></div><div id="comment-21719-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

