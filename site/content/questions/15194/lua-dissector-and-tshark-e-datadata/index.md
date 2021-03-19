+++
type = "question"
title = "Lua dissector and &quot;tshark -e data.data&quot;"
description = '''For a private protocol over TCP, I am writing a Lua-based dissector. The dissector is very much in the spirit of the first part of http://wiki.wireshark.org/Lua/Dissectors. Within Wireshark, this dissector works fine, but if I use tshark -X lua_script:foo.lua ... -e data.data ...  to simply dump the...'''
date = "2012-10-23T06:28:00Z"
lastmod = "2012-10-29T04:30:00Z"
weight = 15194
keywords = [ "lua", "tshark" ]
aliases = [ "/questions/15194" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua dissector and "tshark -e data.data"](/questions/15194/lua-dissector-and-tshark-e-datadata)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15194-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>For a private protocol over TCP, I am writing a Lua-based dissector. The dissector is very much in the spirit of the first part of <a href="http://wiki.wireshark.org/Lua/Dissectors">http://wiki.wireshark.org/Lua/Dissectors</a>. Within Wireshark, this dissector works fine, but if I use</p><pre><code>tshark -X lua_script:foo.lua ... -e data.data ...</code></pre><p>to simply dump the whole TCP PDU onto stdout, I don't get anything. But, of course, if I remove the <code>-X...</code>, the dump works. I am in search for the magic statement to enable this feature. I am using the latest Wireshark version.</p></div><div id="question-tags" class="tags-container tags">lua tshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>23 Oct '12, 06:28</strong></p><img src="https://secure.gravatar.com/avatar/eb3cc272674a6867952ada612d62b155?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Salonbolschewik&#39;s gravatar image" /><p>Salonbolschewik<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Salonbolschewik has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 Oct '12, 18:08</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-15194" class="comments-container"><span id="15206"></span><div id="comment-15206" class="comment"><div id="post-15206-score" class="comment-score"></div><div class="comment-text"><p>It could be the code in <code>foo.lua</code>, the command you're entering, or simply just a bug. Too difficult to tell without more details. Include your code in the question; and the complete command line (plus its output). What OS are you using?</p></div><div id="comment-15206-info" class="comment-info"><span class="comment-age">(23 Oct '12, 18:38)</span> helloworld</div></div></div><div id="comment-tools-15194" class="comment-tools"></div><div class="clear"></div><div id="comment-15194-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15329"></span>

<div id="answer-container-15329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15329-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>But, of course, if I remove the -X..., the dump works.</p></blockquote><p>O.K. that probably means, that you loaded your script in <strong>init.lua</strong>, otherwise you would not see the output of your script.</p><p>So, if you load the script a second time with -X, that will probably lead to a problem with duplicate declarations and you might see an error message in the console window where you started tshark.</p><p>Suggestion: Remove your script from <strong>init.lua</strong> when you run it with -X.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Oct '12, 04:30</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-15329" class="comments-container"></div><div id="comment-tools-15329" class="comment-tools"></div><div class="clear"></div><div id="comment-15329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

