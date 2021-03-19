+++
type = "question"
title = "Lua: Comparing a boolean value"
description = '''I&#x27;ve been trying to get a comparison going on my code, but can&#x27;t seem to manage the way to do it: I have this field:  f.bitmap1_b1_10000000 = ProtoField.bool(&quot;f.bitmap1_b1_10000000&quot;,&quot;condition present?&quot;,8,{&quot;Present&quot;,&quot;Not Present&quot;},0x80)  I then eventually set it&#x27;s value: local bitmap1_b1_10000000 = ...'''
date = "2012-02-24T23:14:00Z"
lastmod = "2012-02-26T11:12:00Z"
weight = 9203
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/9203" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Lua: Comparing a boolean value](/questions/9203/lua-comparing-a-boolean-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9203-score" class="post-score" title="current number of votes">0</div><span id="post-9203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I've been trying to get a comparison going on my code, but can't seem to manage the way to do it:</p><p>I have this field:</p><pre><code>f.bitmap1_b1_10000000 = ProtoField.bool(&quot;f.bitmap1_b1_10000000&quot;,&quot;condition present?&quot;,8,{&quot;Present&quot;,&quot;Not Present&quot;},0x80)</code></pre><p>I then eventually set it's value:</p><pre><code>local bitmap1_b1_10000000 = data(offset,1)
subtree:add(f.bitmap1_b1_10000000,bitmap1_b1_10000000)</code></pre><p>And the value shows up correctly on the dissector window (I've checked, and it works for every one of the 128 fields.. &gt;_&lt;)</p><p>Now, onto parsing the rest of the data, I'm trying to conditionally execute my code based upon the boolean fields, but cannot seem to:</p><p>These DO work on the GUI, but DO NOT work on the code(devel 1.7.0):</p><pre><code>if f.bitmap1_b1_10000000 == 1 then
    offset = offset + 8
end

if f.bitmap1_b1_10000000 == &quot;Present&quot; then
    offset = offset + 8
end</code></pre><p>This too does not work (for some reason beyond my comprehension):</p><pre><code>if (data(correct_offset,1):uint() and 0x80) then
    offset = offset + 8
end</code></pre><p>Neither does this:</p><pre><code>if (data(correct_offset,1):uint() % (2*0x80) &gt;= 0x80) then
    offset = offset + 8
end</code></pre><p>(the offsets are correct on the code, I'm just simplifing them here)</p><p>So, is there a way to actually do it? What am I doing wrong?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '12, 23:14</strong></p><img src="https://secure.gravatar.com/avatar/1d349e4a8dbe4c509b905f1e5d5430c1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gutoandreollo&#39;s gravatar image" /><p><span>gutoandreollo</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gutoandreollo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>25 Feb '12, 17:02</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-9203" class="comments-container"><span id="9206"></span><div id="comment-9206" class="comment"><div id="post-9206-score" class="comment-score"></div><div class="comment-text"><p>By <code>(data(correct_offset,1):uint() and 0x80)</code> do you mean to perform a <em>bitwise</em>-and? If so, this may be part of your problem. I don't know if this has changed since I last implemented a Lua-based dissector, but Wireshark's Lua interpreter does not have an extension for bitwise operators. See <a href="http://lua-users.org/wiki/BitwiseOperators" title="Bitwise Operators">this article</a> on the lua-users wiki.</p></div><div id="comment-9206-info" class="comment-info"><span class="comment-age">(25 Feb '12, 08:50)</span> <span class="comment-user userinfo">multipleinte...</span></div></div></div><div id="comment-tools-9203" class="comment-tools"></div><div class="clear"></div><div id="comment-9203-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9208"></span>

<div id="answer-container-9208" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-9208-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-9208-score" class="post-score" title="current number of votes">1</div><span id="post-9208-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gutoandreollo has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><h2 id="display-filters-lua">Display Filters != Lua</h2><p>By "work on the GUI", are you referring to the <em>Display Filter Textbox</em>? As in: you enter <code>"f.bitmap1_b1_10000000 == 1"</code> into the textbox, which filters your packet list accordingly, but when you try that same predicate in Lua, it does not evaluate to <code>true</code>. Correct? If so, then you're incorrectly assuming the syntax is the same.</p><p>In your Lua, this line:</p><pre><code>if f.bitmap1_b1_10000000 == 1 then</code></pre><p>is comparing whether the <code>ProtoField</code> defined by <code>f.bitmap1_b1_10000000</code> is equal to <code>1</code>, which is nonsense because of a type mismatch. That should be a syntax error.</p><p>Maybe you meant to use the variable (with a similar name) you had declared earlier:</p><pre><code>if bitmap1_b1_10000000 == 1 then</code></pre><p>but that would be comparing a <code>TvbRange</code> with a <code>number</code>, which is the same syntax error as before.</p><p><br />
I'm not sure why this filter:</p><pre><code>f.bitmap1_b1_10000000 == &quot;Present&quot;</code></pre><p>does anything for you. That's comparing a boolean field (which presumably only accepts <code>0</code>, <code>1</code>, <code>false</code>, and <code>true</code>) to a string. I guess it could be comparing only the first byte of the string (empty string is <code>false</code>, else <code>true</code>).</p><h2 id="use-bit.band">Use <code>bit.band</code></h2><p>The <code>and</code> keyword is logical AND; not bitwise AND. You're looking for <code>bit.band</code> (which Wireshark Lua supports natively):</p><pre><code>if (bit.band( data(correct_offset,1):uint(), 0x80 ) == 0x80) then</code></pre><p><br />
Your original line always evaluates to <code>true</code>:</p><pre><code>if (data(correct_offset,1):uint() and 0x80) then</code></pre><p>In Lua, when non-<code>nil</code> objects are logically AND-ed, the result is always the last object. For example, <code>(1 and 0)</code> is <code>true</code> and results in <code>0</code>; and <code>(1 and nil)</code> is <code>false</code> and results in <code>nil</code>.</p><p>So, assuming <code>uint()</code> is never <code>nil</code>, the above line is equivalent to:</p><pre><code>if 0x80 then</code></pre><p>which is also:</p><pre><code>if true then</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Feb '12, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>26 Feb '12, 10:56</strong> </span></p></div></div><div id="comments-container-9208" class="comments-container"><span id="9217"></span><div id="comment-9217" class="comment"><div id="post-9217-score" class="comment-score"></div><div class="comment-text"><p>THANK YOU for your answer.</p><p>On each of the points: On TvbRange: I've found that both of them work, as long as there's a direct relationship between the variable and the TvbRange.. I really cannot see why it should work, but empirically (as of devel 1.7.0), it does.. o.O</p><p>On the display filter, I do realize it's different from Lua, but I had a glimmer of hope that it could maybe work, or at least accept the same syntax. "Present" (and it's opposite, "Not Present") are the binary value table for the variable (as defined on the ProtoField.Bool</p></div><div id="comment-9217-info" class="comment-info"><span class="comment-age">(26 Feb '12, 06:38)</span> <span class="comment-user userinfo">gutoandreollo</span></div></div><span id="9218"></span><div id="comment-9218" class="comment"><div id="post-9218-score" class="comment-score"></div><div class="comment-text"><p>On bit.band, THANK YOU once again for your answer! It works flawlessly! I'd tried bit32.band (as per the lua-users wiki), but its not implemented.. bit.band(), on the other hand, works just fine.</p><p>Now, the next step is: Is there a way to obtain the logical value (true/false) for a ProtoField.Bool? I'm getting to the point where I'm writing the post_dissector, and the variables aren't quite local anymore.. :(</p></div><div id="comment-9218-info" class="comment-info"><span class="comment-age">(26 Feb '12, 06:38)</span> <span class="comment-user userinfo">gutoandreollo</span></div></div><span id="9222"></span><div id="comment-9222" class="comment"><div id="post-9222-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I've found that both of them work, as long as there's a direct relationship between the variable and the TvbRange.. I really cannot see why it should work, but empirically (as of devel 1.7.0), it does..</p></blockquote><p>You're talking about the <strong>Use <code>TvbRange</code></strong> section. Ah, you're right. When I saw your <code>subtree:add</code> line without a <code>TvbRange</code>, I assumed that the variable used was something other than a <code>TvbRange</code> (such as a <code>number</code>), which is something I see done often. It turns out that variable was indeed a <code>TvbRange</code>, so that particular advice wasn't that helpful (oops, I'll proofread next time).</p></div><div id="comment-9222-info" class="comment-info"><span class="comment-age">(26 Feb '12, 10:57)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="9223"></span><div id="comment-9223" class="comment"><div id="post-9223-score" class="comment-score"></div><div class="comment-text"><p>To get the value of that <code>ProtoField</code>, you need to use a <a href="http://www.wireshark.org/docs/wsug_html_chunked/lua_module_Field.html#lua_class_Field"><code>Field</code></a>. Your mileage may vary as it's been reported to not extract fields defined from Lua. If that's the case, you'll have to re-parse your data in your post-dissector.</p></div><div id="comment-9223-info" class="comment-info"><span class="comment-age">(26 Feb '12, 11:12)</span> <span class="comment-user userinfo">helloworld</span></div></div></div><div id="comment-tools-9208" class="comment-tools"></div><div class="clear"></div><div id="comment-9208-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

