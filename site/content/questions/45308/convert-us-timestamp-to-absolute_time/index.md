+++
type = "question"
title = "Convert us-timestamp to absolute_time"
description = '''Hi there, I am currently implementing a dissector in lua and I&#x27;m stuck with converting my microsecond timestamp to absolute_time. This is what I&#x27;m currenly doing: local pl_timestamp = ProtoField.absolute_time(&#x27;xxx.timestamp&#x27;, &#x27;Timestamp&#x27;, base.LOCAL) ...  local tmp1 = (buffer(0,8):le_uint64()) * 100...'''
date = "2015-08-22T05:20:00Z"
lastmod = "2015-08-22T07:37:00Z"
weight = 45308
keywords = [ "absolute_time", "lua", "absolute", "time", "wireshark" ]
aliases = [ "/questions/45308" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Convert us-timestamp to absolute\_time](/questions/45308/convert-us-timestamp-to-absolute_time)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45308-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,</p><p>I am currently implementing a dissector in lua and I'm stuck with converting my microsecond timestamp to absolute_time. This is what I'm currenly doing:</p><pre><code>local pl_timestamp = ProtoField.absolute_time(&#39;xxx.timestamp&#39;, &#39;Timestamp&#39;, base.LOCAL)
...      
local tmp1 = (buffer(0,8):le_uint64()) * 1000
local tmp2 = tmp1:tohex()
local tvb = ByteArray.new(tmp2):tvb(&quot;Time&quot;)
subtree:add(pl_timestamp, tvb(0,8))</code></pre><p>I also tried it with a fixed time that I'm sure is correct:</p><pre><code>local tvb = ByteArray.new(&quot;13FCC7343B5EA000&quot;):tvb(&quot;Time&quot;)</code></pre><p>At the output I get a completely wrong date. I guess the absolute_time is a ns-timestamp counting the ns since 1.1.1970 1:00:00 right? Anybody an idea what I'm doing wrong here?</p><p>I'm greatful for every advise. Enno</p></div><div id="question-tags" class="tags-container tags">absolute_time lua absolute time wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Aug '15, 05:20</strong></p><img src="https://secure.gravatar.com/avatar/e0a83cd3b1bd17b3f4b28e396c496e31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="enno&#39;s gravatar image" /><p>enno<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="enno has no accepted answers">0%</span></p></div></div><div id="comments-container-45308" class="comments-container"><span id="45309"></span><div id="comment-45309" class="comment"><div id="post-45309-score" class="comment-score"></div><div class="comment-text"><p>Using <code>local tvb = ByteArray.new("13FCC7343B5EA000"):tvb("Time")</code> I get Aug 17, 1980 - which according to <a href="http://www.epochconverter.com">epochconverter.com</a> is correct.</p><p>What is it you expect it to be, and why?</p></div><div id="comment-45309-info" class="comment-info"><span class="comment-age">(22 Aug '15, 06:37)</span> Hadriel</div></div><span id="45310"></span><div id="comment-45310" class="comment"><div id="post-45310-score" class="comment-score"></div><div class="comment-text"><p>Oh, and why are you getting the buffer's bytes, multiplying times a 1000, converting to hex, creating a new Tvb, and then using that new Tvb for the time?</p></div><div id="comment-45310-info" class="comment-info"><span class="comment-age">(22 Aug '15, 06:46)</span> Hadriel</div></div><span id="45311"></span><div id="comment-45311" class="comment"><div id="post-45311-score" class="comment-score"></div><div class="comment-text"><p>Ahh, I kind of missed the first sentence, where you want to convert microseconds "timestamp" to ns-timestamp. I see what you're missing - I'll put it in an answer.</p></div><div id="comment-45311-info" class="comment-info"><span class="comment-age">(22 Aug '15, 07:11)</span> Hadriel</div></div></div><div id="comment-tools-45308" class="comment-tools"></div><div class="clear"></div><div id="comment-45308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="45312"></span>

<div id="answer-container-45312" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-45312-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your code's logic, and your statement about "<code>13FCC7343B5EA000</code>" not giving you the result you expect, makes me think you expect the absolute_time to be a number - the number of nanoseconds since the Unix epoch (January 1, 1970, midnight UTC). It isn't. It's <strong>two</strong> numbers: the number of seconds, and the number of nanoseconds portion of a second. When decoded from a <code>Tvb</code>, wireshark expects the first 4 bytes of the given <code>TvbRange</code> to be the seconds, and the second 4 bytes to be the nanoseconds portion.</p><p>Thus a manufactured <code>Tvb</code> of the hex string "13FCC7343B5EA000" is 0x13FCC734 seconds, and 0x3B5EA000 nanoseconds. 0x13FCC734 seconds is 335333172 in decimal, and in Epoch time is Aug 17, 1980. What you probably expected was that the whole hex string became a single number (decimal of 1440245008000000000) representing the number of nanoseconds since the Epoch, which would be Aug 22, 2015.</p><p>If your packet's <code>Tvb</code> buffer contains just a single big number, for the number of microseconds since the Epoch, then you can convert it like so:</p><pre><code>-- returns a UInt64 object of the microseconds in the Tvb buffer
local usecs = buffer(0,8):le_uint64()
-- gets the seconds as a Lua number
local secs  = (usecs / 1000000):tonumber()
-- gets the remainder as a Lua number, in nanoseconds
local nsecs = (usecs % 1000000):tonumber() * 1000

-- create a NSTime object using the above
local nstime = NSTime.new(secs, nsecs)

-- add it to the tree, highlighting the real buffer&#39;s bytes, but with the real NSTime value
subtree:add(pl_timestamp, buffer(0,8), nstime)</code></pre><p>Note: I haven't tested the above, but it should (hopefully) work.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Aug '15, 07:37</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-45312" class="comments-container"><span id="45313"></span><div id="comment-45313" class="comment"><div id="post-45313-score" class="comment-score"></div><div class="comment-text"><p>Works! Thank you very much! Perfect and very fast support!</p></div><div id="comment-45313-info" class="comment-info"><span class="comment-age">(22 Aug '15, 08:22)</span> enno</div></div></div><div id="comment-tools-45312" class="comment-tools"></div><div class="clear"></div><div id="comment-45312-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

