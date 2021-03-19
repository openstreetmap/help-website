+++
type = "question"
title = "tshark SIP Statistics"
description = '''Folks, Is there to way to get successful vs unsuccessful calls in a given pcap using tshark command line? I am using the example below and get some stats, but would need more. Also, no matter which pcap I use, the average set up is always showing up as 0, what am i missing?(there are definitely a lo...'''
date = "2013-11-14T13:44:00Z"
lastmod = "2013-11-14T13:44:00Z"
weight = 27018
keywords = [ "sip", "tshark" ]
aliases = [ "/questions/27018" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [tshark SIP Statistics](/questions/27018/tshark-sip-statistics)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-27018-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-27018-score" class="post-score" title="current number of votes">0</div><span id="post-27018-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Folks,</p><p>Is there to way to get successful vs unsuccessful calls in a given pcap using tshark command line? I am using the example below and get some stats, but would need more. Also, no matter which pcap I use, the average set up is always showing up as 0, what am i missing?(there are definitely a lot of successfull calls in the files i am reading)</p><p>tshark -r sharktest.pcap -q -z sip,stat</p><pre><code>===================================================================
SIP Statistics

Number of SIP messages: 28
Number of resent SIP messages: 25

* SIP Status Codes in reply packets
  SIP 200 OK              :    12 Packets

* List of SIP Request methods
  INVITE          :     4 Packets
  BYE             :    12 Packets

* Average setup time 0 ms
 Min 0 ms
 Max 0 ms</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sip" rel="tag" title="see questions tagged &#39;sip&#39;">sip</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Nov '13, 13:44</strong></p><img src="https://secure.gravatar.com/avatar/d58b21f800db1ae1de34adf888895c02?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sharkdcl&#39;s gravatar image" /><p><span>sharkdcl</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sharkdcl has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Nov '13, 14:58</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-27018" class="comments-container"></div><div id="comment-tools-27018" class="comment-tools"></div><div class="clear"></div><div id="comment-27018-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

