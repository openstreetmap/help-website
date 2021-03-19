+++
type = "question"
title = "LUA dissector field in display filter"
description = '''Hi, I&#x27;m trying to register some fields within a dissector, to be able to use them in the display filter. Tried different things but none of them worked, a simple example below :  DUMMYPROTOCOL = Proto (&quot;DUMMYPROTOCOL&quot;, &quot;B tcp Protocol&quot;) magic = ProtoField.uint32 (&quot;DUMMYPROTOCOL.magic&quot;, &quot;Magic&quot;) DUMM...'''
date = "2014-01-06T02:50:00Z"
lastmod = "2014-01-08T10:27:00Z"
weight = 28595
keywords = [ "lua", "dissector", "fields" ]
aliases = [ "/questions/28595" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [LUA dissector field in display filter](/questions/28595/lua-dissector-field-in-display-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28595-score" class="post-score" title="current number of votes">0</div><span id="post-28595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I'm trying to register some fields within a dissector, to be able to use them in the display filter. Tried different things but none of them worked, a simple example below :</p><pre><code>DUMMYPROTOCOL = Proto (&quot;DUMMYPROTOCOL&quot;, &quot;B tcp Protocol&quot;)
magic = ProtoField.uint32 (&quot;DUMMYPROTOCOL.magic&quot;, &quot;Magic&quot;)
DUMMYPROTOCOL.fields = { magic }

function DUMMYPROTOCOL.dissector (buffer, pinfo, tree)
  subtree = tree:add (DUMMYPROTOCOL, buffer())
  -- Modify columns
  pinfo.cols.protocol = DUMMYPROTOCOL.name
  pinfo.cols.info = &quot;PROTOCOL B&quot;
  subtree:add(&quot;hey&quot;)

  local offset = 0

while ( offset &lt; buffer:len() - 4) do
    if buffer(offset,4):uint() == 0x12345678 then
        subtree:add(magic,buffer(offset,4))
        break
    end
    offset = offset + 1
end</code></pre><p>end</p><p>The field doesn't seem to be registered properly, I get "isn't a valid display filter" "dommyprotocol.magic" is neither a field nor a protocol name, when trying to search for it. Any ideas ?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-fields" rel="tag" title="see questions tagged &#39;fields&#39;">fields</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Jan '14, 02:50</strong></p><img src="https://secure.gravatar.com/avatar/e4e8bc4618a9948a893ae407b22e8160?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lepolac&#39;s gravatar image" /><p><span>lepolac</span><br />
<span class="score" title="16 reputation points">16</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lepolac has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>06 Jan '14, 02:50</strong> </span></p></div></div><div id="comments-container-28595" class="comments-container"></div><div id="comment-tools-28595" class="comment-tools"></div><div class="clear"></div><div id="comment-28595-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28675"></span>

<div id="answer-container-28675" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28675-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28675-score" class="post-score" title="current number of votes">0</div><span id="post-28675-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I get "isn't a valid display filter" "dommyprotocol.magic"</p></blockquote><p>two things:</p><ol><li>the error message says: 'd<strong>o</strong>mmyprotocol.magic', whereas the code says 'D<strong>U</strong>MMYPROTOCOL.magic', but that might be just a typo ;-)</li><li>You defined the field all <strong>uppercase</strong>, so you'll have to <strong>search for the uppercase field</strong> as well. Please try to search for: <code>DUMMYPROTOCOL.magic</code><br />
</li></ol><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Jan '14, 09:13</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div></div><div id="comments-container-28675" class="comments-container"><span id="28678"></span><div id="comment-28678" class="comment"><div id="post-28678-score" class="comment-score"></div><div class="comment-text"><p>Hi, thanks for the reply. 1. yeah, typo :) 2. interestingly, I can search for the protocol name (DUMMYPROTOCOL) only in lowercase, even if defined in uppercase. Makes sense as 'tcp' work but not "TCP" for example. But regardless, it can't find the field.</p></div><div id="comment-28678-info" class="comment-info"><span class="comment-age">(08 Jan '14, 09:33)</span> <span class="comment-user userinfo">lepolac</span></div></div><span id="28679"></span><div id="comment-28679" class="comment"><div id="post-28679-score" class="comment-score"></div><div class="comment-text"><p>O.K. I did not yet check your code, so what happens, if you define all lowercase?</p><p>UPDATE: all lowercase works on my system (Windows - Wireshark 1.10.x)</p></div><div id="comment-28679-info" class="comment-info"><span class="comment-age">(08 Jan '14, 09:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28680"></span><div id="comment-28680" class="comment"><div id="post-28680-score" class="comment-score"></div><div class="comment-text"><p>I get the same error, "dummyprotocol.magic" isn't a valid display filter: "dummyprotocol.magic" is neither a field nor a protocol name. I've got 1.8.5. interesting...</p></div><div id="comment-28680-info" class="comment-info"><span class="comment-age">(08 Jan '14, 09:48)</span> <span class="comment-user userinfo">lepolac</span></div></div><span id="28681"></span><div id="comment-28681" class="comment"><div id="post-28681-score" class="comment-score"></div><div class="comment-text"><p>Can you please test with 1.10.x?</p></div><div id="comment-28681-info" class="comment-info"><span class="comment-age">(08 Jan '14, 10:27)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28675" class="comment-tools"></div><div class="clear"></div><div id="comment-28675-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

