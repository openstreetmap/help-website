+++
type = "question"
title = "LUA: Can&#x27;t plot float values in IO Graph"
description = '''Hi, We have written a LUA postdissector that calculates a number of response time values. These are defined as floating point fields, e.g. rte_art_F = ProtoField.float(&quot;transum.art&quot;,&quot;APDU Rsp Time&quot;)  The postdissector works fine but I can&#x27;t get the Wireshark IO Graph facility to plot the values - I ...'''
date = "2014-08-02T03:48:00Z"
lastmod = "2014-08-02T03:48:00Z"
weight = 35086
keywords = [ "lua", "postdissector" ]
aliases = [ "/questions/35086" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA: Can't plot float values in IO Graph](/questions/35086/lua-cant-plot-float-values-in-io-graph)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35086-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>We have written a LUA postdissector that calculates a number of response time values. These are defined as floating point fields, e.g.</p><pre><code>rte_art_F = ProtoField.float(&quot;transum.art&quot;,&quot;APDU Rsp Time&quot;)</code></pre><p>The postdissector works fine but I can't get the Wireshark IO Graph facility to plot the values - I just get a flat line. I use the Y Axis Unit: Advanced option in IO Graph, choose Calc: MAX(*) and then add transum.art as the value to plot.</p><p>I've tried the same thing with Wireshark compiled dissector fields and these work fine.</p><p>Does IO Graph support LUA postdissector fields? Am I doing something wrong?</p><p>Thanks and regards...Paul</p><p>PS: The dissector can be downloaded from <a href="http://www.tribelabzero.com/resources">http://www.tribelabzero.com/resources</a></p></div><div id="question-tags" class="tags-container tags">lua postdissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Aug '14, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35086" class="comments-container"><span id="35176"></span><div id="comment-35176" class="comment"><div id="post-35176-score" class="comment-score"></div><div class="comment-text"><p>Is this a candidate for a bug report?</p></div><div id="comment-35176-info" class="comment-info"><span class="comment-age">(04 Aug '14, 15:34)</span> PaulOfford</div></div><span id="35181"></span><div id="comment-35181" class="comment"><div id="post-35181-score" class="comment-score"></div><div class="comment-text"><p>What is your</p><ul><li>OS and OS version</li><li>Wireshark version</li></ul></div><div id="comment-35181-info" class="comment-info"><span class="comment-age">(04 Aug '14, 23:19)</span> Kurt Knochner ♦</div></div><span id="35205"></span><div id="comment-35205" class="comment"><div id="post-35205-score" class="comment-score"></div><div class="comment-text"><p>Windows 7 Ultimate Build 7601 SP 1 - Wireshark 1.10.8</p><p>I've upgraded to Wireshark 1.12.0 and I get the same problem.</p><p>Just to be sure I'm doing this right, here's what I put in the dialog box:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/IO_Graph_1.gif" alt="alt text" /></p></div><div id="comment-35205-info" class="comment-info"><span class="comment-age">(05 Aug '14, 05:10)</span> PaulOfford</div></div></div><div id="comment-tools-35086" class="comment-tools"></div><div class="clear"></div><div id="comment-35086-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

