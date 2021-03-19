+++
type = "question"
title = "Lua: Error during loading mpeg_packets_dump.lua"
description = '''Hello,  I just put this file to /usr/local/lib/wireshark.plugins/1.10.2/, then had this error right at the start of wireshark :  Lua: Error during loading:  [string &quot;/usr/local/lib/wireshark/plugins/1.10.2/mpe...&quot;]:30: bad argument #1 to &#x27;new&#x27; (Field_new: a field with this name must exist) A little ...'''
date = "2014-01-07T02:22:00Z"
lastmod = "2014-01-08T09:05:00Z"
weight = 28617
keywords = [ "lua", "tools", "mpeg_dump", "plugins" ]
aliases = [ "/questions/28617" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Lua: Error during loading mpeg\_packets\_dump.lua](/questions/28617/lua-error-during-loading-mpeg_packets_dumplua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28617-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I just put <a href="http://wiki.wireshark.org/mpeg_dump.lua">this file</a> to /usr/local/lib/wireshark.plugins/1.10.2/, then had this error right at the start of wireshark :</p><p>Lua: Error during loading: [string "/usr/local/lib/wireshark/plugins/1.10.2/mpe..."]:30: bad argument #1 to 'new' (Field_new: a field with this name must exist)</p><p>A little help ?</p></div><div id="question-tags" class="tags-container tags">lua tools mpeg_dump plugins</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Jan '14, 02:22</strong></p><img src="https://secure.gravatar.com/avatar/94eb051be96f49a1665b097330fd97bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ychaouche&#39;s gravatar image" /><p>ychaouche<br />
<span class="score" title="31 reputation points">31</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ychaouche has one accepted answer">100%</span></p></div></div><div id="comments-container-28617" class="comments-container"></div><div id="comment-tools-28617" class="comment-tools"></div><div class="clear"></div><div id="comment-28617-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28673"></span>

<div id="answer-container-28673" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28673-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Line 30 contains this:</p><pre><code>mpeg_payload = Field.new(&quot;mp2t.payload&quot;)</code></pre><p>Now, the field <code>mp2t.payload</code> was removed in Wireshark 1.8.x (<a href="http://www.wireshark.org/docs/dfref/m/mp2t.html">see here</a> - reason unknown to me). So, you can't reference that in Wireshark 1.10.x !! Please remove all references to it from the code and it should work.</p><p>BTW: The newly defined variables (fields) <code>mpeg_payload</code> and <code>mpeg_pusi</code> are only defined, but never used in the Lua code, so you can simply delete those lines.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '14, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28673" class="comments-container"><span id="28684"></span><div id="comment-28684" class="comment"><div id="post-28684-score" class="comment-score"></div><div class="comment-text"><p>Thank you that solved the problem ! the plugin however seems not to be up-to-date as another error popped-up when trying to dump packets to file.</p></div><div id="comment-28684-info" class="comment-info"><span class="comment-age">(08 Jan '14, 11:36)</span> ychaouche</div></div><span id="28686"></span><div id="comment-28686" class="comment"><div id="post-28686-score" class="comment-score"></div><div class="comment-text"><p>What is that error message?</p></div><div id="comment-28686-info" class="comment-info"><span class="comment-age">(08 Jan '14, 11:46)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-28673" class="comment-tools"></div><div class="clear"></div><div id="comment-28673-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

