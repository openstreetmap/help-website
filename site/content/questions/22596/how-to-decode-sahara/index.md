+++
type = "question"
title = "How to decode Sahara ?"
description = '''WireShark v0.99 was able to decode Sahara. Now in version 1.10, Sahara decoding is no longer available. Is there any way to decode Sahara with the new version?'''
date = "2013-07-03T05:17:00Z"
lastmod = "2013-07-03T06:28:00Z"
weight = 22596
keywords = [ "decode", "sahara" ]
aliases = [ "/questions/22596" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to decode Sahara ?](/questions/22596/how-to-decode-sahara)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22596-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>WireShark v0.99 was able to decode Sahara. Now in version 1.10, Sahara decoding is no longer available. Is there any way to decode Sahara with the new version?</p></div><div id="question-tags" class="tags-container tags">decode sahara</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Jul '13, 05:17</strong></p><img src="https://secure.gravatar.com/avatar/72672a3f10bdf0874f67ee97f12f61b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="viperfx15&#39;s gravatar image" /><p>viperfx15<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="viperfx15 has no accepted answers">0%</span></p></div></div><div id="comments-container-22596" class="comments-container"></div><div id="comment-tools-22596" class="comment-tools"></div><div class="clear"></div><div id="comment-22596-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22601"></span>

<div id="answer-container-22601" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22601-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I was not able to find a reference to the 'Sahara' protocol in the source code of Wireshark 0.99. Either it is not called 'Sahara' (spelling error) or you had a third-party plugin in Wireshark 0.99 with a 'Sahara' dissector.</p><p>Can you please add more details about that protocol?</p><p><strong>UPDATE:</strong></p><p>To answer your question:</p><blockquote><p>Is there any way to decode Sahara with the new version?</p></blockquote><p>As it's now clear that there is a custom dissector plugin (sahara.dll), you need to contact the author of the plugin and ask him/her to compile a version for you that is compatible with Wireshark 1.10.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jul '13, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 03 Jul '13, 07:11</p></div></div><div id="comments-container-22601" class="comments-container"><span id="22603"></span><div id="comment-22603" class="comment"><div id="post-22603-score" class="comment-score"></div><div class="comment-text"><p>It seems that it is a dissector plugin. However, it is located in the Wireshark/plugins/0.99 folder (sahara.dll) so this would mean it is part of the standard plugins that came with the Wireshark setup package, right? In my new instalation, in the folder Wireshark/plugins/1.10 folder, this dll is not found anymore.</p></div><div id="comment-22603-info" class="comment-info"><span class="comment-age">(03 Jul '13, 06:35)</span> viperfx15</div></div><span id="22605"></span><div id="comment-22605" class="comment"><div id="post-22605-score" class="comment-score"></div><div class="comment-text"><p>The plugin could have just been dropped\installed into that location and isn't part of the standard Wireshark distribution.</p></div><div id="comment-22605-info" class="comment-info"><span class="comment-age">(03 Jul '13, 06:54)</span> grahamb ♦</div></div><span id="22607"></span><div id="comment-22607" class="comment"><div id="post-22607-score" class="comment-score"></div><div class="comment-text"><p>As google does not find anything about sahara.dll in conjunction with Wireshark, I assume it's some home-made dissector plugin that was not released publicly.</p><p>Can you please tell us more about the Sahara protocol?</p></div><div id="comment-22607-info" class="comment-info"><span class="comment-age">(03 Jul '13, 07:07)</span> Kurt Knochner ♦</div></div><span id="22616"></span><div id="comment-22616" class="comment"><div id="post-22616-score" class="comment-score"></div><div class="comment-text"><blockquote><p>However, it is located in the Wireshark/plugins/0.99 folder (sahara.dll) so this would mean it is part of the standard plugins that came with the Wireshark setup package, right?</p></blockquote><p>No. We never distributed a "sahara" plugin; as grahamb notes, perhaps the plugin was installed separately and was put into the standard Wireshark plugin directory, or perhaps the 0.99 that you installed was a special distribution somebody other than wireshark.org provided, with the Sahara plugin included.</p></div><div id="comment-22616-info" class="comment-info"><span class="comment-age">(03 Jul '13, 11:06)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-22601" class="comment-tools"></div><div class="clear"></div><div id="comment-22601-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

