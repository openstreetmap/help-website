+++
type = "question"
title = "no symbols have been loaded"
description = '''hi, during debugging the wireshark dissector i am getting the error as &quot;no symbols have been loaded&quot; , i have given the correct path to .pdb file but still getting the same error. can anybody help me in this issue.'''
date = "2011-06-08T01:57:00Z"
lastmod = "2011-06-08T01:57:00Z"
weight = 4451
keywords = [ "development", "symbol", "debugger", "error" ]
aliases = [ "/questions/4451" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [no symbols have been loaded](/questions/4451/no-symbols-have-been-loaded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-4451-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, during debugging the wireshark dissector i am getting the error as <strong>"no symbols have been loaded"</strong> , i have given the correct path to .pdb file but still getting the same error. can anybody help me in this issue.</p></div><div id="question-tags" class="tags-container tags">development symbol debugger error</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '11, 01:57</strong></p><img src="https://secure.gravatar.com/avatar/257c9f9e498193d7ddde57090efe094a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sagu072&#39;s gravatar image" /><p>sagu072<br />
<span class="score" title="35 reputation points">35</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sagu072 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>retagged 08 Jun '11, 19:48</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-4451" class="comments-container"><span id="4463"></span><div id="comment-4463" class="comment"><div id="post-4463-score" class="comment-score"></div><div class="comment-text"><p>Which debugger are you using?</p><p>I've used gdb, Eclipse, Netbeans, and Visual Studio to debug Wireshark, and I"ve never had to specify a pdb file.</p></div><div id="comment-4463-info" class="comment-info"><span class="comment-age">(08 Jun '11, 19:52)</span> helloworld</div></div><span id="6335"></span><div id="comment-6335" class="comment"><div id="post-6335-score" class="comment-score"></div><div class="comment-text"><p>Hi I am using MSVC++ Express Edition and have the same problem. I can step in wireshark with F11 (starting at WinMain) but when I set a breakpoint within my custom plugin I get the "no symbols have been loaded for this document" message.</p><p>Any help?</p></div><div id="comment-6335-info" class="comment-info"><span class="comment-age">(13 Sep '11, 23:50)</span> Kostas</div></div><span id="6338"></span><div id="comment-6338" class="comment"><div id="post-6338-score" class="comment-score"></div><div class="comment-text"><p>Where are you running Wireshark from for your debug session?</p></div><div id="comment-6338-info" class="comment-info"><span class="comment-age">(13 Sep '11, 23:54)</span> grahamb ♦</div></div><span id="6339"></span><div id="comment-6339" class="comment"><div id="post-6339-score" class="comment-score"></div><div class="comment-text"><p>Sorry it was quite simple. When I start the debugger (at WinMain) my plugin dll had not been loaded, so when I set a breakpoint at a plugin source file, MSVC++ complains.</p><p>However, when I click continue and then load a capture that triggers my plugin, the dll is loaded (with the symbols) and the breakpoint becomes valid!</p></div><div id="comment-6339-info" class="comment-info"><span class="comment-age">(14 Sep '11, 00:14)</span> Kostas</div></div></div><div id="comment-tools-4451" class="comment-tools"></div><div class="clear"></div><div id="comment-4451-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

