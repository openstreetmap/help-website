+++
type = "question"
title = "Using Wireshark libraries in C#"
description = '''I want to make my own application using Wireshark libs. I did it already with NetworkMonitor API, but Wireshark offers some protocolls (i.e. S7comm). The only one possibility I&#x27;ve found is to use Wireshark indirectly, using Lua. (Set a reference on LuaInterface.dll then &quot;using LuaInterface&quot; etc.) ht...'''
date = "2012-05-11T02:49:00Z"
lastmod = "2013-03-25T06:58:00Z"
weight = 10923
keywords = [ "lua", "luainterface", "api", "csharp" ]
aliases = [ "/questions/10923" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Using Wireshark libraries in C\#](/questions/10923/using-wireshark-libraries-in-c)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10923-score" class="post-score" title="current number of votes">0</div><span id="post-10923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to make my own application using Wireshark libs. I did it already with NetworkMonitor API, but Wireshark offers some protocolls (i.e. S7comm).</p><p>The only one possibility I've found is to use Wireshark indirectly, using Lua. (Set a reference on LuaInterface.dll then "using LuaInterface" etc.) <a href="http://www.dreamincode.net/forums/topic/240886-integrating-lua-with-c%23-using-luainterface/">http://www.dreamincode.net/forums/topic/240886-integrating-lua-with-c%23-using-luainterface/</a></p><p>Is it posiible without Lua? I want to make a reference to Wireshark in my project and to use all benefits of C#.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-luainterface" rel="tag" title="see questions tagged &#39;luainterface&#39;">luainterface</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span> <span class="post-tag tag-link-csharp" rel="tag" title="see questions tagged &#39;csharp&#39;">csharp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 May '12, 02:49</strong></p><img src="https://secure.gravatar.com/avatar/f45848e2181a57e335916a9bc57aa0c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ZvDj&#39;s gravatar image" /><p><span>ZvDj</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ZvDj has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 May '12, 14:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-10923" class="comments-container"></div><div id="comment-tools-10923" class="comment-tools"></div><div class="clear"></div><div id="comment-10923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10924"></span>

<div id="answer-container-10924" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10924-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10924-score" class="post-score" title="current number of votes">0</div><span id="post-10924-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Using libwireshark.dll from C# should be like using any other native DLL from C#. See <a href="http://social.msdn.microsoft.com/Forums/en-US/vcgeneral/thread/5df04db1-bbc8-4389-b752-802bc84148fe/">here</a> for some details on how to do that in general.</p><p>However, using libwireshark is not for the faint-hearted, expect some bumps. The API hasn't really been designed for external consumption, more for the Wireshark project as a whole. There have been some other folks successfully using it in other apps (not C# IRC) so it can be done.</p><p>Remember the licensing of libwireshark is GPL, so think about the implications of that and read the <a href="http://www.wireshark.org/faq.html#q1.8">FAQ</a> on that for starters.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 May '12, 03:04</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-10924" class="comments-container"><span id="10933"></span><div id="comment-10933" class="comment"><div id="post-10933-score" class="comment-score"></div><div class="comment-text"><p>Which kind of invoking would you recommend: Explicit, Implicit, Dynamic or "Converting C++ DLL to COM Server"?</p><p>Unfortunatelly are the links on the site, you have send me, not valid. Can you possibly send me links to some Examples of using of libwireshark.dll in C#?</p><p>Thanks in advance</p></div><div id="comment-10933-info" class="comment-info"><span class="comment-age">(11 May '12, 03:57)</span> <span class="comment-user userinfo">ZvDj</span></div></div><span id="10936"></span><div id="comment-10936" class="comment"><div id="post-10936-score" class="comment-score"></div><div class="comment-text"><p>I converted your "answer" to a comment as that's how this site works, please read the FAQ for more info.</p><p>The links works for me, here's what they point to: <a href="http://1code.codeplex.com/wikipage?title=Invoke%20Native%20C%2b%2b%20DLL%20from%20.NET">Invoke Native C++ DLL from .NET Code</a></p><p>I have no links to examples of using libwireshark.dll from C#. <a href="http://lmgtfy.com/?q=using+libwireshark+from+c%23">Google</a> may have some, try that.</p></div><div id="comment-10936-info" class="comment-info"><span class="comment-age">(11 May '12, 04:22)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="10938"></span><div id="comment-10938" class="comment"><div id="post-10938-score" class="comment-score"></div><div class="comment-text"><p>Sorry, I can open yout Link, but when I try to download (Download the All-In-One Code Framework (Library) package), I receive the message "The specified release was not found."</p></div><div id="comment-10938-info" class="comment-info"><span class="comment-age">(11 May '12, 04:35)</span> <span class="comment-user userinfo">ZvDj</span></div></div><span id="10939"></span><div id="comment-10939" class="comment"><div id="post-10939-score" class="comment-score"></div><div class="comment-text"><p>So it is. You'll have to contact MS about that.</p></div><div id="comment-10939-info" class="comment-info"><span class="comment-age">(11 May '12, 05:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="10940"></span><div id="comment-10940" class="comment"><div id="post-10940-score" class="comment-score"></div><div class="comment-text"><p>Anyway, thank you very much</p></div><div id="comment-10940-info" class="comment-info"><span class="comment-age">(11 May '12, 05:09)</span> <span class="comment-user userinfo">ZvDj</span></div></div></div><div id="comment-tools-10924" class="comment-tools"></div><div class="clear"></div><div id="comment-10924-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19811"></span>

<div id="answer-container-19811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-19811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-19811-score" class="post-score" title="current number of votes">0</div><span id="post-19811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>you should be able to create an execute command function in c# that expects a string... then execute the tshark command from the execute command function which invokes tshark and it's respective arguments :-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '13, 06:58</strong></p><img src="https://secure.gravatar.com/avatar/cd1de247055a50b69f5a55700eb3b238?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fdfvo&#39;s gravatar image" /><p><span>fdfvo</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fdfvo has no accepted answers">0%</span></p></div></div><div id="comments-container-19811" class="comments-container"></div><div id="comment-tools-19811" class="comment-tools"></div><div class="clear"></div><div id="comment-19811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

