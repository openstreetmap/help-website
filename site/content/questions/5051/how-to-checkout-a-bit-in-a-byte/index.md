+++
type = "question"
title = "How to checkout a Bit in a Byte?"
description = '''Hi, just a short simple question: How can i checkout a specific Bit in a Byte? I tryed something like this: for i = Value_Start, Value_Stop do  local c = buffer(i,1):uint() &amp;lt;--- is this the right valuetype???   if c and 2^1 == 1 then .....  if c.1 == 1 then .....  if c(1) == 1 then .....  if c[1]...'''
date = "2011-07-15T05:56:00Z"
lastmod = "2011-07-15T14:06:00Z"
weight = 5051
keywords = [ "lua", "bitoperation" ]
aliases = [ "/questions/5051" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [How to checkout a Bit in a Byte?](/questions/5051/how-to-checkout-a-bit-in-a-byte)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5051-score" class="post-score" title="current number of votes">0</div><span id="post-5051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, just a short simple question:</p><p>How can i checkout a specific Bit in a Byte? I tryed something like this:</p><pre><code>for i = Value_Start, Value_Stop do
  local c = buffer(i,1):uint()  &lt;--- is this the right valuetype???

  if c and 2^1        == 1 then .....
  if c.1              == 1 then .....
  if c(1)             == 1 then .....
  if c[1]             == 1 then .....
  if c:1              == 1 then .....
  if c and 0x00000001 == 1 then .....
  if c and 128        == 1 then .....
end</code></pre><p>can anybody give me a short hint, please</p><p>Greets from Hamburg Pfanne</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-bitoperation" rel="tag" title="see questions tagged &#39;bitoperation&#39;">bitoperation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jul '11, 05:56</strong></p><img src="https://secure.gravatar.com/avatar/99abe74976c1c0ca886da31fed9feaa1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pfanne&#39;s gravatar image" /><p><span>Pfanne</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pfanne has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>15 Jul '11, 07:23</strong> </span></p><img src="https://secure.gravatar.com/avatar/fe1cf996b30e896dc95ca3cd47ac7406?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="multipleinterfaces&#39;s gravatar image" /><p><span>multipleinte...</span><br />
<span class="score" title="1321 reputation points"><span>1.3k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="23 badges"><span class="silver">●</span><span class="badgecount">23</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span></p></div></div><div id="comments-container-5051" class="comments-container"></div><div id="comment-tools-5051" class="comment-tools"></div><div class="clear"></div><div id="comment-5051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="5060"></span>

<div id="answer-container-5060" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5060-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5060-score" class="post-score" title="current number of votes">2</div><span id="post-5060-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p><code>TvbRange</code> supports a <a href="http://wiki.wireshark.org/LuaAPI/Tvb#tvbrange:bitfield.28.5Boffset.5D.2C_.5Blength.5D.29">bitfield</a> function that extracts the specified number of bits from an offset.</p><p>Also, Wireshark Lua natively supports <a href="http://bitop.luajit.org/">Lua BitOp</a> (without downloading any external libraries). I recommend using the native support instead of your own Lua bitops functions.</p><p>The documentation from those links should be clear enough.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '11, 14:06</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div></div><div id="comments-container-5060" class="comments-container"></div><div id="comment-tools-5060" class="comment-tools"></div><div class="clear"></div><div id="comment-5060-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5052"></span>

<div id="answer-container-5052" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5052-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5052-score" class="post-score" title="current number of votes">0</div><span id="post-5052-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Lua doesn't support bit operations by default. You may need to download a library like the one from</p><p><a href="http://luaforge.net/projects/bit/">http://luaforge.net/projects/bit/</a></p><p>Number of bitwise operations are supported</p><p>Also I'm not sure how to add a tag but this question should have been tagged with "lua" as well.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '11, 06:25</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-5052" class="comments-container"></div><div id="comment-tools-5052" class="comment-tools"></div><div class="clear"></div><div id="comment-5052-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="5055"></span>

<div id="answer-container-5055" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5055-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5055-score" class="post-score" title="current number of votes">0</div><span id="post-5055-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hi izopizo,</p><p>thanks for your hint. I have solved my problem like this.</p><pre><code>-- Convert Byte to BitArray ####################################################
local function to_bits(n)
 --check_int(n)
 --if(n &lt; 0) then
  -- negative
  --return to_bits(bit.bnot(math.abs(n)) + 1)
 --end

 -- to bits table
 local tbl = {}
 local cnt = 1
 while (n &gt; 0) do
  local last = math.mod(n,2)
  if(last == 1) then
   tbl[cnt] = 1
  else
   tbl[cnt] = 0
  end
  n = (n-last)/2
  cnt = cnt + 1
 end
 return tbl
end

for i = Value_Start, Value_Stop do
  local c = buffer(i,1):uint()

  local BitTable = to_bits(c)     
  if BitTable[8] == 1 then Bit8 = Bit8 .. &quot; 1  &quot; else Bit8 = Bit8 .. &quot; .  &quot; end
  if BitTable[7] == 1 then Bit7 = Bit7 .. &quot; 1  &quot; else Bit7 = Bit7 .. &quot; .  &quot; end
  if BitTable[6] == 1 then Bit6 = Bit6 .. &quot; 1  &quot; else Bit6 = Bit6 .. &quot; .  &quot; end
  if BitTable[5] == 1 then Bit5 = Bit5 .. &quot; 1  &quot; else Bit5 = Bit5 .. &quot; .  &quot; end
  if BitTable[4] == 1 then Bit4 = Bit4 .. &quot; 1  &quot; else Bit4 = Bit4 .. &quot; .  &quot; end
  if BitTable[3] == 1 then Bit3 = Bit3 .. &quot; 1  &quot; else Bit3 = Bit3 .. &quot; .  &quot; end
  if BitTable[2] == 1 then Bit2 = Bit2 .. &quot; 1  &quot; else Bit2 = Bit2 .. &quot; .  &quot; end
  if BitTable[1] == 1 then Bit1 = Bit1 .. &quot; 1  &quot; else Bit1 = Bit1 .. &quot; .  &quot; end
end</code></pre><p>I´am a little bid amezed, becouse Lua dosen´t support this comparatively simple operation.</p><p>Greets From Hamburg Pfanne</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 Jul '11, 12:25</strong></p><img src="https://secure.gravatar.com/avatar/99abe74976c1c0ca886da31fed9feaa1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pfanne&#39;s gravatar image" /><p><span>Pfanne</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pfanne has no accepted answers">0%</span></p></div></div><div id="comments-container-5055" class="comments-container"></div><div id="comment-tools-5055" class="comment-tools"></div><div class="clear"></div><div id="comment-5055-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

