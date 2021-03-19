+++
type = "question"
title = "FIX Protocol dissector"
description = '''Good day. I need to extract data from the FIX protocol dissector(included in Wireshark) by using the LUA scripting. So I&#x27;m able to get all static fields by using extractor variable(for example, fe_FIX_MsgType = Field.new(&quot;fix.MsgType&quot;) ). But I found a problem while trying to extract all the fields ...'''
date = "2010-11-19T08:56:00Z"
lastmod = "2016-02-14T17:14:00Z"
weight = 1023
keywords = [ "lua", "fix", "dissector", "protocol" ]
aliases = [ "/questions/1023" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FIX Protocol dissector](/questions/1023/fix-protocol-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1023-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1023-score" class="post-score" title="current number of votes">0</div><span id="post-1023-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Good day. I need to extract data from the <strong>FIX protocol dissector</strong>(included in <strong>Wireshark</strong>) by using the <strong>LUA</strong> scripting. So I'm able to get all static fields by using extractor variable(for example, <strong>fe_FIX_MsgType = Field.new("fix.MsgType")</strong> ). But I found a problem while trying to extract all the fields of <strong>FIX protocol</strong> of such <strong>message type</strong> as <strong><code>Market Data - Snapshot / Full Refresh</code></strong>, where field <strong><code>NoMDEntries</code></strong> is dynamically changing and represents the number of next following fields. As you understand these fields use the same <strong>ProtoFields</strong> so that after dissecting one value, the other value overwrites it. That's why i can't extract all the needed values. Please help me in this question. How can I get all the fields??? Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-fix" rel="tag" title="see questions tagged &#39;fix&#39;">fix</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Nov '10, 08:56</strong></p><img src="https://secure.gravatar.com/avatar/e2ce68cf3e70fcaeaf2fa42357b49954?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="johndaw&#39;s gravatar image" /><p><span>johndaw</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="johndaw has no accepted answers">0%</span></p></div></div><div id="comments-container-1023" class="comments-container"></div><div id="comment-tools-1023" class="comment-tools"></div><div class="clear"></div><div id="comment-1023-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1139"></span>

<div id="answer-container-1139" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1139-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1139-score" class="post-score" title="current number of votes">1</div><span id="post-1139-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You probably need to ask field extractor to return a table. Run it in brackets {} like below</p><pre><code>fe_FIX_MsgType = Field.new(&quot;fix.MsgType&quot;)

local table_of_msg_types = { fe_FIX_MsgType() } 
for id,msg_type in pairs(table_of_msg_types)
do
    print(&quot;Doing something with Msg id: &quot;..id.&quot; type: &quot;..msg_type.value)
end</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Nov '10, 15:21</strong></p><img src="https://secure.gravatar.com/avatar/96df873546556d82f89c599816554877?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="izopizo&#39;s gravatar image" /><p><span>izopizo</span><br />
<span class="score" title="202 reputation points">202</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="izopizo has no accepted answers">0%</span></p></div></div><div id="comments-container-1139" class="comments-container"><span id="50189"></span><div id="comment-50189" class="comment"><div id="post-50189-score" class="comment-score"></div><div class="comment-text"><p><span>@johndaw</span> I want to know how to get the Fix dissector written in LUA which is included in wireshark. Can any one please point me.</p></div><div id="comment-50189-info" class="comment-info"><span class="comment-age">(14 Feb '16, 17:14)</span> <span class="comment-user userinfo">fixmessenger</span></div></div></div><div id="comment-tools-1139" class="comment-tools"></div><div class="clear"></div><div id="comment-1139-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

