+++
type = "question"
title = "string variable not interpreted right by unpack()"
description = '''I&#x27;m trying to convert a hex string to decimal string byte by byte, and then pass it to a Struct.unpack function to convert to double. However, I get the wrong number even though the exact same string value in a string literal will get the right number. Here is the code: str = &quot;3f91df0b2b89dd1e&quot; deci...'''
date = "2014-03-20T11:40:00Z"
lastmod = "2014-03-20T12:31:00Z"
weight = 31004
keywords = [ "lua", "struct" ]
aliases = [ "/questions/31004" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [string variable not interpreted right by unpack()](/questions/31004/string-variable-not-interpreted-right-by-unpack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31004-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to convert a hex string to decimal string byte by byte, and then pass it to a Struct.unpack function to convert to double. However, I get the wrong number even though the exact same string value in a string literal will get the right number.</p><p>Here is the code:</p><pre><code>str = &quot;3f91df0b2b89dd1e&quot;
decimalStr = &quot;&quot;

for i = 1, string.len(str), 2 do
  decimalStr = decimalStr .. &quot;\\&quot;
  onebyte = string.sub(str, i, i + 1)
  num = tonumber(onebyte, 16)
  decimalStr = decimalStr .. num
end

print(decimalStr)
print(Struct.unpack(&quot;&gt;d&quot;, decimalStr))
print(Struct.unpack(&quot;&gt;d&quot;, &quot;\63\145\223\11\43\137\221\30&quot;))</code></pre><p>result:</p><pre><code>\63\145\223\11\43\137\221\30
1.6136274310717e+136        9
0.017452406437284       9</code></pre><p>I don't understand! <code>decimalStr</code> is "<code>\63\145\223\11\43\137\221\30</code>", but it is giving out the wrong value after <code>unpack</code>. As you can see, if you use the same actual string literal it works.</p><p>What's going on?</p></div><div id="question-tags" class="tags-container tags">lua struct</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Mar '14, 11:40</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p>YXI<br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Mar '14, 12:17</p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-31004" class="comments-container"></div><div id="comment-tools-31004" class="comment-tools"></div><div class="clear"></div><div id="comment-31004-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31009"></span>

<div id="answer-container-31009" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-31009-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Your for-loop is constructing a Lua string, containing the characters exactly as printed. In other words, you've constructed a string of the character "<code>\</code>" followed by the character "<code>6</code>" followed by the character "<code>3</code>", etc.</p><p>But this:</p><pre><code>local foo = &quot;\63\145\223\11\43\137\221\30&quot;</code></pre><p>Does <em>not</em> construct that same string. Why? Because those "<code>\</code>" in this case are escape codes, telling the Lua interpreter that the digits following the "<code>\</code>" are to be interpreted as the decimal value of a character - in this case whose decimal value is 63, <em>not</em> the raw characters "<code>6</code>" followed by "<code>3</code>".</p><p>In other words, before <code>Struct.unpack()</code> even gets the Lua string, Lua has already converted it to a string containing the binary byte whose decimal value is 63 (hex 0x3F) followed by one whose decimal value is 145 (hex 0x91), etc. That's a very different string, obviously.</p><p>Try doing this and you'll see what I mean:</p><pre><code>print(&quot;\63\145\223\11\43\137\221\30&quot;)</code></pre><p>You'll probably see gibberish on your screen, because it's a string of bytes which may or may not be printable characters. But it's not the ascii character "<code>\</code>" followed by "<code>6</code>" followed by "<code>3</code>", etc.</p><p>This is just like in most any programming language I can think of - if you escape things inside a string literal in the source code/script, the compiler/interpreter knows you mean to handle them as something else.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Mar '14, 12:31</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-31009" class="comments-container"><span id="31010"></span><div id="comment-31010" class="comment"><div id="post-31010-score" class="comment-score"></div><div class="comment-text"><p>BTW, if you can tell me what it is you're trying to accomplish - the bigger picture - perhaps I can help you get there faster. But if you'd like to get there on your own that's cool too. :)</p></div><div id="comment-31010-info" class="comment-info"><span class="comment-age">(20 Mar '14, 12:35)</span> Hadriel</div></div><span id="31016"></span><div id="comment-31016" class="comment"><div id="post-31016-score" class="comment-score"></div><div class="comment-text"><p>Well, the big picture is I need to convert bytes of different lengths to various numbers (unsigned int, int, float, double, etc).<br />
When I have 4 bytes or less it's more or less straight forward. When I have more that 4 bytes, I've been using the UInt64/Int64 to get the value from the bytes, pack it first and then unpack to convert to the type I want. However, when converting 8 bytes to double, it doesn't work right in Windows. Following your post to my question, I decided to skip the pack step and go directly to unpack, passing to it a string of the bytes' values in decimals. Obviously I thought it's a normal string of numbers separated by "\". Now I realize it's not the case. How did you get the decimal number sequence with escape characters from hex? If you have an easier way to do what I need to do, please share.</p></div><div id="comment-31016-info" class="comment-info"><span class="comment-age">(20 Mar '14, 14:27)</span> YXI</div></div><span id="31017"></span><div id="comment-31017" class="comment"><div id="post-31017-score" class="comment-score"></div><div class="comment-text"><p>"How did you get the decimal number sequence with escape characters from hex?"</p><p>I used my calculator to convert the hex value to a decimal value. Mac's built-in calculator in programmer view mode is quite useful. :)</p><p>But obviously you wouldn't do that in a Lua script - you'd use <code>string.byte()</code> in a for-loop or as an argument to <code>string.gsub()</code>. But in wireshark you could just use <code>Struct.fromhex()</code>.</p><p>But that's assuming you started out with a string of hex-ascii characters. Is that the case for you? Where did this string come from? If it's from a packet's contents, why do you need to use Lua to convert them instead of using the provided tvb/tvbrange or tree functions?</p></div><div id="comment-31017-info" class="comment-info"><span class="comment-age">(20 Mar '14, 14:51)</span> Hadriel</div></div><span id="31018"></span><div id="comment-31018" class="comment"><div id="post-31018-score" class="comment-score"></div><div class="comment-text"><p>I cannot use tvb/tvbrange functions because my values are stored in disjoint bytes. For example, a 8-byte value can be stored in offset 0-4 and then 16-20. I could use byteArray:tvb() to create a new tvb using these bytes. However, whenever I create a new tvb this way, a new tab is added to the packet bytes pane in the wireshark GUI. And since I have lots of these tabs, I believe it is the reason why my wireshark is crashing whenever I click on a tree item that refers to a newly created tvb. So now what I do is to get the value by this code: Let's say byteList have the byte locations I need from the payload. byteList = { 4, 5, 6, 7, 12, 13, 14, 15}</p><pre><code>    allBytes = ByteArray.new()

    for i = 1, #byteList do

        nextByte = buffer(offset + byteList[i], 1):bytes()

        allBytes:append(nextByte)

    end

    value = UInt64.fromhex(tostring(allBytes))</code></pre><p>I do some bit shifts and masking that is some other extra requirement, and then I get the string again by str = value:tohex()</p><p>Now from here I now plan to use unpack to finally get the value I need that will work in Windows as well.</p></div><div id="comment-31018-info" class="comment-info"><span class="comment-age">(20 Mar '14, 15:37)</span> YXI</div></div><span id="31026"></span><div id="comment-31026" class="comment"><div id="post-31026-score" class="comment-score"></div><div class="comment-text"><p>For the first part of your comment: Wireshark shouldn't crash, so please either submit a bug or provide enough of a sample script here for me to reproduce the crash. Crashes are bad mojo.</p></div><div id="comment-31026-info" class="comment-info"><span class="comment-age">(20 Mar '14, 17:48)</span> Hadriel</div></div><span id="31027"></span><div id="comment-31027" class="comment not_top_scorer"><div id="post-31027-score" class="comment-score"></div><div class="comment-text"><p>For the second part of your comment: that seems like a hard way to go about it - why not just use <code>Tvb:raw()</code> to get a Lua binary string of the portion that has your bytes, and then operate on that string in Lua, to get the substring(s) your need (for example using <code>string.sub()</code> or even <code>string.match()</code>), concatenate the substrings and then feed that resulting new string to <code>Struct.unpack()</code>?</p></div><div id="comment-31027-info" class="comment-info"><span class="comment-age">(20 Mar '14, 17:53)</span> Hadriel</div></div></div><div id="comment-tools-31009" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-31009-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

