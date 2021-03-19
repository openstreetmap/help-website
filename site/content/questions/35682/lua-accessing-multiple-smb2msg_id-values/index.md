+++
type = "question"
title = "LUA: Accessing multiple smb2.msg_id values"
description = '''Hi, I&#x27;m writing some code that includes the parsing of SMB2 packets. Some packets have, say, three SMB2 apdus. If I use wireshark Apply as column the smb2.msg_id field I see all three msg_id values in the Packet List separated by commas. If I access the msg_id value in my LUA script I get the first ...'''
date = "2014-08-22T15:28:00Z"
lastmod = "2014-08-26T12:54:00Z"
weight = 35682
keywords = [ "lua", "smb2" ]
aliases = [ "/questions/35682" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA: Accessing multiple smb2.msg\_id values](/questions/35682/lua-accessing-multiple-smb2msg_id-values)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35682-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm writing some code that includes the parsing of SMB2 packets. Some packets have, say, three SMB2 apdus. If I use wireshark Apply as column the smb2.msg_id field I see all three msg_id values in the Packet List separated by commas. If I access the msg_id value in my LUA script I get the first msg_id in the packet only.</p><p>How can I access all the msg_id values?</p><p>Thanks and regards...Paul</p></div><div id="question-tags" class="tags-container tags">lua smb2</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '14, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/2e1b4057f2ff59fe059b23cc6571abaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PaulOfford&#39;s gravatar image" /><p>PaulOfford<br />
<span class="score" title="131 reputation points">131</span><span title="28 badges"><span class="badge1">●</span><span class="badgecount">28</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PaulOfford has 5 accepted answers">11%</span></p></div></div><div id="comments-container-35682" class="comments-container"></div><div id="comment-tools-35682" class="comment-tools"></div><div class="clear"></div><div id="comment-35682-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35772"></span>

<div id="answer-container-35772" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-35772-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Gerald Combs asked a similar question years ago on the Wireshark developers mailing list, and Tamás Regõs provided a response that you may find useful.</p><p>To quote:</p><pre><code>In case the field occurrence is more than 1 then result of the Field.new will be a table/array and not just 1 value.

Try something like this:

    ip_src_f = Field.new(&quot;ip.src&quot;)
    local ip_src_table = { ip_src_f() }

    for i,ip_src in ipairs(p_src_table) do
        local src = tostring(ip_src.value)
        -- ....
      end</code></pre><p>Ref: <a href="https://www.wireshark.org/lists/wireshark-dev/201005/msg00115.html">https://www.wireshark.org/lists/wireshark-dev/201005/msg00115.html</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Aug '14, 12:54</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-35772" class="comments-container"><span id="35884"></span><div id="comment-35884" class="comment"><div id="post-35884-score" class="comment-score"></div><div class="comment-text"><p>Thanks, that sounds promising. I'll give it a try and feedback the results.</p><p>Best regards...Paul</p></div><div id="comment-35884-info" class="comment-info"><span class="comment-age">(29 Aug '14, 16:16)</span> PaulOfford</div></div><span id="35921"></span><div id="comment-35921" class="comment"><div id="post-35921-score" class="comment-score"></div><div class="comment-text"><p>Just tested this - it works a treat. Thanks for your help.</p></div><div id="comment-35921-info" class="comment-info"><span class="comment-age">(01 Sep '14, 23:09)</span> PaulOfford</div></div></div><div id="comment-tools-35772" class="comment-tools"></div><div class="clear"></div><div id="comment-35772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

