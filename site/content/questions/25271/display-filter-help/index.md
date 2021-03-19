+++
type = "question"
title = "Display filter help"
description = '''Below are the display filters in wireshark 1.2. I am not able find corresponding filters in Wireshark 1.6.7. Could you please help ? wlan_mgt.wme.be.ac_param.acm wlan_mgt.wme.bg.ac_param.acm wlan_mgt.wme.video.ac_param.acm wlan_mgt.wme.voice.ac_param.acm wlan_mgt.extchanswitch.new.channumber wlan_mg...'''
date = "2013-09-26T04:34:00Z"
lastmod = "2013-09-26T06:21:00Z"
weight = 25271
keywords = [ "display-filter" ]
aliases = [ "/questions/25271" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Display filter help](/questions/25271/display-filter-help)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25271-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Below are the display filters in wireshark 1.2. I am not able find corresponding filters in Wireshark 1.6.7. Could you please help ?</p><pre><code>wlan_mgt.wme.be.ac_param.acm
wlan_mgt.wme.bg.ac_param.acm
wlan_mgt.wme.video.ac_param.acm
wlan_mgt.wme.voice.ac_param.acm
wlan_mgt.extchanswitch.new.channumber
wlan_mgt.ht.info
wlan_mgt.extchanswitch.new.regclass
wlan_mgt.extchanswitch.switchmode
wlan_mgt.measure.req.repcond
wlan_mgt.measure.req.reportmac
wlan_mgt.measure.req.reqmode.reserved1
wlan_mgt.measure.req.reqmode.reserved2
wlan_mgt.measure.req.threshold</code></pre></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '13, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/b4114b9082a0f82fda642868a1d28ed3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Keerthi&#39;s gravatar image" /><p>Keerthi<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Keerthi has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 26 Sep '13, 09:11</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-25271" class="comments-container"></div><div id="comment-tools-25271" class="comment-tools"></div><div class="clear"></div><div id="comment-25271-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="25277"></span>

<div id="answer-container-25277" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25277-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Please check here</p><blockquote><p><a href="http://www.wireshark.org/docs/dfref/w/wlan_mgt.html">http://www.wireshark.org/docs/dfref/w/wlan_mgt.html</a></p></blockquote><p>In the last column you'll find the releases that support each filter. Apparently there have been several changes and thus you cannot map the filter from 1.2 directly to a later release.</p><p>Example</p><pre><code>wlan_mgt.measure.req.threshold Threshold/Offset Unsigned integer, 1 byte 1.0.0 to 1.4.15</code></pre><p>became</p><pre><code>wlan_mgt.measure.req.beacon.sub.bri.threshold_offset Threshold/Offset Unsigned integer, 1 byte  1.6.0 to 1.10.2</code></pre><p>So, you need to work through the list of fields and map them to the new names. The column <strong>Description</strong> should help you to do so.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Sep '13, 06:21</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-25277" class="comments-container"></div><div id="comment-tools-25277" class="comment-tools"></div><div class="clear"></div><div id="comment-25277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

