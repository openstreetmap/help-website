+++
type = "question"
title = "licensing question on dissector"
description = '''When I start reading your file called README.dissector, it mentions a skeletal file called packet-PROTOABBREV.c. At the top of that file, it mentions the following license: GNU General Public License as published by  * the Free Software Foundation Basically, my team may want me to investigate the us...'''
date = "2017-09-07T05:44:00Z"
lastmod = "2017-09-07T12:21:00Z"
weight = 63573
keywords = [ "dissector", "license" ]
aliases = [ "/questions/63573" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [licensing question on dissector](/questions/63573/licensing-question-on-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63573-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>When I start reading your file called <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob_plain;f=doc/README.dissector">README.dissector</a>, it mentions a skeletal file called <a href="https://github.com/boundary/wireshark/blob/master/doc/packet-PROTOABBREV.c">packet-PROTOABBREV.c</a>. At the top of that file, it mentions the following license:</p><p><a href="https://www.gnu.org/licenses/gpl-faq.html#WhyUseGPL">GNU General Public License as published by * the Free Software Foundation</a></p><p>Basically, my team may want me to investigate the use of this software with this license on it.</p><p>Questions:</p><ol><li><p>To get around this license, do I have any <strong>options</strong> besides using this (<a href="https://github.com/boundary/wireshark/blob/master/doc/packet-PROTOABBREV.c">packet-PROTOABBREV.c</a>) file.</p></li><li><p>Or, is it the case that if my team uses any Wireshark dissector that my team will be obliged to abide by this license. For example, we can't sell our product developed with the above C file?</p></li><li><p>Does this license affect your answer (specifically <strong>header fields</strong>) in any way, please explain?</p></li><li><p>How can my team avoid the license? What can we explicitly do and not do to legally follow the license. (Should we go as far as have our legal team investigate this further?)</p></li><li><p>My team wants to modify other messages that we have in our protocol. Can we do this and avoid the license, please explain?</p></li></ol><p>Again thanks,</p></div><div id="question-tags" class="tags-container tags">dissector license</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '17, 05:44</strong></p><img src="https://secure.gravatar.com/avatar/45327d89d1ff1135df093945666003ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike123456&#39;s gravatar image" /><p>Mike123456<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike123456 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 07 Sep '17, 06:28</p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-63573" class="comments-container"><span id="63574"></span><div id="comment-63574" class="comment"><div id="post-63574-score" class="comment-score">1</div><div class="comment-text"><p>Your comment has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p><p>This is why I suggested continuing on the wireshark-dev mailing list.</p></div><div id="comment-63574-info" class="comment-info"><span class="comment-age">(07 Sep '17, 06:28)</span> Jaap ♦</div></div></div><div id="comment-tools-63573" class="comment-tools"></div><div class="clear"></div><div id="comment-63573-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63578"></span>

<div id="answer-container-63578" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-63578-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>is it the case that if my team uses any Wireshark dissector that my team will be obliged to abide by this license.</p></blockquote><p>All dissectors linked into Wireshark, <a href="https://www.gnu.org/licenses/gpl-faq.html#GPLPlugins">or dynamically loaded by Wireshark as plugins</a>, must be licensed under the GPL. No exceptions, no workarounds, no way to avoid it.</p><blockquote><p>For example, we can't sell our product developed with the above C file?</p></blockquote><p><a href="https://www.gnu.org/licenses/gpl-faq.html#DoesTheGPLAllowMoney">You can sell it</a>, <em>but</em> if you sell it to somebody, <a href="https://www.gnu.org/licenses/gpl-faq.html#DoesTheGPLAllowRequireFee">they're then allowed to give copies to anybody they want without paying you anything</a>. <a href="https://www.gnu.org/licenses/gpl-faq.html#GPLRequireSourcePostedPublic">Whoever has your program has the right to get the source to the program, including your modifications</a>, and they can then give that source to anybody they want.</p><blockquote><p>Should we go as far as have our legal team investigate this further?</p></blockquote><p>Yes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '17, 12:21</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-63578" class="comments-container"></div><div id="comment-tools-63578" class="comment-tools"></div><div class="clear"></div><div id="comment-63578-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

