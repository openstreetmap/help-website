+++
type = "question"
title = "How do I setup Wireshark to run Lua&#x27;s CLRPackage (Works with LFW not with Wireshark"
description = '''As the person here I&#x27;m trying to setup Wireshark so that I can use the LuaInterface to use some of the classes in the .NET framework : I have a .Net dll able to decipher frames and I want to reuse it.  When I try to launch the command &quot; require &#x27;luanet&#x27; &quot; with LuaForWindows it works:  But when I try...'''
date = "2015-04-01T02:14:00Z"
lastmod = "2015-04-01T05:41:00Z"
weight = 41087
keywords = [ "luainterface" ]
aliases = [ "/questions/41087" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I setup Wireshark to run Lua's CLRPackage (Works with LFW not with Wireshark](/questions/41087/how-do-i-setup-wireshark-to-run-luas-clrpackage-works-with-lfw-not-with-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41087-score" class="post-score" title="current number of votes">0</div><span id="post-41087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>As the person <a href="https://ask.wireshark.org/questions/5868/how-do-i-setup-wireshark-to-run-luas-clrpackage">here</a> I'm trying to setup Wireshark so that I can use the LuaInterface to use some of the classes in the .NET framework : I have a .Net dll able to decipher frames and I want to reuse it.</p><p>When I try to launch the command " require 'luanet' " with LuaForWindows it works:</p><p><img src="http://imageshack.com/a/img537/8434/JQXxrk.png" alt="alt text" /></p><p>But when I try to evaluate the same command with wireshark it doesn't work : <img src="http://imageshack.com/a/img538/4052/Bj0wjz.jpg" alt="alt text" /> <img src="http://imageshack.com/a/img537/4807/D0Sdfb.png" alt="alt text" /> <img src="http://imageshack.com/a/img661/2354/zbQVrB.png" alt="alt text" /></p><p>The difference between Wireshark and LuaForWindows is that it doesn't use the same lua5.1.dll. Does a consistent lua5.1.dll exists with luanet and luaInterface taken from <a href="http://imageshack.com/a/img538/4052/Bj0wjz.jpg">here</a> and Wireshark?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-luainterface" rel="tag" title="see questions tagged &#39;luainterface&#39;">luainterface</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '15, 02:14</strong></p><img src="https://secure.gravatar.com/avatar/91c3b4de80a272c387ee6db9accbb6ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SWLuaTest&#39;s gravatar image" /><p><span>SWLuaTest</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SWLuaTest has one accepted answer">100%</span></p></img></div></div><div id="comments-container-41087" class="comments-container"></div><div id="comment-tools-41087" class="comment-tools"></div><div class="clear"></div><div id="comment-41087-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41089"></span>

<div id="answer-container-41089" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41089-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41089-score" class="post-score" title="current number of votes">1</div><span id="post-41089-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SWLuaTest has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Roughly translating the error dialog, I suspect that there might be a "bittedness" issue. Is your version of Wireshark 32 or 64 bit? And the same question for luanet?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Apr '15, 03:05</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></img></div></div><div id="comments-container-41089" class="comments-container"><span id="41091"></span><div id="comment-41091" class="comment"><div id="post-41091-score" class="comment-score"></div><div class="comment-text"><p>You are right the problem came from my version of Wireshark... I download Wireshark in 32bit (I had 64bit version) and it works now.</p></div><div id="comment-41091-info" class="comment-info"><span class="comment-age">(01 Apr '15, 05:13)</span> <span class="comment-user userinfo">SWLuaTest</span></div></div><span id="41093"></span><div id="comment-41093" class="comment"><div id="post-41093-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-41093-info" class="comment-info"><span class="comment-age">(01 Apr '15, 05:41)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-41089" class="comment-tools"></div><div class="clear"></div><div id="comment-41089-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

