+++
type = "question"
title = "SSL Lua dissector - how?"
description = '''I have a protocol that is over SSL that I&#x27;d like to dissect. I&#x27;m having a hard time just conceptually figuring out how one goes about doing this. I&#x27;ve created a dissector for the right port that gets a reference to the ssl dissector and then calls it. I&#x27;ve also tried registering it as a post-dissect...'''
date = "2016-12-19T19:56:00Z"
lastmod = "2017-01-11T04:37:00Z"
weight = 58247
keywords = [ "chained-dissector", "ssl", "dissector", "postdissector", "lua" ]
aliases = [ "/questions/58247" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [SSL Lua dissector - how?](/questions/58247/ssl-lua-dissector-how)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58247-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a protocol that is over SSL that I'd like to dissect. I'm having a hard time just conceptually figuring out how one goes about doing this. I've created a dissector for the right port that gets a reference to the ssl dissector and then calls it. I've also tried registering it as a post-dissector. In both cases the SSL dissector seems to work a-ok (I have a client-random/master key file set up in the SSL protocol preferences) and I can see my protocol's raw data in the Follow SSL Stream window. But I'd like to dissect that protocol and get at the decrypted data.</p><p>I'm guessing that what I'm supposed to do is get a reference to one of the fields populated by the SSL dissector like ssl.segment, ssl.segment.data, ssl.reassembled.data, etc and then work with that. But whether I call the ssl dissector explicitly or use a post-dissector, those variables are always nil.</p><pre><code>protocol_foo = Proto(&quot;foo&quot;, &quot;Foo protocol&quot;)
port = 4172

g_field_segment = Field.new(&quot;ssl.segment&quot;)
g_field_segment_data = Field.new(&quot;ssl.segment.data&quot;)
g_field_segments = Field.new(&quot;ssl.segments&quot;)
g_field_reassembled_data = Field.new(&quot;ssl.reassembled.data&quot;)

function protocol_foo.dissector(tvb, pinfo, root)

    print(&quot;====== protocol_foo&quot;)

    for k,v in pairs({ g_field_segment, g_field_segment_data, g_field_segments, g_field_reassembled_data }) do
        if v() ~= nil then
            print(&quot;Field &quot; .. v.name .. &quot; is NOT nil&quot;)
        else
            print(&quot;Field &quot; .. v.name .. &quot; is nil&quot;)
        end
    end

end

-- post-dissector registration
local ssl_dissector = Dissector.get(&quot;ssl&quot;)
local dissector_table_tcp = DissectorTable.get(&quot;tcp.port&quot;)
dissector_table_tcp:add(port, ssl_dissector)
register_postdissector(protocol_foo)</code></pre><p>or calling explicitly ...</p><pre><code>protocol_foo = Proto(&quot;foo&quot;, &quot;Foo protocol&quot;)
port = 4172

g_field_segment = Field.new(&quot;ssl.segment&quot;)
g_field_segment_data = Field.new(&quot;ssl.segment.data&quot;)
g_field_segments = Field.new(&quot;ssl.segments&quot;)
g_field_reassembled_data = Field.new(&quot;ssl.reassembled.data&quot;)

function protocol_foo.dissector(tvb, pinfo, root)

    print(&quot;====== protocol_foo&quot;)

    local ssl_dissector = Dissector.get(&quot;ssl&quot;)
    ssl_dissector:call(tvb, pinfo, root)

    for k,v in pairs({ g_field_segment, g_field_segment_data, g_field_segments, g_field_reassembled_data }) do
        if v() ~= nil then
            print(&quot;Field &quot; .. v.name .. &quot; is NOT nil&quot;)
        else
            print(&quot;Field &quot; .. v.name .. &quot; is nil&quot;)
        end
    end

end

-- dissector registration
local dissector_table_tcp = DissectorTable.get(&quot;tcp.port&quot;)
dissector_table_tcp:add(port, protocol_foo)</code></pre><p>Other fields, like ssl.handshake.* seem to be populated well enough, but not the ones I want. Am I just going about this the wrong way?</p><p>Update: I can appreciate that this seems like an elementary question, but I can't find any examples on the wireshark site, on the web, or in any of the questions and answers in this forum or on SO that do this - I can't find an example of how to dissect the decrypted output of the ssl dissector (although I've read many questions on this forum that seem to indicate that people are in fact doing this successfully).</p></div><div id="question-tags" class="tags-container tags">chained-dissector ssl dissector postdissector lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Dec '16, 19:56</strong></p><img src="https://secure.gravatar.com/avatar/60bc21f7c0f24d7933c966ae4035fcdc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tedmiddleton&#39;s gravatar image" /><p>tedmiddleton<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tedmiddleton has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 21 Dec '16, 16:49</p></div></div><div id="comments-container-58247" class="comments-container"></div><div id="comment-tools-58247" class="comment-tools"></div><div class="clear"></div><div id="comment-58247-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="58487"></span>

<div id="answer-container-58487" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58487-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think you're going about it backwards. Rather than calling SSL from your dissector I'd suggest:</p><ol><li>Write your dissector as a normal dissector (named <code>foo</code>).</li><li>Configure the SSL dissector to decode your port as <code>foo</code> (in the same place where you specify the IP address and key file)</li></ol><p>Your protocol dissector will now be called with a TVB containing the (decrypted) data. Your dissector can, at this point, be unaware that SSL was even involved.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Jan '17, 15:09</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-58487" class="comments-container"><span id="58649"></span><div id="comment-58649" class="comment"><div id="post-58649-score" class="comment-score"></div><div class="comment-text"><p>I'm a bit confused - when you say, "in the same place where you specify the IP address and key file," do you mean the Wireshark SSL protocol preferences? Because that's where I've configured the master key file I'm using. I don't seem to see an option for sub-dissection in those preferences?</p></div><div id="comment-58649-info" class="comment-info"><span class="comment-age">(10 Jan '17, 16:18)</span> tedmiddleton</div></div><span id="58664"></span><div id="comment-58664" class="comment"><div id="post-58664-score" class="comment-score"></div><div class="comment-text"><p>In that case see the answer to <a href="https://ask.wireshark.org/questions/58217/how-do-i-dissect-decrypted-ssl-data-when-im-using-a-master-secret-log">this question</a>.</p><p>Though @koundi's answer is probably the better way (if your port number is constant).</p></div><div id="comment-58664-info" class="comment-info"><span class="comment-age">(11 Jan '17, 06:24)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-58487" class="comment-tools"></div><div class="clear"></div><div id="comment-58487-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="58661"></span>

<div id="answer-container-58661" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58661-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You should consider redesigning your flow. If your protocol works on top of SSl, then the ssl dissector should be called first. Let the TCP dissector worry about that.</p><p>All you need to do while registering proto_foo is to add it to the dissector table using ssl.port.</p><p>Instead of</p><p><code>local dissector_table_tcp = DissectorTable.get("tcp.port") dissector_table_tcp:add(port, protocol_foo)</code></p><p>you can do</p><p><code>local dissector_table_ssl = DissectorTable.get("ssl.port") dissector_table_ssl:add(port, protocol_foo)</code></p><p>and not worry about calling the ssl dissector altogether. Now the decrypted data if available will be passed on to the foo dissector where you will do your processing.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jan '17, 04:37</strong></p><img src="https://secure.gravatar.com/avatar/ed73b970d0135dbac8294249cdadff66?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="koundi&#39;s gravatar image" /><p>koundi<br />
<span class="score" title="97 reputation points">97</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="koundi has no accepted answers">0%</span></p></div></div><div id="comments-container-58661" class="comments-container"><span id="58844"></span><div id="comment-58844" class="comment"><div id="post-58844-score" class="comment-score"></div><div class="comment-text"><p>"bad argument #1 to 'get' (DissectorTable_get: no such dissector_table)". Wireshark doesn't seem to like "ssl.port"?</p></div><div id="comment-58844-info" class="comment-info"><span class="comment-age">(17 Jan '17, 09:37)</span> tedmiddleton</div></div><span id="58846"></span><div id="comment-58846" class="comment"><div id="post-58846-score" class="comment-score">1</div><div class="comment-text"><p>Well it didn't <em>always</em> support <code>ssl.port</code>. I'm guessing you're using 2.0.x or earlier? In that case you'll need to use the solution described in my answer (or just upgrade :-)).</p></div><div id="comment-58846-info" class="comment-info"><span class="comment-age">(17 Jan '17, 10:54)</span> JeffMorriss ♦</div></div><span id="59070"></span><div id="comment-59070" class="comment"><div id="post-59070-score" class="comment-score"></div><div class="comment-text"><p>Yup - I was using 2.0.x. I've upgraded to 2.2 and I no longer get the "no such dissector_table" error with ssl.port. But wireshark/tshark still isn't decoding those packets as SSL or my protocol; at least not on first encounter (when I load the .pcap file). I have to tell wireshark to "decode as..." SSL before it tries decoding and decrypting the packets; even then, it doesn't hand the result off to my dissector.</p></div><div id="comment-59070-info" class="comment-info"><span class="comment-age">(25 Jan '17, 15:42)</span> tedmiddleton</div></div><span id="59072"></span><div id="comment-59072" class="comment"><div id="post-59072-score" class="comment-score"></div><div class="comment-text"><p>The Decode-As bit will still be necessary. Registering yourself for <code>ssl.port</code> X does not cause the SSL dissector to register for <code>tcp.port</code> X.</p><p>I don't know why your dissector wouldn't be called though. Are you sure you registered it for the appropriate port? Is any other dissector registered on that port? You can check by looking at the <code>View-&gt;Internals-&gt;Dissector Tables</code> dialog. Look in the Integer table for <code>SSL TCP dissector</code>. You should see your Lua dissector there under port X.</p></div><div id="comment-59072-info" class="comment-info"><span class="comment-age">(25 Jan '17, 17:49)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-58661" class="comment-tools"></div><div class="clear"></div><div id="comment-58661-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

