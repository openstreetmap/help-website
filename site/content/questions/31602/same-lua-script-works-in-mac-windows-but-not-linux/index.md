+++
type = "question"
title = "Same Lua script works in Mac, Windows, but NOT Linux"
description = '''Hi, I&#x27;ve developed a Lua dissector that runs in the Mac and Windows version of Wireshark (binaries from recent nightly builds). Since there is no binary for Linux in the nightly builds, I built it from source for my ubuntu 12.04. However, the behavior for the following lines of code has changed: loc...'''
date = "2014-04-07T16:39:00Z"
lastmod = "2014-04-10T09:49:00Z"
weight = 31602
keywords = [ "lua", "linux" ]
aliases = [ "/questions/31602" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Same Lua script works in Mac, Windows, but NOT Linux](/questions/31602/same-lua-script-works-in-mac-windows-but-not-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31602-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31602-score" class="post-score" title="current number of votes">0</div><span id="post-31602-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I've developed a Lua dissector that runs in the Mac and Windows version of Wireshark (binaries from recent nightly builds). Since there is no binary for Linux in the nightly builds, I built it from source for my ubuntu 12.04.</p><p>However, the behavior for the following lines of code has changed:</p><pre><code>local packageID_string = string.format(&quot;0x%08x&quot;, packageID)
local funcName = &quot;pkgExtract&quot; .. packageID_string

if _G[funcName] ~= nil then
    _G[funcName](buffer, offset)
else
    tree_payload:add(buffer(offset, pkg_payload_len), &quot;Package ID not defined&quot;)
end</code></pre><p>Basically my payload has many differently structured packages. My script has many package specific functions. My code tell Wireshark to dynamically call the right function to dissect a particular package based on package ID.</p><p>The script works fine in Mac and Windows where it would call the right functions. But for some reason in Linux, instead of dissecting the packages, I get "<code>Package ID not defined</code>". So it regards <code>_G[funcName]</code> to be nil. I printed the <code>funcNames</code> and they are correct and the functions are definitely defined in the script. What's going on?</p><p>Here is my Wireshark flavor:</p><pre><code>Version 1.11.3-2260-gf06cdf3 (Git Rev Unknown from unknown)

Compiled (64-bit) with GTK+ 3.4.2, with Cairo 1.10.2, with Pango 1.30.0, with
GLib 2.32.4, with libpcap, with libz 1.2.3.4, without POSIX capabilities,
without libnl, without SMI, without c-ares, without ADNS, with Lua 5.1, without
Python, without GnuTLS, without Gcrypt, without Kerberos, without GeoIP, without
PortAudio, with AirPcap.
Running on Linux 3.2.0-29-generic, with locale en_US.UTF-8, with libpcap version
1.1.1, with libz 1.2.3.4, without AirPcap.
      Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz
Built using gcc 4.6.3.</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Apr '14, 16:39</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Apr '14, 19:03</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-31602" class="comments-container"><span id="31604"></span><div id="comment-31604" class="comment"><div id="post-31604-score" class="comment-score"></div><div class="comment-text"><p>Can you show the code that sets the global <code>_G[funcName]</code> to be the function(s)?</p></div><div id="comment-31604-info" class="comment-info"><span class="comment-age">(07 Apr '14, 19:07)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31605"></span><div id="comment-31605" class="comment"><div id="post-31605-score" class="comment-score"></div><div class="comment-text"><p>BTW, not that it matters, but is there some reason you're putting them in the global table instead of just a local table in the script? Are they set from other Lua scripts?</p></div><div id="comment-31605-info" class="comment-info"><span class="comment-age">(07 Apr '14, 19:13)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31606"></span><div id="comment-31606" class="comment"><div id="post-31606-score" class="comment-score"></div><div class="comment-text"><p>The functions are generated by python. I have python code writing to the Lua file lines like "function pkgExtract%s(buffer, offset)" %pkgID, which is the start of the function. Is this what you mean?</p></div><div id="comment-31606-info" class="comment-info"><span class="comment-age">(07 Apr '14, 19:32)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31607"></span><div id="comment-31607" class="comment"><div id="post-31607-score" class="comment-score"></div><div class="comment-text"><p>As far as global vs. local tables, I guess my Lua experience is so limited, I have not given it any thought. When you say local tables, do you mean declare all the functions as "local"?</p></div><div id="comment-31607-info" class="comment-info"><span class="comment-age">(07 Apr '14, 19:36)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-31602" class="comment-tools"></div><div class="clear"></div><div id="comment-31602-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31610"></span>

<div id="answer-container-31610" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31610-score" class="post-score" title="current number of votes">1</div><span id="post-31610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It should behave the same in Linux, Mac, and Windows - there's been a recent change. What version were you running on Windows/Mac?</p><hr /><pre><code>&quot;When you say local tables, do you mean declare all the functions as &quot;local&quot;?&quot;</code></pre><p>When your script has this: "<code>_G[funcName]</code>", it's trying to access an entry in the Lua <em>global</em> table - an entry named whatever the variable <code>funcName</code> resolves to. ("<code>_G</code>" is the name of the global table)</p><hr /><pre><code>&quot;The functions are generated by python. I have python code writing to the Lua file lines like &quot;function pkgExtract%s(buffer, offset)&quot; %pkgID, which is the start of the function. Is this what you mean?&quot;</code></pre><p>You mean the Python code is writing something like this:</p><pre><code>function pkgExtract0x0a01fe32(buffer, offset)
    -- do stuff
end</code></pre><p>And it writes the above into the same Lua script file that has the code you posted in the question?</p><p>If so, then there's at least one problem: that doesn't actually create a <em>global</em> function named "<code>pkgExtract0x0a01fe32</code>" - i.e., it's not in the "<code>_G</code>" global table. Wireshark <em>used</em> to do that, but the code got changed recently to stop doing that. Instead, it creates a function of that name in the local file environment, meaning it's no longer global, and no longer put into the "<code>_G</code>" table. That was done to prevent Lua scripts from accidentally polluting the global table and affecting other scripts. (because people kept forgetting to use the word "<code>local</code>" before their variables and function definitions)</p><p>So change your Python code and the Lua code in your question to do this:</p><pre><code>-- this is in your Lua file before the Python-generated code,
-- or Python generates one of these too (but only once)
local myfuncs = {}

-- Python generates this
function myfuncs.pkgExtract0x0a01fe32(buffer, offset)
    -- do stuff
end

-- presumably this is in your dissector function
local packageID_string = string.format(&quot;0x%08x&quot;, packageID)
local funcName = &quot;pkgExtract&quot; .. packageID_string

if myfuncs[funcName] ~= nil then
    myfuncs[funcName](buffer, offset)
else
    tree_payload:add(buffer(offset, pkg_payload_len), &quot;Package ID not defined&quot;)
end</code></pre><p>BTW, there's no need to do the <code>string.format()</code> and concatenation thing... Lua's table keys can be numbers. So you could do this instead:</p><pre><code>-- this is in your Lua file before the Python-generated code,
-- or Python generates one of these too (but only once)
local myfuncs = {}

-- Python generates this - note the &#39;0x0a01fe32&#39; is not
-- in quotes, so it&#39;s a number key
myfuncs[0x0a01fe32] = function(buffer, offset)
    -- do stuff
end

-- presumably this is in your dissector function
-- the &#39;packageID&#39; is a variable of a number, not a string
if myfuncs[packageID] ~= nil then
    myfuncs[packageID](buffer, offset)
else
    tree_payload:add(buffer(offset, pkg_payload_len), &quot;Package ID not defined&quot;)
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Apr '14, 20:37</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Apr '14, 20:38</strong> </span></p></div></div><div id="comments-container-31610" class="comments-container"><span id="31640"></span><div id="comment-31640" class="comment"><div id="post-31640-score" class="comment-score"></div><div class="comment-text"><p>You are right. Wireshark on my Mac and Windows are from the nightly builds about a month ago. When I downloaded the newest Mac version from last night, it behaves just like the Linux version. Thanks for helping me figure out how to cope with this.</p><p>Now this is one drawback of using nightly builds instead of a stable release. If I simply told other people to use the nightly build, my code would have been broken. Are you guys going to release what's in the nightly builds (1.11.3) soon?</p></div><div id="comment-31640-info" class="comment-info"><span class="comment-age">(08 Apr '14, 09:43)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31642"></span><div id="comment-31642" class="comment"><div id="post-31642-score" class="comment-score"></div><div class="comment-text"><p>I've heard a rumor that the next stable release (1.12) is coming out in June - that will be whatever the 1.11.3 code is at that point in time; and then lucky release number 1.13 becomes the next development (unstable) release and 1.11.3 ends.</p></div><div id="comment-31642-info" class="comment-info"><span class="comment-age">(08 Apr '14, 10:43)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31647"></span><div id="comment-31647" class="comment"><div id="post-31647-score" class="comment-score"></div><div class="comment-text"><p>Apparently 1.11.3 is getting released on April 15th, and a 1.11.4 will be created for continued development; so whenever 1.12 gets released it will be based on 1.11.4 not 1.11.3 I think.</p></div><div id="comment-31647-info" class="comment-info"><span class="comment-age">(08 Apr '14, 18:05)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31713"></span><div id="comment-31713" class="comment"><div id="post-31713-score" class="comment-score"></div><div class="comment-text"><p>Would both GTK+ and QT versions be released together? I thought I read somewhere that GTK+ version is more stable.</p></div><div id="comment-31713-info" class="comment-info"><span class="comment-age">(10 Apr '14, 09:11)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31715"></span><div id="comment-31715" class="comment"><div id="post-31715-score" class="comment-score"></div><div class="comment-text"><p>You mean for 1.12, or 1.11.3?</p><p>For 1.11.3: linux and windows get both GTK and Qt, but Mac only gets Qt... or at least that's all it's gotten in the automated nightly builds, so I assume that's all it will get in the released version of 1.11.3. Note that you can compile the Mac version on your own for both GTK and Qt.</p><p>It remains to be seen what happens with 1.12. The problem isn't that Qt is less stable... the problem is it's still missing a bunch of features that the GTK version has. For the features it has, Qt is superior in my opinion, but not having all the features is tough. Many of the missing features are really esoteric stuff that I bet only a very small, niche population uses... but some missing features aren't so esoteric.</p></div><div id="comment-31715-info" class="comment-info"><span class="comment-age">(10 Apr '14, 09:49)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-31610" class="comment-tools"></div><div class="clear"></div><div id="comment-31610-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

