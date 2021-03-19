+++
type = "question"
title = "bad argument #1 to &#x27;get_index&#x27; (index out of range) in Wireshark Lua dissector"
description = '''In my dissector I have this code local defaultdata = data_tvb():bytes() local newdata = ByteArray.new() newdata:set_size(defaultdata:len()) for i=0,defaultdata:len()-2 do  local var = bit.band((bit.lshift(defaultdata:get_index(i), 1) + bit.rshift(defaultdata:get_index(i+1), 7)), 0xff) newdata:set_in...'''
date = "2014-02-13T02:00:00Z"
lastmod = "2014-02-14T02:03:00Z"
weight = 29825
keywords = [ "lua", "dissector", "sub-dissector" ]
aliases = [ "/questions/29825" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [bad argument \#1 to 'get\_index' (index out of range) in Wireshark Lua dissector](/questions/29825/bad-argument-1-to-get_index-index-out-of-range-in-wireshark-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29825-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In my dissector I have this code</p><pre><code>local defaultdata = data_tvb():bytes()
local newdata = ByteArray.new()
newdata:set_size(defaultdata:len())
for i=0,defaultdata:len()-2 do 
local var = bit.band((bit.lshift(defaultdata:get_index(i), 1) + bit.rshift(defaultdata:get_index(i+1), 7)), 0xff)
newdata:set_index(i, var) end
local var = bit.band((bit.lshift(defaultdata:get_index(defaultdata:len()-1), 1) + bit.rshift(defaultdata:get_index(0), 7)), 0xff)
newdata:set_index(defaultdata:len()-1,var)
data_tvb = ByteArray.tvb(newdata, &quot;Decoded&quot;) end</code></pre><p>My problem is in second bitwise operation in <code>get_index</code> function.</p><p>I know, that problem might be in <code>get_index(0)</code> or <code>get_index(defaultdata:len()-1)</code> because in Lua there is no element of the zero index(not that of C) but nothing actually works with another values.</p><p>With any values I got this message: <code>bad argument #1 to 'get_index' (index out of range)</code> So, as I mentioned above, part, that not depend on this code work correctly.</p></div><div id="question-tags" class="tags-container tags">lua dissector sub-dissector</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Feb '14, 02:00</strong></p><img src="https://secure.gravatar.com/avatar/17ecc8e7661ef2ed3fd682730cd6f7a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="im_infamous&#39;s gravatar image" /><p>im_infamous<br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="im_infamous has one accepted answer">100%</span></p></div></div><div id="comments-container-29825" class="comments-container"></div><div id="comment-tools-29825" class="comment-tools"></div><div class="clear"></div><div id="comment-29825-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="29862"></span>

<div id="answer-container-29862" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29862-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Problem solved. The matter is that my dissector don't cover cases of null application protocol payload, and thats why i got these errors. The solution is to add one "if" statement, that checks out length of the payload. Hadriel, thank you very much for your help.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Feb '14, 02:03</strong></p><img src="https://secure.gravatar.com/avatar/17ecc8e7661ef2ed3fd682730cd6f7a6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="im_infamous&#39;s gravatar image" /><p>im_infamous<br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="im_infamous has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 14 Feb '14, 02:07</p></div></div><div id="comments-container-29862" class="comments-container"></div><div id="comment-tools-29862" class="comment-tools"></div><div class="clear"></div><div id="comment-29862-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="29834"></span>

<div id="answer-container-29834" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-29834-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>ByteArray:set_index() and get_index() actually use 0-based indexing, not normal Lua 1-based indexing. The only time you should see that "index out of range" error is if the index number you used in ByteArray:get_index() was either negative, or it's greater than or equal to the length of the Byte Array. Which exact line in that code snippet is causing you the error? Also, just to be clear, your code snippet is this, right?:</p><pre><code>    local defaultdata = data_tvb():bytes()
    local newdata = ByteArray.new()
    newdata:set_size(defaultdata:len())
    for i=0,defaultdata:len()-2 do 
        local var = bit.band((bit.lshift(defaultdata:get_index(i), 1) + bit.rshift(defaultdata:get_index(i+1), 7)), 0xff)
        newdata:set_index(i, var) 
    end
    local var = bit.band((bit.lshift(defaultdata:get_index(defaultdata:len()-1), 1) + bit.rshift(defaultdata:get_index(0), 7)), 0xff)
    newdata:set_index(defaultdata:len()-1,var)
    data_tvb = ByteArray.tvb(newdata, &quot;Decoded&quot;)
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Feb '14, 10:02</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-29834" class="comments-container"><span id="29835"></span><div id="comment-29835" class="comment"><div id="post-29835-score" class="comment-score"></div><div class="comment-text"><p>Thanks for your reply! Yep, we are talking about that snippet. The error now is in the second line and sounds like "attempt to index ByteArray global (a nil value)"</p></div><div id="comment-29835-info" class="comment-info"><span class="comment-age">(13 Feb '14, 10:38)</span> im_infamous</div></div><span id="29836"></span><div id="comment-29836" class="comment"><div id="post-29836-score" class="comment-score"></div><div class="comment-text"><p>What wireshark version/release are you using?</p></div><div id="comment-29836-info" class="comment-info"><span class="comment-age">(13 Feb '14, 11:10)</span> Hadriel</div></div><span id="29852"></span><div id="comment-29852" class="comment"><div id="post-29852-score" class="comment-score"></div><div class="comment-text"><p>Im using wireshark portable 1.8.2</p></div><div id="comment-29852-info" class="comment-info"><span class="comment-age">(13 Feb '14, 20:55)</span> im_infamous</div></div><span id="29855"></span><div id="comment-29855" class="comment not_top_scorer"><div id="post-29855-score" class="comment-score"></div><div class="comment-text"><p>When evaluating lua in wireshark, I got message "bad argument #1 to 'get index' (index out of range) and when it comes to lua executor "attempt to index global ByteArray(a nil value)"</p></div><div id="comment-29855-info" class="comment-info"><span class="comment-age">(13 Feb '14, 22:59)</span> im_infamous</div></div><span id="29856"></span><div id="comment-29856" class="comment"><div id="post-29856-score" class="comment-score">1</div><div class="comment-text"><p>Oh, you were trying this in just the stand-alone lua interpreter? (i.e. outside of wireshark) Then yes, of course it would give that "a nil value" error. That error is telling you there's no global variable named "ByteArray", and thus no table to try calling "ByteArray.new()" on. There is no such global variable in that, because ByteArray is a table created by Wireshark, not something Lua comes with. That's why I was asking what version you were running, because it didn't make sense that it couldn't find a ByteArry table - but if you got that error when you were just running the Lua interpreter by itself, then sure it won't work. As for the other error - the "index out of range" one, I'll look into the 1.8.2 code but basically it means what I had said: the index number you're giving it is either negative or greater than or equal to the length of the byte array.</p></div><div id="comment-29856-info" class="comment-info"><span class="comment-age">(14 Feb '14, 00:34)</span> Hadriel</div></div><span id="29858"></span><div id="comment-29858" class="comment"><div id="post-29858-score" class="comment-score">1</div><div class="comment-text"><p>Is it possible the Tvb only had one or zero bytes in it? In other words, your call to 'data_tvb():bytes()', which returns a ByteArray from the Tvb - could it just be only one byte? If so, your for-loop will get messed up and be trying to get_index() too large a number.<br />
</p><p>Regardless, try putting some print() statements in the code to see what the values of those things are. Like 'print("len="..defaultdata:len())'</p></div><div id="comment-29858-info" class="comment-info"><span class="comment-age">(14 Feb '14, 00:49)</span> Hadriel</div></div></div><div id="comment-tools-29834" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-29834-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

