+++
type = "question"
title = "TextWindow.new() doesn&#x27;t work well?"
description = '''Hi everybody I tried to show a window containing a message using TextWindow.new() but it always gave me a message that tshark stopped working when I run the file, the try is in a lua file that doesn&#x27;t containing anything except TextWindow.new() and its method functions like append and so on, What&#x27;s ...'''
date = "2012-12-16T07:37:00Z"
lastmod = "2012-12-16T13:06:00Z"
weight = 16942
keywords = [ "lua", "tshark" ]
aliases = [ "/questions/16942" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [TextWindow.new() doesn't work well?](/questions/16942/textwindownew-doesnt-work-well)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16942-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi everybody I tried to show a window containing a message using TextWindow.new() but it always gave me a message that tshark stopped working when I run the file, the try is in a lua file that doesn't containing anything except TextWindow.new() and its method functions like append and so on, What's the problem? I did this because I wanted to try it alone before I merge it inside a big lua file. By the way my os is vista. Thanks a lot.</p></div><div id="question-tags" class="tags-container tags">lua tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Dec '12, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/912ebc145cb38ec3da99be6003d7d9b8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Leena&#39;s gravatar image" /><p>Leena<br />
<span class="score" title="51 reputation points">51</span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="18 badges"><span class="silver">●</span><span class="badgecount">18</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Leena has no accepted answers">0%</span></p></div></div><div id="comments-container-16942" class="comments-container"></div><div id="comment-tools-16942" class="comment-tools"></div><div class="clear"></div><div id="comment-16942-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16945"></span>

<div id="answer-container-16945" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-16945-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>What's the problem?</p></blockquote><p>TextWindow.new and tshark? How would tshark open a new Window? That function is only usable within Wireshark. You can check for gui support with gui_enabled(), see the following example.</p><blockquote><p><code>http://wiki.wireshark.org/Lua/Examples</code><br />
</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Dec '12, 13:06</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-16945" class="comments-container"><span id="17008"></span><div id="comment-17008" class="comment"><div id="post-17008-score" class="comment-score"></div><div class="comment-text"><p>Is this(the message I got) what is meant by helloworld answers:</p><p>-- If not running from Wireshark, enable the tap immediately, then</p><p>-- abort, or else we'll get an error below for trying to do GUI</p><p>-- stuff from the command line.</p><p>in the question:<a href="http://ask.wireshark.org/questions/9682/trigger-an-executable-file-once-wireshark-finds-a-keyword-on-live-capture">http://ask.wireshark.org/questions/9682/trigger-an-executable-file-once-wireshark-finds-a-keyword-on-live-capture</a></p><p>?? Thanks.</p></div><div id="comment-17008-info" class="comment-info"><span class="comment-age">(17 Dec '12, 23:43)</span> Leena</div></div><span id="17011"></span><div id="comment-17011" class="comment"><div id="post-17011-score" class="comment-score"></div><div class="comment-text"><p>In the answer of @helloworld you can see, that the code checks if the GUI is available. If no, it takes a different route.</p><p><code> if not gui_enabled() then     make_tap(_filter)     return end</code></p><p>So, you'll have to do similar things in your code. If the LUA script runs in tshark, you can't open a GUI window, as that is not possible.</p></div><div id="comment-17011-info" class="comment-info"><span class="comment-age">(18 Dec '12, 00:40)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-16945" class="comment-tools"></div><div class="clear"></div><div id="comment-16945-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

