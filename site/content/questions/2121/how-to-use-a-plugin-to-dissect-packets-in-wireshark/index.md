+++
type = "question"
title = "how to use a plugin to dissect packets in wireshark??"
description = '''Hey, I have created a plugin for Wireshark for the NetScalar NNM protocol. Now I have compiled the source code successfully. I want to capture NNM packets using this wireshark. So when I open the application, do I need to do anything to register the plugin? The protocol is not identified by wireshar...'''
date = "2011-02-03T00:24:00Z"
lastmod = "2011-02-03T11:55:00Z"
weight = 2121
keywords = [ "plugins", "wireshark" ]
aliases = [ "/questions/2121" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to use a plugin to dissect packets in wireshark??](/questions/2121/how-to-use-a-plugin-to-dissect-packets-in-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2121-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>I have created a plugin for Wireshark for the NetScalar NNM protocol. Now I have compiled the source code successfully. I want to capture NNM packets using this wireshark. So when I open the application, do I need to do anything to register the plugin? The protocol is not identified by wireshark when I run it on a NNM trace.</p><p>Any help??</p><p>Thanks and Regards,</p><p>Sid</p></div><div id="question-tags" class="tags-container tags">plugins wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '11, 00:24</strong></p><img src="https://secure.gravatar.com/avatar/5a41ae1c710064aebdb9a4e0a1788d12?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sid&#39;s gravatar image" /><p>sid<br />
<span class="score" title="45 reputation points">45</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sid has no accepted answers">0%</span></p></div></div><div id="comments-container-2121" class="comments-container"></div><div id="comment-tools-2121" class="comment-tools"></div><div class="clear"></div><div id="comment-2121-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="2134"></span>

<div id="answer-container-2134" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-2134-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>When coded correctly and placed where Wireshark looks, there's no further action needed from you.</p><p>You can check if Wireshark loaded your dissector, by looking at the About dialog box, at the Plugins tab. Or you can enter your protocol filter name in the display filter edit box. It will turn green if it's registered correctly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '11, 11:55</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-2134" class="comments-container"></div><div id="comment-tools-2134" class="comment-tools"></div><div class="clear"></div><div id="comment-2134-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

