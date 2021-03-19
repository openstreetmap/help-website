+++
type = "question"
title = "fetching multiple named values with lua"
description = '''In working on a lua extension, I want to be able to extract multiple instances of a field within a single packet. For example, in DNS, it&#x27;s not uncommon to have multiple responses to a query. As an example, in this dns capture file, there are multiple responses in packets 4, 24 and 29. What I would ...'''
date = "2011-01-01T16:50:00Z"
lastmod = "2011-01-02T06:04:00Z"
weight = 1579
keywords = [ "lua" ]
aliases = [ "/questions/1579" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [fetching multiple named values with lua](/questions/1579/fetching-multiple-named-values-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1579-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In working on a lua extension, I want to be able to extract multiple instances of a field within a single packet. For example, in DNS, it's not uncommon to have multiple responses to a query. As an example, in <a href="http://wiki.wireshark.org/SampleCaptures?action=AttachFile&amp;do=get&amp;target=dns.cap">this dns capture file</a>, there are multiple responses in packets 4, 24 and 29. What I would like to do is get <strong>all</strong> instances of a field such as <em>dns.resp.name</em> for those packets using lua. Here is what I have so far:</p><pre><code>-- dns.lua
-- example of a tap that shows DNS answers when there are more than one returned

dns_tap = Listener.new(nil, &quot;dns.count.answers &gt; 1&quot;)
msg = &quot;&quot;
count = Field.new(&quot;dns.count.answers&quot;)
dns_name = Field.new(&quot;dns.resp.name&quot;)
bad = true

function dns_tap.packet(pinfo)
    msg = &quot;Packet &quot; .. pinfo.number .. &quot; had &quot; .. tostring(count()) .. &quot; answers.&quot;
    debug(msg)
    if bad then
        for xx in dns_name() do
        debug(xx)
        end
    end
end</code></pre><p>However, this doesn't work. If invoked with this command line:</p><p><code>tshark -X lua_script:dns.lua -r dns.cap &gt; out.txt</code></p><p>all I get is the first dns_name infinitely repeated until I halt the program. What I want is just the finite list of actual answers. I am the using very latest SVN version (version 35289 from /trunk) on Windows, but I get the same result on Linux.</p></div><div id="question-tags" class="tags-container tags">lua</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jan '11, 16:50</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p>beroset<br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span></p></div></div><div id="comments-container-1579" class="comments-container"></div><div id="comment-tools-1579" class="comment-tools"></div><div class="clear"></div><div id="comment-1579-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1585"></span>

<div id="answer-container-1585" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1585-score" class="post-score" title="current number of votes">3</div></div></td><td><div class="item-right"><div class="answer-body"><p>OK, I finally got it. The key is that if there may be multiple values, one must use a lua table as <code>{ dns_name() }</code> instead of the singular <code>dns_name()</code>.</p><p>The working version of this code sample is this:</p><pre><code>-- dns.lua
-- example of a tap that shows DNS answers when there are more than one returned
dns_tap = Listener.new(nil, &quot;dns.count.answers &gt; 1&quot;)
msg = &quot;&quot;
count = Field.new(&quot;dns.count.answers&quot;)
dns_name = Field.new(&quot;dns.resp.name&quot;)
function dns_tap.packet(pinfo)
    msg = &quot;Packet &quot; .. pinfo.number .. &quot; had &quot; .. tostring(count()) .. &quot; answers.&quot;
    debug(msg)
    local answers = {dns_name()}  -- this is how to do it
    for i in pairs(answers) do    -- iterate through all of the values returned
       debug(answers[i])
    end
end</code></pre>There may some merit in adding a bit more text to the auto-generated documentation to make this point clearer. I'll look into doing that.</div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '11, 06:04</strong></p><img src="https://secure.gravatar.com/avatar/6f579677517345ebea1cfef9e9e88f0c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="beroset&#39;s gravatar image" /><p>beroset<br />
<span class="score" title="226 reputation points">226</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="beroset has 4 accepted answers">33%</span></p></div></div><div id="comments-container-1585" class="comments-container"></div><div id="comment-tools-1585" class="comment-tools"></div><div class="clear"></div><div id="comment-1585-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

