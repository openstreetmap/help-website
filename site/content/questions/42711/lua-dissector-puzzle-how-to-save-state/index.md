+++
type = "question"
title = "Lua dissector puzzle : how to save state"
description = '''I am trying to write a dissector to dissect my protocol in Wireshark. There are some statuses I want to save for every TCP stream (or session). I want to know the last packet length in the same TCP stream. I try to use a big table to store. I use the Field(&quot;tcp.stream&quot;) to index the stream but it ca...'''
date = "2015-05-27T19:04:00Z"
lastmod = "2015-06-27T18:26:00Z"
weight = 42711
keywords = [ "lua" ]
aliases = [ "/questions/42711" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Lua dissector puzzle : how to save state](/questions/42711/lua-dissector-puzzle-how-to-save-state)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42711-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to write a dissector to dissect my protocol in Wireshark. There are some statuses I want to save for every TCP stream (or session). I want to know the last packet length in the same TCP stream.</p><p>I try to use a big table to store. I use the Field("tcp.stream") to index the stream but it caused an amazing bug. When I double-click the Pinfo columns, the result in the tree item (which had dissected correctly) suddenly goes bad .I try to use pinfo.visited to slove it , but the pinfo.visted always be true .</p><p>So, can someone help me?</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 May '15, 19:04</strong></p><img src="https://secure.gravatar.com/avatar/bac8cbee0f3a1748b25438dff604892a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DavidNorth&#39;s gravatar image" /><p>DavidNorth<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DavidNorth has no accepted answers">0%</span></p></div></div><div id="comments-container-42711" class="comments-container"><span id="42712"></span><div id="comment-42712" class="comment"><div id="post-42712-score" class="comment-score"></div><div class="comment-text"><p>the bug happend not only when i double-click the pinfo cols , click differnet pinfo cols can also cause the the bug</p></div><div id="comment-42712-info" class="comment-info"><span class="comment-age">(27 May '15, 19:07)</span> DavidNorth</div></div></div><div id="comment-tools-42711" class="comment-tools"></div><div class="clear"></div><div id="comment-42711-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="43616"></span>

<div id="answer-container-43616" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-43616-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>As pointed out earlier, the protocol tree is rebuilt each time you click on a packet in the GUI - or more to the point, the packet is completely re-dissected/parsed each time it's clicked, as well as some other times (like when you apply a display filter).</p><p>You said you tried to use a big Lua table to store using the <code>Field("tcp.stream")</code> as the index - that's a pretty good idea, but doesn't go far enough... I assume all you're storing in that stream-indexed table is the last packet's length for that given TCP stream index, right? So of course when some earlier packet gets dissected a second/third time, the packet length in that table for that stream index will represent the length of the last <em>dissected</em> packet of the stream, which may not be the packet previous to the one being re-dissected in the GUI list.</p><p>So what you need to do is also have a Lua table indexed by packet numbers (<code>pinfo.number</code>), where the value of the table entry is that packet number's previous-packet length. Then in your dissector or tap function check if the current packet is already in that list for its <code>info.number</code>, and if it is then the previous-packet length is the value of the found entry; if an entry isn't already in that table, then go get the number from your stream-indexed table (which represents the previous packet length), replace it with the current packet's length, and put the previous-packet length into the packet-number-indexed table so it will be found if this packet gets dissected again in the future.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jun '15, 18:26</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43616" class="comments-container"><span id="43644"></span><div id="comment-43644" class="comment"><div id="post-43644-score" class="comment-score"></div><div class="comment-text"><p>Thanks a million. You are very helpful.I'm not good at English， I don't know how to express my gratitude But what you said really means a lot to me,thanks!!!!!^__^</p></div><div id="comment-43644-info" class="comment-info"><span class="comment-age">(28 Jun '15, 20:42)</span> DavidNorth</div></div></div><div id="comment-tools-43616" class="comment-tools"></div><div class="clear"></div><div id="comment-43616-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="42740"></span>

<div id="answer-container-42740" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-42740-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>According to JeffMorriss</p><p><a href="https://ask.wireshark.org/questions/14936/lua-postdissector-executed-every-time-i-click-on-a-packet">"The protocol tree is rebuilt each time you click on the item.."</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 May '15, 06:20</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p>izopizo<br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 28 Jun '15, 20:57</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-42740" class="comments-container"></div><div id="comment-tools-42740" class="comment-tools"></div><div class="clear"></div><div id="comment-42740-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

