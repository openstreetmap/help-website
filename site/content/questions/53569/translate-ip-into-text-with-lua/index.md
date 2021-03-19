+++
type = "question"
title = "translate IP into text with Lua"
description = '''Hello, I have some format of IPs for my endpoints. For example: 10.0.X.28 is host1, 10.0.X.11 is host2. I&#x27;m writing some LUA dissector to parse my protocol. Part of this dissector, I&#x27;d like to change the IPs which are shown, to host1/host2 etc. How this can be done? Thank you'''
date = "2016-06-20T01:43:00Z"
lastmod = "2016-06-21T06:11:00Z"
weight = 53569
keywords = [ "lua" ]
aliases = [ "/questions/53569" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [translate IP into text with Lua](/questions/53569/translate-ip-into-text-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53569-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have some format of IPs for my endpoints. For example: 10.0.X.28 is host1, 10.0.X.11 is host2.</p><p>I'm writing some LUA dissector to parse my protocol. Part of this dissector, I'd like to change the IPs which are shown, to host1/host2 etc.</p><p>How this can be done?</p><p>Thank you</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '16, 01:43</strong></p><img src="https://secure.gravatar.com/avatar/b02c5dfff2049bed61dbced93bf455d4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BMWE&#39;s gravatar image" /><p>BMWE<br />
<span class="score" title="46 reputation points">46</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BMWE has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Jun '16, 06:19</p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span></p></div></div><div id="comments-container-53569" class="comments-container"><span id="53582"></span><div id="comment-53582" class="comment"><div id="post-53582-score" class="comment-score"></div><div class="comment-text"><p>Do I get you right that you want to translate each IP address from a fixed list to a text string? Do you also want to use these strings (your hostnames) in the display filter? Lua dissectors can use Lua tables to define a string for each index value which may be almost anything.</p></div><div id="comment-53582-info" class="comment-info"><span class="comment-age">(21 Jun '16, 01:41)</span> sindy</div></div><span id="53585"></span><div id="comment-53585" class="comment"><div id="post-53585-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I have some format for the IP (like in the exsmple). FROM this format Id like ti convert the IP to some name (not necceserly the hostname)</p></div><div id="comment-53585-info" class="comment-info"><span class="comment-age">(21 Jun '16, 04:35)</span> BMWE</div></div></div><div id="comment-tools-53569" class="comment-tools"></div><div class="clear"></div><div id="comment-53569-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="53587"></span>

<div id="answer-container-53587" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-53587-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>A quote from one of my Lua ad-hoc dissectors:</p><pre><code>-- Define Translation Tables for Individual Items
lfb_indictn_values = {}
lfb_indictn_values[0] = &quot;lfbAllowed&quot;
lfb_indictn_values[1] = &quot;lfbNotAllowed&quot;
lfb_indictn_values[2] = &quot;pathReserved&quot;

-- Export &#39;MyProto&#39;
My_proto = Proto(&quot;mine&quot;,&quot;MyProto&quot;)
...
My_proto_LFB_Indictn = ProtoField.uint8(&quot;my_proto.LFB_Indictn&quot;,&quot;LFB_Indictn&quot;,base.DEC,lfb_indictn_values)
...
My_proto.fields = {..., My_proto_LFB_Indictn, ...}</code></pre><p>and then, in the dissector function itself:</p><pre><code>    local lfb_ind = buffer:range(7,1)
    subtree:add(MLPP_LFB_Indictn,lfb_ind)</code></pre><p>So you could modify it for your purpose, by changing the <code>ProtoField.uint8</code> to <code>ProtoField.IPv4</code> and replacing the reference values of 0, 1, 2 with your IP addresses if ftype.IPv4 allows to use the value -&gt; text translations; otherwise, you would have to treat the IPv4 field as uint32 and convert your IP addresses to the corresponding uint32 values.</p><pre><code>endpoint_hostname = {}
endpoint_hostname[10.0.7.28] = &quot;host number 28&quot;
endpoint_hostname[10.0.7.17] = &quot;host number 17&quot;</code></pre><p>or, possibly,</p><pre><code>...
endpoint_hostname[&quot;10.0.7.28&quot;] = &quot;host number 28&quot;
...</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jun '16, 06:11</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-53587" class="comments-container"><span id="53593"></span><div id="comment-53593" class="comment"><div id="post-53593-score" class="comment-score"></div><div class="comment-text"><p>I'm missing something in your solution: In the main screen, where one can see all the packets, there is source and destination columns, where IP can be seen. I'm looking to replace those IPs.</p><p>In addition, I have some constant IPs (which is more simple), but I have also some template for IPs: 10.0.X.28, where X can be any value. How can I change those IPs?</p></div><div id="comment-53593-info" class="comment-info"><span class="comment-age">(21 Jun '16, 08:54)</span> BMWE</div></div><span id="53594"></span><div id="comment-53594" class="comment"><div id="post-53594-score" class="comment-score"></div><div class="comment-text"><p>I've converted your "Answer" (which it clearly wasn't as it did not answer your original Question) into a Comment, see site FAQ for details.</p><p>From your Question it wasn't clear to me that you want to change the way how IP addresses are dissected at IP layer, I thought you were talking about IP addresses inside your own protocol.</p><p>In general, a dissector only deals with the part of the frame it has been given for processing as a TVB parameter, and it cannot affect how other dissectors handle other parts of the frame. So if you want to change the way how IP addresses are extracted into packet info fields and filterable fields, you would have to <strong>replace</strong> the IPv4 dissector with your own one. I.e. you would have to register your own dissector for the IPv4 layer, replace pointers to it in Ethertype etc. dissector tables, and make it call icmp, tcp, udp etc. dissectors based on the contents of <code>ip.proto</code> field of the IPv4 header (according to contents of dissector table <code>ip.proto</code>).</p><p>As for ignoring the X byte, that would require to do the translation manually, i.e. you would not be able to use the translation embedded into the Lua API (but it would still be possible to use the table, except that you would have to use only the last byte of the IPv4 address as the key).</p><p>But there is another way to achieve your goal than using a Lua dissector, you might want to use Wireshark's name resolution ability to translate the IP addresses to text using the local <code>hosts</code> file, as suggested <a href="https://www.wireshark.org/docs/wsug_html_chunked/ChAdvNameResolutionSection.html">here</a>.</p></div><div id="comment-53594-info" class="comment-info"><span class="comment-age">(21 Jun '16, 10:02)</span> sindy</div></div></div><div id="comment-tools-53587" class="comment-tools"></div><div class="clear"></div><div id="comment-53587-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

