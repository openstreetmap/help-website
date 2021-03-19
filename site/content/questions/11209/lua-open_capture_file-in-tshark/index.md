+++
type = "question"
title = "Lua open_capture_file in tshark"
description = '''I want to parse all files in a directory using a Lua tap. The tap is already working, but the problem now is opening snoop files from Lua in tshark. When I try this: for filename in Dir.open(&quot;D:/snoop/&quot;,&quot;snoop&quot;) do  local logfile = filename..&quot;.csv&quot;  open_capture_file(filename) end  I see: tshark: Lu...'''
date = "2012-05-22T05:31:00Z"
lastmod = "2012-05-23T02:00:00Z"
weight = 11209
keywords = [ "lua", "tshark" ]
aliases = [ "/questions/11209" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Lua open\_capture\_file in tshark](/questions/11209/lua-open_capture_file-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11209-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11209-score" class="post-score" title="current number of votes">0</div><span id="post-11209-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I want to parse all files in a directory using a Lua tap. The tap is already working, but the problem now is opening snoop files from Lua in <code>tshark</code>. When I try this:</p><pre><code>for filename in Dir.open(&quot;D:/snoop/&quot;,&quot;snoop&quot;)
do
    local logfile = filename..&quot;.csv&quot;
    open_capture_file(filename)
end</code></pre><p>I see:</p><pre><code>tshark: Lua: Error during loading:
 [string &quot;lua_tap_1.lua&quot;]:88: open_capture_file: GUI not available
Capturing on Microsoft
0 packets captured</code></pre><p>Is there anything like <a href="http://wiki.wireshark.org/LuaAPI/GUI#open_capture_file.28filename.2C_filter.29"><code>open_capture_file()</code></a> for <code>tshark</code> (not GUI)?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 May '12, 05:31</strong></p><img src="https://secure.gravatar.com/avatar/9f5a1001269517ce97c85ff8fbb57897?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tciops&#39;s gravatar image" /><p><span>tciops</span><br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tciops has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 May '12, 06:27</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11209" class="comments-container"></div><div id="comment-tools-11209" class="comment-tools"></div><div class="clear"></div><div id="comment-11209-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="11210"></span>

<div id="answer-container-11210" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11210-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11210-score" class="post-score" title="current number of votes">0</div><span id="post-11210-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>No, there is no Lua function to open a capture file in <code>tshark</code> (as can be seen in the <a href="http://www.wireshark.org/docs/wsug_html_chunked/wsluarm.html">Wireshark User Manual</a> and <a href="http://wiki.wireshark.org/LuaAPI">wiki</a>). Instead, you can use a shell script to pass the files to <code>tshark</code> for Lua tap processing. This would replace the Lua that opens the <code>.snoop</code> files.</p><p>For example, this <code>bash</code> script (tested in OSX) passes all <code>.snoop</code> files in the current directory to <code>tshark</code> (one file at a time), where <code>tap.lua</code> processes the file contents.</p><pre><code>for x in *.snoop; do tshark -q -Xlua_script:/path/to/tap.lua -r &quot;$x&quot;; done</code></pre><h4 id="parameters">Parameters:</h4><ul><li><strong><code>-q</code></strong> = silences the packet info output from processing the capture file</li><li><strong><code>-Xlua_script</code></strong> = loads a Lua script (unnecessary if file is already in Lua initialization path)</li><li><strong><code>-r</code></strong> = opens a capture file, prints packet info, and then exits</li></ul><p><strong>EDIT:</strong> No need for <code>-v</code> when <code>-r</code> is provided. In fact, <code>-v</code> prevents <code>-r</code> from doing anything.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 May '12, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>23 May '12, 13:20</strong> </span></p></div></div><div id="comments-container-11210" class="comments-container"><span id="11219"></span><div id="comment-11219" class="comment"><div id="post-11219-score" class="comment-score"></div><div class="comment-text"><blockquote><p>tested in OSX</p></blockquote><p>...but it should work on all UN*Xes, and should work with other Bourne-compatible shells (Bourne shell, Korn shell, etc.) It should work on Windows with, for example, the Cygwin Bourne shell or other Bourne-compatible shells for Windows, although <code>/path/to/tap.lua</code> would become <code>drive_and:\path\to\tap.lua</code>.</p></div><div id="comment-11219-info" class="comment-info"><span class="comment-age">(22 May '12, 11:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="11223"></span><div id="comment-11223" class="comment"><div id="post-11223-score" class="comment-score"></div><div class="comment-text"><p>for windows:</p><blockquote><p><code>FOR /F "tokens=*" %F IN ('dir /b c:\temp\*.snoop') DO tshark.exe -q -r %F -Xlua_script:c:\temp\tap.lua</code></p></blockquote></div><div id="comment-11223-info" class="comment-info"><span class="comment-age">(22 May '12, 12:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="11246"></span><div id="comment-11246" class="comment"><div id="post-11246-score" class="comment-score"></div><div class="comment-text"><p>Or with Windows PowerShell:</p><p><code>ls C:\temp\*.snoop | % { tshark -q -r "$_.FullName" "-Xlua_script:C:\temp\tap.lua"</code> }</p></div><div id="comment-11246-info" class="comment-info"><span class="comment-age">(23 May '12, 02:00)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-11210" class="comment-tools"></div><div class="clear"></div><div id="comment-11210-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

