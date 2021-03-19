+++
type = "question"
title = "how to extract memcache value"
description = '''I have a few pcap files, I can see the memcache protocol in wireshark and its corresponding data, but when I use tshark to batch export data, it only shows one character(0x0b), anyone knows why?  the command I use: tshark -Y &quot;memcache contains set&quot; -r input.pcap -T fields -e memcache.value  Thank yo...'''
date = "2016-10-15T21:51:00Z"
lastmod = "2016-10-16T03:21:00Z"
weight = 56419
keywords = [ "memcache", "tshark", "wireshark" ]
aliases = [ "/questions/56419" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how to extract memcache value](/questions/56419/how-to-extract-memcache-value)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-56419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-56419-score" class="post-score" title="current number of votes">0</div><span id="post-56419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a few pcap files, I can see the memcache protocol in wireshark and its corresponding data, but when I use tshark to batch export data, it only shows one character(0x0b), anyone knows why?</p><p>the command I use: tshark -Y "memcache contains set" -r input.pcap -T fields -e memcache.value Thank you! BTW, memcache key works fine.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-memcache" rel="tag" title="see questions tagged &#39;memcache&#39;">memcache</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Oct '16, 21:51</strong></p><img src="https://secure.gravatar.com/avatar/48901a8156df6f726c326ab0bf35703d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="1a1a11a&#39;s gravatar image" /><p><span>1a1a11a</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="1a1a11a has no accepted answers">0%</span></p></div></div><div id="comments-container-56419" class="comments-container"><span id="56420"></span><div id="comment-56420" class="comment"><div id="post-56420-score" class="comment-score"></div><div class="comment-text"><p>Is there just a single (key,value) pair per a memcached network message or more? For analysis by anyone else than the author of the dissector, an example of capture file is necessary. You can upload it to Cloudshark (which is the preferred method here) or to any generic file sharing service and edit your question with a login-free link to it.</p></div><div id="comment-56420-info" class="comment-info"><span class="comment-age">(16 Oct '16, 03:21)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-56419" class="comment-tools"></div><div class="clear"></div><div id="comment-56419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

