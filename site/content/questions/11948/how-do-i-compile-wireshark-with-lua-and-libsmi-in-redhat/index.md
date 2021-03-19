+++
type = "question"
title = "How do I compile Wireshark with Lua and libsmi in Redhat?"
description = '''I tried to compile Wireshark 1.6.8 with Lua and libsmi in RHEL with the below commands, but I&#x27;m seeing errors: $ ./configure --prefix=&quot;/home/OPENSOURCE/WIRESHARK/1.6.8/Linux/RHEL4_2.6&quot; &#92;  --with-lua=&quot;/home/OPENSOURCE/LUA/5.1/Linux/RHEL4_2.6&quot; &#92;  --with-libsmi=&quot;/home/OPENSOURCE/LIBSMI/0.4.8/Linux/RHEL...'''
date = "2012-06-15T08:26:00Z"
lastmod = "2012-06-21T04:17:00Z"
weight = 11948
keywords = [ "development", "build", "redhat", "error" ]
aliases = [ "/questions/11948" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I compile Wireshark with Lua and libsmi in Redhat?](/questions/11948/how-do-i-compile-wireshark-with-lua-and-libsmi-in-redhat)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11948-score" class="post-score" title="current number of votes">0</div><span id="post-11948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried to compile Wireshark 1.6.8 with Lua and libsmi in RHEL with the below commands, but I'm seeing errors:</p><pre><code>$ ./configure --prefix=&quot;/home/OPENSOURCE/WIRESHARK/1.6.8/Linux/RHEL4_2.6&quot; \
        --with-lua=&quot;/home/OPENSOURCE/LUA/5.1/Linux/RHEL4_2.6&quot; \
        --with-libsmi=&quot;/home/OPENSOURCE/LIBSMI/0.4.8/Linux/RHEL4_2.6&quot;

$ make --&gt; After running &quot;make&quot; command, it&#39;s hung up with below error
 &quot;/home/OPENSOURCE/LUA/5.1/Linux/RHEL4_2.6/lib/liblua.a: could not read symbols: Bad value&quot;</code></pre><p>I also recompiled Lua and tried again, but no luck...same error.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-build" rel="tag" title="see questions tagged &#39;build&#39;">build</span> <span class="post-tag tag-link-redhat" rel="tag" title="see questions tagged &#39;redhat&#39;">redhat</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '12, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/44faace1ef2ed45ab38566e289e2bf63?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mevalal&#39;s gravatar image" /><p><span>Mevalal</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mevalal has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jun '12, 13:56</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-11948" class="comments-container"></div><div id="comment-tools-11948" class="comment-tools"></div><div class="clear"></div><div id="comment-11948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="11962"></span>

<div id="answer-container-11962" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11962-score" class="post-score" title="current number of votes">0</div><span id="post-11962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><ul><li>is there a file called '/home/OPENSOURCE/LUA/5.1/Linux/RHEL4_2.6/lib/liblua.a'?</li><li>What is its size?</li><li>what is the output of this command: <strong><code>nm /home/OPENSOURCE/LUA/5.1/Linux/RHEL4_2.6/lib/liblua.a</code></strong></li><li>can you please add a few lines of make output before that last error message.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '12, 09:18</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jun '12, 09:32</strong> </span></p></div></div><div id="comments-container-11962" class="comments-container"><span id="12068"></span><div id="comment-12068" class="comment"><div id="post-12068-score" class="comment-score"></div><div class="comment-text"><p>Hello, Thanks for your help.</p><p>Yes it's called '/home/OPENSOURCE/LUA/5.1/Linux/RHEL4_2.6/lib/liblua.a' and size of it is "326764" bytes Also output of</p><p><code># nm /home/OPENSOURCE/LUA/5.1/Linux/RHEL4_2.6/lib/liblua.a |more lapi.o: 00000000000017a0 t aux_upvalue 00000000000012f0 t f_call 00000000000013b0 t f_Ccall 00000000000000d0 t getcurrenv 0000000000000000 t index2adr 00000000000000f0 T luaA_pushobject 00000000000001f0 T lua_atpanic 0000000000001280 T lua_call</code></p><p>Regadrs Mevalal</p></div><div id="comment-12068-info" class="comment-info"><span class="comment-age">(20 Jun '12, 02:42)</span> <span class="comment-user userinfo">Mevalal</span></div></div></div><div id="comment-tools-11962" class="comment-tools"></div><div class="clear"></div><div id="comment-11962-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11983"></span>

<div id="answer-container-11983" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11983-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11983-score" class="post-score" title="current number of votes">0</div><span id="post-11983-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This is probably the issue you're seeing:</p><pre><code>libtool: link:  gcc -shared  -fPIC -DPIC  .libs/libwireshark_la-addr_and_mask.o .libs/libwireshark_la-addr_resolv.o 
[...]
-pthread -Wl,-soname -Wl,libwireshark.so.0 -Wl,-version-script -Wl,.libs/libwireshark.ver -o .libs/libwireshark.so.0.0.0
/usr/bin/ld: /home/tony/src/lua-5.1.5/src/build/lib/liblua.a(lapi.o): relocation R_X86_64_32 against `luaO_nilobject_&#39; can not be used when making a shared object; recompile with -fPIC
/home/tony/src/lua-5.1.5/src/build/lib/liblua.a: could not read symbols: Bad value
[...]
make: *** [install] Error 2</code></pre><p>The error message was actually quite helpful. It was telling you to recompile <code>liblua.a</code> with the <code>-fPIC</code> compiler flag. Try this:</p><ol><li>Open <code>${lua-5.1}/src/Makefile</code></li><li>Edit <code>CFLAGS</code> (it should be on/near line 11) so that it includes <code>-fPIC</code>. (e.g., <code>CFLAGS=-fPIC -O2 -Wall $(MYCFLAGS)</code>)</li><li>Save the Makefile.</li><li>Recompile <code>liblua</code> (and install it).</li></ol><p>You now should be able to finish the linker process in the Wireshark build.</p><h3 id="its-easier-to-use-the-rhel-package-manager.">It's easier to use the RHEL package manager.</h3><p>Before I even tried the above, I played around with installing a Wireshark dev environment on CentOS (a derivative of RHEL). It's simple and painless. I didn't need to build <code>liblua</code> from source as it's already available as a package. The same is true for <code>libsmi</code>. The following commands worked from a fresh install of a CentOS VM:</p><pre><code>#!/bin/sh
########################################################################
# This script installs the tools necessary for Wireshark development.
# If the tools are already installed, the package manager is smart
# enough to not re-install.
########################################################################

# Install build tools (gcc, gdb, flex, etc.)
sudo yum install &#39;Development Tools&#39;

# Required packages (any dependencies get pulled in automatically)
sudo yum install gtk2-devel.x86_64 libpcap-devel.x86_64

# Optional packages
sudo yum install lua-devel.x86_64 libsmi-devel.x86_64</code></pre><p>Note that the package manager only has Lua 5.1.4 available. If you need any other version (such as 5.1.5), you'll have to build from source as you were doing earlier.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jun '12, 19:26</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>15 Jun '12, 20:59</strong> </span></p></div></div><div id="comments-container-11983" class="comments-container"><span id="12103"></span><div id="comment-12103" class="comment"><div id="post-12103-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your Help I have recompile LUA - with your provided option, LIBSMI and wireshark. Now it's working fine.</p></div><div id="comment-12103-info" class="comment-info"><span class="comment-age">(21 Jun '12, 04:17)</span> <span class="comment-user userinfo">Mevalal</span></div></div></div><div id="comment-tools-11983" class="comment-tools"></div><div class="clear"></div><div id="comment-11983-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

