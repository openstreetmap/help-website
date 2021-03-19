+++
type = "question"
title = "Not able to filter YMSG in wireshark packet sniffer!"
description = '''Hi there,I want to read the ymsg packets to understand its protocol at different request from the client,so I tried to use wireshark packet sniffer to trace the packets of Yahoo messanger.Wireshark is tracing the tcp,udp,https packets but I find no ymsg packets in the list even though I am using yah...'''
date = "2011-04-20T01:55:00Z"
lastmod = "2011-04-27T19:24:00Z"
weight = 3630
keywords = [ "filter", "ymsg", "wireshark" ]
aliases = [ "/questions/3630" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Not able to filter YMSG in wireshark packet sniffer!](/questions/3630/not-able-to-filter-ymsg-in-wireshark-packet-sniffer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3630-score" class="post-score" title="current number of votes">0</div><span id="post-3630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there,I want to read the ymsg packets to understand its protocol at different request from the client,so I tried to use wireshark packet sniffer to trace the packets of Yahoo messanger.Wireshark is tracing the tcp,udp,https packets but I find no ymsg packets in the list even though I am using yahoo messanger.Any idea why isnt working for me?</p><p>NOTE:I am using a proxy enabled network to connect to the internet.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-ymsg" rel="tag" title="see questions tagged &#39;ymsg&#39;">ymsg</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Apr '11, 01:55</strong></p><img src="https://secure.gravatar.com/avatar/decf6d3b968a9fdc7fe57656bf2ce8dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kiddo&#39;s gravatar image" /><p><span>kiddo</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kiddo has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Apr '11, 19:25</strong> </span></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span></p></div></div><div id="comments-container-3630" class="comments-container"><span id="3774"></span><div id="comment-3774" class="comment"><div id="post-3774-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any idea why isnt working for me?</p></blockquote><p>The short answer: no</p><p>The longer answer: you'll need to do some digging to see what's going on.</p><p>Wireshark has the capability to dissect the the YMSG protocol.</p><p>It looks for TCP packets which have YMSG as the first 4 bytes of the TCP payload.</p><p>(Continued in the next comment)</p></div><div id="comment-3774-info" class="comment-info"><span class="comment-age">(27 Apr '11, 19:23)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="3775"></span><div id="comment-3775" class="comment"><div id="post-3775-score" class="comment-score"></div><div class="comment-text"><p>The first thing I would do is to search the capture for the string "YMSG": Wireshark ! Edit ! Find packet.</p><p>If there are no frames with the string YMSG then there's something fishy about how the capture is being done or with the client. In this case you'd need to describe your [capture] setup:</p><p>Are you capturing on the same computer as the YMSG client is being run, etc etc...</p><p>If there are packets with the string YMSG (which are not dissected as YMSG) then the question becomes why aren't the packets recognized as YMSG.</p><p>So: first: Are there any packets with the string YMSG in your capture ?</p></div><div id="comment-3775-info" class="comment-info"><span class="comment-age">(27 Apr '11, 19:24)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div></div><div id="comment-tools-3630" class="comment-tools"></div><div class="clear"></div><div id="comment-3630-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

