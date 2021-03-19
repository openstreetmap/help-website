+++
type = "question"
title = "How can I show a string for a decoded value?"
description = '''I am trying to have a dissector for my proprietary protocol. I have to decode Flags byte in my protocol as bit-string and I have done it with below code:  f.msg_flags = ProtoField.uint8(&quot;MyProto.Flags&quot;, &quot;Flags&quot;, base.HEX) f.msgver = ProtoField.uint8(&quot;MyProto.msgver&quot;, &quot;Version&quot;, base_DEC, nil, 0xE0) ...'''
date = "2012-08-17T05:37:00Z"
lastmod = "2012-08-17T06:30:00Z"
weight = 13700
keywords = [ "lua", "bit", "dissector", "bits", "string" ]
aliases = [ "/questions/13700" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I show a string for a decoded value?](/questions/13700/how-can-i-show-a-string-for-a-decoded-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13700-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to have a dissector for my proprietary protocol. I have to decode Flags byte in my protocol as bit-string and I have done it with below code:</p><pre><code>f.msg_flags = ProtoField.uint8(&quot;MyProto.Flags&quot;, &quot;Flags&quot;, base.HEX)
f.msgver = ProtoField.uint8(&quot;MyProto.msgver&quot;, &quot;Version&quot;, base_DEC, nil, 0xE0)
f.prototype = ProtoField.uint8(&quot;MyProto.prototype&quot;, &quot;Protocol Type&quot;, base.DEC, nil, 0x10)
f.reserver = ProtoField.uint8(&quot;MyProto.reserved&quot;, &quot;Reserved&quot;, base.DEC, nil, 0x0E)

local msg_flags = buffer (offset,1):bytes()
        subtree:add(f.msg_flags,buffer(offset,1))
        subtree:add(f.msgver,buffer(offset,1))
        subtree:add(f.prototype,buffer(offset,1))
        subtree:add(f.reserver,buffer(offset,1))</code></pre><p>And Wireshark decodes with above code:</p><pre><code>Flags:    0x2e
001. .... = Version: 1
...0 .... = Protocol Type: 0
.... 111. = Reserved: 7</code></pre><p>But I want to set the Name String for the bit field 'Protocol Type' based the value. If Protocol Type bit is set to '0' then I want to show it as "MYPROTO1" and if bit is set to '1' then show it as "MYPROTO2".</p><p>i.e: After wireshark decode I want to see it as</p><pre><code>Flags:    0x2e
001. .... = Version: 1
...0 .... = Protocol Type: MYPROTO1 (0)
.... 111. = Reserved: 7</code></pre><p>Any help is greatly appreciated.</p></div><div id="question-tags" class="tags-container tags">lua bit dissector bits string</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Aug '12, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/ceb9fa89fe77c08ded53b2ccf693aeaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Aruna%20Sirigere&#39;s gravatar image" /><p>Aruna Sirigere<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Aruna Sirigere has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Aug '12, 06:23</p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-13700" class="comments-container"></div><div id="comment-tools-13700" class="comment-tools"></div><div class="clear"></div><div id="comment-13700-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="13701"></span>

<div id="answer-container-13701" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13701-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>What you need is called a value string. I couldn't find any particularly good examples very quickly, but it should look something like this:</p><pre><code>local VALS_MYPROTO = {[0] = &quot;MYPROTO1&quot;, [1] = &quot;MYPROTO2&quot;}</code></pre><p>...and then when you declare your protofield, provide this table as the <code>valuestring</code> parameter:</p><pre><code>f.prototype = ProtoField.uint8(&quot;MyProto.prototype&quot;, &quot;Protocol Type&quot;, base.DEC, VALS_MYPROTO, 0x10)</code></pre><p>That should do what you want. The equivalent in C would be this:</p><pre><code>static const value_string vs_myproto[] = {
    {0, &quot;MYPROTO1&quot;},
    {1, &quot;MYPROTO2&quot;},
    {0, NULL}
};

static hf_register_info hf[] = {
  {&amp;hf_prototype, {&quot;Protocol Type&quot;, &quot;myproto.prototype&quot;, FT_UINT8, BASE_HEX, VALS(vs_myproto), 0x10, &quot;Protocol Type&quot;, HFILL}}
};</code></pre><p>Note that in C, you could also use a <code>true_false_string</code> in stead of a <code>value_string</code> for a 1-bit field (boolean). In either case, you add this code to your protofield declaration, and Wireshark will do the rest -that is, you do not need to do anything special for it to display your value string.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '12, 06:24</strong></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p>multipleinte...<br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="multipleinterfaces has 9 accepted answers">12%</span></p></div></div><div id="comments-container-13701" class="comments-container"><span id="13703"></span><div id="comment-13703" class="comment"><div id="post-13703-score" class="comment-score"></div><div class="comment-text"><p>As a little further explanation, the value "0x10" in the fine examples above is a mask to isolate the bit(s) required for the value string.</p></div><div id="comment-13703-info" class="comment-info"><span class="comment-age">(17 Aug '12, 06:32)</span> grahamb ♦</div></div><span id="13744"></span><div id="comment-13744" class="comment"><div id="post-13744-score" class="comment-score"></div><div class="comment-text"><p>Thanks Multipleinterfaces and jaap. It worked.. :)</p></div><div id="comment-13744-info" class="comment-info"><span class="comment-age">(19 Aug '12, 22:47)</span> Aruna Sirigere</div></div><span id="13747"></span><div id="comment-13747" class="comment"><div id="post-13747-score" class="comment-score"></div><div class="comment-text"><p>I've converted your "answer" to a comment as that's how this site works. You can accept the best answer to your question by clicking the "check mark" icon next to the answer which helps other users to see what solved your problem.</p></div><div id="comment-13747-info" class="comment-info"><span class="comment-age">(20 Aug '12, 03:26)</span> grahamb ♦</div></div></div><div id="comment-tools-13701" class="comment-tools"></div><div class="clear"></div><div id="comment-13701-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="13702"></span>

<div id="answer-container-13702" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-13702-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>In <code>ProtoField.uint8("MyProto.prototype", "Protocol Type", base.DEC, nil, 0x10)</code> replace the nil by a value string.</p><pre><code>local VALS_VER  = {[0] = &quot;MYPROTO1&quot;, [1] = &quot;Not MYPROTO1&quot;}
ProtoField.uint8(&quot;MyProto.prototype&quot;, &quot;Protocol Type&quot;, base.DEC, VALS_VER, 0x10)</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>17 Aug '12, 06:30</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 17 Aug '12, 06:31</p></div></div><div id="comments-container-13702" class="comments-container"></div><div id="comment-tools-13702" class="comment-tools"></div><div class="clear"></div><div id="comment-13702-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

