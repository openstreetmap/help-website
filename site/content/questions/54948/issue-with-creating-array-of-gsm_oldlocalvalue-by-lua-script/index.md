+++
type = "question"
title = "Issue with creating array of gsm_old.localValue by Lua Script"
description = '''HI I think that it is a bug, but i decided to talk about it and if it is so then I will create the bug. I have a multi chunk frame.  In this frame first chunk has GSM_MAP protocol and inside this protocol there is gsm_old.opCode and inside it there is gsm_old.localValue = 1 In this frame second chun...'''
date = "2016-08-18T07:38:00Z"
lastmod = "2016-08-19T01:18:00Z"
weight = 54948
keywords = [ "errorcode", "lua", "opcode", "gsm_old.localvalue" ]
aliases = [ "/questions/54948" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Issue with creating array of gsm\_old.localValue by Lua Script](/questions/54948/issue-with-creating-array-of-gsm_oldlocalvalue-by-lua-script)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-54948-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-54948-score" class="post-score" title="current number of votes">0</div><span id="post-54948-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p><strong>HI</strong></p><p>I think that it is a bug, but i decided to talk about it and if it is so then I will create the bug.</p><p>I have a multi chunk frame.</p><p>In this frame first chunk has GSM_MAP protocol and inside this protocol there is gsm_old.opCode and inside it there is gsm_old.localValue = 1</p><p>In this frame second chunk has GSM_MAP protocol and inside this protocol there is gsm_old.opCode and inside it there is gsm_old.localValue = 2</p><p>In this frame second chunk has GSM_MAP protocol and inside this protocol there is gsm_old.errorCode and inside it there is gsm_old.localValue = 3</p><pre><code>1 chunk-&gt;GSM_MAP-&gt;gsm_old.opCode-&gt;gsm_old.localValue = 1
2 chunk-&gt;GSM_MAP-&gt;gsm_old.opCode-&gt;gsm_old.localValue = 2
3 chunk-&gt;GSM_MAP-&gt;gsm_old.errorCode-&gt;gsm_old.localValue = 3</code></pre><p>I created lua script in which I used dissector table "sctp.ppi" or "gsm_map". And when I get the array of</p><pre><code>local gsm_old_localvalue = Field.new (&quot;gsm_old.localValue&quot;)</code></pre><p>by command</p><pre><code>local Gsm_Old_LocaLvalue_Array = { gsm_old_localvalue () }</code></pre><p>I get the following array</p><pre><code>Gsm_Old_LocalValue_Array[1]=3
Gsm_Old_LocalValue_Array[2]=1
Gsm_Old_LocalValue_Array[3]=2</code></pre><p>As you can see the order of gsm_old.localValue is incorrect in array. Because the order should be the following</p><pre><code>Gsm_Old_LocalValue_Array[1]=1
Gsm_Old_LocalValue_Array[2]=2
Gsm_Old_LocalValue_Array[3]=3</code></pre><p>As we can see this issue happens with gsm_old.localValue that contains in gsm_old.errorCode. In this case the value puts in the first place of the array. If there is not gsm_old.errorCode in every chunk of the one frame then the order of gsm_old.localValue in array is correct.</p><p>Can somebody explain me the root cause of this issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-errorcode" rel="tag" title="see questions tagged &#39;errorcode&#39;">errorcode</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-opcode" rel="tag" title="see questions tagged &#39;opcode&#39;">opcode</span> <span class="post-tag tag-link-gsm_old.localvalue" rel="tag" title="see questions tagged &#39;gsm_old.localvalue&#39;">gsm_old.localvalue</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '16, 07:38</strong></p><img src="https://secure.gravatar.com/avatar/2d7d6eacf9c502b9188b233cb3e1d8ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="domeno&#39;s gravatar image" /><p><span>domeno</span><br />
<span class="score" title="21 reputation points">21</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="domeno has no accepted answers">0%</span></p></div></div><div id="comments-container-54948" class="comments-container"><span id="54969"></span><div id="comment-54969" class="comment"><div id="post-54969-score" class="comment-score"></div><div class="comment-text"><p>The problem is the same as in</p><p><a href="https://www.wireshark.org/lists/wireshark-users/201111/msg00083.html">https://www.wireshark.org/lists/wireshark-users/201111/msg00083.html</a></p><p>I think in new version we have the same problem.</p></div><div id="comment-54969-info" class="comment-info"><span class="comment-age">(19 Aug '16, 01:18)</span> <span class="comment-user userinfo">domeno</span></div></div></div><div id="comment-tools-54948" class="comment-tools"></div><div class="clear"></div><div id="comment-54948-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

