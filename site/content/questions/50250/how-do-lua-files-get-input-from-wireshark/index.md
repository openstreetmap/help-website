+++
type = "question"
title = "How do .lua files get input from wireshark?"
description = '''I have a .lua script that has GUI dependencies that I would like to remove. In other words, the .lua script makes calls to functions such as Field.new(), TextWindow.new(), etc. I want to either remove GUI altogether or automate the GUI in some way.  Are there non-GUI alternatives to passing in pcap ...'''
date = "2016-02-16T17:35:00Z"
lastmod = "2016-02-17T14:20:00Z"
weight = 50250
keywords = [ "lua", "gui", "luainterface", "tshark", "wireshark" ]
aliases = [ "/questions/50250" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do .lua files get input from wireshark?](/questions/50250/how-do-lua-files-get-input-from-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50250-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a .lua script that has GUI dependencies that I would like to remove. In other words, the .lua script makes calls to functions such as Field.new(), TextWindow.new(), etc.</p><p>I want to either remove GUI altogether or automate the GUI in some way.</p><p>Are there non-GUI alternatives to passing in pcap files to a lua script and processing the file without using Field.new(), TextWindow.new(), and Listener.new()?</p><p>or is there a way I can have my .lua script open the gui and then execute on the newly opened gui?</p><p>Ideally I would never have to open wireshark to run my .lua script.</p><p>Thanks for the help</p></div><div id="question-tags" class="tags-container tags">lua gui luainterface tshark wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Feb '16, 17:35</strong></p><img src="https://secure.gravatar.com/avatar/2a64be647ac8ec21b76a6c042bebb6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testname0110&#39;s gravatar image" /><p>testname0110<br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testname0110 has 3 accepted answers">75%</span></p></div></div><div id="comments-container-50250" class="comments-container"></div><div id="comment-tools-50250" class="comment-tools"></div><div class="clear"></div><div id="comment-50250-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="50285"></span>

<div id="answer-container-50285" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50285-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I figured it out. To input a pcap file to a lua script you do the following:</p><p>"tshark -X lua_script:file.lua -r file.pcap -o rtp.heuristic_rtp -w out"</p><p>the -w out keeps the terminal from showing stdout, which speeds up the process from 10 minutes to 1ms.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Feb '16, 14:20</strong></p><img src="https://secure.gravatar.com/avatar/2a64be647ac8ec21b76a6c042bebb6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testname0110&#39;s gravatar image" /><p>testname0110<br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testname0110 has 3 accepted answers">75%</span></p></div></div><div id="comments-container-50285" class="comments-container"></div><div id="comment-tools-50285" class="comment-tools"></div><div class="clear"></div><div id="comment-50285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="50251"></span>

<div id="answer-container-50251" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50251-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>Field.new()</code> and <code>Listener.new()</code> aren't GUI dependencies, it's a Shark dependencies - they should work in TShark as well.</p><p><code>TextWindow.new()</code> is a GUI dependency, and you eliminate it by producing your output in some other fashion, e.g. using <a href="http://www.lua.org/manual/5.2/manual.html#6.8">Lua's input and output facilities</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Feb '16, 18:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-50251" class="comments-container"><span id="50277"></span><div id="comment-50277" class="comment"><div id="post-50277-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that's very helpful. But I still don't understand how Listener.new(), Field.new() are getting inputs from my pcap file.</p></div><div id="comment-50277-info" class="comment-info"><span class="comment-age">(17 Feb '16, 10:32)</span> testname0110</div></div><span id="50278"></span><div id="comment-50278" class="comment"><div id="post-50278-score" class="comment-score"></div><div class="comment-text"><p>They're getting the inputs because the file is being read by Wireshark or TShark and the Lua interpreter embedded inside Wireshark and TShark is given those objects from Wireshark or TShark.</p><p>If you want to be able to access them in a version of Lua that is <em>NOT</em> embedded inside Wireshark or TShark, such as the one in the <code>lua</code> command, that will <em>NOT</em> work.</p></div><div id="comment-50278-info" class="comment-info"><span class="comment-age">(17 Feb '16, 10:42)</span> Guy Harris ♦♦</div></div><span id="50286"></span><div id="comment-50286" class="comment"><div id="post-50286-score" class="comment-score"></div><div class="comment-text"><p>Ok I got it. I was piping the input pcap file incorrectly, but thanks for the help!</p></div><div id="comment-50286-info" class="comment-info"><span class="comment-age">(17 Feb '16, 14:22)</span> testname0110</div></div></div><div id="comment-tools-50251" class="comment-tools"></div><div class="clear"></div><div id="comment-50251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

