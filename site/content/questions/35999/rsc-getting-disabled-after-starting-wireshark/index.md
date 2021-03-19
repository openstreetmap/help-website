+++
type = "question"
title = "RSC getting disabled after starting wireshark"
description = '''RSC table before starting wireshark PS C:&#92;Users&#92;Administrator&amp;gt; get-netadapterrsc Name IPv4Enabled IPv6Enabled IPv4Operational IPv6Operational IPv4FailureReason IPv6Failure  State State Reason ---- ----------- ----------- --------------- --------------- ----------------- ------------ Ethernet 4 Tr...'''
date = "2014-09-04T05:26:00Z"
lastmod = "2014-09-04T07:24:00Z"
weight = 35999
keywords = [ "windows2012r2", "rsc" ]
aliases = [ "/questions/35999" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RSC getting disabled after starting wireshark](/questions/35999/rsc-getting-disabled-after-starting-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35999-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35999-score" class="post-score" title="current number of votes">0</div><span id="post-35999-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>RSC table before starting wireshark</p><p><code>PS C:\Users\Administrator&gt; get-netadapterrsc</code></p><code></code><p><code>Name        IPv4Enabled  IPv6Enabled  IPv4Operational IPv6Operational IPv4FailureReason IPv6Failure                                       State           State                             Reason ----        -----------  -----------  --------------- --------------- ----------------- ------------ Ethernet 4  True         True         True            True            NoFailure         NoFailure Ethernet 3  True         True         True            True            NoFailure         NoFailure</code></p><p>RSC table after starting wireshark.</p><p><code>PS C:\Users\Administrator&gt; get-netadapterrsc|format-table -wrap -autosize</code></p><code></code><p><code>Name       IPv4Enabled IPv6Enabled IPv4OperationalState IPv6OperationalState IPv4FailureReason IPv6FailureReason ----       ----------- ----------- -------------------- -------------------- ----------------- ----------------- Ethernet 4 True        True        False                False                NDISCompatibility NDISCompatibility Ethernet 3 True        True        False                False                NDISCompatibility NDISCompatibility</code></p><p>The above output is complaining about the NDIS for compatibility.</p><p>I want to stop RSC gettings disabled.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windows2012r2" rel="tag" title="see questions tagged &#39;windows2012r2&#39;">windows2012r2</span> <span class="post-tag tag-link-rsc" rel="tag" title="see questions tagged &#39;rsc&#39;">rsc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Sep '14, 05:26</strong></p><img src="https://secure.gravatar.com/avatar/a76c80d3ab3b8e4115206df2f80176b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Naveen1115&#39;s gravatar image" /><p><span>Naveen1115</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Naveen1115 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>04 Sep '14, 10:07</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-35999" class="comments-container"><span id="36003"></span><div id="comment-36003" class="comment"><div id="post-36003-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I want to stop RSC gettings disabled. You might have to pach WinPcap then. WinPcap is the "module" doing the actual capturing on Windows using NDIS 5 i beleve. Perhaps it needs to be updated to NDIS 6 to habdle RSC(?). Unfortunately WinPcap development seems to have stalled.</p></blockquote></div><div id="comment-36003-info" class="comment-info"><span class="comment-age">(04 Sep '14, 07:24)</span> <span class="comment-user userinfo">Anders ♦</span></div></div></div><div id="comment-tools-35999" class="comment-tools"></div><div class="clear"></div><div id="comment-35999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

