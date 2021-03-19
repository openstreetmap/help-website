+++
type = "question"
title = "Slow network speed Can anyone tell me whats wrong ?"
description = '''Hello I got problems with slow network. About 15 MB/S I dont know why I get this ? I think I should&#x27;nt get all those LEN=0 I need some advice 192.168.0.202 Windows 8.1 client 192.168.0.2 solaris server http://s15.postimg.org/bqu69yw57/packets.jpg Thanks Casper.'''
date = "2015-06-08T14:05:00Z"
lastmod = "2015-06-08T16:39:00Z"
weight = 42987
keywords = [ "performance", "slow", "solaris", "network" ]
aliases = [ "/questions/42987" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Slow network speed Can anyone tell me whats wrong ?](/questions/42987/slow-network-speed-can-anyone-tell-me-whats-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42987-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42987-score" class="post-score" title="current number of votes">0</div><span id="post-42987-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello I got problems with slow network.</p><p>About 15 MB/S I dont know why I get this ? I think I should'nt get all those LEN=0</p><p>I need some advice</p><p>192.168.0.202 Windows 8.1 client 192.168.0.2 solaris server</p><p><a href="http://s15.postimg.org/bqu69yw57/packets.jpg">http://s15.postimg.org/bqu69yw57/packets.jpg</a></p><p>Thanks Casper.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-slow" rel="tag" title="see questions tagged &#39;slow&#39;">slow</span> <span class="post-tag tag-link-solaris" rel="tag" title="see questions tagged &#39;solaris&#39;">solaris</span> <span class="post-tag tag-link-network" rel="tag" title="see questions tagged &#39;network&#39;">network</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>08 Jun '15, 14:05</strong></p><img src="https://secure.gravatar.com/avatar/09730f485aca964b69597659669f9b4f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Reb00t&#39;s gravatar image" /><p><span>Reb00t</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Reb00t has no accepted answers">0%</span></p></div></div><div id="comments-container-42987" class="comments-container"><span id="42988"></span><div id="comment-42988" class="comment"><div id="post-42988-score" class="comment-score"></div><div class="comment-text"><p>Could you provide us a trace on cloudshark or dropbox?</p></div><div id="comment-42988-info" class="comment-info"><span class="comment-age">(08 Jun '15, 14:14)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="42989"></span><div id="comment-42989" class="comment"><div id="post-42989-score" class="comment-score"></div><div class="comment-text"><p>Another option is to upload it here, then post the URL (assuming the data is not confidential): <a href="https://appliance.cloudshark.org/upload/">https://appliance.cloudshark.org/upload/</a></p><p>It's hard to speculate from the picture, except to say that those LEN=0 aren't a problem - it is very common for TCP clients to send an ACK message without bytes of payload, thus payload lengths of 0.</p><p>Edit:</p><p>Note that from the TCP Ack number progress it looks like the client received 230680 bytes in a time period of 0.001355 seconds. That's at least a microburst of ~170 MB/s.</p></div><div id="comment-42989-info" class="comment-info"><span class="comment-age">(08 Jun '15, 16:39)</span> <span class="comment-user userinfo">Quadratic</span></div></div></div><div id="comment-tools-42987" class="comment-tools"></div><div class="clear"></div><div id="comment-42987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

