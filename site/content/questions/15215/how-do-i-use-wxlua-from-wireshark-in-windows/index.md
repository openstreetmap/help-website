+++
type = "question"
title = "How do I use wxLua from Wireshark in Windows?"
description = '''Could you please provide some detailed instruction on &quot;This is where you would do any fancy GUI stuff with Wireshark&#x27;s GUI calls or with, e.g., wxWidgets (via wxLua) or Qt (via lqt).&quot;? How do I use wxLua for example? I tried to copy wx.dll from wxLua installer to the Program Files&#92;Wireshark library,...'''
date = "2012-10-24T02:33:00Z"
lastmod = "2012-10-24T21:21:00Z"
weight = 15215
keywords = [ "windows", "lua" ]
aliases = [ "/questions/15215" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How do I use wxLua from Wireshark in Windows?](/questions/15215/how-do-i-use-wxlua-from-wireshark-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15215-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Could you please provide some detailed instruction on "This is where you would do any fancy GUI stuff with Wireshark's GUI calls or with, e.g., wxWidgets (via wxLua) or Qt (via lqt)."? How do I use wxLua for example? I tried to copy wx.dll from wxLua installer to the Program Files\Wireshark library, but Wireshark crashed as soon as I tried to evaluate 'require "wx"' in the lua console.</p></div><div id="question-tags" class="tags-container tags">windows lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Oct '12, 02:33</strong></p><img src="https://secure.gravatar.com/avatar/6b1530d9110da70127334fe6d5d033dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cserby&#39;s gravatar image" /><p>cserby<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cserby has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>converted 24 Oct '12, 21:15</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-15215" class="comments-container"></div><div id="comment-tools-15215" class="comment-tools"></div><div class="clear"></div><div id="comment-15215-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="15236"></span>

<div id="answer-container-15236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-15236-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The crash is probably occurring because you copied <code>lua51.dll</code> from the wxLua distribution to <code>%PROGRAMFILES%\Wireshark</code>. You need to use the same Lua binary from Wireshark.</p><p>These steps work for me:</p><ol><li>Download <a href="http://sourceforge.net/projects/wxlua/files/wxlua/2.8.12.2/">wxLua 2.18.2 binaries</a></li><li>Extract and copy <code>wx.dll</code> to <code>%PROGRAMFILES%\Wireshark</code>.</li><li><strong>IMPORTANT:</strong> Copy <code>%PROGRAMFILES%\Wireshark\liblua5.1.dll</code> to <code>%PROGRAMFILES%\Wireshark\lua51.dll</code>. You need the both binaries in the same directory (one used by Wireshark; the other by wxLua). Do not copy <code>lua51.dll</code> from the wxLua distribution.</li><li>Open Wireshark.</li><li>Go to menu: <strong>Tools &gt; Lua &gt; Evaluate</strong>.</li><li>In the <strong>Evaluate Lua</strong> window, copy and paste the text from <a href="http://pastebin.com/9f7Mk7dx"><code>dialog.wx.lua</code></a>.</li><li>Click <strong>Evaluate</strong> button.</li></ol><p>You should see something like this:</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Snapshot_10:24:12_11:13_PM.png" alt="alt text" /></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Oct '12, 21:21</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></img></div></div><div id="comments-container-15236" class="comments-container"><span id="40647"></span><div id="comment-40647" class="comment"><div id="post-40647-score" class="comment-score"></div><div class="comment-text"><p>When I followed above steps and tried to Evaluate simple require("wx") It is giving me error like this</p><p>"Lua : Error During execurion of dialog callback: error loading module 'wx' from file C:\Program Files\wireshark\wx.dll: %1 isnot a valid Win32 application"</p><p>Can you do something with this error???</p></div><div id="comment-40647-info" class="comment-info"><span class="comment-age">(18 Mar '15, 02:17)</span> ankit</div></div><span id="40649"></span><div id="comment-40649" class="comment"><div id="post-40649-score" class="comment-score"></div><div class="comment-text"><p>That type of error is sometimes due to a 32\64 bit mismatch. Are you sure that Wireshark and wxLua are the same architecture?</p></div><div id="comment-40649-info" class="comment-info"><span class="comment-age">(18 Mar '15, 03:40)</span> grahamb ♦</div></div></div><div id="comment-tools-15236" class="comment-tools"></div><div class="clear"></div><div id="comment-15236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

