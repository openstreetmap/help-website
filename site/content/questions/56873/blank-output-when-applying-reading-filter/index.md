+++
type = "question"
title = "Blank output when applying reading filter"
description = '''My ncap file is displayed properly without any filter tshark -r myfile.ncap 1 0.000000 ArrisGro_16:a0:14 → AskeyCom_9a:2b:a1 802.11 400 QoS Data, SN=2900, FN=0, 2 0.000234 ArrisGro_16:a0:14 → AskeyCom_9a:2b:a1 802.11 400 QoS Data, SN=2900, FN=0,  [...]  However, when applying a filter, tshark does n...'''
date = "2016-10-31T12:11:00Z"
lastmod = "2016-11-01T01:59:00Z"
weight = 56873
keywords = [ "filter", "capture", "packets", "tshark", "wireshark" ]
aliases = [ "/questions/56873" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Blank output when applying reading filter](/questions/56873/blank-output-when-applying-reading-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56873-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My <code>ncap</code> file is displayed properly without any filter</p><pre><code>tshark -r myfile.ncap
1 0.000000 ArrisGro_16:a0:14 → AskeyCom_9a:2b:a1 802.11 400 QoS Data, SN=2900, FN=0,
2 0.000234 ArrisGro_16:a0:14 → AskeyCom_9a:2b:a1 802.11 400 QoS Data, SN=2900, FN=0, 
[...]</code></pre><p>However, when applying a filter, <code>tshark</code> does not output any line:</p><pre><code>tshark -r myfile.ncap -Y eth.addr_resolved==ArrisGro_16:a0:14</code></pre><p><strong>Why is there no output when I apply the filter?</strong></p></div><div id="question-tags" class="tags-container tags">filter capture packets tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Oct '16, 12:11</strong></p><img src="https://secure.gravatar.com/avatar/1d0a5c898c23c1ae1a7b009804920031?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user31415&#39;s gravatar image" /><p>user31415<br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user31415 has no accepted answers">0%</span></p></div></div><div id="comments-container-56873" class="comments-container"></div><div id="comment-tools-56873" class="comment-tools"></div><div class="clear"></div><div id="comment-56873-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="56888"></span>

<div id="answer-container-56888" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56888-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Why is there no output when I apply the filter?</p></blockquote><p>Because there is no <code>eth</code> field in your <code>wlan</code> (802.11) frames, and thus no frame can match the display filter expression.</p><p>Use <code>tshark -r myfile.ncap -Y wlan.addr_resolved==ArrisGro_16:a0:14</code> instead.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Nov '16, 01:59</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-56888" class="comments-container"></div><div id="comment-tools-56888" class="comment-tools"></div><div class="clear"></div><div id="comment-56888-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

