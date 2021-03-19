+++
type = "question"
title = "Convert table to Byte array using CLRPackage"
description = '''I&#x27;m trying to convert a Lua Table to a C# Byte array. I was able to get a conversion to a Double array to work as follows: &amp;gt; require &#x27;CLRPackage&#x27; &amp;gt; import &quot;System&quot; &amp;gt; tbl = {11,22,33,44} &amp;gt; dbl_arr = Double[4] &amp;gt; dbl_arr:GetValue(0) &amp;gt; dbl_arr:GetValue(1) &amp;gt; for i=0,3 do Console.Writ...'''
date = "2011-08-26T06:54:00Z"
lastmod = "2011-09-06T10:01:00Z"
weight = 5885
keywords = [ "lua", "luainterface", "clrpackage", ".net", "conversation" ]
aliases = [ "/questions/5885" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Convert table to Byte array using CLRPackage](/questions/5885/convert-table-to-byte-array-using-clrpackage)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5885-score" class="post-score" title="current number of votes">0</div><span id="post-5885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to convert a Lua Table to a C# <code>Byte</code> array. I was able to get a conversion to a <code>Double</code> array to work as follows:</p><pre><code>&gt; require &#39;CLRPackage&#39;
&gt; import &quot;System&quot;
&gt; tbl = {11,22,33,44}
&gt; dbl_arr = Double[4]
&gt; dbl_arr:GetValue(0)
&gt; dbl_arr:GetValue(1)
&gt; for i=0,3 do Console.WriteLine(dbl_arr:GetValue(i)) end
0
0
0
0
&gt; for i,v in ipairs(tbl) do dbl_arr:SetValue(v,i-1) end
&gt; for i=0,3 do Console.WriteLine(dbl_arr:GetValue(i)) end
11
22
33
44
&gt;</code></pre><p>However if I change the <code>dbl_arr</code> to a <code>Byte</code> array (<code>dbl_arr = Byte[4]</code>), then I get the following error: <code>(error object is not a string)</code></p><p>I was able to get a bit more information from the error by doing this:</p><pre><code>suc,err = pcall(function() byte_arr:SetValue(12,0) end)</code></pre><p>Now <code>suc</code> is false and <code>err</code> returns the following message:</p><pre><code>SetValue failed
System.ArgumentException: Cannot widen from source type to target type either
   because the source type is a not a primitive type or the conversion cannot
   be accomplished.
at System.Array.InternalSetValue(Void* target, Object value)
at System.Array.SetValue(Object value, Int32 index)</code></pre><p>I tried doing <code>Convert.ToByte(12)</code> and passing that in, but it still fails. I have a feeling its storing the intermediate results as a Lua 'number', which then automatically converts it to a C# Double. This is the only explanation I can come up with based on that error.</p><p>I've tried a bunch of different things with no luck. Any help would be appreciated.</p><p>I've also asked <a href="http://stackoverflow.com/questions/7167229/convert-table-to-byte-array">this question</a> on Stackoverflow to try and get some answers. I thought I would try here since it seems like Lua would be used more by people involved with Wireshark.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-luainterface" rel="tag" title="see questions tagged &#39;luainterface&#39;">luainterface</span> <span class="post-tag tag-link-clrpackage" rel="tag" title="see questions tagged &#39;clrpackage&#39;">clrpackage</span> <span class="post-tag tag-link-.net" rel="tag" title="see questions tagged &#39;.net&#39;">.net</span> <span class="post-tag tag-link-conversation" rel="tag" title="see questions tagged &#39;conversation&#39;">conversation</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Aug '11, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/8ceec9f7f83e3c12a72b6442393bde2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SwDevMan81&#39;s gravatar image" /><p><span>SwDevMan81</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SwDevMan81 has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Sep '11, 10:37</strong> </span></p></div></div><div id="comments-container-5885" class="comments-container"><span id="5893"></span><div id="comment-5893" class="comment"><div id="post-5893-score" class="comment-score"></div><div class="comment-text"><p>Off topic? You might get better results from <a href="http://stackoverflow.com">stackoverflow.com</a>.</p></div><div id="comment-5893-info" class="comment-info"><span class="comment-age">(26 Aug '11, 14:31)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="5963"></span><div id="comment-5963" class="comment"><div id="post-5963-score" class="comment-score"></div><div class="comment-text"><p>I did try SO first, but didnt get any response. I was hoping someone here might have run into this while using Wireshark or might have some ideas. I've linked the SO question in my original question.</p></div><div id="comment-5963-info" class="comment-info"><span class="comment-age">(30 Aug '11, 11:05)</span> <span class="comment-user userinfo">SwDevMan81</span></div></div></div><div id="comment-tools-5885" class="comment-tools"></div><div class="clear"></div><div id="comment-5885-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6129"></span>

<div id="answer-container-6129" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6129-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6129-score" class="post-score" title="current number of votes">1</div><span id="post-6129-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SwDevMan81 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I found a workaround for this issue. I'll post it here, although I'm still curious why the above doesn't work.</p><p>Here is the workaround. I basically create a <code>MemoryStream</code> and use the <code>WriteByte</code> function to force the value to a Byte (since there is no overload of the function, it only accepts a byte). Then I call <code>ToArray</code> to get the <code>byte[]</code> from the <code>MemoryStream</code>:</p><pre><code>&gt; require &#39;CLRPackage&#39;
&gt; import &quot;System&quot;
&gt; tbl = {11,22,33,44}
&gt; mem_stream = MemoryStream()
&gt; for i,v in ipairs(tbl) do mem_stream:WriteByte(v) end
&gt; byte_arr = mem_stream:ToArray()
&gt; for i=0,byte_arr.Length-1 do Console.WriteLine(string.format(&quot;%d&quot;, byte_arr:GetValue(i))) end
11
22
33
44</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '11, 10:01</strong></p><img src="https://secure.gravatar.com/avatar/8ceec9f7f83e3c12a72b6442393bde2a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SwDevMan81&#39;s gravatar image" /><p><span>SwDevMan81</span><br />
<span class="score" title="36 reputation points">36</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SwDevMan81 has one accepted answer">50%</span></p></div></div><div id="comments-container-6129" class="comments-container"></div><div id="comment-tools-6129" class="comment-tools"></div><div class="clear"></div><div id="comment-6129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

