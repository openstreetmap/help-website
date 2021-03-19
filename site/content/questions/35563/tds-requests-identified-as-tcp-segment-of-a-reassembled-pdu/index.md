+++
type = "question"
title = "TDS requests identified as [&#x27;TCP segment of a reassembled PDU]&#x27;"
description = '''I have a problem with the TDS protocol as every single request is being identified as [TCP segment of a reassembled PDU]. The packets originate from ASP scripts running in IIS 8.0 on Windows Server 2012. I have tried to analyze a wireshark dump with Microsoft Network Monitor 3.4 and while it does re...'''
date = "2014-08-19T03:49:00Z"
lastmod = "2014-08-20T01:21:00Z"
weight = 35563
keywords = [ "tds", "pdu", "protocol" ]
aliases = [ "/questions/35563" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [TDS requests identified as \['TCP segment of a reassembled PDU\]'](/questions/35563/tds-requests-identified-as-tcp-segment-of-a-reassembled-pdu)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35563-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35563-score" class="post-score" title="current number of votes">0</div><span id="post-35563-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a problem with the TDS protocol as every single request is being identified as [TCP segment of a reassembled PDU]. The packets originate from ASP scripts running in IIS 8.0 on Windows Server 2012. I have tried to analyze a wireshark dump with Microsoft Network Monitor 3.4 and while it does recognize the packets as TDS RPC Requests, it also fails to properly decode it.</p><p>Is there a known weakness decoding TDS RPC Requests?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tds" rel="tag" title="see questions tagged &#39;tds&#39;">tds</span> <span class="post-tag tag-link-pdu" rel="tag" title="see questions tagged &#39;pdu&#39;">pdu</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Aug '14, 03:49</strong></p><img src="https://secure.gravatar.com/avatar/b796380fa7643d02e9caeedce9d63427?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="galmok&#39;s gravatar image" /><p><span>galmok</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="galmok has no accepted answers">0%</span></p></div></div><div id="comments-container-35563" class="comments-container"><span id="35579"></span><div id="comment-35579" class="comment"><div id="post-35579-score" class="comment-score"></div><div class="comment-text"><p>The best way for us to answer the question is to be able to look at your capture.</p><p>Can you post a small capture (if there's no private data in the capture) which shows the problem on Google Drive or Dropbox, etc ?</p></div><div id="comment-35579-info" class="comment-info"><span class="comment-age">(19 Aug '14, 07:53)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="35580"></span><div id="comment-35580" class="comment"><div id="post-35580-score" class="comment-score"></div><div class="comment-text"><p>If there's reassembly going on, the example capture should have the entire application PDU (which may be split of multiple TCP segments).</p><p>Is there any chance the TDS protocol may be encrypted?</p></div><div id="comment-35580-info" class="comment-info"><span class="comment-age">(19 Aug '14, 08:12)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="35603"></span><div id="comment-35603" class="comment"><div id="post-35603-score" class="comment-score"></div><div class="comment-text"><p>I'll make a capture for you to look at. But I am not sure I can make a log that does not include sensitive/internal information, but if we can make this an iterative process where I filter the dump and you let me know if you need more, then I think this can work. I would prefer to mail the dropbox link to the dump instead of showing it for the public.</p></div><div id="comment-35603-info" class="comment-info"><span class="comment-age">(19 Aug '14, 23:20)</span> <span class="comment-user userinfo">galmok</span></div></div><span id="35604"></span><div id="comment-35604" class="comment"><div id="post-35604-score" class="comment-score"></div><div class="comment-text"><p>If you raise a bug on the <a href="https://bugs.wireshark.org/bugzilla/">Wireshark Bugzilla</a>, bugs\attachments can be marked as private so that only the Wireshark core developers have access to them. See also the wiki page on <a href="http://wiki.wireshark.org/ReportingBugs">reporting bugs</a>.</p></div><div id="comment-35604-info" class="comment-info"><span class="comment-age">(20 Aug '14, 01:21)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-35563" class="comment-tools"></div><div class="clear"></div><div id="comment-35563-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

