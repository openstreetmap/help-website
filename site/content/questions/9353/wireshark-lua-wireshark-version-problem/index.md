+++
type = "question"
title = "Wireshark Lua - Wireshark Version problem"
description = '''Hi,   I have developed a post dissector using Wireshark Lua. Its is running without any problem on Development release 1.7.0 or higher, but it doesn&#x27;t run properly on versions less than 1.7.0. Why is it so ? Is there any dependencies on the versions for wireshark lua support?'''
date = "2012-03-05T01:36:00Z"
lastmod = "2012-03-05T05:22:00Z"
weight = 9353
keywords = [ "lua" ]
aliases = [ "/questions/9353" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark Lua - Wireshark Version problem](/questions/9353/wireshark-lua-wireshark-version-problem)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9353-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have developed a post dissector using Wireshark Lua. Its is running without any problem on Development release 1.7.0 or higher, but it doesn't run properly on versions less than 1.7.0. Why is it so ?</p><p>Is there any dependencies on the versions for wireshark lua support?</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>05 Mar '12, 01:36</strong></p><img src="https://secure.gravatar.com/avatar/eaba5d948ba0b95759c596eb2c6e7ecb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rijith&#39;s gravatar image" /><p>Rijith<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rijith has no accepted answers">0%</span></p></div></div><div id="comments-container-9353" class="comments-container"></div><div id="comment-tools-9353" class="comment-tools"></div><div class="clear"></div><div id="comment-9353-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9357"></span>

<div id="answer-container-9357" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9357-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>No, there are no new dependencies in 1.7.x. However, the API was modified and bugs were fixed in 1.7.x. There is no known documentation that specifically lists those changes (yet).</p><p>You might be using a newer function in an old version of Wireshark, in which case you should use <a href="http://wiki.wireshark.org/LuaAPI/Utils#get_version.28.29"><code>get_version()</code></a> to determine whether or not to use that particular API function.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '12, 05:22</strong></p><img src="https://secure.gravatar.com/avatar/aa651167cb1d51fa9dca1212f1123bfa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bstn&#39;s gravatar image" /><p>bstn<br />
<span class="score" title="375 reputation points">375</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bstn has 4 accepted answers">14%</span></p></div></div><div id="comments-container-9357" class="comments-container"></div><div id="comment-tools-9357" class="comment-tools"></div><div class="clear"></div><div id="comment-9357-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

