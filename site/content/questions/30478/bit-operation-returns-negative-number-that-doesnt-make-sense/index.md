+++
type = "question"
title = "bit operation returns negative number that doesn&#x27;t make sense"
description = '''Hi, This may be a pure Lua question (I&#x27;m using Lua to write a dissector). I haven&#x27;t got any responses from the Lua forum so I&#x27;m here for help.  I have this line of code using bit op which is embedded in the Wireshark Lua tool. This is a regular bitwise and operation, not the 64bit version. a = bit.b...'''
date = "2014-03-06T09:03:00Z"
lastmod = "2014-03-06T20:20:00Z"
weight = 30478
keywords = [ "lua", "negative", "bit_op" ]
aliases = [ "/questions/30478" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [bit operation returns negative number that doesn't make sense](/questions/30478/bit-operation-returns-negative-number-that-doesnt-make-sense)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30478-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30478-score" class="post-score" title="current number of votes">0</div><span id="post-30478-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>This may be a pure Lua question (I'm using Lua to write a dissector). I haven't got any responses from the Lua forum so I'm here for help.<br />
</p><p>I have this line of code using bit op which is embedded in the Wireshark Lua tool. This is a regular bitwise and operation, not the 64bit version.</p><p>a = bit.band(0xb5ffffff, 0xffffffff) It returns: -1241513985.</p><p>How come? It should return the first argument, in decimal, which is 3053453311.</p><p>What's going on?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-negative" rel="tag" title="see questions tagged &#39;negative&#39;">negative</span> <span class="post-tag tag-link-bit_op" rel="tag" title="see questions tagged &#39;bit_op&#39;">bit_op</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Mar '14, 09:03</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>06 Mar '14, 09:50</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-30478" class="comments-container"></div><div id="comment-tools-30478" class="comment-tools"></div><div class="clear"></div><div id="comment-30478-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30481"></span>

<div id="answer-container-30481" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30481-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30481-score" class="post-score" title="current number of votes">2</div><span id="post-30481-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark's bitop library is based on Mike Pall's bitop library (see <a href="http://bitop.luajit.org">here</a>). As described in the <a href="http://bitop.luajit.org/semantics.html">semantics page</a> of the documentation, in the fifth bullet point about ranges:</p><ul><li>But the Lua number type must be signed and may be limited to 32 bits. Defining the result type as an unsigned number would not be cross-platform safe. All bit operations are thus defined to <strong>return results in the range of signed 32 bit numbers</strong> (converted to the Lua number type).</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '14, 09:44</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30481" class="comments-container"><span id="30482"></span><div id="comment-30482" class="comment"><div id="post-30482-score" class="comment-score"></div><div class="comment-text"><p>BTW, yeah I know that's weird - I understand why it was done that way in the generic bitop library... but for Wireshark since we know we use doubles for our Lua numbers we could have changed that behavior. But I wasn't the one who imported that library, and it's been in wireshark for a long time it seems, so changing its behavior isn't safe (in theory).</p></div><div id="comment-30482-info" class="comment-info"><span class="comment-age">(06 Mar '14, 09:49)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30488"></span><div id="comment-30488" class="comment"><div id="post-30488-score" class="comment-score"></div><div class="comment-text"><p>Oh, thanks.<br />
Since at this stage I'm just interested in the bit manipulation and don't need the value, I can just leave everything as is. Later on when I do need the value, I can do a 2's complement if the first bit of the value is 1. As a matter of fact, I was planning to use Struct pack() and unpack() to convert unsigned numbers to signed numbers after I do the bit operations. If the bit operations are already interpreting my numbers as signed, then I don't need to do the conversion using Struct? Or I should still do it since the struct conversion is more universal, especially the system independent in/In options?</p></div><div id="comment-30488-info" class="comment-info"><span class="comment-age">(06 Mar '14, 11:44)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="30493"></span><div id="comment-30493" class="comment"><div id="post-30493-score" class="comment-score"></div><div class="comment-text"><p>Well that's a new question, so a new ask.wireshark.org topic. :)</p></div><div id="comment-30493-info" class="comment-info"><span class="comment-age">(06 Mar '14, 13:09)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30495"></span><div id="comment-30495" class="comment"><div id="post-30495-score" class="comment-score"></div><div class="comment-text"><p>I kind of figured out my own answer. Just do the bit operations and then use the Struct pack() and unpack() to convert to signed numbers if I need to. This way I don't have to worry about checking MSB or calculate two's complement.</p></div><div id="comment-30495-info" class="comment-info"><span class="comment-age">(06 Mar '14, 13:11)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="30500"></span><div id="comment-30500" class="comment"><div id="post-30500-score" class="comment-score"></div><div class="comment-text"><p>But why go to all the trouble? Why not just do:</p><pre><code>local function unsign(n)
    if n &lt; 0 then
        n = 4294967296 + n
    end
    return n
end

local a = unsign( bit.band(0xb5ffffff, 0xffffffff) )
...</code></pre><p>Won't that do it? (I haven't tried, but it looks right, though it's late at night where I am right now...)</p></div><div id="comment-30500-info" class="comment-info"><span class="comment-age">(06 Mar '14, 13:30)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30517"></span><div id="comment-30517" class="comment not_top_scorer"><div id="post-30517-score" class="comment-score"></div><div class="comment-text"><p>Because I have a lot of different values that need different conversions based on each one's requirement. Some may be from unsigned to signed, some from Big Endian to Little Endian, and some from long long to double. With pack, unpack functions I can treat them all with the same two steps and simply pass the format dynamically.</p></div><div id="comment-30517-info" class="comment-info"><span class="comment-age">(06 Mar '14, 20:20)</span> <span class="comment-user userinfo">YXI</span></div></div></div><div id="comment-tools-30481" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-30481-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30479"></span>

<div id="answer-container-30479" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30479-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30479-score" class="post-score" title="current number of votes">0</div><span id="post-30479-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There's a conversion to signed going on somewhere. A 32 bit signed value of -1241513985 is represented by 0xb5ffffff. I don't know Lua so can't help you any further.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Mar '14, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Mar '14, 09:13</strong> </span></p></div></div><div id="comments-container-30479" class="comments-container"></div><div id="comment-tools-30479" class="comment-tools"></div><div class="clear"></div><div id="comment-30479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

