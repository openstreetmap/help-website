+++
type = "question"
title = "Which device/setup could create duplicate tcp acks ?"
description = '''Hello, i´m troubeshooting an network issue in our network environment. What i see is a high number (up to 400%) of duplicated tcp acknowledgements in our traffic. The timestamps of these packet are neary equal. The percentage of regular tcp packets is real low ( &amp;lt;1%). So the only duplicated packe...'''
date = "2013-05-31T04:50:00Z"
lastmod = "2013-05-31T05:07:00Z"
weight = 21649
keywords = [ "duplicate", "acks", "tcp" ]
aliases = [ "/questions/21649" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Which device/setup could create duplicate tcp acks ?](/questions/21649/which-devicesetup-could-create-duplicate-tcp-acks)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-21649-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-21649-score" class="post-score" title="current number of votes">0</div><span id="post-21649-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i´m troubeshooting an network issue in our network environment. What i see is a high number (up to 400%) of duplicated tcp acknowledgements in our traffic. The timestamps of these packet are neary equal. The percentage of regular tcp packets is real low ( &lt;1%). So the only duplicated packets are the tcp acks.</p><p>This are three packets i´ve captured:</p><pre><code>415 7.506864    source-ip   destination-ip  TCP 66  [TCP Dup ACK 193#1] http &gt; 9740 [ACK] Seq=1944 Ack=446 Win=65090 Len=0 TSval=989488 TSecr=1913040616

416 7.507888    source-ip   destination-ip  TCP 66  [TCP Dup ACK 242#1] http &gt; 34887 [ACK] Seq=2515 Ack=411 Win=65125 Len=0 TSval=989488 TSecr=1913040616

417 7.508328    source-ip   destination-ip  TCP 66  [TCP Dup ACK 306#1] http &gt; 47222 [ACK] Seq=9500 Ack=434 Win=65102 Len=0 TSval=989488 TSecr=1913040616</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-duplicate" rel="tag" title="see questions tagged &#39;duplicate&#39;">duplicate</span> <span class="post-tag tag-link-acks" rel="tag" title="see questions tagged &#39;acks&#39;">acks</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 May '13, 04:50</strong></p><img src="https://secure.gravatar.com/avatar/e1d5b4e8f4d270d656d00e11a093fb92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mn44&#39;s gravatar image" /><p><span>mn44</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mn44 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 May '13, 05:15</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-21649" class="comments-container"><span id="21651"></span><div id="comment-21651" class="comment"><div id="post-21651-score" class="comment-score"></div><div class="comment-text"><p>You can look mac,ip id etc to see if its really a dup ack,in our setup we have riverbed device where when server sends ack,riverbed again forwards it,so we identify it by looking mac,it keeps changing so its normal behaviour.</p></div><div id="comment-21651-info" class="comment-info"><span class="comment-age">(31 May '13, 05:07)</span> <span class="comment-user userinfo">kishan pandey</span></div></div></div><div id="comment-tools-21649" class="comment-tools"></div><div class="clear"></div><div id="comment-21649-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

