+++
type = "question"
title = "missing base.HEX definition in Lua"
description = '''I&#x27;m trying to write a dissector in Lua, and I ran this code: local asc = Proto(&quot;asc&quot;, &quot;ASC Protocol&quot;)  local f = asc.fields  f.version = ProtoField.uint8(&quot;asc.version&quot;, &quot;version&quot;, base.HEX, nil, 0xC)  but I receive the following error: attempt to index global &#x27;base&#x27; (a nil value)  How do I fix this?'''
date = "2012-05-04T05:03:00Z"
lastmod = "2012-10-11T05:18:00Z"
weight = 10681
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/10681" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [missing base.HEX definition in Lua](/questions/10681/missing-basehex-definition-in-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10681-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to write a dissector in Lua, and I ran this code:</p><pre><code>local asc = Proto(&quot;asc&quot;, &quot;ASC Protocol&quot;) 
local f = asc.fields 
f.version = ProtoField.uint8(&quot;asc.version&quot;, &quot;version&quot;, base.HEX, nil, 0xC)</code></pre><p>but I receive the following error:</p><pre><code>attempt to index global &#39;base&#39; (a nil value)</code></pre><p>How do I fix this?</p></div><div id="question-tags" class="tags-container tags">lua dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 May '12, 05:03</strong></p><img src="https://secure.gravatar.com/avatar/a637cbdbbb00c38a1643b374a0833e9f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Olga&#39;s gravatar image" /><p>Olga<br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Olga has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 23 May '12, 07:01</p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-10681" class="comments-container"></div><div id="comment-tools-10681" class="comment-tools"></div><div class="clear"></div><div id="comment-10681-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14923"></span>

<div id="answer-container-14923" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14923-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>For others stumbling on this: in Fedora (and possibly other distributions) you need to install the wireshark-devel package.</p><p>yum install wireshark-devel</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Oct '12, 05:18</strong></p><img src="https://secure.gravatar.com/avatar/adba0c88151c266923dc729dd3af6207?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jannes&#39;s gravatar image" /><p>Jannes<br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jannes has no accepted answers">0%</span></p></div></div><div id="comments-container-14923" class="comments-container"></div><div id="comment-tools-14923" class="comment-tools"></div><div class="clear"></div><div id="comment-14923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10904"></span>

<div id="answer-container-10904" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-10904-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The <code>base</code> table (which includes <code>base.HEX</code>, <code>base.DEC</code>, etc.) is defined in <code>init.lua</code>, which Wireshark/Tshark automatically loads at startup. That error you're seeing is an indication that either:</p><p>1) <code>init.lua</code> was not loaded (e.g., because it could not be found)</p><p>OR</p><p>2) <code>base</code> was accidentally overwritten somewhere in your script (e.g., <code>base = nil</code>) before <code>base.HEX</code></p><p>These are the default installation locations for <code>init.lua</code>:</p><ul><li><strong>OS X <a href="http://wireshark.org">wireshark.org</a> packages</strong>: <code>/Applications/Wireshark.app/Contents/Resources/share/wireshark/init.lua</code></li><li><strong>Ubuntu</strong>: <code>/etc/wireshark/init.lua</code></li><li><strong>Windows <a href="http://wireshark.org">wireshark.org</a> installer</strong>: <code>C:\Program Files\Wireshark\init.lua</code></li><li><strong>Builds from source on UN*X</strong>: <code>/usr/local/share/wireshark/init.lua</code></li></ul><p>Problem 1 above is typically seen in development builds of Wireshark. That is, you're building Wireshark in a sandbox, you've set the install prefix to a local build directory, yet when you start Wireshark (even with <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcRunFirstTime.html"><code>WIRESHARK_RUN_FROM_BUILD_DIRECTORY</code></a> environment variable set to <code>1</code>), it still cannot find <code>init.lua</code>. The workaround is to copy <code>init.lua</code> (and <code>console.lua</code>, which is a helpful tool loaded by <code>init.lua</code>) to your home directory, which is in the <a href="http://ask.wireshark.org/questions/8328/order-of-entries-in-dissector-tables-at-startup-and-lua#answer-container-8387">Lua initialization path</a>, and restart Wireshark/Tshark.</p><p><strong>UPDATE:</strong></p><p>In <a href="http://pastebin.com/uK2AnTTP">your init.lua</a>, you've loaded your script at line 34 before any of the Wireshark variables are declared (the <code>base</code> table is defined at line 247). Any file loading should be done at the end of init.lua (when initialization is complete). However, I don't recommend modifying <code>C:\Program Files\Wireshark\init.lua</code> because any errors introduced there break initialization for all other scripts. Instead, you should:</p><ul><li>Create/edit <code>C:\Users\*username*\AppData\Roaming\Wireshark\init.lua</code></li></ul><p>OR</p><ul><li>Delete your original <code>init.lua</code> changes, and move your Lua script into <code>C:\Program Files\Wireshark\plugins\1.8.0\</code> (where <code>1.8.0</code> is the current version of Wireshark), where it would be loaded automatically without any other file modification.</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 May '12, 14:13</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p>helloworld<br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jun '12, 12:47</p></div></div><div id="comments-container-10904" class="comments-container"><span id="11250"></span><div id="comment-11250" class="comment"><div id="post-11250-score" class="comment-score"></div><div class="comment-text"><p>thank you for your reply, but i defined base as base={} and this works</p></div><div id="comment-11250-info" class="comment-info"><span class="comment-age">(23 May '12, 05:26)</span> Olga</div></div><span id="11257"></span><div id="comment-11257" class="comment"><div id="post-11257-score" class="comment-score"></div><div class="comment-text"><p>I assume you define "works" as in "the interpreter no longer complains about your previous problem". If, on the other hand, you define "works" here as: "the bitfield is displayed in hexadecimal format", then your change does <strong>not</strong> "work" as intended.</p><p>If you set <code>base = {}</code>, then <code>base.HEX</code> is <strong><code>nil</code></strong>, which means you effectively have:</p><pre><code>f.version = ProtoField.uint8(&quot;asc.version&quot;, &quot;version&quot;, nil, nil, 0xC)</code></pre></div><div id="comment-11257-info" class="comment-info"><span class="comment-age">(23 May '12, 07:11)</span> helloworld</div></div><span id="11258"></span><div id="comment-11258" class="comment"><div id="post-11258-score" class="comment-score"></div><div class="comment-text"><p>Specifying <code>nil</code> there tells <code>ProtoField</code> to use the default, which is <code>base.DEC</code>. So, your protocol tree would show:</p><pre><code>.... 01.. = version: 1</code></pre><p>instead of:</p><pre><code>.... 01.. = version: 0x01</code></pre></div><div id="comment-11258-info" class="comment-info"><span class="comment-age">(23 May '12, 07:11)</span> helloworld</div></div><span id="11328"></span><div id="comment-11328" class="comment"><div id="post-11328-score" class="comment-score"></div><div class="comment-text"><blockquote><p>init.lua was not loaded (e.g., because it could not be found)</p></blockquote><p>In init.lua, I defined the path to my dissector:</p><pre><code>disable_lua = false

MYPROTO_SCRIPT_PATH=&quot;C:\\Program Files\\Wireshark\\&quot;
dofile(MYPROTO_SCRIPT_PATH..&quot;asc_sccp.lua&quot;)</code></pre><p>...and Wireshark loads my dissector, so I suppose that Wireshark sees <code>init.lua</code>. <code>init.lua</code> and <code>console.lua</code> exist in <code>C:\Program Files\Wireshark\</code>.</p></div><div id="comment-11328-info" class="comment-info"><span class="comment-age">(25 May '12, 04:06)</span> Olga</div></div><span id="11338"></span><div id="comment-11338" class="comment"><div id="post-11338-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark are you running?</p><p>The <code>base</code> table is only defined in <code>init.lua</code> in any standard Wireshark installation. If you're indeed loading <code>init.lua</code>, then something in your script (or loaded by your script) is likely overwriting <code>base</code>. You can quickly test this by adding a couple debug-prints before and after loading your script:</p><pre><code>debug(&#39;BEFORE: &#39;..base.HEX)
dofile(MYPROTO_SCRIPT_PATH..&quot;asc_sccp.lua&quot;)
debug(&#39;AFTER: &#39;..base.HEX)</code></pre></div><div id="comment-11338-info" class="comment-info"><span class="comment-age">(25 May '12, 10:12)</span> helloworld</div></div><span id="11428"></span><div id="comment-11428" class="comment not_top_scorer"><div id="post-11428-score" class="comment-score"></div><div class="comment-text"><p>Wireshark version: Version 1.6.7 OS Windows</p><p>i did debug print, restart wireshark and i recieved following error Lua: Error during loading: [string "C:\Program Files\Wireshark\init.lua"]:33: attempt to index global 'base' (a nil value)</p></div><div id="comment-11428-info" class="comment-info"><span class="comment-age">(28 May '12, 08:12)</span> Olga</div></div><span id="11700"></span><div id="comment-11700" class="comment not_top_scorer"><div id="post-11700-score" class="comment-score"></div><div class="comment-text"><p>Ok. This would be easier to troubleshoot if we could see the entire contents of your <code>init.lua</code>. Please copy and paste it into <a href="http://pastebin.com">http://pastebin.com</a> and link it here.</p></div><div id="comment-11700-info" class="comment-info"><span class="comment-age">(05 Jun '12, 18:44)</span> helloworld</div></div><span id="12307"></span><div id="comment-12307" class="comment not_top_scorer"><div id="post-12307-score" class="comment-score"></div><div class="comment-text"><p><a href="http://pastebin.com/uK2AnTTP">http://pastebin.com/uK2AnTTP</a></p></div><div id="comment-12307-info" class="comment-info"><span class="comment-age">(29 Jun '12, 05:51)</span> Olga</div></div><span id="12333"></span><div id="comment-12333" class="comment not_top_scorer"><div id="post-12333-score" class="comment-score"></div><div class="comment-text"><p>You're loading your file way too early in <code>init.lua</code>. See updated answer.</p></div><div id="comment-12333-info" class="comment-info"><span class="comment-age">(29 Jun '12, 12:48)</span> helloworld</div></div></div><div id="comment-tools-10904" class="comment-tools"><span class="comments-showing"> showing 5 of 9 </span> <a href="#" class="show-all-comments-link">show 4 more comments</a></div><div class="clear"></div><div id="comment-10904-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

