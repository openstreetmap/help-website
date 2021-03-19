+++
type = "question"
title = "Wireshark plugin binary compatibility in Linux"
description = '''Suppose I create a Wireshark plugin in Ubuntu (say version 12.04, but I would prefer an answer for any general system), how compatible will it be across all Wireshark versions in different Linux platforms like Fedora, Mint, etc? Also, could it possibly be compatible with Wireshark in older versions ...'''
date = "2012-11-21T05:20:00Z"
lastmod = "2012-11-21T09:29:00Z"
weight = 16155
keywords = [ "linux", "binary_compatibility", "plugins" ]
aliases = [ "/questions/16155" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark plugin binary compatibility in Linux](/questions/16155/wireshark-plugin-binary-compatibility-in-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16155-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Suppose I create a Wireshark plugin in Ubuntu (say version 12.04, but I would prefer an answer for any general system), how compatible will it be across all Wireshark versions in <em>different</em> Linux platforms like Fedora, Mint, etc?</p><p>Also, could it possibly be compatible with Wireshark in older versions of Ubuntu like 11.04?</p></div><div id="question-tags" class="tags-container tags">linux binary_compatibility plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '12, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p>SidR<br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div></div><div id="comments-container-16155" class="comments-container"></div><div id="comment-tools-16155" class="comment-tools"></div><div class="clear"></div><div id="comment-16155-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16170"></span>

<div id="answer-container-16170" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16170-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>As long as you adhere to the practices laid out in README.developer you should be able to write portable source code. As for binary compatibility, you most likely will be able to move the so around, but library compatibility may be an issue.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '12, 09:29</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-16170" class="comments-container"><span id="16171"></span><div id="comment-16171" class="comment"><div id="post-16171-score" class="comment-score"></div><div class="comment-text"><p>In other words, the plugin compiled in Ubuntu has a good chance of working in Fedora.</p><p>Is there any list that clearly lays out compatibility issues between platforms?</p><p>Also, do you mind elaborating about library compatibility? Why will it be an issue and for what cases specifically?</p></div><div id="comment-16171-info" class="comment-info"><span class="comment-age">(21 Nov '12, 09:56)</span> SidR</div></div><span id="16176"></span><div id="comment-16176" class="comment"><div id="post-16176-score" class="comment-score"></div><div class="comment-text"><p>run this command and look at the output.</p><blockquote><p><code>ldd yourplugin.so</code><br />
</p></blockquote><p>If any one of those libraries is substantially different on one of the mentioned systems, your plugin may get into trouble.</p></div><div id="comment-16176-info" class="comment-info"><span class="comment-age">(21 Nov '12, 12:16)</span> Kurt Knochner ♦</div></div><span id="16200"></span><div id="comment-16200" class="comment"><div id="post-16200-score" class="comment-score"></div><div class="comment-text"><p>As for library compatibility, have a look <a href="http://www.gnu.org/software/libtool/manual/html_node/Versioning.html">here</a> for instance.</p></div><div id="comment-16200-info" class="comment-info"><span class="comment-age">(22 Nov '12, 04:14)</span> Jaap ♦</div></div></div><div id="comment-tools-16170" class="comment-tools"></div><div class="clear"></div><div id="comment-16170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

