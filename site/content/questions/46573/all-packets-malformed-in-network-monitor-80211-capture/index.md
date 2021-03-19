+++
type = "question"
title = "All Packets Malformed in Network Monitor 802.11 capture"
description = '''I have been attempting to sniff the wifi transactions between two devices using monitor mode. I am running windows 10 currently (same issues on win7 tho), with wireshark 1.12.7. I have the airPcap library from the latest acrylic wifi release. Using either of my two wifi to usb devices (rnx-g1 and ze...'''
date = "2015-10-15T10:37:00Z"
lastmod = "2015-10-16T12:40:00Z"
weight = 46573
keywords = [ "netmon", "wifi", "malformed", "packet", "monitor" ]
aliases = [ "/questions/46573" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [All Packets Malformed in Network Monitor 802.11 capture](/questions/46573/all-packets-malformed-in-network-monitor-80211-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46573-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have been attempting to sniff the wifi transactions between two devices using monitor mode. I am running windows 10 currently (same issues on win7 tho), with wireshark 1.12.7. I have the airPcap library from the latest acrylic wifi release. Using either of my two wifi to usb devices (rnx-g1 and zew2500p) I appear to be able to sniff the transactions, but they are all malformed. Does anyone know what would cause this, and how it can be fixed? See the image below. <img src="https://osqa-ask.wireshark.org/upfiles/cap1.PNG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">netmon wifi malformed packet monitor</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '15, 10:37</strong></p><img src="https://secure.gravatar.com/avatar/bbc42cd4e48ddec1204f1afc1ac98915?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="phillipvanoss&#39;s gravatar image" /><p>phillipvanoss<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="phillipvanoss has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 16 Oct '15, 12:41</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-46573" class="comments-container"><span id="46576"></span><div id="comment-46576" class="comment"><div id="post-46576-score" class="comment-score"></div><div class="comment-text"><p>Link does not work.</p></div><div id="comment-46576-info" class="comment-info"><span class="comment-age">(15 Oct '15, 11:01)</span> Christian_R</div></div><span id="46577"></span><div id="comment-46577" class="comment"><div id="post-46577-score" class="comment-score"></div><div class="comment-text"><p>Try this one <a href="http://imgur.com/JqBOjwA">http://imgur.com/JqBOjwA</a></p></div><div id="comment-46577-info" class="comment-info"><span class="comment-age">(15 Oct '15, 11:05)</span> phillipvanoss</div></div><span id="46578"></span><div id="comment-46578" class="comment"><div id="post-46578-score" class="comment-score"></div><div class="comment-text"><p>Hiding trhe details of the frame in the screenhot does not help to give you an answer!</p></div><div id="comment-46578-info" class="comment-info"><span class="comment-age">(15 Oct '15, 11:35)</span> Kurt Knochner ♦</div></div><span id="46582"></span><div id="comment-46582" class="comment"><div id="post-46582-score" class="comment-score">1</div><div class="comment-text"><p>So did you capture the trace from the image above with Wireshark or with Microsoft Network Monitor?</p></div><div id="comment-46582-info" class="comment-info"><span class="comment-age">(15 Oct '15, 14:21)</span> Guy Harris ♦♦</div></div><span id="46613"></span><div id="comment-46613" class="comment"><div id="post-46613-score" class="comment-score"></div><div class="comment-text"><p>This particular capture was done with Microsoft Network Monitor and then opened in Wireshark.</p></div><div id="comment-46613-info" class="comment-info"><span class="comment-age">(16 Oct '15, 05:48)</span> phillipvanoss</div></div></div><div id="comment-tools-46573" class="comment-tools"></div><div class="clear"></div><div id="comment-46573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="46630"></span>

<div id="answer-container-46630" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46630-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>So AirPcap is irrelevant to this, as it wasn't used to capture the traffic.</p><p>Either Microsoft or the vendors of 802.11 drivers for Windows do a really bad job of consistently providing, or not providing, the FCS for frames. If you could file a bug on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a> for this and, ideally, attach the capture file to the bug, we might be able to try to find <em>something</em> in the capture file to indicate whether frames have an FCS or not. To quote a comment in the code for Network Monitor files:</p><pre><code>             * It appears to be the case that management
             * frames (and control and extension frames ?) may
             * or may not have an FCS and data frames don&#39;t.
             * (Netmon capture files have been seen for this
             *  encapsulation having management frames either
             *  completely with or without an FCS. Also: instances have been
             *  seen where both Management and Control frames
             *  do not have an FCS).
             * An &quot;FCS length&quot; of -2 means &quot;NetMon weirdness&quot;.</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Oct '15, 12:40</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-46630" class="comments-container"></div><div id="comment-tools-46630" class="comment-tools"></div><div class="clear"></div><div id="comment-46630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

