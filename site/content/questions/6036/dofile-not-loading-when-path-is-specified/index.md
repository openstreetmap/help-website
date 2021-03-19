+++
type = "question"
title = "dofile not loading when path is specified"
description = '''Hi, I have written a dissector and placed it in /home/me I edited init.lua with dofile(&quot;/home/me/mydissector.lua&quot;) when i run wireshark i get Lua: Error During Loading If i cd /home/me and run wireshak the dissector is loaded properly. I am running Wireshark 1.4.1 &amp;amp; Lua 5.1 on CentOS 5.6 as root...'''
date = "2011-08-31T17:17:00Z"
lastmod = "2011-11-08T20:26:00Z"
weight = 6036
keywords = [ "lua" ]
aliases = [ "/questions/6036" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [dofile not loading when path is specified](/questions/6036/dofile-not-loading-when-path-is-specified)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-6036-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have written a dissector and placed it in /home/me</p><p>I edited init.lua with dofile("/home/me/mydissector.lua") when i run wireshark i get Lua: Error During Loading</p><p>If i cd /home/me and run wireshak the dissector is loaded properly.</p><p>I am running Wireshark 1.4.1 &amp; Lua 5.1 on CentOS 5.6 as root.</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Aug '11, 17:17</strong></p><img src="https://secure.gravatar.com/avatar/e9a64b38c3c80a882aa3c808b71cccbb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mrb&#39;s gravatar image" /><p>mrb<br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mrb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 31 Aug '11, 17:35</p></div></div><div id="comments-container-6036" class="comments-container"><span id="6039"></span><div id="comment-6039" class="comment"><div id="post-6039-score" class="comment-score"></div><div class="comment-text"><p>There should be additional detail after "Error during loading". For example:</p><pre><code>tshark: Lua: Error during loading:
 [string &quot;dummy.lua&quot;]:2: bad argument #1 to &#39;dofile&#39; (dofile: file does not exist)</code></pre><p>What is your full error message?</p></div><div id="comment-6039-info" class="comment-info"><span class="comment-age">(31 Aug '11, 19:16)</span> helloworld</div></div></div><div id="comment-tools-6036" class="comment-tools"></div><div class="clear"></div><div id="comment-6036-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7308"></span>

<div id="answer-container-7308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-7308-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>just to check, if you have seen 'disable potentialy harmful lua functions when running superuser' comment in the init.lua?</p><p>there's a special check for running under root that disables dofile and other os related libraries.</p><pre><code>if running_superuser then
    local disabled_lib = {}
    setmetatable(disabled_lib,{ __index = function() error(&quot;this package has been disabled&quot;) end } );

    dofile = function() error(&quot;dofile has been disabled&quot;) end
...
end</code></pre><p>If you absolutely need to run wireshark as root then you can temporarly disable that check by adding say '0 and' to if condition:</p><pre><code>if 0 and running_superuser then
    local disabled_lib = {}
...</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Nov '11, 20:26</strong></p><img src="https://secure.gravatar.com/avatar/35d96b8e73e6deb4e332d076fd3269b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ShomeaX&#39;s gravatar image" /><p>ShomeaX<br />
<span class="score" title="73 reputation points">73</span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ShomeaX has no accepted answers">0%</span></p></div></div><div id="comments-container-7308" class="comments-container"></div><div id="comment-tools-7308" class="comment-tools"></div><div class="clear"></div><div id="comment-7308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

