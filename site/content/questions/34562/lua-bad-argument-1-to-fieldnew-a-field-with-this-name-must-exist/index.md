+++
type = "question"
title = "[Lua] Bad argument #1 to Field.new (a field with this name must exist)"
description = '''Recently I created a few ProtoFields in a Lua file that contains a dissector. The ProtoFields seem to work great when I test the dissector, and I can even use them as a display filter. The file looks like this: proto_name = Proto(&quot;foo&quot;,&quot;FOO PROTOCOL&quot;) msg_id = ProtoField.uint16 (&quot;foo.msg_id&quot;, &quot;msg_i...'''
date = "2014-07-10T07:23:00Z"
lastmod = "2014-07-10T09:06:00Z"
weight = 34562
keywords = [ "listener", "lua", "dissector", "fields", "wireshark" ]
aliases = [ "/questions/34562" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[Lua\] Bad argument \#1 to Field.new (a field with this name must exist)](/questions/34562/lua-bad-argument-1-to-fieldnew-a-field-with-this-name-must-exist)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34562-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Recently I created a few ProtoFields in a Lua file that contains a dissector. The ProtoFields seem to work great when I test the dissector, and I can even use them as a display filter. The file looks like this:</p><pre><code>proto_name = Proto(&quot;foo&quot;,&quot;FOO PROTOCOL&quot;)
msg_id = ProtoField.uint16 (&quot;foo.msg_id&quot;, &quot;msg_id&quot;, base.DEC, table_of_stuff)
msg_sub_id = ProtoField.uint16 (&quot;foo.msg_sub_id&quot;, &quot;msg_sub_id_unused&quot;)
msg_size = ProtoField.uint32 (&quot;foo.msg_size&quot;, &quot;msg_size&quot;)
proto_name.fields = {msg_id, msg_sub_id, msg_size}

function proto_name.dissector (buffer, pinfo, tree)
   --fields are added to treeitems
end

tcp_table = DissectorTable.get(&quot;tcp.port&quot;)
tcp_table:add(&lt;port number&gt;, proto_name)</code></pre><p>The problem occurs in a separate file, where I want to create a Listener to gather some statistics for the protocol. In this file I have</p><pre><code>get_msg_id = Field.new(&quot;foo.msg_id&quot;)
--code below is never reached
--Listener function</code></pre><p>I'm aware that Field objects have to be created outside of the callback functions of dissectors, post-dissectors, heuristic-dissectors, and taps, which is why I did so in my code.</p><p>My questions and concerns are:</p><p>Why are my fields in the Listener file not recognized, when they are clearly recognized in the dissector?</p><p>Are they instantly destroyed after they're used in the dissector?</p><p>Do the Field extractors have to be created in the same file that the Protofields were created in?</p><p>Does the Listener have to be created in the same file as the Dissector for this particular scenario?</p><p>I really appreciate the help and advice!</p><p>Thanks,</p><p>Jeffrey</p></div><div id="question-tags" class="tags-container tags">listener lua dissector fields wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '14, 07:23</strong></p><img src="https://secure.gravatar.com/avatar/e66163b53ebae2cb35d621d806073ea2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jphmiller&#39;s gravatar image" /><p>jphmiller<br />
<span class="score" title="6 reputation points">6</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jphmiller has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Jul '14, 12:22</p></div></div><div id="comments-container-34562" class="comments-container"><span id="34563"></span><div id="comment-34563" class="comment"><div id="post-34563-score" class="comment-score"></div><div class="comment-text"><p>Oh also,</p><p>Wireshark Version 1.10.8 Windows 7</p></div><div id="comment-34563-info" class="comment-info"><span class="comment-age">(10 Jul '14, 07:38)</span> jphmiller</div></div><span id="34584"></span><div id="comment-34584" class="comment"><div id="post-34584-score" class="comment-score"></div><div class="comment-text"><p>I just did some more research, I found that there was a bug [3513] that prevented Field.new from retrieving a previously defined custom fields. The fix was back in October... could anyone give me a confirmation that this fix was back ported to version 1.10.8?</p></div><div id="comment-34584-info" class="comment-info"><span class="comment-age">(10 Jul '14, 14:28)</span> jphmiller</div></div></div><div id="comment-tools-34562" class="comment-tools"></div><div class="clear"></div><div id="comment-34562-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="34565"></span>

<div id="answer-container-34565" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-34565-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Well, first you have this:</p><pre><code>get_msg_id = Field.new(&quot;proto_name.msg_id&quot;)</code></pre><p>...but "<code>proto_name</code>" isn't the string name of your protocol - it's the name of a Lua variable that represents a <code>Proto</code> object. There is no protocol named "<code>proto_name</code>" in your example, but there is one named "<code>foo</code>". So the line should be:</p><pre><code>get_msg_id = Field.new(&quot;foo.msg_id&quot;)</code></pre><p>Also, you need to make sure the file that defines the new protocol (the one with the code at the beginning of your question) is loaded before the file with the <code>Field.new()</code> call.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '14, 09:06</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-34565" class="comments-container"><span id="34570"></span><div id="comment-34570" class="comment"><div id="post-34570-score" class="comment-score"></div><div class="comment-text"><p>I'm sorry I copied line of code incorrectly. I fixed the original post.</p><p>I have: get_msg_id = Field.new("foo.msg_id")</p><p>How is the load priority in \Wireshark\plugins\&lt;version&gt; decided for 2 lua source files?</p><p>I also placed both files in \Wireshark and tried at the bottom of the init.lua</p><p>dofile("dissector.lua")</p><p>dofile("listener.lua")</p><p>and received the same error. I figured Wireshark started with loading init.lua, and so before it did anything else I thought I could load them in here, where I can specify which loads before the other. Perhaps it's not doing what I think it's doing?</p></div><div id="comment-34570-info" class="comment-info"><span class="comment-age">(10 Jul '14, 11:24)</span> jphmiller</div></div><span id="34572"></span><div id="comment-34572" class="comment"><div id="post-34572-score" class="comment-score">1</div><div class="comment-text"><p>Sadly there is no specific order for files loaded from the plugin directory - the code relies on another library function to do it, which is known to not provide any specific ordering guarantee, and might be different on different operating systems or even disk formats.</p><p>Since your two files are not really independent, you could name the first one <code>myproto.lua</code> and the second one <code>myproto.txt</code>, so that wireshark only auto-loads the first one (it only auto-loads files with <code>.lua</code> extension<code>), and then at the bottom of your</code>myproto.lua<code>file call</code>dofile()` using the second file's name to load it. Or just combine the two files into one bigger file.</p></div><div id="comment-34572-info" class="comment-info"><span class="comment-age">(10 Jul '14, 11:44)</span> Hadriel</div></div><span id="34573"></span><div id="comment-34573" class="comment"><div id="post-34573-score" class="comment-score"></div><div class="comment-text"><p>I tried both of those ideas and continued to receive:</p><p>bad argument #1 to 'new' (Field_new: a field with this name must exist)</p><p>Did I not register my protocol fields properly or something?</p></div><div id="comment-34573-info" class="comment-info"><span class="comment-age">(10 Jul '14, 11:53)</span> jphmiller</div></div><span id="34585"></span><div id="comment-34585" class="comment"><div id="post-34585-score" class="comment-score">1</div><div class="comment-text"><p>No you did register them, with this line:</p><pre><code>proto_name.fields = {msg_id, msg_sub_id, msg_size}</code></pre><p>... so long as the <code>Field.new()</code> is after that, it should work.</p><p>Oh... wait a minute... you're on 1.10.8 - try it on 1.12.0 instead. There was a bug that prevented a Lua-created ProtoField from being used by a Lua-based Field. It was fixed late last year, but my guess is not in 1.10.x.</p></div><div id="comment-34585-info" class="comment-info"><span class="comment-age">(10 Jul '14, 14:38)</span> Hadriel</div></div><span id="34597"></span><div id="comment-34597" class="comment"><div id="post-34597-score" class="comment-score"></div><div class="comment-text"><p>Yep, that was it. I installed 1.12.0, plunked everything in and was good to go.</p><p>For anybody experiencing this same problem with the current stable version (1.10.8). The fix for this Field.new() bug (3513) was implemented in 1.11.2. You'll have to upgrade.</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3513">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=3513</a></p></div><div id="comment-34597-info" class="comment-info"><span class="comment-age">(11 Jul '14, 05:31)</span> jphmiller</div></div></div><div id="comment-tools-34565" class="comment-tools"></div><div class="clear"></div><div id="comment-34565-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

