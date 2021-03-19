+++
type = "question"
title = "How to capture packets of specific application who keeps changing its ports periodically?"
description = '''Hello,  I am a naive user of wireshark. I am working on a project that requires capturing packets of Skype. However, this application uses random port and it keeps changing it&#x27;s port periodically and randomly. Is there any way to capture packets of such an application? Thanks.'''
date = "2016-08-21T04:25:00Z"
lastmod = "2016-08-25T08:49:00Z"
weight = 55021
keywords = [ "packet-capture" ]
aliases = [ "/questions/55021" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to capture packets of specific application who keeps changing its ports periodically?](/questions/55021/how-to-capture-packets-of-specific-application-who-keeps-changing-its-ports-periodically)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55021-score" class="post-score" title="current number of votes">0</div><span id="post-55021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am a naive user of wireshark. I am working on a project that requires capturing packets of Skype. However, this application uses random port and it keeps changing it's port periodically and randomly. Is there any way to capture packets of such an application?</p><p>Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packet-capture" rel="tag" title="see questions tagged &#39;packet-capture&#39;">packet-capture</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Aug '16, 04:25</strong></p><img src="https://secure.gravatar.com/avatar/5c4b121a17aec061db4833cb49d74dc9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="harshil7924&#39;s gravatar image" /><p><span>harshil7924</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="harshil7924 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Aug '16, 04:26</strong> </span></p></div></div><div id="comments-container-55021" class="comments-container"><span id="55033"></span><div id="comment-55033" class="comment"><div id="post-55033-score" class="comment-score">1</div><div class="comment-text"><p>If you capture all traffic, then by definition, even if the port changes, you will have those frames on the new port. I think that answers your question, but I suspect you really want more: you want to capture the frames, and easily identify them for some type of analysis.</p><p>Is there anything in the packets themselves that help identify what they are? Any other information that is consistent across the packets, that is NOT related to TCP or UDP port?</p><p>Some protocols require special helper modules for handling. For example, FTP uses a separate port for data transfer and can be random so most firewalls have difficulty with this random port change. The helper module follows the command stream and detects the port change and then auto-configures appropriately to allow for this. Maybe your protocol has such a module, and you can make use of it somehow? For instance, if this exists, you could be all set:</p><p>Sniffing using iptables - <a href="https://www.honeynet.org/node/691">https://www.honeynet.org/node/691</a></p></div><div id="comment-55033-info" class="comment-info"><span class="comment-age">(21 Aug '16, 14:07)</span> <span class="comment-user userinfo">Bob Jones</span></div></div><span id="55117"></span><div id="comment-55117" class="comment"><div id="post-55117-score" class="comment-score"></div><div class="comment-text"><p>Thanks Jones for answer. My project is just about Skype traffic classification and analysis. I need to capture the Skype traffic and train my classifier. The payload of Skype packets are encrypted, so I can't identify on basis of them.</p></div><div id="comment-55117-info" class="comment-info"><span class="comment-age">(25 Aug '16, 08:49)</span> <span class="comment-user userinfo">harshil7924</span></div></div></div><div id="comment-tools-55021" class="comment-tools"></div><div class="clear"></div><div id="comment-55021-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

