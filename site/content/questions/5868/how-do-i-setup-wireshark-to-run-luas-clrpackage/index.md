+++
type = "question"
title = "How do I setup Wireshark to run Lua&#x27;s CLRPackage"
description = '''I&#x27;m trying to setup Wireshark so that I can use the LuaInterface to use some of the classes in the .NET framework. I&#x27;m able to get it working running through the Lua command line, but when I try to require &quot;CLRPackage&quot; in the init.lua startup script, it doesnt appear to find the required files. I ge...'''
date = "2011-08-25T07:15:00Z"
lastmod = "2015-02-12T05:53:00Z"
weight = 5868
keywords = [ "lua", "luainterface", "clrpackage", ".net", "wireshark" ]
aliases = [ "/questions/5868" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How do I setup Wireshark to run Lua's CLRPackage](/questions/5868/how-do-i-setup-wireshark-to-run-luas-clrpackage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5868-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5868-score" class="post-score" title="current number of votes">1</div><span id="post-5868-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to setup <a href="http://www.wireshark.org/">Wireshark</a> so that I can use the <a href="http://penlight.luaforge.net/packages/LuaInterface/#T5">LuaInterface</a> to use some of the classes in the .NET framework. I'm able to get it working running through the Lua command line, but when I try to <code>require "CLRPackage"</code> in the <code>init.lua</code> startup script, it doesnt appear to find the required files. I get the following exception when starting Wireshark:</p><pre><code>Lua: Error during loading:
 C:\Program Files\Wireshark\luascript.lua:25: module &#39;CLRPackage&#39; not found:
    no field package.preload[&#39;CLRPackage&#39;]
    no file &#39;.\CLRPackage.lua&#39;
    no file &#39;C:\Program Files\Wireshark\lua\CLRPackage.lua&#39;
    no file &#39;C:\Program Files\Wireshark\lua\CLRPackage\init.lua&#39;
    no file &#39;C:\Program Files\Wireshark\CLRPackage.lua&#39;
    no file &#39;C:\Program Files\Wireshark\CLRPackage\init.lua&#39;
    no file &#39;C:\Program Files\Lua\5.1\lua\CLRPackage.luac&#39;
    no file &#39;.\CLRPackage.dll&#39;
    no file &#39;.\CLRPackage51.dll&#39;
    no file &#39;C:\Program Files\Wireshark\CLRPackage.dll&#39;
    no file &#39;C:\Program Files\Wireshark\CLRPackage51.dll&#39;
    no file &#39;C:\Program Files\Wireshark\clibs\CLRPackage.dll&#39;
    no file &#39;C:\Program Files\Wireshark\clibs\CLRPackage51.dll&#39;
    no file &#39;C:\Program Files\Wireshark\loadall.dll&#39;
    no file &#39;C:\Program Files\Wireshark\clibs\loadall.dll&#39;</code></pre><p>I've tried setting the <code>package.path</code> and <code>package.cpath</code> to match what is set at the command line, but that doesnt seem to help.</p><pre><code>package.path = &quot;;.\\?.lua;C:\\Program Files\\Lua\\5.1\\lua\\?.lua;C:\\Program Files\\Lua\\5.1\\lua\\?\\init.lua;C:\\Program Files\\Lua\\5.1\\?.lua;C:\\Program Files\\Lua\\5.1\\?\\init.lua;C:\\Program Files\\Lua\\5.1\\lua\\?.luac;C:\\Program Files\\Lua\\5.1\\lua\\?lua&quot;

package.cpath = package.cpath .. &quot;.\\?.dll;.\\?51.dll;C:\\Program Files\\Lua\\5.1\\?.dll;C:\\Program Files\\Lua\\5.1\\?51.dll;C:\\Program Files\\Lua\\5.1\\clibs\\?.dll;C:\\Program Files\\Lua\\5.1\\clibs\\?51.dll;C:\\Program Files\\Lua\\5.1\\loadall.dll;C:\\Program Files\\Lua\\5.1\\clibs\\loadall.dll;C:\\Program Files\\Lua\\5.1\\clibs\\luanet.dll&quot;</code></pre><p>When I do this, I get the following error:</p><pre><code>Lua: Error during loading:
   error loading module &#39;luanet&#39; from file 
   &#39;C:\Program Files\Lua\5.1\clibs\luanet.dll&#39;:
   The spcecified module could not be found.</code></pre><p>This is a strange error since the file definitely exists.</p><p>I've installed the Lua package for windows in <code>C:\Program Files\Lua\5.1</code>.</p><p>Has anyone been able to get this working? Any help would be appreciated.</p><p>I'm using Wireshark 1.4.4 with Lua 5.1.4 I downloaded luaforwindows from <a href="code.google.com/p/luaforwindows/downloads/list">here</a>. It's version 5.1.4-45</p><p>Microsoft Windows XP Professional Version 2002 Service Pack 3</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-luainterface" rel="tag" title="see questions tagged &#39;luainterface&#39;">luainterface</span> <span class="post-tag tag-link-clrpackage" rel="tag" title="see questions tagged &#39;clrpackage&#39;">clrpackage</span> <span class="post-tag tag-link-.net" rel="tag" title="see questions tagged &#39;.net&#39;">.net</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Aug '11, 07:15</strong></p><img src="https://secure.gravatar.com/avatar/8ceec9f7f83e3c12a72b6442393bde2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SwDevMan81&#39;s gravatar image" /><p><span>SwDevMan81</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SwDevMan81 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Sep '11, 10:04</strong> </span></p></div></div><div id="comments-container-5868" class="comments-container"></div><div id="comment-tools-5868" class="comment-tools"></div><div class="clear"></div><div id="comment-5868-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5880"></span>

<div id="answer-container-5880" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5880-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5880-score" class="post-score" title="current number of votes">3</div><span id="post-5880-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SwDevMan81 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><strong>Your Wireshark is old.</strong> The current stable release is <a href="http://www.wireshark.org/download.html">Wireshark 1.6.1</a>.</p><p><strong>Wireshark already includes Lua.</strong> You don't need to install your own copy of Lua because Wireshark comes with its own Lua interpreter (and will only use its own). However, your Wireshark Lua scripts can still call the libraries installed by LuaForWindows.</p><p><strong>LuaInterface 1.5.3 is probably incompatible.</strong> LuaForWindows v5.1.4-45 ships with LuaInterface 1.5.3, which might be incompatible with your Wireshark installation (exhibited by runtime error <a href="http://msdn.microsoft.com/en-us/library/ms235560(v=vs.80).aspx">R6034</a> upon loading luanet.dll). This was true for me with Wireshark 1.6.1 on Windows 7. You can get compatible binaries of LuaInterface 2.0.3 from this <a href="http://code.google.com/p/luaforwindows/issues/detail?id=35">ticket</a>.</p><p><strong>Instructions</strong></p><p>1) Copy the VS2005 SP1 Redistributables from LuaForWindows to Wireshark's program directory (or you can download the redist package from Microsoft...see ticket):</p><p><em>From:</em></p><ul><li><code>%PROGRAMFILES%\Lua\5.1\install\support\Microsoft.VC80.CRT.SP1\Microsoft.VC80.CRT.manifest</code></li><li><code>%PROGRAMFILES%\Lua\5.1\install\support\Microsoft.VC80.CRT.SP1\msvcm80.dll</code></li><li><code>%PROGRAMFILES%\Lua\5.1\install\support\Microsoft.VC80.CRT.SP1\msvcp80.dll</code></li><li><code>%PROGRAMFILES%\Lua\5.1\install\support\Microsoft.VC80.CRT.SP1\msvcr80.dll</code></li></ul><p><em>To:</em></p><ul><li><code>%PROGRAMFILES%\Wireshark\Microsoft.VC80.CRT.manifest</code></li><li><code>%PROGRAMFILES%\Wireshark\msvcm80.dll</code></li><li><code>%PROGRAMFILES%\Wireshark\msvcp80.dll</code></li><li><code>%PROGRAMFILES%\Wireshark\msvcr80.dll</code></li></ul><p>2) Download LuaInterface 2.0.3 ZIP from this <a href="http://code.google.com/p/luaforwindows/issues/detail?id=35">ticket</a>, and copy the following from it:</p><p><em>From:</em></p><ul><li><code>...\bin\Release\LuaInterface.dll</code></li><li><code>...\bin\Release\luanet.dll</code></li></ul><p><em>To:</em></p><ul><li><code>%PROGRAMFILES%\Wireshark\clibs\LuaInterface.dll</code></li><li><code>%PROGRAMFILES%\Wireshark\clibs\luanet.dll</code></li></ul><p><em>From:</em></p><ul><li><code>...\LuaInterface\lua\CLRForm.lua</code></li><li><code>...\LuaInterface\lua\CLRPackage.lua</code><br />
</li></ul><p><em>To:</em></p><ul><li><code>%PROGRAMFILES%\Wireshark\lua\CLRForm.lua</code></li><li><code>%PROGRAMFILES%\Wireshark\lua\CLRPackage.lua</code></li></ul><p>3) Restart Wireshark/TShark if already running.</p><p>4) <em>OPTIONAL:</em> From Wireshark, open menu <strong>Tools &gt; Lua &gt; Evaluate</strong>. In the textbox that appears, enter some <a href="http://penlight.luaforge.net/packages/LuaInterface#T7">sample code</a>, and click <strong>Evaluate</strong>.</p><p>This should result in something like this:</p><p><a href="http://postimage.org/image/2nrqg8flw/"><img src="http://s1.postimage.org/2nrqg8flw/Screen_Shot_2011_08_25_at_10_24_05_PM.jpg" alt="screenshot" /></a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '11, 19:41</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Aug '11, 20:00</strong> </span></p></div></div><div id="comments-container-5880" class="comments-container"><span id="5884"></span><div id="comment-5884" class="comment"><div id="post-5884-score" class="comment-score"></div><div class="comment-text"><p>+1 @helloworld - Your answer was exactly what I need. Thanks so much for the quick response!</p></div><div id="comment-5884-info" class="comment-info"><span class="comment-age">(26 Aug '11, 06:48)</span> <span class="comment-user userinfo">SwDevMan81</span></div></div><span id="39832"></span><div id="comment-39832" class="comment"><div id="post-39832-score" class="comment-score"></div><div class="comment-text"><p>This solution will only work for Wireshark versions up to and including 1.11.2. In Wireshark 1.11.3, Lua was updated from 5.1 to 5.2 and doesn't support backward compatibility. For information on setting up the LuaInterface with Wireshark 1.11.3 and beyond with Lua 5.2, see <a href="https://ask.wireshark.org/questions/39553/how-do-i-setup-wireshark-to-run-luas-clrpackage">here</a></p></div><div id="comment-39832-info" class="comment-info"><span class="comment-age">(12 Feb '15, 05:53)</span> <span class="comment-user userinfo">SwDevMan81</span></div></div></div><div id="comment-tools-5880" class="comment-tools"></div><div class="clear"></div><div id="comment-5880-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

