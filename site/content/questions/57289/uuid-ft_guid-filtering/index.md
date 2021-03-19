+++
type = "question"
title = "UUID (FT_GUID) Filtering"
description = '''Hello all,  I was working with a pcap file and I tested following filter definition:  the filter &quot;dcerpc.dg_act_id&quot; works the filter &quot;dcerpc.dg_act_id == 0c41f903-0000-1010-b841-123412341236&quot; doesn&#x27;t work.   Do I use the filter correctly or is there a bug about filtering UUID?'''
date = "2016-11-10T22:17:00Z"
lastmod = "2016-11-11T04:33:00Z"
weight = 57289
keywords = [ "filter", "uuid", "dcerpc" ]
aliases = [ "/questions/57289" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [UUID (FT\_GUID) Filtering](/questions/57289/uuid-ft_guid-filtering)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57289-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57289-score" class="post-score" title="current number of votes">0</div><span id="post-57289-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all,</p><p>I was working with a pcap file and I tested following filter definition:</p><ul><li>the filter "dcerpc.dg_act_id" works</li><li>the filter "dcerpc.dg_act_id == 0c41f903-0000-1010-b841-123412341236" doesn't work.</li></ul><p>Do I use the filter correctly or is there a bug about filtering UUID?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-uuid" rel="tag" title="see questions tagged &#39;uuid&#39;">uuid</span> <span class="post-tag tag-link-dcerpc" rel="tag" title="see questions tagged &#39;dcerpc&#39;">dcerpc</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Nov '16, 22:17</strong></p><img src="https://secure.gravatar.com/avatar/6257a856e7271c04dd39469c7a5332ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="BirolCapa&#39;s gravatar image" /><p><span>BirolCapa</span><br />
<span class="score" title="30 reputation points">30</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="BirolCapa has no accepted answers">0%</span></p></div></div><div id="comments-container-57289" class="comments-container"><span id="57303"></span><div id="comment-57303" class="comment"><div id="post-57303-score" class="comment-score"></div><div class="comment-text"><p>I don't have a capture file with this field in it to test things with. It would help if you could supply one (you can use <a href="https://www.cloudshark.org/">cloudshark</a> or any online file sharing service)</p></div><div id="comment-57303-info" class="comment-info"><span class="comment-age">(11 Nov '16, 03:43)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div><span id="57305"></span><div id="comment-57305" class="comment"><div id="post-57305-score" class="comment-score"></div><div class="comment-text"><p>Hello, thank you for your feedback. You may access the related pcap file by using the following link:</p><p><a href="http://bit.ly/2fHdRLL">http://bit.ly/2fHdRLL</a></p></div><div id="comment-57305-info" class="comment-info"><span class="comment-age">(11 Nov '16, 03:49)</span> <span class="comment-user userinfo">BirolCapa</span></div></div></div><div id="comment-tools-57289" class="comment-tools"></div><div class="clear"></div><div id="comment-57289-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57308"></span>

<div id="answer-container-57308" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57308-score" class="post-score" title="current number of votes">0</div><span id="post-57308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Thanks for the pcap, it looks like all filtering on fields of type "Globally Unique Identifier" are failing in wireshark 2.2.1 and while they are working in wireshark 1.12.13.</p><p>Could you file a bug report on <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a>? Please also attach the capture file to the bug for bugfixing/testing purposes.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Nov '16, 04:08</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Nov '16, 04:08</strong> </span></p></div></div><div id="comments-container-57308" class="comments-container"><span id="57313"></span><div id="comment-57313" class="comment"><div id="post-57313-score" class="comment-score"></div><div class="comment-text"><p>Hello, I created a bug report:</p><p>Bug 13121 - UUID (FT_GUID) Filtering (edit)</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13121">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=13121</a></p></div><div id="comment-57313-info" class="comment-info"><span class="comment-age">(11 Nov '16, 04:33)</span> <span class="comment-user userinfo">BirolCapa</span></div></div></div><div id="comment-tools-57308" class="comment-tools"></div><div class="clear"></div><div id="comment-57308-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

