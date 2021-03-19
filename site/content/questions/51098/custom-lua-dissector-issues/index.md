+++
type = "question"
title = "Custom Lua dissector issues"
description = '''Issues in loading my lua script tshark -v ==&amp;gt; TShark 1.8.10 OS: Centos 2.6 Steps:  vi hello.lua  add following text:  print (&quot;Hello world!!&quot;) save &amp;amp; quit (:wq)  pwd: /tmp/source/lua tshark -v -Xlua_script:/tmp/source/lua (also tried: tshark -v -X lua_script:/tmp/source/lua) prints tshark vers...'''
date = "2016-03-22T10:11:00Z"
lastmod = "2016-03-22T11:31:00Z"
weight = 51098
keywords = [ "lua" ]
aliases = [ "/questions/51098" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Custom Lua dissector issues](/questions/51098/custom-lua-dissector-issues)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51098-score" class="post-score" title="current number of votes">0</div><span id="post-51098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Issues in loading my lua script tshark -v ==&gt; TShark 1.8.10 OS: Centos 2.6 Steps:</p><ol><li><code>vi hello.lua</code></li><li>add following text: <code>print ("Hello world!!")</code></li><li>save &amp; quit (<code>:wq</code>)</li><li><code>pwd: /tmp/source/lua</code></li><li><code>tshark -v -Xlua_script:/tmp/source/lua</code> (also tried: <code>tshark -v -X lua_script:/tmp/source/lua</code>)</li><li>prints tshark version (1.8.10) &amp; exits. (happens for both root &amp; normal user)</li><li>As work around suggested by google, tried to copy hello.lua to personal plugins folder (found from wireshark==&gt; Help ==&gt; Folders ==&gt; personal plugin (<code>/home/build/.wireshark/plugins</code>). I could not find my plugin loaded, checked at wireshark==&gt; Help ==&gt; Plugins.</li><li>again more google: checked this command <code>tshark -v | grep Lua       capabilities, with SMI 0.4.8, without c-ares, without ADNS, without Lua, without</code></li></ol><p>anyhelp is really appreciated.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '16, 10:11</strong></p><img src="https://secure.gravatar.com/avatar/ba0e896697d08a57b1ce91aceda14bf4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="khader&#39;s gravatar image" /><p><span>khader</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="khader has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Mar '16, 10:22</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-51098" class="comments-container"></div><div id="comment-tools-51098" class="comment-tools"></div><div class="clear"></div><div id="comment-51098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51100"></span>

<div id="answer-container-51100" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51100-score" class="post-score" title="current number of votes">0</div><span id="post-51100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Doesn't the output of step 8 give it away:</p><blockquote><p>capabilities, with SMI 0.4.8, without c-ares, without ADNS, <strong>without Lua</strong>, without</p></blockquote><p>Your, really old, copy of tshark hasn't been compiled with lua support.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Mar '16, 10:24</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-51100" class="comments-container"><span id="51102"></span><div id="comment-51102" class="comment"><div id="post-51102-score" class="comment-score"></div><div class="comment-text"><p>Yes, you right!!! But one of my "google" search asked me to overlook at it!! Moreover I installed wireshark couple of days back on my 32 Bit machine. I "THINK" latest version is: TShark 1.8.10. Anywasy tired same steps 1 to 5 on my x64 bit machine. It works AWESOME!!! Again thanks for the hi(n)ts</p></div><div id="comment-51102-info" class="comment-info"><span class="comment-age">(22 Mar '16, 11:11)</span> <span class="comment-user userinfo">khader</span></div></div><span id="51103"></span><div id="comment-51103" class="comment"><div id="post-51103-score" class="comment-score">1</div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-51103-info" class="comment-info"><span class="comment-age">(22 Mar '16, 11:31)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-51100" class="comment-tools"></div><div class="clear"></div><div id="comment-51100-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

