+++
type = "question"
title = "Adding new features to wireshark"
description = '''Hello,  I would like to know about the below things.  Please let me know can I add a custom protocol (in the application layer) as a plugin? Can we write our own plugin (add new features for ex: display statistics information ) and integrate this into wireshark ?  Thank you.'''
date = "2016-08-18T02:03:00Z"
lastmod = "2016-08-18T05:16:00Z"
weight = 54938
keywords = [ "plugin" ]
aliases = [ "/questions/54938" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Adding new features to wireshark](/questions/54938/adding-new-features-to-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54938-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I would like to know about the below things.</p><ol><li>Please let me know can I add a custom protocol (in the application layer) as a plugin?</li><li>Can we write our own plugin (add new features for ex: display statistics information ) and integrate this into wireshark ?</li></ol><p>Thank you.</p></div><div id="question-tags" class="tags-container tags">plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '16, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/1d8583ebaa635698618e362af9eeb4d7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stadkama&#39;s gravatar image" /><p>stadkama<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stadkama has no accepted answers">0%</span></p></div></div><div id="comments-container-54938" class="comments-container"></div><div id="comment-tools-54938" class="comment-tools"></div><div class="clear"></div><div id="comment-54938-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="54944"></span>

<div id="answer-container-54944" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-54944-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Yes and yes. See the <a href="https://www.wireshark.org/docs/wsdg_html_chunked/">Developers Guide</a> which mainly discusses building dissectors using C, but you can also do this using Lua. There is also the doc directory in the source tree with the particular files <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.dissector;h=c5410452509d33880a904b46854154fa87255dce;hb=HEAD">README.dissector</a> and <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=blob;f=doc/README.plugins;h=bf40f456f9aaa3bae156544d3002ec0f3ea71f38;hb=HEAD">README.plugins</a> that may be of interest.</p><p>Note that Wireshark is licenced under the GPL, so if you distribute your plugin outside your company you must make the source code for the plugin available.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '16, 05:16</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-54944" class="comments-container"><span id="55264"></span><div id="comment-55264" class="comment"><div id="post-55264-score" class="comment-score"></div><div class="comment-text"><p>Thank you. can we make GUI changes also like adding a menu item which has some features?</p></div><div id="comment-55264-info" class="comment-info"><span class="comment-age">(01 Sep '16, 04:25)</span> stadkama</div></div><span id="55265"></span><div id="comment-55265" class="comment"><div id="post-55265-score" class="comment-score"></div><div class="comment-text"><p>Did you look at README.plugins, Sect. 6 discusses GUI options for plugins?</p><p>There's also the Lua equivalent <a href="https://wiki.wireshark.org/LuaAPI/GUI">here</a>.</p></div><div id="comment-55265-info" class="comment-info"><span class="comment-age">(01 Sep '16, 04:36)</span> grahamb ♦</div></div><span id="55516"></span><div id="comment-55516" class="comment"><div id="post-55516-score" class="comment-score"></div><div class="comment-text"><p>I went through it...If I am not wrong it is done using Qt right?</p></div><div id="comment-55516-info" class="comment-info"><span class="comment-age">(13 Sep '16, 01:47)</span> stadkama</div></div><span id="55518"></span><div id="comment-55518" class="comment"><div id="post-55518-score" class="comment-score"></div><div class="comment-text"><p>If using C (or C++ actually), then yes you are directly using Qt. If using Lua, then you are limited to the Wireshark Lua API.</p></div><div id="comment-55518-info" class="comment-info"><span class="comment-age">(13 Sep '16, 04:24)</span> grahamb ♦</div></div></div><div id="comment-tools-54944" class="comment-tools"></div><div class="clear"></div><div id="comment-54944-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

