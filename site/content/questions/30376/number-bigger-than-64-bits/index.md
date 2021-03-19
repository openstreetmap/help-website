+++
type = "question"
title = "number bigger than 64 bits"
description = '''Hi, Just wondering if anyone has to write a dissector in Lua that contains values bigger than 64 bit. How do you do it. Thanks.'''
date = "2014-03-03T18:23:00Z"
lastmod = "2014-03-06T01:42:00Z"
weight = 30376
keywords = [ "lua", "big_number" ]
aliases = [ "/questions/30376" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [number bigger than 64 bits](/questions/30376/number-bigger-than-64-bits)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30376-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30376-score" class="post-score" title="current number of votes">0</div><span id="post-30376-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>Just wondering if anyone has to write a dissector in Lua that contains values bigger than 64 bit. How do you do it.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-big_number" rel="tag" title="see questions tagged &#39;big_number&#39;">big_number</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Mar '14, 18:23</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> retagged <strong>04 Mar '14, 04:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-30376" class="comments-container"></div><div id="comment-tools-30376" class="comment-tools"></div><div class="clear"></div><div id="comment-30376-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="30391"></span>

<div id="answer-container-30391" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30391-score" class="post-score" title="current number of votes">0</div><span id="post-30391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To do what with? Just to show it in the display tree? Have it be filterable by value? Or to actually perform some arithmetic on it?</p><p>If it's just to display in the tree, I suppose you can treat it as a byte string. You can even show it's numerical value by processing each byte in Lua and building/concatenating a string representing the numeric value, that you add to the tree item using Lua. (it would take some careful Lua coding to make such a bignum string, but it's possible)</p><p>But to have it be filterable by numeric value (i.e., have a display filter like 'myproto.bugnum = 42446744073709551615') isn't possible as far as I know, since there's no filter type for numbers bigger than 64-bit.</p><p>There's no way of performing Lua arithmetic (ie, add, subtract, divide) on numbers that big directly as a Lua number, because Lua itself only handles numbers as doubles; and though a double can certainly represent massive numbers, it loses precision above 53-bits (or 52 bits... I always forget which). As of Wireshark 1.11.3 we now have Lua arithmetic for 64-bit numbers, as Int64/UInt64 userdata objects, but nothing bigger. So if you need to handle something bigger, you'll have to write the Lua code to do it based on smaller number chunks of the bigger number.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '14, 04:23</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30391" class="comments-container"><span id="30400"></span><div id="comment-30400" class="comment"><div id="post-30400-score" class="comment-score"></div><div class="comment-text"><p>Thanks Hadriel. I do need to do a lot of stuff on the big numbers (bit operations such as shifting, masking), change endianess, and also type conversion, e.g. interpreting an unsigned long long number as a double. I think this is definitely beyond the capability of Wireshark Lua even for the newest development version. I know Lua has libraries that handle numbers to an arbitrary size, but I haven't seen anyone using it writing Wireshark dissectors. In reality, most of my values are going to be capped at 64 bits, so I will probably ignore the really big numbers for now. I'm still using wireshark 1.10.2. I think I will have to move to 1.11.2 to do all the 64 bit stuff. However, since it's not a stable release, I'm hesitating to do it. You can probably tell I'm still a novice to the whole thing. But how stable is the development release? Any serious risks?</p><p>Thanks so much, YXI</p></div><div id="comment-30400-info" class="comment-info"><span class="comment-age">(04 Mar '14, 08:14)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="30402"></span><div id="comment-30402" class="comment"><div id="post-30402-score" class="comment-score"></div><div class="comment-text"><p>Well... it's fairly stable, if you keep to the automated nightly builds instead of just pulling down the latest source code and compiling yourself. But the 64-bit stuff is only in 1.11.3, not 1.11.2, so you can only get it from the nightly builds here: <a href="http://www.wireshark.org/download/automated/">http://www.wireshark.org/download/automated/</a></p><p>Info on the Int64/UInt64 is here: <a href="http://wiki.wireshark.org/LuaAPI/Int64">http://wiki.wireshark.org/LuaAPI/Int64</a></p><p>If you need some new Lua function/class/whatever exposed into Wireshark, just submit a bugzilla enhancement request, or post it in a new question here with the tag 'lua'. I've been on a kick lately exposing more stuff into Lua. The changes merged into 1.11.3 so far are documented here: <a href="http://wiki.wireshark.org/Lua/ApiChanges">http://wiki.wireshark.org/Lua/ApiChanges</a></p><p>Which bignum library for Lua would you like to see in Wireshark?</p></div><div id="comment-30402-info" class="comment-info"><span class="comment-age">(04 Mar '14, 08:44)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30410"></span><div id="comment-30410" class="comment"><div id="post-30410-score" class="comment-score"></div><div class="comment-text"><p>Hi Hadriel,</p><p>I haven't decided which one I like (I looked at both lbc and lmapm). So you may need to wait for more input from the community on this one.</p><p>I saw that you committed changes very recently to add Lua struct (pack, unpack, etc) functionalities to Wireshark. Are they ready to be used? will they work on 64 bit numbers? I do need to do endianness swaps, converting signed to unsigned number, long to double, etc. I think using the struct library may be the easiest way to go. Is that true?</p><p>Thanks, YXI</p></div><div id="comment-30410-info" class="comment-info"><span class="comment-age">(04 Mar '14, 09:47)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="30414"></span><div id="comment-30414" class="comment"><div id="post-30414-score" class="comment-score"></div><div class="comment-text"><p>I looked into lbc and lmapm (and lbn and lqd and lgmp), and the easiest to include in Wireshark would be lbc, by far. Unfortunately it's also probably the slowest. :(</p><p>I assume though that raw speed isn't that important?</p></div><div id="comment-30414-info" class="comment-info"><span class="comment-age">(04 Mar '14, 11:01)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30423"></span><div id="comment-30423" class="comment"><div id="post-30423-score" class="comment-score"></div><div class="comment-text"><p>Speed is not important to me. Neither of these two have bit operation APIs though.</p></div><div id="comment-30423-info" class="comment-info"><span class="comment-age">(04 Mar '14, 16:49)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="30425"></span><div id="comment-30425" class="comment not_top_scorer"><div id="post-30425-score" class="comment-score"></div><div class="comment-text"><p>No, but I'd add that. I added it for Int64/UInt64, for example.</p></div><div id="comment-30425-info" class="comment-info"><span class="comment-age">(04 Mar '14, 19:22)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-30391" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-30391-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="30411"></span>

<div id="answer-container-30411" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30411-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30411-score" class="post-score" title="current number of votes">0</div><span id="post-30411-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Yes, Struct is in the latest nightly builds, and has Int64/UInt64 support by using 'e'/'E' in the pattern. Note that it's "Struct" not "struct", however - I didn't want to collide with someone's use of the real struct library if they were already using it. Also, our auto-generated docs for it are <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Struct.html">here</a>, but it's not very helpful. I've been hoping to update the doc generator for the API, because we're very limited in the type of documentation that can be generated for the API. (it's auto-generated by a Perl script from source code)</p><p>So here are some rough notes from the source file:</p><pre><code>** Some changes are based on a patch to struct.h from
** Flemming Madsen, from here:
** http://lua-users.org/lists/lua-l/2009-10/msg00572.html
** In particular, these changes from him:
** -Can handle &#39;long long&#39; integers (i8 / I8); though they&#39;re converted to doubles
** -Can insert/specify padding anywhere in a struct. (&#39;X&#39; eg. when a string is following a union)
** -Can report current offset in both pack and unpack (&#39;=&#39;)
** -Can mask out return values when you only want to calculate sizes or unmarshal pascal-style strings. &#39;(&#39; &amp; &#39;)&#39;
**
** Changes I made:
** -Added support for Int64/UIn64 being packed/unpacked, using &#39;e&#39;/&#39;E&#39;
** -Made it follow Wireshark&#39;s conventions so we could get API docs
** =======================================================
*/
/*
** Valid formats:
** &gt; - big endian
** &lt; - little endian
** ![num] - alignment
** x[num]   - pad num bytes, default 1
** X[num]   - pad to num align, default MAXALIGN
**
** Following are system-dependent sizes:
** b/B - signed/unsigned byte
** h/H - signed/unsigned short
** i/I - signed/unsigned int
** l/L - signed/unsigned long
** f - float
** d - double
** T   - size_t
**
** Following are system-independent sizes:
** in/In - signed/unsigned integer of size `n&#39; bytes
          Note: unpack of i/I is done to a Lua_number, typically a double,
          so unpacking a 64-bit field (i8/I8) will lose precision.
          Use e/E to unpack into a Wireshark Int64/UInt64 object/userdata instead.
** e/E - signed/unsigned eight-byte Integer (64bits, long long), to/from Int64/UInt64 object
** cn - sequence of `n&#39; chars (from/to a string); when packing, n==0 means
        the whole string; when unpacking, n==0 means use the previous
        read number as the string length
** s - zero-terminated string
** &#39; &#39; - ignored
** &#39;(&#39; &#39;)&#39;  - stop assigning items. &#39;)&#39; start assigning (padding when packing)
** &#39;=&#39;      - return current position / offset
*/</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '14, 09:58</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-30411" class="comments-container"><span id="30412"></span><div id="comment-30412" class="comment"><div id="post-30412-score" class="comment-score"></div><div class="comment-text"><p>Oh, and I added a tohex()/fromhex() function, as documented in the API docs.</p></div><div id="comment-30412-info" class="comment-info"><span class="comment-age">(04 Mar '14, 10:01)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30422"></span><div id="comment-30422" class="comment"><div id="post-30422-score" class="comment-score"></div><div class="comment-text"><p>This is great. I really need it. Will let you know how it goes.</p></div><div id="comment-30422-info" class="comment-info"><span class="comment-age">(04 Mar '14, 16:48)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="30447"></span><div id="comment-30447" class="comment"><div id="post-30447-score" class="comment-score"></div><div class="comment-text"><p>Hadriel and others,</p><p>If I simply have these two lines of code:</p><p>a = UInt64.new("ff000000")</p><p>b = a.rshift(2)</p><p>I get: Lua: Error During execution of dialog callback: [string "a = UInt64.new("ff000000")..."]:2: bad argument #2 to 'rshift' (number expected, got no value)</p><p>What did I do wrong?</p><p>Thanks.</p></div><div id="comment-30447-info" class="comment-info"><span class="comment-age">(05 Mar '14, 14:59)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="30448"></span><div id="comment-30448" class="comment"><div id="post-30448-score" class="comment-score"></div><div class="comment-text"><p>You called 'rshift()' with a single argument - a number 2 - instead of with 2 arguments: the 'a' object, and the number 2. You need to use a <code>:</code> colon instead of <code>.</code> period, because a colon is basically Lua shorthand for <code>a.rshift(a,2)</code>.</p><p>So you should do this:</p><pre><code>a = UInt64.new(0xff000000)
b = a:rshift(2)</code></pre><p>Note also I didn't put the ff000000 in quotes, as that would make it a string, and although UInt64/Int64 new() accepts a string, it decodes it in base 10, which means it has to be a string of digits, not hex. Maybe I should change it to decode in base 0, so you could use hex inside (if you prepend with 0x).</p><p>Also, you don't need to use the 'new' method - you can just call it like this:</p><pre><code>a = UInt64(0xff000000)
b = a:rshift(2)</code></pre></div><div id="comment-30448-info" class="comment-info"><span class="comment-age">(05 Mar '14, 15:16)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30449"></span><div id="comment-30449" class="comment"><div id="post-30449-score" class="comment-score"></div><div class="comment-text"><p>BTW, I think your post and mine were just changed to comments, because this ask.wireshark.org site isn't really a forum model of topic threads, but instead a question+answer model site. So each topic is a single question and one or more answers to that question. So you should ask future questions as new, separate topics, not in this one.</p><p>(everyone makes that mistake, but the folks behind ask.wireshark.org are refusing to yield to how everyone else communicates naturally, under the hope that by keeping it a question+answer model then people will search for their question being already answered previously. It's a nice dream. :)</p></div><div id="comment-30449-info" class="comment-info"><span class="comment-age">(05 Mar '14, 15:36)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30451"></span><div id="comment-30451" class="comment not_top_scorer"><div id="post-30451-score" class="comment-score"></div><div class="comment-text"><p>Thanks Hadriel. Sorry for my mistake. You can probably tell I'm still new to Lua. The funny thing was I did not get any error messages using "." instead of ":" on the band() and bor() functions, with only one argument, like b=a.band(0xff). That's why I didn't even suspect my syntax was wrong for the shift operations.<br />
Anyway, thanks for the explanations. I will start a new question next time I change the topic.</p></div><div id="comment-30451-info" class="comment-info"><span class="comment-age">(05 Mar '14, 18:20)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="30452"></span><div id="comment-30452" class="comment not_top_scorer"><div id="post-30452-score" class="comment-score"></div><div class="comment-text"><p>Hmmm.. well technically that's because they're not errors - you just created a new UInt64 of value 0xff and didn't <code>and</code>/<code>or</code> it with anything. The and/or/xor functions all take any number of arguments, including only one argument. So when you do <code>b=a.band(0xff)</code>, you're really calling <code>band()</code> with just the 0xff argument, and thus creating a new UInt64 of value 0xff, and assigning it to variable <code>b</code>. The problem you had before was the <code>rshift()</code> function, which must have two arguments, but you were only giving it one. For example, you could have done this: <code>b=UInt64.rshift(0xff000000, 2)</code> and it would have worked as well.</p><p>I know that's a bit confusing, not being consistent in different functions, but I was trying to mimic exactly what the Lua bitop library does for all of these functions, since Wireshark has the bitop library available in Lua but it only handles up to 32bit integers... and the bitop library does exactly the same thing Int64/UIn64 does for and/or/xor vs. rshift and the others.</p></div><div id="comment-30452-info" class="comment-info"><span class="comment-age">(05 Mar '14, 19:04)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="30471"></span><div id="comment-30471" class="comment not_top_scorer"><div id="post-30471-score" class="comment-score"></div><div class="comment-text"><p><span>@Hadriel</span>, <span>@YXI</span></p><p>Yep, the mods do try to keep things as a Q&amp;A. User assistance in keeping it that way would be appreciated. StackOverflow etc. seem to do OK with that model. I think we need to have a start page that consists of nothing but a search box, then users might actually use it. :-)</p><p>It's sometime difficult to determine if a supplementary question should be promoted to its own question, but that's a judgement call.</p></div><div id="comment-30471-info" class="comment-info"><span class="comment-age">(06 Mar '14, 01:42)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-30411" class="comment-tools"><span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a></div><div class="clear"></div><div id="comment-30411-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

