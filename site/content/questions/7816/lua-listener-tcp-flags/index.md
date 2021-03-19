+++
type = "question"
title = "Lua Listener - TCP flags"
description = '''I&#x27;ve written a small Lua Listener.  I wish to visit every TCP packet received.  Here&#x27;s how I declare the tap:  local tap = Listener.new(&quot;tcp&quot;)  And here&#x27;s how I try to take the flags state.    if (tcp.flags) then  Within the tcp.packet method.  The code does not work as I expect it to work. I want t...'''
date = "2011-12-07T03:18:00Z"
lastmod = "2011-12-07T05:58:00Z"
weight = 7816
keywords = [ "lua" ]
aliases = [ "/questions/7816" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Lua Listener - TCP flags](/questions/7816/lua-listener-tcp-flags)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7816-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7816-score" class="post-score" title="current number of votes">0</div><span id="post-7816-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've written a small Lua Listener.<br />
I wish to visit every TCP packet received.<br />
Here's how I declare the tap:</p><pre><code>    local tap = Listener.new(&quot;tcp&quot;)</code></pre><p>And here's how I try to take the flags state.<br />
</p><pre><code>    if (tcp.flags) then</code></pre><p>Within the tcp.packet method.<br />
The code does not work as I expect it to work. I want to be able to grab to TCP flags state.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Dec '11, 03:18</strong></p><img src="https://secure.gravatar.com/avatar/920a90d8a3dca941060cc1e39cc76346?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trevor&#39;s gravatar image" /><p><span>Trevor</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trevor has no accepted answers">0%</span> </br></br></p></div></div><div id="comments-container-7816" class="comments-container"></div><div id="comment-tools-7816" class="comment-tools"></div><div class="clear"></div><div id="comment-7816-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7817"></span>

<div id="answer-container-7817" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7817-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7817-score" class="post-score" title="current number of votes">2</div><span id="post-7817-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Trevor has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First, you need to declare a <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Field.html#lua_class_Field"><code>Field</code></a> that extracts <code>tcp.flags</code> from the current packet. Then, you call the <code>Field</code> object within <code>tap.packet()</code> to get the <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Field.html#lua_class_FieldInfo"><code>FieldInfo</code></a> object that contains the value of the flags (as shown in the Lua below, tested in Wireshark 1.7.0).</p><pre><code>-- There are two arguments to `Listener.new`; you were missing
-- the first arg in your question.
local tap = Listener.new(nil, &quot;tcp&quot;)

-- Declare a `Field` to extract `tcp.flags`. This must be done
-- outside of `tap.packet`.
local f_flags = Field.new(&quot;tcp.flags&quot;)

-- Packet handler
local function tap.packet(pinfo, buf)
    -- When called, the `f_flags` field extracts `tcp.flags` from
    -- the current packet and returns a `FieldInfo` object.
    local f = f_flags()
    if f then
        print(string.format(&quot;tcp.flags = %#x&quot;, f.value))
    end
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Dec '11, 04:40</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div></div><div id="comments-container-7817" class="comments-container"><span id="7819"></span><div id="comment-7819" class="comment"><div id="post-7819-score" class="comment-score"></div><div class="comment-text"><p>Wow - you really gave a lot - beyond the obvious immediate solution. I just did not know how to properly work with Lua scripting in WS. Many many thanks Helloworld :) !</p></div><div id="comment-7819-info" class="comment-info"><span class="comment-age">(07 Dec '11, 05:58)</span> <span class="comment-user userinfo">Trevor</span></div></div></div><div id="comment-tools-7817" class="comment-tools"></div><div class="clear"></div><div id="comment-7817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

