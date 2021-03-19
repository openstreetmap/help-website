+++
type = "question"
title = "Why Some LUA APIs not supporting in Wireshark 1.10.6?"
description = '''I have installed wireshark version 1.10.6 in Ubuntu(14.04) And I have written sample lua file which i am trying to run in windows and ubuntu both.in windows7 it is working fine but in ubuntu it is creating problem see the picture my lua code is below local myproto = Proto(&quot;myproto&quot;, &quot;My Protocol&quot;) f...'''
date = "2015-04-09T01:07:00Z"
lastmod = "2015-04-09T10:46:00Z"
weight = 41313
keywords = [ "lua", "api", "wireshark" ]
aliases = [ "/questions/41313" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why Some LUA APIs not supporting in Wireshark 1.10.6?](/questions/41313/why-some-lua-apis-not-supporting-in-wireshark-1106)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41313-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have installed wireshark version 1.10.6 in Ubuntu(14.04) And I have written sample lua file which i am trying to run in windows and ubuntu both.in windows7 it is working fine but in ubuntu it is creating problem see the picture my lua code is below</p><p><code>local myproto = Proto("myproto", "My Protocol") function myproto.dissector (buf, pkt, root)    local t = root:add(myproto, buf()):append_text("hi")    t:add(buf(0, 1),string.format("First Byte: %d",buf(0,1):uint())) end local tcp_table = DissectorTable.get("tcp.port") tcp_table:add(8443, myproto) tcp_table:add(61639, myproto)</code></p><p>windows_wireshark</p><p><img src="https://osqa-ask.wireshark.org/upfiles/windows.png" alt="windows_wireshark" /></p><p>ubuntu_wireshark <img src="https://osqa-ask.wireshark.org/upfiles/ubuntu.png" alt="alt text" /></p><p>I am using Lua 5.2</p></div><div id="question-tags" class="tags-container tags">lua api wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Apr '15, 01:07</strong></p><img src="https://secure.gravatar.com/avatar/8efce51fbbf3dbd6c9b9132056f45eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ankit&#39;s gravatar image" /><p>ankit<br />
<span class="score" title="65 reputation points">65</span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ankit has one accepted answer">25%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 10 Apr '15, 14:06</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></img></div></div><div id="comments-container-41313" class="comments-container"><span id="41321"></span><div id="comment-41321" class="comment"><div id="post-41321-score" class="comment-score"></div><div class="comment-text"><p>What version of Wireshark are you running on Windows? Is it also 1.10.6?</p></div><div id="comment-41321-info" class="comment-info"><span class="comment-age">(09 Apr '15, 06:18)</span> JeffMorriss ♦</div></div><span id="41326"></span><div id="comment-41326" class="comment"><div id="post-41326-score" class="comment-score"></div><div class="comment-text"><p>I am using 1.12.4 latest one in windows and when i did apt-get install wireshark command in ubuntu. It installed 1.10.6 wireshark version</p></div><div id="comment-41326-info" class="comment-info"><span class="comment-age">(09 Apr '15, 08:28)</span> ankit</div></div></div><div id="comment-tools-41313" class="comment-tools"></div><div class="clear"></div><div id="comment-41313-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41329"></span>

<div id="answer-container-41329" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-41329-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm no Lua-for-Wireshark expert, but:</p><p>I'd say that somewhere between 1.10 and 1.12 the append_text() API was modified to return the tree item. So if you want to use that exact code it'll only work in 1.12+.</p><p>But, I think you probably don't really want/need to anyway. I think this should work in both versions:</p><pre><code>function myproto.dissector (buf, pkt, root)
   local t = root:add(myproto, buf())
   t:append_text(&quot;hi&quot;)
   t:add(buf(0, 1),string.format(&quot;First Byte: %d&quot;,buf(0,1):uint()))
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Apr '15, 10:46</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-41329" class="comments-container"><span id="41339"></span><div id="comment-41339" class="comment"><div id="post-41339-score" class="comment-score"></div><div class="comment-text"><p>thanks jeffMorriss for looking into my problem. But here my problem is after append_text in parent tree it is giving me error for e.g in above same code <code>function myproto.dissector (buf, pkt, root)    local t = root:add(myproto, buf())    localst = t:append_text("hi")    st:add(buf(0,1)),string.format("First Byte:%d,buf(0,1):uint())</code></p><p>and one more thing, according to you 1.12 is latest one for ubuntu. but when i am doing apt-get install wireshark after apt-get update. it is telling me that you have already latest version....</p></div><div id="comment-41339-info" class="comment-info"><span class="comment-age">(09 Apr '15, 21:34)</span> ankit</div></div><span id="41344"></span><div id="comment-41344" class="comment"><div id="post-41344-score" class="comment-score"></div><div class="comment-text"><p>You are using Ubuntu 14.04, the latest version of Wireshark for that release is <a href="http://packages.ubuntu.com/search?keywords=wireshark&amp;searchon=names&amp;suite=trusty&amp;section=all">1.10.6</a>.</p><p>To get a newer version of Wireshark that has the functionality in the Lua API you require, you'll either have to; compile your own from the Wireshark sources (can build any version), move to a newer version of <a href="http://packages.ubuntu.com/search?keywords=wireshark&amp;searchon=names&amp;exact=1&amp;suite=all&amp;section=all">Ubuntu</a> (at least utopic, 14.10) which will get you 1.12.1, or use the <a href="https://launchpad.net/~wireshark-dev/+archive/ubuntu/stable">Wireshark development ppa</a> which again gives you 1.12.1.</p></div><div id="comment-41344-info" class="comment-info"><span class="comment-age">(10 Apr '15, 02:26)</span> grahamb ♦</div></div><span id="41761"></span><div id="comment-41761" class="comment"><div id="post-41761-score" class="comment-score"></div><div class="comment-text"><p>Oh, sorry, I meant to provide another response (thanks, Graham, for answering the version problem).</p><p>Why are you trying to add an item to the thing which is returned by append_text()? I think you should be able to do it as I had: create the top-level protocol item, append text to it, and then add an item the top-level protocol item ('t' in my sample code). There's no need for the 'st' variable in your (latest) code.</p></div><div id="comment-41761-info" class="comment-info"><span class="comment-age">(23 Apr '15, 14:59)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-41329" class="comment-tools"></div><div class="clear"></div><div id="comment-41329-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

