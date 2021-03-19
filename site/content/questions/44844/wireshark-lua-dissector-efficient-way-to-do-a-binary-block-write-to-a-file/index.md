+++
type = "question"
title = "wireshark lua dissector -- efficient way to do a binary block write to a file?"
description = '''I am writing a lua dissector for a propietary protocol. The packets include bytes of embedded .png images that are contained in a tvb (buffer) object that I need to write to a .png file. In order to successfully write them to a file, below are couple of ways attempted. Both required &quot;walking through...'''
date = "2015-08-04T19:02:00Z"
lastmod = "2015-08-05T14:38:00Z"
weight = 44844
keywords = [ "lua" ]
aliases = [ "/questions/44844" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [wireshark lua dissector -- efficient way to do a binary block write to a file?](/questions/44844/wireshark-lua-dissector-efficient-way-to-do-a-binary-block-write-to-a-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44844-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44844-score" class="post-score" title="current number of votes">0</div><span id="post-44844-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am writing a lua dissector for a propietary protocol. The packets include bytes of embedded .png images that are contained in a tvb (buffer) object that I need to write to a .png file. In order to successfully write them to a file, below are couple of ways attempted. Both required "walking through" each byte of the buffer with string.char, making them VERY SLOW performing. Is there a better way to do this in lua, maybe with a fwrite-like single call to write the entire range of buffer bytes?</p><pre><code>-- Attempt #1
-- ============

local filename = &quot;foo.png&quot;

local file = assert(io.open(filename, &quot;w+b&quot;))

local i = 0

local lopt = size

local value

while lopt &gt; 0 do

    value = buffer(offset+5+i,1):uint()

        file:write(string.char(value))

        i = i + 1

        lopt = lopt - 1
end

file:write(buffer(offset+5):string())

file:flush()

file:close()

-- Attempt #2
-- ============
local filename = &quot;foo.png&quot;

local file = assert(fopen(filename, &quot;w+b&quot;))

local t = {}

for i=0,size

    do t[i] = string.char(buffer(offset+4+i,1):uint())

end

file:write(unpack(t))

file:flush()

file:close()</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Aug '15, 19:02</strong></p><img src="https://secure.gravatar.com/avatar/0e669f5129ac13bdba3262abcfbaa92b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mfbaker&#39;s gravatar image" /><p><span>mfbaker</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mfbaker has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Aug '15, 19:12</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-44844" class="comments-container"></div><div id="comment-tools-44844" class="comment-tools"></div><div class="clear"></div><div id="comment-44844-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="44847"></span>

<div id="answer-container-44847" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-44847-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-44847-score" class="post-score" title="current number of votes">1</div><span id="post-44847-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="mfbaker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes: in Wireshark/tshark version 1.12 the <code>Tvb</code>, <code>TvbRange</code>, and <code>ByteArray</code> objects were given new methods called "<code>raw()</code>", which gives back a Lua string of the contents of the Tvb/TvbRange/ByteArray. The functions are documented in <a href="https://www.wireshark.org/docs/wsdg_html_chunked/lua_module_Tvb.html">the API</a>, and noted in the <a href="https://wiki.wireshark.org/Lua/ApiChanges">changes to the API wiki page</a>. (they actually got added in 1.11, but that was a development release, so for general release it's 1.12)</p><p>So if you know the beginning offset in the <code>Tvb</code> and the length, you can just grab the whole chunk at once and then write it to the file in one chunk. In your example above, I assume that "<code>buffer</code>" is the <code>Tvb</code>, "<code>size</code>" is the size of the PNG chunk, and "<code>offset+5</code>" is where it begins, in which case this would do it:</p><pre><code>file:write(buffer:raw(offset+5, size))</code></pre><p>(plus the other stuff to open/close the file, which is presumably being done outside your dissector function anyway)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Aug '15, 19:27</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-44847" class="comments-container"><span id="44874"></span><div id="comment-44874" class="comment"><div id="post-44874-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much, Hadriel -- using the "raw()" API worked, with ~4x performance improvement! A capture file that I was testing had 5300 images, which before the change took about 23 seconds to load. With using raw() API instead, the same file took 5.9 seconds -- an awesome improvement!</p></div><div id="comment-44874-info" class="comment-info"><span class="comment-age">(05 Aug '15, 09:40)</span> <span class="comment-user userinfo">mfbaker</span></div></div><span id="44878"></span><div id="comment-44878" class="comment"><div id="post-44878-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-44878-info" class="comment-info"><span class="comment-age">(05 Aug '15, 11:06)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="44891"></span><div id="comment-44891" class="comment"><div id="post-44891-score" class="comment-score"></div><div class="comment-text"><p>Question is answered, thanks again, Hadriel!</p></div><div id="comment-44891-info" class="comment-info"><span class="comment-age">(05 Aug '15, 14:38)</span> <span class="comment-user userinfo">mfbaker</span></div></div></div><div id="comment-tools-44847" class="comment-tools"></div><div class="clear"></div><div id="comment-44847-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

