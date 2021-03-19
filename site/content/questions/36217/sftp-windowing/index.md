+++
type = "question"
title = "SFTP Windowing"
description = '''I am troubleshooting an issue were large SFTP file transfers of &amp;gt; 3gb never reach speeds faster than 10mbs on a 25mbs circuit (there is no other traffic at the time of transfer). I understand the concept of how TCP windowing works. In researching the SFTP protocol I understand the SFTP does some ...'''
date = "2014-09-11T16:37:00Z"
lastmod = "2014-09-11T18:34:00Z"
weight = 36217
keywords = [ "windowing", "sftp" ]
aliases = [ "/questions/36217" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [SFTP Windowing](/questions/36217/sftp-windowing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36217-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36217-score" class="post-score" title="current number of votes">0</div><span id="post-36217-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am troubleshooting an issue were large SFTP file transfers of &gt; 3gb never reach speeds faster than 10mbs on a 25mbs circuit (there is no other traffic at the time of transfer). I understand the concept of how TCP windowing works. In researching the SFTP protocol I understand the SFTP does some form of its own windowing and further places restraints or limits on payload size that are much smaller than that is allowed in SSH2. As I don't have a capture yet to analyze. I am looking for advise as to what to look for?</p><p>Thank you for your time.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-windowing" rel="tag" title="see questions tagged &#39;windowing&#39;">windowing</span> <span class="post-tag tag-link-sftp" rel="tag" title="see questions tagged &#39;sftp&#39;">sftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '14, 16:37</strong></p><img src="https://secure.gravatar.com/avatar/5b20990cd21bd091665e684410ebe9fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdJ&#39;s gravatar image" /><p><span>EdJ</span><br />
<span class="score" title="16 reputation points">16</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdJ has no accepted answers">0%</span></p></div></div><div id="comments-container-36217" class="comments-container"></div><div id="comment-tools-36217" class="comment-tools"></div><div class="clear"></div><div id="comment-36217-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36218"></span>

<div id="answer-container-36218" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36218-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36218-score" class="post-score" title="current number of votes">0</div><span id="post-36218-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you have a situation where maximum theoretical speed can't be achieved (well, it is always a little less than the theoretical maximum, of course, even in best case situations), you need to look for where the time is lost. There are a couple of causes for lost time (the list is probably not close to complete, but just to have a few):</p><ul><li>The sender is not able to send the data fast enough (e.g. slow read speed on its disks)</li><li>The sender is slowed down by the receiver, e.g. low or even zero TCP window signaling</li><li>Packet loss, resulting in retransmissions which take time and reduce the throughput because the sender will throttle down to avoid further packet loss before accelerating again</li><li>The sender sends inefficient packet sizes, e.g. when TCP time stamps are enabled and the additional bytes force the payload to be split into multiple segments, one large segment and one small</li><li>delay by devices in the network path</li></ul><p>In Wireshark, you might want to take a look at the IOGraph in the statistics menu to see if there is a pattern. Otherwise, find the packets with the largest delta times and determine why those happen.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Sep '14, 18:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36218" class="comments-container"></div><div id="comment-tools-36218" class="comment-tools"></div><div class="clear"></div><div id="comment-36218-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

