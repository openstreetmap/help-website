+++
type = "question"
title = "make Wireshark analysis vlan aware"
description = '''I&#x27;ve often the problem, that I have the same traffic flow on diffrent vlans but in the same capture file. Than you get a lot of errors from the analysis engine that you have duplicate packets etc. Is there a way to configure Wireshark to treat the same flow on diffrent vlans as diffrent flows in the...'''
date = "2010-09-13T17:49:00Z"
lastmod = "2010-09-15T12:29:00Z"
weight = 50
keywords = [ "vlan", "flows" ]
aliases = [ "/questions/50" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [make Wireshark analysis vlan aware](/questions/50/make-wireshark-analysis-vlan-aware)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50-score" class="post-score" title="current number of votes">2</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've often the problem, that I have the same traffic flow on diffrent vlans but in the same capture file. Than you get a lot of errors from the analysis engine that you have duplicate packets etc.</p><p>Is there a way to configure Wireshark to treat the same flow on diffrent vlans as diffrent flows in the analysis?</p><p>I know that I can split up the capture file in several smaller files filtered by vlan. This would solve the problem, but that's not what I want to do ;-)</p></div><div id="question-tags" class="tags-container tags">vlan flows</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Sep '10, 17:49</strong></p><img src="https://secure.gravatar.com/avatar/ea89a7136cee2bff4cc1ddbaf5e1b676?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Oliver&#39;s gravatar image" /><p>Oliver<br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Oliver has no accepted answers">0%</span></p></div></div><div id="comments-container-50" class="comments-container"></div><div id="comment-tools-50" class="comment-tools"></div><div class="clear"></div><div id="comment-50-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="99"></span>

<div id="answer-container-99" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-99-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is already an enhancement request for this feature filed at <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=4561" title="Bug 4561">bugzilla</a>. There are more situations than just multiple vlans. However, I suspect the vlan case to be the most seen in the field (well, at least in the networks where I do troubleshooting), so fixing it first for vlan tagging only might be justified IMHO :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Sep '10, 12:29</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-99" class="comments-container"></div><div id="comment-tools-99" class="comment-tools"></div><div class="clear"></div><div id="comment-99-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="53"></span>

<div id="answer-container-53" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There is currently no configuration option to support that. The code would have to be changed so that:</p><ol><li>The VLAN ID is stored with the packet info,</li><li>The re-assembly and analysis functions in the dissectors use this ID as a key to search for and process conversation and packet data.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '10, 03:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53" class="comments-container"></div><div id="comment-tools-53" class="comment-tools"></div><div class="clear"></div><div id="comment-53-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

