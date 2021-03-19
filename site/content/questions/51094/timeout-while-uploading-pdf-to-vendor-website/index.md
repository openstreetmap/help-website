+++
type = "question"
title = "timeout while uploading pdf to vendor website"
description = '''Hello, I have a user that uses a website to upload a pdf files to a web site, when they try to upload the user sees the hour glass (circle) spinning and it eventually times out. This happens about 50% of the time. I have a wireshark capture and when looking for issues I see there is a time out with ...'''
date = "2016-03-22T08:26:00Z"
lastmod = "2016-03-22T08:57:00Z"
weight = 51094
keywords = [ "timeouts" ]
aliases = [ "/questions/51094" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [timeout while uploading pdf to vendor website](/questions/51094/timeout-while-uploading-pdf-to-vendor-website)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51094-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51094-score" class="post-score" title="current number of votes">0</div><span id="post-51094-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have a user that uses a website to upload a pdf files to a web site, when they try to upload the user sees the hour glass (circle) spinning and it eventually times out. This happens about 50% of the time.</p><p>I have a wireshark capture and when looking for issues I see there is a time out with the website being the source and the user's pc being the destination. I have reviewed the router settings with the vendor and we are NOT blocking the communication.</p><p>Any ideas of what to do to determine where the problem is?</p><p>The vendor says they do not have any issues with anyone else.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timeouts" rel="tag" title="see questions tagged &#39;timeouts&#39;">timeouts</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Mar '16, 08:26</strong></p><img src="https://secure.gravatar.com/avatar/f632b5c8ae227e2c79b4f4116fef01ab?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tucktech&#39;s gravatar image" /><p><span>tucktech</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tucktech has no accepted answers">0%</span></p></div></div><div id="comments-container-51094" class="comments-container"><span id="51096"></span><div id="comment-51096" class="comment"><div id="post-51096-score" class="comment-score"></div><div class="comment-text"><p>Many such issues are caused by wrong handling of MTU limitations somewhere on the path between the client and server, causing TCP segments to be lost due to unusually small MTU value on some portion of the network path combined with blocking of ICMP traffic requesting that the sender would segment the packet into smaller ones somewhere between this bottleneck and the sender. If you can, try to trim the MSS values in SYN packets forwarded by your router to smaller values and see whether it solves the issue (bear in mind that you have to trim the MSS value in both directions as you don't know which end does not receive the icmp feedback). Why it happens only in some cases could be explained by existence of several network paths between client and server, and only one of them to be dropping the icmp.</p><p>Look <a href="http://www.netfilter.org/documentation/HOWTO/netfilter-extensions-HOWTO.html#toc4.7">here</a> for maybe better explanation of what happens.</p></div><div id="comment-51096-info" class="comment-info"><span class="comment-age">(22 Mar '16, 08:57)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-51094" class="comment-tools"></div><div class="clear"></div><div id="comment-51094-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

