+++
type = "question"
title = "UInt64 bitwise and operation wrong in Windows"
description = '''UInt64 is supposed be able to bitwise AND with another 64 bit integer. The API says: uint64:band(arg1 [, arg2 [, ...]]) arg1 : number|UInt64|UUInt64|string The number/UInt64/UIn64/hex-string to bitwise &#x27;and&#x27; the UInt64 with.  However, it doesn&#x27;t seems to work correctly on the Windows platform. See t...'''
date = "2014-03-21T08:31:00Z"
lastmod = "2014-03-21T14:06:00Z"
weight = 31051
keywords = [ "lua" ]
aliases = [ "/questions/31051" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UInt64 bitwise and operation wrong in Windows](/questions/31051/uint64-bitwise-and-operation-wrong-in-windows)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31051-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31051-score" class="post-score" title="current number of votes">0</div><span id="post-31051-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>UInt64 is supposed be able to bitwise AND with another 64 bit integer. The API says:</p><pre><code>uint64:band(arg1 [, arg2 [, ...]])
arg1 : number|UInt64|UUInt64|string
The number/UInt64/UIn64/hex-string to bitwise &#39;and&#39; the UInt64 with.</code></pre><p>However, it doesn't seems to work correctly on the Windows platform.</p><p>See the code below:</p><pre><code>str = &quot;3f91df0b2b89dd1e&quot;
num = UInt64.fromhex(str)
print(num)
newNum = num:band(0xffffffff00000000)
print(newNum)</code></pre><p>In Mac, my tshark result is:</p><pre><code>4580687535080594718
4580687534350139392  -- correct</code></pre><p>In Windows, the same code using tshark gets:</p><pre><code>4580687535080594718
730455326 -- wrong</code></pre><p>It seems windows can only handle 32 bit mask, not 64.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Mar '14, 08:31</strong></p><img src="https://secure.gravatar.com/avatar/b18cada3e3589f311e24f5ffbd1737bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="YXI&#39;s gravatar image" /><p><span>YXI</span><br />
<span class="score" title="21 reputation points">21</span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="YXI has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Mar '14, 09:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span></p></div></div><div id="comments-container-31051" class="comments-container"><span id="31055"></span><div id="comment-31055" class="comment"><div id="post-31055-score" class="comment-score"></div><div class="comment-text"><p>Please post the "About Wireshark" output for your windows wireshark.</p></div><div id="comment-31055-info" class="comment-info"><span class="comment-age">(21 Mar '14, 09:11)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31056"></span><div id="comment-31056" class="comment"><div id="post-31056-score" class="comment-score"></div><div class="comment-text"><p>Version 1.11.3-1851-gb2689ab (wireshark-1.11.3-rc1-1851-gb2689ab-dirty from master)</p><p>Copyright 1998-2014 Gerald Combs <span><span class="__cf_email__" data-cfemail="8ee9ebfcefe2eacef9e7fcebfde6effce5a0e1fce9">[email protected]</span></span> and contributors. This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>Compiled (32-bit) with GTK+ 3.4.4, with Cairo 1.10.2, with Pango 1.30.1, with GLib 2.32.4, with WinPcap (4_1_3), with libz 1.2.5, with SMI 0.4.8, with c-ares 1.9.1, with Lua 5.1, without Python, with GnuTLS 2.12.18, with Gcrypt 1.4.6, with MIT Kerberos, with GeoIP, with PortAudio V19-devel (built Mar 4 2014), with AirPcap.</p><p>Running on 32-bit Windows 7 Service Pack 1, build 7601, with WinPcap version 4.1.3 (packet.dll version 4.1.0.2980), based on libpcap version 1.0 branch 1_0_rel0b (20091008), GnuTLS 2.12.18, Gcrypt 1.4.6, without AirPcap. Intel(R) Core(TM) i7-3615QM CPU @ 2.30GHz, with 2815MB of physical memory.</p><p>Built using Microsoft Visual C++ 10.0 build 40219</p><p>Wireshark is Open Source Software released under the GNU General Public License.</p><p>Check the man page and <a href="http://www.wireshark.org">http://www.wireshark.org</a> for more information.</p></div><div id="comment-31056-info" class="comment-info"><span class="comment-age">(21 Mar '14, 09:23)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31057"></span><div id="comment-31057" class="comment"><div id="post-31057-score" class="comment-score"></div><div class="comment-text"><p>Then it's probably because it's a 32-bit build you're using, as opposed to Mac/Linux vs. Windows (maybe). If the windows system you're running is 64-bit capable, can you try a 64-bit build of wireshark?</p><p>Still, it should have worked, so I'll look into it as well.</p></div><div id="comment-31057-info" class="comment-info"><span class="comment-age">(21 Mar '14, 09:41)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31058"></span><div id="comment-31058" class="comment"><div id="post-31058-score" class="comment-score"></div><div class="comment-text"><p>BTW, you shouldn't really do:</p><pre><code>newNum = num:band(0xffffffff00000000)</code></pre><p>because a raw <code>0xffffffff00000000</code> is a Lua number, and bigger than 53 bits of precision. (this is similar to a previous example you gave in a previous question thread)</p></div><div id="comment-31058-info" class="comment-info"><span class="comment-age">(21 Mar '14, 09:45)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-31051" class="comment-tools"></div><div class="clear"></div><div id="comment-31051-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31062"></span>

<div id="answer-container-31062" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31062-score" class="post-score" title="current number of votes">1</div><span id="post-31062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I've reproduced this on a 32-bit Windows XP system. The problem is Lua itself is treating the <code>0xffffffff00000000</code> as a 32-bit number, even though it should be a double even on 32-bit machines.</p><p>For example, try this:</p><pre><code>print(0xffffffff00000000)</code></pre><p>That prints out <code>4294967295</code> instead of <code>1.8446744069415e+19</code>.</p><p>As a work-around (and in fact the right way to do <code>band</code> with such a large mask number), do one of these:</p><pre><code>newNum = num:band(UInt64.fromhex(&quot;ffffffff00000000&quot;))
newNum = num:band(UInt64(0, 0xffffffff))</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Mar '14, 10:22</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-31062" class="comments-container"><span id="31063"></span><div id="comment-31063" class="comment"><div id="post-31063-score" class="comment-score"></div><div class="comment-text"><p>Interesting - it's a limitation in Lua 5.1 itself... I'd even call it a bug in Lua 5.1, which are super-rare these days, but apparently it's been discussed on the mailing list and isn't considered a bug. But basically on a 32-bit system, literal hex numbers (such as <code>0xffffffff00000000</code>) are truncated to 32-bits big.</p><p>So yet another reason not to use a number that big as a Lua number, but instead create a UInt64/Int64 out of two smaller numbers or out of a string.</p></div><div id="comment-31063-info" class="comment-info"><span class="comment-age">(21 Mar '14, 10:48)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31065"></span><div id="comment-31065" class="comment"><div id="post-31065-score" class="comment-score"></div><div class="comment-text"><p>Your suggestion made sense, but it didn't work for some reason. I ran this code in tshark in the Mac (didn't try Windows):</p><p>str = "3f91df0b2b89dd1e"</p><p>value = UInt64.fromhex(str)</p><p>myMask = 0xffffffff00000000</p><p>num = value:band(myMask)</p><p>print(num)</p><p>numNew = value:band(UInt64.fromhex(myMask))</p><p>print(numNew)</p><p>The result:</p><p>4580687534350139392</p><p>0</p><p>So directly using the big number worked, but passing in the 64bit type returned 0.</p></div><div id="comment-31065-info" class="comment-info"><span class="comment-age">(21 Mar '14, 12:58)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31066"></span><div id="comment-31066" class="comment"><div id="post-31066-score" class="comment-score"></div><div class="comment-text"><p>Because you're doing: <code>UInt64.fromhex(myMask)</code>, and <code>myMask</code> is not a hex string in your example, but rather a Lua number. (and it's a number that won't be the same number on 32-bit machines apparently)</p><p>Do this instead:</p><pre><code>-- the value
local value = UInt64.fromhex(&quot;3f91df0b2b89dd1e&quot;)

-- myMask is a UInt64, not a hex string
local myMask = UInt64.fromhex(&quot;ffffffff00000000&quot;)

-- so this
local num = value:band(myMask)
print(num)

-- or this
local numNew = value:band(UInt64.fromhex(&quot;ffffffff00000000&quot;))
print(numNew)

-- or this
local otherNum = value:band(UInt64(0, 0xffffffff))
print(otherNum)</code></pre></div><div id="comment-31066-info" class="comment-info"><span class="comment-age">(21 Mar '14, 13:19)</span> <span class="comment-user userinfo">Hadriel</span></div></div><span id="31068"></span><div id="comment-31068" class="comment"><div id="post-31068-score" class="comment-score"></div><div class="comment-text"><p>Yes! Feel so stupid today. Sorry for wasting your time. Good news is now it works in Windows. Finally got Windows to give me the right numbers. Thank you so much!!!</p></div><div id="comment-31068-info" class="comment-info"><span class="comment-age">(21 Mar '14, 14:02)</span> <span class="comment-user userinfo">YXI</span></div></div><span id="31069"></span><div id="comment-31069" class="comment"><div id="post-31069-score" class="comment-score"></div><div class="comment-text"><p>Sure no problem.</p></div><div id="comment-31069-info" class="comment-info"><span class="comment-age">(21 Mar '14, 14:06)</span> <span class="comment-user userinfo">Hadriel</span></div></div></div><div id="comment-tools-31062" class="comment-tools"></div><div class="clear"></div><div id="comment-31062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

