+++
type = "question"
title = "dll missing for my dissector after building wireshark on windows"
description = '''Hello, I have a problem when I build wireshark on windows. I read carefully the tutorial https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html. The build end without error but in my dissector plugin folder there isn&#x27;t any dll file. New files after compilation are: - plugin.obj   - mydis...'''
date = "2015-09-03T01:43:00Z"
lastmod = "2015-09-03T12:00:00Z"
weight = 45611
keywords = [ "plugin", "dll" ]
aliases = [ "/questions/45611" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dll missing for my dissector after building wireshark on windows](/questions/45611/dll-missing-for-my-dissector-after-building-wireshark-on-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45611-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a problem when I build wireshark on windows. I read carefully the tutorial <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.">https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html.</a> The build end without error but in my dissector plugin folder there isn't any dll file. New files after compilation are: - plugin.obj - mydissector.rc - vc120.pdb I don't understand why. Maybe I missed something... Thanks in advance for help. Regards</p><p>Sylvain</p></div><div id="question-tags" class="tags-container tags">plugin dll</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Sep '15, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/fe134700e9c8fcec7b7bd553aac46396?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sylvain&#39;s gravatar image" /><p>Sylvain<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sylvain has one accepted answer">100%</span></p></div></div><div id="comments-container-45611" class="comments-container"><span id="45621"></span><div id="comment-45621" class="comment"><div id="post-45621-score" class="comment-score"></div><div class="comment-text"><p>Could you post the output of nmake command when you compile your plugin?</p></div><div id="comment-45621-info" class="comment-info"><span class="comment-age">(03 Sep '15, 11:40)</span> Pascal Quantin</div></div></div><div id="comment-tools-45611" class="comment-tools"></div><div class="clear"></div><div id="comment-45611-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45622"></span>

<div id="answer-container-45622" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45622-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Thank you but I found the answer ! I had a problem with the libxml librarie. It was not compiled properly. Advice for future : dont forget to link the librarie in the makefile.nmake of your dissector.</p><p>Sylvain</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Sep '15, 12:00</strong></p><img src="https://secure.gravatar.com/avatar/fe134700e9c8fcec7b7bd553aac46396?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sylvain&#39;s gravatar image" /><p>Sylvain<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sylvain has one accepted answer">100%</span></p></div></div><div id="comments-container-45622" class="comments-container"></div><div id="comment-tools-45622" class="comment-tools"></div><div class="clear"></div><div id="comment-45622-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

