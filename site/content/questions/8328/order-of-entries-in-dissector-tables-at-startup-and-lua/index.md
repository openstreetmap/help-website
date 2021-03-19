+++
type = "question"
title = "Order of entries in dissector tables at startup and lua"
description = '''Hello, I&#x27;m trying to modify RTP dissector table with Lua. When I create a Lua script like below and run it either from plugins directory or the command line  it doesn&#x27;t work, and I can see via Internals -&amp;gt; Dissector Tables that my entry was overwritten by AMR protocol. local ip_dissector = Dissec...'''
date = "2012-01-11T09:07:00Z"
lastmod = "2012-01-14T10:42:00Z"
weight = 8328
keywords = [ "development", "lua", "dissector", "startup", "rtp" ]
aliases = [ "/questions/8328" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Order of entries in dissector tables at startup and lua](/questions/8328/order-of-entries-in-dissector-tables-at-startup-and-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8328-score" class="post-score" title="current number of votes">0</div><span id="post-8328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I'm trying to modify RTP dissector table with Lua. When I create a Lua script like below and run it either from plugins directory or the command line it doesn't work, and I can see via <code>Internals -&gt; Dissector Tables</code> that my entry was overwritten by AMR protocol.</p><pre><code>local ip_dissector = Dissector.get(&quot;ip&quot;)
local rtp_table = DissectorTable.get(&quot;rtp.pt&quot;)
rtp_table:add(96, ip_dissector)</code></pre><p>However, when I enter the same code via the evaluate window and reload the pcap file, it works as expected. This leads me to think that startup Lua code is executed before the other protocol adds itself to the same table, effectively being overwritten.</p><p>Am I right and, if yes, is there a way in which I can control that order? By maybe somehow putting that Lua code in a function and running it when all dissectors and protocols have been fully loaded?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-startup" rel="tag" title="see questions tagged &#39;startup&#39;">startup</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '12, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jan '12, 10:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-8328" class="comments-container"></div><div id="comment-tools-8328" class="comment-tools"></div><div class="clear"></div><div id="comment-8328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="8387"></span>

<div id="answer-container-8387" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8387-score" class="post-score" title="current number of votes">2</div><span id="post-8387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="izopizo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><h2 id="amr-preferences">AMR preferences</h2><p>As <em>@Anders</em> pointed out, the problem is due to your preference for <em>"AMR dynamic payload type"</em> conflicting with your dissector registration. Set that preference to <code>0</code> to prevent AMR from being put into the dissector table for <code>rtp.pt</code>.</p><p><a href="http://postimage.org/image/p7ocku28n/"><img src="http://s15.postimage.org/p7ocku28n/Screen_Shot_2012_01_12_at_6_22_17_PM.jpg" alt="Screenshot" /></a></p><br />
<h2 id="initialization-order">Initialization order</h2><p>Actually, the dissectors are <strong>not</strong> loaded randomly. Wireshark loads the C dissectors and then the Lua scripts, each of which is always loaded in the same order. Note that preferences are read last during initialization, which is the reason the AMR preference took effect over your Lua dissector.</p><p>The <a href="http://anonsvn.wireshark.org/viewvc/trunk/epan/dissectors/Makefile.common?revision=40439&amp;view=markup#l1463"><code>Makefile</code></a> generates dissector-registration code (<a href="http://pastebin.com/pYLPMzZm"><code>register.c</code></a>) based on dissector source. The C dissectors are thus registered in the order seen in this generated code, which is ascending ASCII order.</p><p>Then, Lua scripts (which can contain dissectors) are also loaded in ascending ASCII order as follows:</p><ol><li><code>${GLOBAL_CONFIG_DIR}/init.lua</code></li><li><code>${GLOBAL_PLUGINS_DIR}/**/*.lua</code></li><li><code>${PERSONAL_CONFIG_DIR}/init.lua</code></li><li><code>${PERSONAL_PLUGINS_DIR}/**/*.lua</code></li></ol><p>The path variables above can be determined in Wireshark (<code>Help &gt; About &gt; Folders</code>). Example values:</p><table data-cellpadding="5" data-cellspacing="5" data-frame="box" data-rules="rows"><tbody><tr class="header"><th>Variable name</th><th>Mac OSX value</th><th>Windows value</th></tr><tr class="odd"><td><code>GLOBAL_CONFIG_DIR</code></td><td><code>/usr/share/wireshark</code></td><td><code>%WIRESHARK%</code></td></tr><tr class="even"><td><code>GLOBAL_PLUGINS_DIR</code></td><td><code>/usr/lib/wireshark/plugins/1.7.1</code></td><td><code>%WIRESHARK%\plugins\1.7.1</code></td></tr><tr class="odd"><td><code>PERSONAL_CONFIG_DIR</code></td><td><code>$HOME/.wireshark</code></td><td><code>%APPDATA%\Wireshark</code></td></tr><tr class="even"><td><code>PERSONAL_PLUGINS_DIR</code></td><td><code>$HOME/.wireshark/plugins</code></td><td><code>%APPDATA%\Wireshark\plugins</code></td></tr></tbody></table><p><br />
</p><h2 id="control-of-initialization-order">Control of initialization order</h2>You can't change the initialization order of the C dissectors unless you modify the code. However, you <em>do</em> have control of Lua script loading, but it requires you to make changes to prevent the scripts from being auto-loaded:<ol><li>Move all Lua scripts outside of <code>${PERSONAL_PLUGINS_DIR}</code> <strong>OR</strong> rename them to a different extension (such as <code>".lua_"</code>).</li><li>Modify <code>${PERSONAL_CONFIG_DIR}/init.lua</code> to explicitly load the Lua scripts in a specific order.</li></ol><p><strong>Example:</strong> Let's say I had this directory structure:</p><pre><code>~/.wireshark/plugins/
    |-- a.lua
    |-- b.lua
    -- x/
        |-- c.lua
        |-- d.lua
        |-- e.lua
        -- f.lua</code></pre><p>...which has a load order of <code>a</code> through <code>f</code>. I want to change the order to <em>"everything in the <code>x</code> directory alphabetically, then <code>b</code>, and <code>a</code>"</em>. So, I move the Lua scripts outside of <code>~/.wireshark/plugins</code> to say, <code>~/.wireshark/lua/</code>; and I add <code>~/.wireshark/init.lua</code>, which contains:</p><pre><code>-- USER_DIR is initialized in ${GLOBAL_CONFIG_DIR}/init.lua
local basedir = ( USER_DIR or persconffile_path() )..&#39;lua/&#39;

-- load all Lua scripts in &quot;~/.wireshark/lua/x&quot; (ascending ASCII order)
local xdir = basedir..&#39;x/&#39;
for f in Dir.open(xdir, &quot;.lua&quot;) do
    dofile(xdir..f)
end

dofile(basedir..&#39;b.lua&#39;)
dofile(basedir..&#39;a.lua&#39;)</code></pre><p>Assume the contents of each Lua script contains:</p><pre><code>print( (require &#39;debug&#39;).getinfo(1).source )</code></pre><p>which prints the absolute path to the running script. Now, if I start Wireshark or TShark, I should see the load order from the command line, like so:</p><pre><code>$ tshark -v
@/Users/tony/.wireshark/lua/x/c.lua
@/Users/tony/.wireshark/lua/x/d.lua
@/Users/tony/.wireshark/lua/x/e.lua
@/Users/tony/.wireshark/lua/x/f.lua
@/Users/tony/.wireshark/lua/x/z.lua
@/Users/tony/.wireshark/lua/b.lua
@/Users/tony/.wireshark/lua/a.lua
TShark 1.7.1 (SVN Rev Unknown from unknown)

Copyright 1998-2012 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GLib 2.28.8, with libpcap (version unknown), with libz
1.2.5, without POSIX capabilities, with SMI 0.4.8, with c-ares 1.7.4, with Lua
5.1, with Python 2.7.1, with GnuTLS 2.8.6, with Gcrypt 1.5.0, with MIT Kerberos,
with GeoIP.

Running on Mac OS 10.7.2 (Darwin 11.2.0), with locale en_US.UTF-8, with libpcap
version 1.1.1, with libz 1.2.5.

Built using llvm-gcc 4.2.1 (Based on Apple Inc. build 5658) (LLVM build
2336.1.00).</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Jan '12, 10:42</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Jan '12, 10:42</strong> </span></p></div></div><div id="comments-container-8387" class="comments-container"></div><div id="comment-tools-8387" class="comment-tools"></div><div class="clear"></div><div id="comment-8387-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="8329"></span>

<div id="answer-container-8329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-8329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-8329-score" class="post-score" title="current number of votes">0</div><span id="post-8329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Dissectors are loaded in a random order, and there is nothing you can do to control the specific order in which they are loaded. What you could do in stead is to disable the AMR protocol in <code>Analyze -&gt; Enabled Protocols</code> (you may then need to restart Wireshark). This will prevent the AMR dissector from registering, which will prevent packets from being dissected as AMR packets (allowing you to use <code>rtp.pt 96</code> for your own protocol). This shouldn't be a problem for you unless your dissector must perform a handoff to the AMR dissector.</p><p>The reason it works in the evaluate window is because all of the protocols are already registered at that point, so your dissector will be the last on to overwrite that table entry.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '12, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-8329" class="comments-container"><span id="8332"></span><div id="comment-8332" class="comment"><div id="post-8332-score" class="comment-score"></div><div class="comment-text"><p>You can set the PT preference for AMR to 0</p></div><div id="comment-8332-info" class="comment-info"><span class="comment-age">(11 Jan '12, 22:47)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-8329" class="comment-tools"></div><div class="clear"></div><div id="comment-8329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

