+++
type = "question"
title = "Canot run lua script in tshark"
description = '''I am using wireshark/tshark 1.10.6 on ubuntu 12.04. When trying to run  tshark -X lua_script:hello.lua  I don&#x27;t see the &quot;hello.lua&quot; got executed (which should print &quot;hello&quot;). Yes, I have set the /usr/share/wireshark/init.lua to have .... -- Set disable_lua to true to disable Lua support. disable_lua...'''
date = "2015-02-10T11:12:00Z"
lastmod = "2015-02-11T07:18:00Z"
weight = 39777
keywords = [ "lua" ]
aliases = [ "/questions/39777" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Canot run lua script in tshark](/questions/39777/canot-run-lua-script-in-tshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39777-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39777-score" class="post-score" title="current number of votes">0</div><span id="post-39777-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark/tshark 1.10.6 on ubuntu 12.04. When trying to run</p><pre><code>tshark -X lua_script:hello.lua</code></pre><p>I don't see the "hello.lua" got executed (which should print "hello").</p><p>Yes, I have set the /usr/share/wireshark/init.lua to have</p><pre><code>....
-- Set disable_lua to true to disable Lua support.
disable_lua = false

if disable_lua then
    return
end
....</code></pre><p>The strange thing is, when I run tshark with strace, I don't see it attempted to open init.lua at all.</p><p>Any idea why? Thanks!</p><p>EDIT 1 Thanks to Hadriel who pointed out my error in writing. I updated the problem statement</p><p>EDIT 2 I am not running it as root, just want to run a lua script using tshark with an input pcap file.<br />
</p><pre><code>$ tshark -v
TShark 1.10.6 (Git Rev Unknown from unknown)

Copyright 1998-2014 Gerald Combs &lt;[email protected]&gt; and contributors.
This is free software; see the source for copying conditions. There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Compiled (64-bit) with GLib 2.32.4, with libpcap, with libz 1.2.3.4, without
POSIX capabilities, without libnl, without SMI, with c-ares 1.7.5, without Lua,
without Python, without GnuTLS, without Gcrypt, without Kerberos, without GeoIP.

Running on Linux 3.2.0-64-generic, with locale en_US.UTF-8, with libpcap version
1.1.1, with libz 1.2.3.4.
      Intel(R) Core(TM) i7-2670QM CPU @ 2.20GHz

Built using gcc 4.6.3.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '15, 11:12</strong></p><img src="https://secure.gravatar.com/avatar/0228802baecfa9b8d8764a043fea883b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharkfun&#39;s gravatar image" /><p><span>sharkfun</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharkfun has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Feb '15, 20:49</strong> </span></p></div></div><div id="comments-container-39777" class="comments-container"></div><div id="comment-tools-39777" class="comment-tools"></div><div class="clear"></div><div id="comment-39777-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="39790"></span>

<div id="answer-container-39790" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39790-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39790-score" class="post-score" title="current number of votes">1</div><span id="post-39790-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="sharkfun has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>OK, so the problem is the version info says "without Lua", which means support for Lua wasn't compiled into tshark/wireshark when it was built for your platform. Therefore it won't load <code>init.lua</code> or anything Lua-related.</p><p>Did Wireshark come with Ubuntu, or did you get it from an RPM installer (i.e., apt-get/yum/whatever)?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 22:18</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39790" class="comments-container"><span id="39798"></span><div id="comment-39798" class="comment"><div id="post-39798-score" class="comment-score"></div><div class="comment-text"><p>Thanks Hadriel!</p></div><div id="comment-39798-info" class="comment-info"><span class="comment-age">(11 Feb '15, 07:18)</span> <span class="comment-user userinfo">sharkfun</span></div></div></div><div id="comment-tools-39790" class="comment-tools"></div><div class="clear"></div><div id="comment-39790-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="39778"></span>

<div id="answer-container-39778" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-39778-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-39778-score" class="post-score" title="current number of votes">0</div><span id="post-39778-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There should be a space between the "<code>-X</code>" and "<code>lua_script:...</code>", so like this:</p><pre><code>tshark -X lua_script:hello.lua</code></pre><p>Setting "<code>disable_lua = true</code>" in <code>init.lua</code> means you're <strong>disabling</strong> Lua. Why are you doing that?</p><p>Also, verify Lua is actually compiled into Wireshark, by running "<code>tshark -v</code>" at the command line, or in the Wireshark GUI selecting the menu Help -&gt; About Wireshark, and in the third paragraph it should say "with Lua" somewhere.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '15, 11:20</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-39778" class="comments-container"><span id="39779"></span><div id="comment-39779" class="comment"><div id="post-39779-score" class="comment-score"></div><div class="comment-text"><p>Thank you Hadriel. Updated my question.</p></div><div id="comment-39779-info" class="comment-info"><span class="comment-age">(10 Feb '15, 11:27)</span> <span class="comment-user userinfo">sharkfun</span></div></div><span id="39780"></span><div id="comment-39780" class="comment"><div id="post-39780-score" class="comment-score"></div><div class="comment-text"><p>At the top of your init.lua, put this line:</p><pre><code>print(&quot;loading init.lua&quot;)</code></pre><p>Then see if that gets printed out, to see if init.lua is loaded.</p><p>Also, can you paste the output of "<code>tshark -v</code>" here?</p></div><div id="comment-39780-info" class="comment-info"><span class="comment-age">(10 Feb '15, 11:43)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="39781"></span><div id="comment-39781" class="comment"><div id="post-39781-score" class="comment-score"></div><div class="comment-text"><p>Oh, and you're not running tshark with root privileges are you? Wireshark disables Lua by default in such cases. You have to edit the <code>init.lua</code> file's "<code>run_user_scripts_when_superuser = false</code>" line to be "<code>run_user_scripts_when_superuser = true</code>" to use Lua with root privileges.</p></div><div id="comment-39781-info" class="comment-info"><span class="comment-age">(10 Feb '15, 11:47)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="39789"></span><div id="comment-39789" class="comment"><div id="post-39789-score" class="comment-score"></div><div class="comment-text"><p>Updated based on what you requested. I ran it as a normal user. Updated the original question. Thanks Hadriel!</p></div><div id="comment-39789-info" class="comment-info"><span class="comment-age">(10 Feb '15, 20:50)</span> <span class="comment-user userinfo">sharkfun</span></div></div></div><div id="comment-tools-39778" class="comment-tools"></div><div class="clear"></div><div id="comment-39778-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

