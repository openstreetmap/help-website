+++
type = "question"
title = "Why does my Lua dissector cause Wireshark to consume all memory?"
description = '''My Lua dissector works well if I have only a few packets within a .pcap file. The reassembly is working, and the bytes are as expected once the last PDU is reached. The more packets there are, the faster (and larger) the memory consumption of Wireshark becomes (until it runs out and bails on me). I ...'''
date = "2015-04-01T13:12:00Z"
lastmod = "2015-06-29T09:30:00Z"
weight = 41107
keywords = [ "lua", "dissect", "dissector", "postdissector", "dissection" ]
aliases = [ "/questions/41107" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why does my Lua dissector cause Wireshark to consume all memory?](/questions/41107/why-does-my-lua-dissector-cause-wireshark-to-consume-all-memory)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41107-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41107-score" class="post-score" title="current number of votes">0</div><span id="post-41107-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My Lua dissector works well if I have only a few packets within a .pcap file. The reassembly is working, and the bytes are as expected once the last PDU is reached. The more packets there are, the faster (and larger) the memory consumption of Wireshark becomes (until it runs out and bails on me). I am not a software developer, so please be gentle. Your assistance is appreciated.</p><pre><code>SOMETHING_TCP_PORT = 30003
SOMETHING = Proto(&quot;SOMETHING&quot;,&quot;SOMETHING&quot;)

function SOMETHING.init()
end

function SOMETHING.dissector(buffer, pinfo, tree)
if buffer:len() &gt; 3 then
    if string.upper(tostring(buffer(0, 4))) == &quot;0401F0CE&quot; then
        tvbLength = 20728
    elseif string.upper(tostring(buffer(0, 4))) == &quot;0501F0CE&quot; then
        tvbLength = 12024
    elseif string.upper(tostring(buffer(0, 4))) == &quot;2201F0CE&quot; then
        tvbLength = 7028
    elseif string.upper(tostring(buffer(0, 4))) == &quot;2B01F0CE&quot; then
        tvbLength = 7028
    else
        tvbLength = buffer:len()
    end
end

pinfo.cols.info = &quot;SOMETHING &quot;
pinfo.cols.protocol = &quot;SOMETHING&quot;

local n = pinfo.desegment_offset or 0
while true do
    local nextPDU = n + tvbLength

    if nextPDU &gt; buffer:len() then
        pinfo.desegment_len = nextPDU - buffer:len()
        pinfo.desegment_offset = n
        return
    end

    if string.upper(tostring(buffer(n, 4))) == &quot;2201F0CE&quot; or string.upper(tostring(buffer(n, 4))) == &quot;2B01F0CE&quot; then
        if string.upper(tostring(buffer(n, 4))) == &quot;2201F0CE&quot; then
            pinfo.cols.info:append(&quot;- Some Message &quot;)

            subtree = tree:add(SOMETHING, buffer(), &quot;SOMETHING - Some Message&quot;)

            subtree:add(buffer(n, 4), &quot;Found - &quot; .. string.upper(tostring(buffer(n, 4))))
            n = n + 4
        elseif string.upper(tostring(buffer(n, 4))) == &quot;2B01F0CE&quot; then
            pinfo.cols.info:append(&quot;- Some Other Message &quot;)

            subtree = tree:add(SOMETHING, buffer(), &quot;SOMETHING - Some Message&quot;)

            subtree:add(buffer(n, 4), &quot;Found - &quot; .. string.upper(tostring(buffer(n, 4))))
            n = n + 4
        else
            return
        end

        subtree:add(buffer(n, 4), &quot;  Message size = &quot; .. buffer(n, 4):le_uint() .. &quot; bytes&quot;)
        if buffer(n, 4):le_uint() ~= 7028 then
            subtree:add(buffer(n, 4), &quot;  Message size is incorrect!&quot;)
        end
        n = n + 4

        -- DECODE HERE

        n = nextPDU
        if nextPDU == buffer:len() then
            return
        end
    end

    if string.upper(tostring(buffer(n, 4))) == &quot;0401F0CE&quot; then
        pinfo.cols.info:append(&quot;- Some Message &quot;)

        subtree = tree:add(SOMETHING, buffer(), &quot;SOMETHING - Some Message&quot;)

        subtree:add(buffer(n, 4), &quot;Found - &quot; .. string.upper(tostring(buffer(n, 4))))
        n = n + 4

        subtree:add(buffer(n, 4), &quot;  Message size = &quot; .. buffer(n, 4):le_uint() .. &quot; bytes&quot;)
        if buffer(n, 4):le_uint() ~= 20728 then
            subtree:add(buffer(n, 4), &quot;  Message size is incorrect!&quot;)
        end
        n = n + 4

        -- DECODE HERE

        n = nextPDU
        if nextPDU == buffer:len() then
            return
        end
    end

    if string.upper(tostring(buffer(n, 4))) == &quot;0501F0CE&quot; then
        pinfo.cols.info:append(&quot;- Some Message &quot;)

        subtree = tree:add(SOMETHING, buffer(), &quot;SOMETHING - Some Message&quot;)

        subtree:add(buffer(n, 4), &quot;Found - &quot; .. string.upper(tostring(buffer(n, 4))))
        n = n + 4

        subtree:add(buffer(n, 4), &quot;  Message size = &quot; .. buffer(n, 4):le_uint() .. &quot; bytes&quot;)
        if buffer(n, 4):le_uint() ~= 12024 then
            subtree:add(buffer(n, 4), &quot;  Message size is incorrect!&quot;)
        end
        n = n + 4

        -- DECODE HERE

        n = nextPDU
        if nextPDU == buffer:len() then
            return
        end
    end
end
end

tcp_table = DissectorTable.get(&quot;tcp.port&quot;)

tcp_table:add(SOMETHING_TCP_PORT,SOMETHING)</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissect" rel="tag" title="see questions tagged &#39;dissect&#39;">dissect</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-postdissector" rel="tag" title="see questions tagged &#39;postdissector&#39;">postdissector</span> <span class="post-tag tag-link-dissection" rel="tag" title="see questions tagged &#39;dissection&#39;">dissection</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Apr '15, 13:12</strong></p><img src="https://secure.gravatar.com/avatar/84cb87876efe350a7f4440f98807d344?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JustSomeNoob&#39;s gravatar image" /><p><span>JustSomeNoob</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JustSomeNoob has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Apr '15, 13:13</strong> </span></p></div></div><div id="comments-container-41107" class="comments-container"></div><div id="comment-tools-41107" class="comment-tools"></div><div class="clear"></div><div id="comment-41107-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43672"></span>

<div id="answer-container-43672" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43672-score" class="post-score" title="current number of votes">0</div><span id="post-43672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I believe what's happening is wireshark is getting stuck in your while-loop, and never returning from it. This can happen because in certain cases your code will never have <code>nextPDU</code> be greater than <code>buffer:len()</code>. For example, if your dissector sees a TCP segment that has the first 4 bytes <strong>not</strong> match one of the hex strings you expect to see, then it will set <code>tvbLength = buffer:len()</code>, enter the while-loop with the variable <code>n</code> equal to <code>0</code>, and thus have a <code>nextPDU</code> equal to <code>buffer:len()</code>... but that's <em>equal-to</em>, not <em>greater-than</em>, so the while loop won't return... <strong>ever</strong>. And since the if-then statements within the while loop allocate memory (by creating multiple <code>TvbRange</code>s), the memory usage will keep growing and growing.</p><p>So you're going to have to change your code logic to prevent being stuck in that while-loop forever. Like for example verify the <code>nextPDU</code> value changes on each loop, or something.</p><hr /><p>Also, your code is fairly inefficient - it creates a bunch of <code>TvbRange</code> objects and Lua strings multiple times instead of once.</p><p>For example, at the top of the dissector function:</p><pre><code>if buffer:len() &gt; 3 then
    if string.upper(tostring(buffer(0, 4))) == &quot;0401F0CE&quot; then
        tvbLength = 20728
    elseif string.upper(tostring(buffer(0, 4))) == &quot;0501F0CE&quot; then
        tvbLength = 12024
    elseif string.upper(tostring(buffer(0, 4))) == &quot;2201F0CE&quot; then
        tvbLength = 7028
    elseif string.upper(tostring(buffer(0, 4))) == &quot;2B01F0CE&quot; then
        tvbLength = 7028
    else
        tvbLength = buffer:len()
    end
end</code></pre><p>There are three things in that if-then block that cause memory to be allocated:</p><ol><li><code>buffer(0,4)</code> creates a <code>TvbRange</code> object in C-code and Lua.</li><li><code>tostring()</code> of the <code>TvbRange</code> creates a string in Lua.</li><li><code>string.upper()</code> creates another string in Lua.</li></ol><p>You call those three things up to four times in the above if-then block, depending on whether the <code>elseif</code> clauses get executed. For numbers 2 and 3 above, they will only create one string each in Lua for all four if/elseif clauses because they result in the same string and Lua internally only stores one copy of a given string; but still it's extra processing that isn't necessary. Instead, you should do this:</p><pre><code>if buffer:len() &gt; 3 then
    local msgType = string.upper(tostring(buffer(0, 4)))
    if msgType == &quot;0401F0CE&quot; then
        tvbLength = 20728
    elseif msgType == &quot;0501F0CE&quot; then
        tvbLength = 12024
    elseif msgType == &quot;2201F0CE&quot; then
        tvbLength = 7028
    elseif msgType == &quot;2B01F0CE&quot; then
        tvbLength = 7028
    else
        tvbLength = buffer:len()
    end
end</code></pre><p>That both reduces the memory allocated, and improves performance.</p><p>By the way, what if <code>buffer:len()</code> is <strong>not</strong> greater than 3? Then <code>tvbLength</code> isn't set to anything.</p><hr /><p>Next you have this:</p><pre><code>    if string.upper(tostring(buffer(n, 4))) == &quot;2201F0CE&quot; or string.upper(tostring(buffer(n, 4))) == &quot;2B01F0CE&quot; then
        if string.upper(tostring(buffer(n, 4))) == &quot;2201F0CE&quot; then
            pinfo.cols.info:append(&quot;- Some Message &quot;)

            subtree = tree:add(SOMETHING, buffer(), &quot;SOMETHING - Some Message&quot;)

            subtree:add(buffer(n, 4), &quot;Found - &quot; .. string.upper(tostring(buffer(n, 4))))
            n = n + 4
        elseif string.upper(tostring(buffer(n, 4))) == &quot;2B01F0CE&quot; then
            pinfo.cols.info:append(&quot;- Some Other Message &quot;)

            subtree = tree:add(SOMETHING, buffer(), &quot;SOMETHING - Some Message&quot;)

            subtree:add(buffer(n, 4), &quot;Found - &quot; .. string.upper(tostring(buffer(n, 4))))
            n = n + 4
        else
            return
        end

        subtree:add(buffer(n, 4), &quot;  Message size = &quot; .. buffer(n, 4):le_uint() .. &quot; bytes&quot;)
        if buffer(n, 4):le_uint() ~= 7028 then
            subtree:add(buffer(n, 4), &quot;  Message size is incorrect!&quot;)
        end
        n = n + 4

        -- DECODE HERE

        n = nextPDU
        if nextPDU == buffer:len() then
            return
        end
    end</code></pre><p>Again, you're creating multiple <code>TvbRange</code> objects and strings for them and so on, even though they're identical. So instead do this:</p><pre><code>    local msgTypeBuf = buffer(n, 4)
    local msgType = string.upper(tostring(msgTypeBuf))
    if msgType == &quot;2201F0CE&quot; or msgType == &quot;2B01F0CE&quot; then
        if msgType == &quot;2201F0CE&quot; then
            pinfo.cols.info:append(&quot;- Some Message &quot;)

            subtree = tree:add(SOMETHING, buffer(), &quot;SOMETHING - Some Message&quot;)

            subtree:add(msgTypeBuf, &quot;Found - &quot; .. msgType)
            n = n + 4
        elseif msgType == &quot;2B01F0CE&quot; then
            pinfo.cols.info:append(&quot;- Some Other Message &quot;)

            subtree = tree:add(SOMETHING, buffer(), &quot;SOMETHING - Some Message&quot;)

            subtree:add(msgTypeBuf, &quot;Found - &quot; .. msgType)
            n = n + 4
        else
            return
        end

        local msgLengthBuf = buffer(n, 4)
        local msgLength = msgLengthBuf:le_uint()
        subtree:add(msgLengthBuf, &quot;  Message size = &quot; .. msgLength .. &quot; bytes&quot;)
        if msgLength ~= 7028 then
            subtree:add(msgLengthBuf, &quot;  Message size is incorrect!&quot;)
        end
        n = n + 4

        -- DECODE HERE

        n = nextPDU
        if nextPDU == buflen then
            return
        end
    end</code></pre><p>And similarly in the later if-then statements.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '15, 09:30</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43672" class="comments-container"></div><div id="comment-tools-43672" class="comment-tools"></div><div class="clear"></div><div id="comment-43672-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

