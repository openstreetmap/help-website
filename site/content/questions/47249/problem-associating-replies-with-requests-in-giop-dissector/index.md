+++
type = "question"
title = "Problem associating replies with requests in GIOP dissector"
description = '''The GIOP dissector tries to associate replies with requests. It does this by comparing the request ID. Unfortunately, this isn&#x27;t good enough. When there are multiple connections, the same request ID can get used on different connections. So it needs to check IP address and port number too. I have ma...'''
date = "2015-11-04T09:32:00Z"
lastmod = "2015-11-04T09:32:00Z"
weight = 47249
keywords = [ "dissector", "giop" ]
aliases = [ "/questions/47249" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem associating replies with requests in GIOP dissector](/questions/47249/problem-associating-replies-with-requests-in-giop-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-47249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-47249-score" class="post-score" title="current number of votes">0</div><span id="post-47249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>The GIOP dissector tries to associate replies with requests. It does this by comparing the request ID. Unfortunately, this isn't good enough. When there are multiple connections, the same request ID can get used on different connections. So it needs to check IP address and port number too.</p><p>I have made some changes to packet-giop.c to extend the list of requests to include source address and port number. Then when searching for a matching frame number it checks port &amp; ip address too.</p><p>This works well, except I appear to have to check the wrong IP address. So before submitting this as a change I'd like to know why.</p><p>I'm getting the addresses from the packet_info structure. The list stores pinfo-&gt;src &amp; pinfo-&gt;srcport. Then to get it to work, when searching for a matching request, using the packet_info of the reply, it compares the stored values with pinfo-&gt;src &amp; pinfo-&gt;dstport.</p><p>I would have expected the IP address to be pinfo-&gt;dst, not src. After all, the reply is sending back to the IP that sent the request and it is the destination port that is required, but if I change it to use dst it doesn't work.</p><p>Can someone explain why this is</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-giop" rel="tag" title="see questions tagged &#39;giop&#39;">giop</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Nov '15, 09:32</strong></p><img src="https://secure.gravatar.com/avatar/3d25bda262a989924649329d5e0b6b0b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Ling&#39;s gravatar image" /><p><span>Andy Ling</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Ling has no accepted answers">0%</span></p></div></div><div id="comments-container-47249" class="comments-container"></div><div id="comment-tools-47249" class="comment-tools"></div><div class="clear"></div><div id="comment-47249-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

