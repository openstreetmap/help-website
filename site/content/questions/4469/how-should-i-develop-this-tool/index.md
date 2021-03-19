+++
type = "question"
title = "How should I develop this tool?"
description = '''Hi, I&#x27;d like to develop some enhancements to the Wireshark GUI, and I&#x27;m not sure what the best approach is. The graph interface in Statistics -&amp;gt; IOGraphs is very helpful but I&#x27;d like to add on to that, perhaps have some more visualization that could be viewed side by side with the graph. The stuf...'''
date = "2011-06-09T02:19:00Z"
lastmod = "2011-06-09T06:48:00Z"
weight = 4469
keywords = [ "gui", "addons", "plugins" ]
aliases = [ "/questions/4469" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How should I develop this tool?](/questions/4469/how-should-i-develop-this-tool)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4469-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'd like to develop some enhancements to the Wireshark GUI, and I'm not sure what the best approach is.</p><p>The graph interface in Statistics -&gt; IOGraphs is very helpful but I'd like to add on to that, perhaps have some more visualization that could be viewed side by side with the graph.</p><p>The stuff would be very specific to mobile development, so I'm not sure adding directly into WS is the best idea (or is it?)</p><p>Ideally I could have some plugin that users could download separately. Think of a firefox add-on.</p><p>Also, I've looked into LUA and I'm not sure if it has enough power for what I'm trying to do. The visualizations have to be just as robust, if not more, than the current graph feature.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">gui addons plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Jun '11, 02:19</strong></p><img src="https://secure.gravatar.com/avatar/1e8ce1d540bf3e95d8b50c96a744124d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jackson%20Zhou&#39;s gravatar image" /><p>Jackson Zhou<br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jackson Zhou has no accepted answers">0%</span></p></div></div><div id="comments-container-4469" class="comments-container"></div><div id="comment-tools-4469" class="comment-tools"></div><div class="clear"></div><div id="comment-4469-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4473"></span>

<div id="answer-container-4473" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4473-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'll need to code this directly in C and GTK in Wireshark (see the gtk/ directory in the source tree). Wireshark does not support GUI plugins (only protocol dissector plugins and file access--wiretap--plugins). The Lua API is for dissectors, not GUI work (AFAIK).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Jun '11, 06:48</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-4473" class="comments-container"><span id="4520"></span><div id="comment-4520" class="comment"><div id="post-4520-score" class="comment-score"></div><div class="comment-text"><p>True. The Lua API is intended for writing dissectors, but it does have <strong>limited</strong> <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Gui.html">GUI support</a> (not enough for graphs/visualization).</p></div><div id="comment-4520-info" class="comment-info"><span class="comment-age">(10 Jun '11, 21:17)</span> helloworld</div></div></div><div id="comment-tools-4473" class="comment-tools"></div><div class="clear"></div><div id="comment-4473-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

