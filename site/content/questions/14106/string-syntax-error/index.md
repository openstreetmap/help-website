+++
type = "question"
title = "String syntax error"
description = '''Hi! I have one little problem: C:&#92;Program Files&#92;Wireshark&#92;tshark -x lua_script:hello.lua Capturing on Microsoft tshark: Invalid capture filter &quot;lua_script:hello.lua&quot; for interface Microsoft! That string isn&#x27;t a valid capture filter &amp;lt;syntax error=&quot;&quot;&amp;gt;. See the User&#x27;s Guide for a description of t...'''
date = "2012-09-07T01:47:00Z"
lastmod = "2012-09-07T01:56:00Z"
weight = 14106
keywords = [ "executable", "tshark", "syntax" ]
aliases = [ "/questions/14106" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [String syntax error](/questions/14106/string-syntax-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14106-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi! I have one little problem:</p><p>C:\Program Files\Wireshark\tshark -x lua_script:hello.lua Capturing on Microsoft tshark: Invalid capture filter "lua_script:hello.lua" for interface Microsoft!</p><p>That string isn't a valid capture filter &lt;syntax error=""&gt;. See the User's Guide for a description of the capture filter syntax. 0 packets captured</p><p>hello.lua contains only this: print("Hello World")</p><p>What's the problem?</p></div><div id="question-tags" class="tags-container tags">executable tshark syntax</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '12, 01:47</strong></p><img src="https://secure.gravatar.com/avatar/5c2ae72f5684890320d7616b442365a3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="speede05&#39;s gravatar image" /><p>speede05<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="speede05 has no accepted answers">0%</span></p></div></div><div id="comments-container-14106" class="comments-container"></div><div id="comment-tools-14106" class="comment-tools"></div><div class="clear"></div><div id="comment-14106-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14107"></span>

<div id="answer-container-14107" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14107-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The problem is that you used "-x" instead of "-X". As -x does not take an argument, tshark sees "lua_script:hello.lua" as a capture filter.</p><p>Capitalize! ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '12, 01:56</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-14107" class="comments-container"><span id="14108"></span><div id="comment-14108" class="comment"><div id="post-14108-score" class="comment-score"></div><div class="comment-text"><p>ok..but it's not good... new problem...</p><p>'tshark' is not recognized as an internal or external command, operable program or batch file.</p></div><div id="comment-14108-info" class="comment-info"><span class="comment-age">(07 Sep '12, 02:06)</span> speede05</div></div><span id="14109"></span><div id="comment-14109" class="comment"><div id="post-14109-score" class="comment-score"></div><div class="comment-text"><p>that's because of the blank in "Program Files". So, quote yourself!</p><blockquote><p><code>"C:\Program Files\Wireshark\tshark" -X ....</code></p></blockquote></div><div id="comment-14109-info" class="comment-info"><span class="comment-age">(07 Sep '12, 02:19)</span> Kurt Knochner ♦</div></div><span id="14111"></span><div id="comment-14111" class="comment"><div id="post-14111-score" class="comment-score"></div><div class="comment-text"><p>what can i do? i tried in root running, but is not good</p></div><div id="comment-14111-info" class="comment-info"><span class="comment-age">(07 Sep '12, 02:38)</span> speede05</div></div><span id="14112"></span><div id="comment-14112" class="comment"><div id="post-14112-score" class="comment-score"></div><div class="comment-text"><p>What do you mean by "running in root" and what exactkly is not good?</p></div><div id="comment-14112-info" class="comment-info"><span class="comment-age">(07 Sep '12, 02:43)</span> Kurt Knochner ♦</div></div><span id="14113"></span><div id="comment-14113" class="comment"><div id="post-14113-score" class="comment-score"></div><div class="comment-text"><p>i moved the wireshark folder into "C"... i can here running the script, but not good...</p><p>so... "C:\Wireshark&gt;tshark -X lua_script:hello.lua Capturing on Microsoft 0 packets captured"</p><p>where is the string "Hello World"</p></div><div id="comment-14113-info" class="comment-info"><span class="comment-age">(07 Sep '12, 02:53)</span> speede05</div></div><span id="14114"></span><div id="comment-14114" class="comment not_top_scorer"><div id="post-14114-score" class="comment-score"></div><div class="comment-text"><p>Which version of tshark are you running? Do you see "with lua 5.1" in the output of "tshark -v"?</p></div><div id="comment-14114-info" class="comment-info"><span class="comment-age">(07 Sep '12, 02:59)</span> SYN-bit ♦♦</div></div><span id="14115"></span><div id="comment-14115" class="comment not_top_scorer"><div id="post-14115-score" class="comment-score"></div><div class="comment-text"><p>where did you place the file hello.lua?</p><p>Do you see the following (or a similar) message?</p><blockquote><p><code>tshark: The file "hello.lua" doesn't exist.</code></p></blockquote></div><div id="comment-14115-info" class="comment-info"><span class="comment-age">(07 Sep '12, 03:03)</span> Kurt Knochner ♦</div></div><span id="14116"></span><div id="comment-14116" class="comment not_top_scorer"><div id="post-14116-score" class="comment-score"></div><div class="comment-text"><p>BTW: The script needs to be in the folder where you start the tshark command, not in the Wireshark install folder, unless you specify the whole path.</p><p>So, either this (hello.lua in c:\temp)</p><blockquote><p><code>cd \temp</code><br />
<code>c:\temp&gt;"c:\Program Files\Wireshark\tshark.exe" -X lua_script:hello.lua</code></p></blockquote><p>or this (hello.lua in c:\programm files\wireshark)</p><blockquote><p><code>"c:\Program Files\Wireshark\tshark.exe" -X lua_script:"c:\Program Files\Wireshark\hello.lua"</code></p></blockquote><p>You need to double quote the blank in the path name, as that's a specific problem of the DOS box commandline.</p></div><div id="comment-14116-info" class="comment-info"><span class="comment-age">(07 Sep '12, 03:13)</span> Kurt Knochner ♦</div></div><span id="14117"></span><div id="comment-14117" class="comment not_top_scorer"><div id="post-14117-score" class="comment-score"></div><div class="comment-text"><p>ohh... it's good... i dont enabled lua :...</p></div><div id="comment-14117-info" class="comment-info"><span class="comment-age">(07 Sep '12, 03:23)</span> speede05</div></div></div><div id="comment-tools-14107" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-14107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

