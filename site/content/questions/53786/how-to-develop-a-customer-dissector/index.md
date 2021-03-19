+++
type = "question"
title = "How to develop a customer dissector"
description = '''I want to make a new dissector as a plugin which can be used under windows.  I am new to wireshare development and have some questions would like to ask:  I am struggling on choosing development platform. Since I see the set up for windows from here is complicated but at the same time I am not sure ...'''
date = "2016-07-02T06:53:00Z"
lastmod = "2016-07-02T08:12:00Z"
weight = 53786
keywords = [ "dissector" ]
aliases = [ "/questions/53786" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [How to develop a customer dissector](/questions/53786/how-to-develop-a-customer-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53786-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to make a new dissector as a plugin which can be used under windows.<br />
<br />
I am new to wireshare development and have some questions would like to ask:</p><ul><li>I am struggling on choosing development platform. Since I see the set up for windows from <a href="https://www.wireshark.org/docs/wsdg_html_chunked/ChSetupWin32.html">here</a> is complicated but at the same time I am not sure how to debug under linux although I have already built wireshark under Ubuntu since I am new to linux environment for developing also. Anyway, Is it possible to build this plugin under linux for both linux and windows platform?</li><li>I have the above questions after seeing <a href="http://www.codeproject.com/Articles/19426/Creating-Your-Own-Custom-Wireshark-Dissector">This</a>. I found both Makefile.am and nmake file and wondering can I build the plugin under ubuntu for both OS.</li><li>If it is possible, can anyone show me how to build it? Is it just add some options after <strong>./configure</strong>?</li></ul><p>Thank you very much.</p></div><div id="question-tags" class="tags-container tags">dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jul '16, 06:53</strong></p><img src="https://secure.gravatar.com/avatar/7c0faeca14601a7e181f27988b503982?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SulfredLee&#39;s gravatar image" /><p>SulfredLee<br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SulfredLee has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-53786" class="comments-container"></div><div id="comment-tools-53786" class="comment-tools"></div><div class="clear"></div><div id="comment-53786-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53788"></span>

<div id="answer-container-53788" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53788-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><ol><li>No, cross compilation is not supported.</li><li>No, cross compilation is not supported. Also the referenced article is outdated (22 Jul 2007).</li><li>No, cross compilation is not supported.</li></ol><p>So, in short, either choose to develop in Ubuntu (install the wireshark-dev package should get you everything you need, then add gdb and ddd packages for your debugging needs), or Windows (follow the steps in the developer guide to the letter).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jul '16, 08:12</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-53788" class="comments-container"><span id="53789"></span><div id="comment-53789" class="comment"><div id="post-53789-score" class="comment-score"></div><div class="comment-text"><p>Thanks for replying. I have already installed gdb and ddd. One more question. to build a wireshark which can be able to debug. Is it just do <code>./configure --enable-debug</code>? To build a wireshark which is release, is it just do <code>./configure --disable-debug</code>?</p></div><div id="comment-53789-info" class="comment-info"><span class="comment-age">(02 Jul '16, 15:33)</span> SulfredLee</div></div></div><div id="comment-tools-53788" class="comment-tools"></div><div class="clear"></div><div id="comment-53788-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

