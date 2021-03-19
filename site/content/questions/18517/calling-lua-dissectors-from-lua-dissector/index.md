+++
type = "question"
title = "Calling Lua Dissectors from Lua Dissector"
description = '''I&#x27;m dealing with two custom protocols that use the same GRE protocol type. Each protocol currently has a separate Lua dissector (I&#x27;d like to keep it this way). I&#x27;m writing a script in Lua to perform some heuristics to determine which of the custom protocols is being used, with the idea that I&#x27;ll pas...'''
date = "2013-02-11T16:15:00Z"
lastmod = "2016-12-14T06:03:00Z"
weight = 18517
keywords = [ "lua", "dissector" ]
aliases = [ "/questions/18517" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Calling Lua Dissectors from Lua Dissector](/questions/18517/calling-lua-dissectors-from-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18517-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18517-score" class="post-score" title="current number of votes">0</div><span id="post-18517-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I'm dealing with two custom protocols that use the same GRE protocol type. Each protocol currently has a separate Lua dissector (I'd like to keep it this way). I'm writing a script in Lua to perform some heuristics to determine which of the custom protocols is being used, with the idea that I'll pass the packet off to the appropriate Lua dissector. I've got all of the heuristics written, but I can't quite figure how to call a dissector written in Lua from another dissector written in Lua. Do I need to create a new DissectorTable? How are the (final) two dissectors referenced (<code>dofile</code> in the new dissector, etc.)? Any pointers you can provide would be appreciated.</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Feb '13, 16:15</strong></p><img src="https://secure.gravatar.com/avatar/4109c74ac072d9252ecba5a3ff5366ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="krach09&#39;s gravatar image" /><p><span>krach09</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="krach09 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '13, 18:13</strong> </span></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span></p></div></div><div id="comments-container-18517" class="comments-container"></div><div id="comment-tools-18517" class="comment-tools"></div><div class="clear"></div><div id="comment-18517-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="18522"></span>

<div id="answer-container-18522" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-18522-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-18522-score" class="post-score" title="current number of votes">1</div><span id="post-18522-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should use <a href="http://wiki.wireshark.org/LuaAPI/Dissector#Dissector.get.28name.29"><code>Dissector.get</code></a>, which looks up the registered dissector by name -- no matter where you registered it (Lua or C). Then, use <a href="http://wiki.wireshark.org/LuaAPI/Dissector#dissector:call.28tvb.2C_pinfo.2C_tree.29"><code>Dissector:call</code></a>, passing the payload to be dissected (along with the packet info and protocol tree node).</p><p>From <a href="http://ask.wireshark.org/questions/10658/how-to-use-lua-to-write-multi-protocol-dissector-plugin">similar question</a>:</p><pre><code>function proto_lap5.dissector(buf, pinfo, tree)
    if buf:len() &gt; HEADER_LEN then
        -- create a new buffer containing only the XLES data,
        -- and pass it to the XLES dissector
        Dissector.get(&quot;xles&quot;):call(buf(HEADER_LEN):tvb(), pinfo, tree)
    end
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Feb '13, 18:11</strong></p><img src="https://secure.gravatar.com/avatar/362ba1008ad9a075d1556d33e97dfed6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="helloworld&#39;s gravatar image" /><p><span>helloworld</span><br />
<span class="score" title="3149 reputation points"><span>3.1k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="41 badges"><span class="bronze">●</span><span class="badgecount">41</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="helloworld has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Feb '13, 18:17</strong> </span></p></div></div><div id="comments-container-18522" class="comments-container"><span id="18524"></span><div id="comment-18524" class="comment"><div id="post-18524-score" class="comment-score"></div><div class="comment-text"><p>Since I am dealing with multiple custom protocols on top of the same GRE protocol type, how do I register all of the LUA dissectors at the same time without them conflicting?</p></div><div id="comment-18524-info" class="comment-info"><span class="comment-age">(11 Feb '13, 19:06)</span> <span class="comment-user userinfo">krach09</span></div></div><span id="18525"></span><div id="comment-18525" class="comment"><div id="post-18525-score" class="comment-score"></div><div class="comment-text"><p>You just need to use unique names for the dissectors in their <code>Proto</code> declarations (this is a requirement anyway).</p></div><div id="comment-18525-info" class="comment-info"><span class="comment-age">(11 Feb '13, 19:58)</span> <span class="comment-user userinfo">helloworld</span></div></div><span id="18548"></span><div id="comment-18548" class="comment"><div id="post-18548-score" class="comment-score"></div><div class="comment-text"><p>They are all using unique names. But if I have the following listed in init.lua:</p><p>dofile("file0.lua")<br />
dofile("file1.lua")<br />
dofile("file2.lua")</p><p>How does Wireshark know that file0.lua contains the logic to determine wether file1.lua or file2.lua should be used as the dissector?</p></div><div id="comment-18548-info" class="comment-info"><span class="comment-age">(12 Feb '13, 06:28)</span> <span class="comment-user userinfo">krach09</span></div></div><span id="18557"></span><div id="comment-18557" class="comment"><div id="post-18557-score" class="comment-score"></div><div class="comment-text"><p>I figured it out ... thanks.</p></div><div id="comment-18557-info" class="comment-info"><span class="comment-age">(12 Feb '13, 09:50)</span> <span class="comment-user userinfo">krach09</span></div></div><span id="58077"></span><div id="comment-58077" class="comment"><div id="post-58077-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>I am facing a similar issue. Can you please explain.</p></div><div id="comment-58077-info" class="comment-info"><span class="comment-age">(14 Dec '16, 06:03)</span> <span class="comment-user userinfo">spark</span></div></div></div><div id="comment-tools-18522" class="comment-tools"></div><div class="clear"></div><div id="comment-18522-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

