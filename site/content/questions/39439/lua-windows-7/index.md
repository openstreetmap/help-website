+++
type = "question"
title = "Lua: windows 7"
description = '''Hello, I have Wireshark version: 1.12.3 on windows 7. I have a pcap file and a lua file. Are there any links which explains the steps to load lua file ? On Windows I see &quot;Lua&quot; pull down but no where to load lua file itself. I tried updating init.lua: dofile(&quot;test.lua&quot;) but do not see that being invo...'''
date = "2015-01-27T12:33:00Z"
lastmod = "2015-01-27T12:43:00Z"
weight = 39439
keywords = [ "lua" ]
aliases = [ "/questions/39439" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Lua: windows 7](/questions/39439/lua-windows-7)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39439-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have Wireshark version: 1.12.3 on windows 7.</p><p>I have a pcap file and a lua file. Are there any links which explains the steps to load lua file ?</p><p>On Windows I see "Lua" pull down but no where to load lua file itself. I tried updating init.lua: dofile("test.lua") but do not see that being invoked.</p><p>Any suggestions ?</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jan '15, 12:33</strong></p><img src="https://secure.gravatar.com/avatar/b93121bbedf3182f691f395b8b6c9c7e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="foomail123&#39;s gravatar image" /><p>foomail123<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="foomail123 has no accepted answers">0%</span></p></div></div><div id="comments-container-39439" class="comments-container"></div><div id="comment-tools-39439" class="comment-tools"></div><div class="clear"></div><div id="comment-39439-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="39440"></span>

<div id="answer-container-39440" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-39440-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>See <a href="http://wiki.wireshark.org/Lua#How_Lua_fits_into_Wireshark">this wiki link</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jan '15, 12:43</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39440" class="comments-container"><span id="39443"></span><div id="comment-39443" class="comment"><div id="post-39443-score" class="comment-score"></div><div class="comment-text"><p>Thank you for pointer. I had seen that link. Per instructions, I followed I did add (in file init.lua) as above: dofile("test.lua")</p><p>I do not see the string printed on console. How do I know if lua script is loaded by wireshark or not to begin with ?</p><p>The other question the link above mentions 'tshark' command line executable/script. It does not exist on Windows as I see.</p><p>Any suggestions ?</p><p>I</p></div><div id="comment-39443-info" class="comment-info"><span class="comment-age">(27 Jan '15, 14:23)</span> foomail123</div></div><span id="39457"></span><div id="comment-39457" class="comment"><div id="post-39457-score" class="comment-score"></div><div class="comment-text"><p>The link above doesn't say to add it to the <code>init.lua</code> file using <code>dofile()</code>, but now that I look at it it also doesn't say what you <em>should</em> do, which is actually to just put your Lua file in the Personal Plugins directory. That directory is the one labeled "Personal Plugins" when you run Wireshark and go to the Help menu, select "About Wireshark", and click on the "Folders" tab.</p><p>But anyway, <code>dofile()</code> should also work, and if it's not working then it's one of a few possibilities:</p><ol><li>The <code>init.lua</code> file you put it in isn't being executed. One reason this might be is if the Wireshark you're running doesn't have Lua compiled in. To find out, in Wireshark choose "About Wireshark" in the Help menu, and on the first tab it will say if Lua is in or out in the third paragraph (along with all the other compiled information).</li><li>You're running in superuser mode mode.</li><li>The <code>init.lua</code> file you put that <code>dofile()</code> in is the wrong <code>init.lua</code> file.</li></ol><p>One way to help diagnose this is if you put something like the following before the <code>dofile("my file")</code> line in the <code>init.lua</code>:</p><pre><code>new_dialog(&quot;before dofile&quot;, function() return; end, &quot;before dofile called&quot;)</code></pre><p>That will make a dialog window pop up, with that "before dofile" title and a text field. If you don't see that dialog window, then it's not even getting to the <code>dofile()</code> call. Note that the dialog window might be hidden behind the Wireshark GUI window (because the dialog will pop up first but then wire shark's main guy window will pop up right afterwards in front of it), so move the main Wireshark window out of the way to see if the dialog window is there.</p></div><div id="comment-39457-info" class="comment-info"><span class="comment-age">(28 Jan '15, 09:36)</span> Hadriel</div></div><span id="39458"></span><div id="comment-39458" class="comment"><div id="post-39458-score" class="comment-score"></div><div class="comment-text"><blockquote><p>The other question the link above mentions 'tshark' command line executable/script. It does not exist on Windows as I see.</p></blockquote><p>I don't use Windows, but <code>tshark</code> is a command line program - so you need to be at a command prompt, such as by going to Start-&gt;Run-&gt;"cmd" or whatever. Or check <a href="https://ask.wireshark.org/questions/10087/how-do-i-run-tshark-on-windows">this link</a>.</p></div><div id="comment-39458-info" class="comment-info"><span class="comment-age">(28 Jan '15, 09:39)</span> Hadriel</div></div><span id="39459"></span><div id="comment-39459" class="comment"><div id="post-39459-score" class="comment-score"></div><div class="comment-text"><p>tshark is part of the optional components in Windows installer. If you cannot find it in your Wireshark folder, it means that it was unchecked during installation (it is checked by default).</p></div><div id="comment-39459-info" class="comment-info"><span class="comment-age">(28 Jan '15, 09:40)</span> Pascal Quantin</div></div><span id="39460"></span><div id="comment-39460" class="comment"><div id="post-39460-score" class="comment-score"></div><div class="comment-text"><p>Also note that the Wireshark directory isn't automatically added to your path on install, so when using tshark you must either:</p><ul><li>always "cd" to the Wireshark directory before running tshark.</li><li>always provide the path, e.g. <code>C:\Program Files\Wireshark\tshark ...</code>.</li><li>add the Wireshark directory to your path, e.g. see <a href="http://windowsitpro.com/systems-management/how-can-i-add-new-folder-my-system-path">here</a>.</li><li>If using Powershell create an alias in your profile, e.g. <code>New-Alias tshark path\to\toshark</code></li></ul></div><div id="comment-39460-info" class="comment-info"><span class="comment-age">(28 Jan '15, 10:28)</span> grahamb ♦</div></div></div><div id="comment-tools-39440" class="comment-tools"></div><div class="clear"></div><div id="comment-39440-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

