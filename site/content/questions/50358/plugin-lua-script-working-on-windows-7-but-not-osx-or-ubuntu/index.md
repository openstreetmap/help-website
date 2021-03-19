+++
type = "question"
title = "plugin (.lua script) working on Windows 7 but not OSX or UBUNTU?"
description = '''I have a working script which runs on tshark on windows (processes PCAP files, gives valid output). On windows, both the GUI and tshark can run this script and give me valid output. GUI fails on mac but does properly process some pcaps on mac. On ubuntu the script fails both for GUI and command line...'''
date = "2016-02-19T17:01:00Z"
lastmod = "2016-02-19T18:06:00Z"
weight = 50358
keywords = [ "windows", "lua", "ubuntu", "pcap", "osx" ]
aliases = [ "/questions/50358" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [plugin (.lua script) working on Windows 7 but not OSX or UBUNTU?](/questions/50358/plugin-lua-script-working-on-windows-7-but-not-osx-or-ubuntu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50358-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50358-score" class="post-score" title="current number of votes">0</div><span id="post-50358-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a working script which runs on tshark on windows (processes PCAP files, gives valid output). On windows, both the GUI and tshark can run this script and give me valid output. GUI fails on mac but does properly process some pcaps on mac. On ubuntu the script fails both for GUI and command line.</p><p>Does anyone know what the next best logical steps would be to troubleshoot this? I need my .lua script to work on ubuntu.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows" rel="tag" title="see questions tagged &#39;windows&#39;">windows</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-osx" rel="tag" title="see questions tagged &#39;osx&#39;">osx</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Feb '16, 17:01</strong></p><img src="https://secure.gravatar.com/avatar/2a64be647ac8ec21b76a6c042bebb6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testname0110&#39;s gravatar image" /><p><span>testname0110</span><br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testname0110 has 3 accepted answers">75%</span></p></div></div><div id="comments-container-50358" class="comments-container"><span id="50359"></span><div id="comment-50359" class="comment"><div id="post-50359-score" class="comment-score">1</div><div class="comment-text"><p>What version of Wireshark is running on each platform? If they're not all the same version as the one running on Windows, that might be a clue as to what the problem may be.</p><p>Also, what exactly is the failure? On the Ubuntu system for example, does <code>Help -&gt; About Wireshark</code> indicate that Wireshark was compiled <strong>with Lua 5.2</strong> (or some other version)?</p><p>Lastly, does the Ubuntu <code>init.lua</code> script have <code>disable_lua = true</code>? If so, you'll need to set it to <code>false</code>.</p><p>See also: <a href="https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm.html">https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm.html</a></p></div><div id="comment-50359-info" class="comment-info"><span class="comment-age">(19 Feb '16, 17:57)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div><span id="50360"></span><div id="comment-50360" class="comment"><div id="post-50360-score" class="comment-score"></div><div class="comment-text"><p>this was it. I actually thought of that right after I posted this (derp). it completely fixed the mac problem and now I am trying to fix the version for linux. Do you know how I can get 1.12.9 (wireshark version) for ubuntu? I can't seem to find the install package now.</p></div><div id="comment-50360-info" class="comment-info"><span class="comment-age">(19 Feb '16, 18:05)</span> <span class="comment-user userinfo">testname0110</span></div></div></div><div id="comment-tools-50358" class="comment-tools"></div><div class="clear"></div><div id="comment-50358-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50361"></span>

<div id="answer-container-50361" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50361-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50361-score" class="post-score" title="current number of votes">0</div><span id="post-50361-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="testname0110 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>the newest version of wireshark does not fully support old plugins. That seems to be the issue. the version 2.0 is unstable. To fix the issue I used xterm to open old wireshark and that solved my problem (on mac at least)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Feb '16, 18:06</strong></p><img src="https://secure.gravatar.com/avatar/2a64be647ac8ec21b76a6c042bebb6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testname0110&#39;s gravatar image" /><p><span>testname0110</span><br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testname0110 has 3 accepted answers">75%</span></p></div></div><div id="comments-container-50361" class="comments-container"></div><div id="comment-tools-50361" class="comment-tools"></div><div class="clear"></div><div id="comment-50361-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

