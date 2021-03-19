+++
type = "question"
title = "Traffic monitor with filters"
description = '''I would like to perform some specific traffic monitoring. I wonder if I can achieve it with Wireshark in any way (GUI, Lua, or scripting tshark). These are monitoring criteria I&#x27;d like to implement:  display average bandwidth load in real-time; capture traffic during some period (can be days) and ca...'''
date = "2014-03-27T14:36:00Z"
lastmod = "2014-03-27T14:36:00Z"
weight = 31239
keywords = [ "bandwidth", "traffic", "traffic-analysis", "monitor" ]
aliases = [ "/questions/31239" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Traffic monitor with filters](/questions/31239/traffic-monitor-with-filters)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31239-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to perform some specific traffic monitoring. I wonder if I can achieve it with Wireshark in any way (GUI, Lua, or scripting tshark). These are monitoring criteria I'd like to implement:</p><ul><li>display average bandwidth load in real-time;</li><li>capture traffic during some period (can be days) and calculate traffic size (upload/download separately) after it stopped capturing;</li><li>filter the above by the process name or id (browser, email client, web server, any other process);</li><li>filter the above by IP or domain (if applicable);</li><li>Filter http requests according to regex rules (e.g., if certain Content-Type is present)</li></ul><p>In first two cases, I believe its important not to keep all the captured packets in memory - just calculate size/bandwidth and discard the content.</p><p>If Wireshark is not the tool to achieve it, what would you recommend? Thanks</p></div><div id="question-tags" class="tags-container tags">bandwidth traffic traffic-analysis monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Mar '14, 14:36</strong></p><img src="https://secure.gravatar.com/avatar/c0756ff055e37f9defa66cc2204377a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Naz&#39;s gravatar image" /><p>Naz<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Naz has no accepted answers">0%</span></p></div></div><div id="comments-container-31239" class="comments-container"></div><div id="comment-tools-31239" class="comment-tools"></div><div class="clear"></div><div id="comment-31239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

