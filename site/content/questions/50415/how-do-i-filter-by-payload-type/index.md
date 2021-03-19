+++
type = "question"
title = "How do I filter by payload type?"
description = '''Given my raw pcap I go to Telephony &amp;gt; RTP &amp;gt; show all streams. I have 2 streams of h264 and 2 streams of mp4-latm. I have a method in my script to obtain and iterate through ssrc values. However, it iterates through a variable which contains all four ssrc values. I need a filter to parse out th...'''
date = "2016-02-22T10:50:00Z"
lastmod = "2016-02-22T14:22:00Z"
weight = 50415
keywords = [ "type", "payload", "stream", "rtp" ]
aliases = [ "/questions/50415" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How do I filter by payload type?](/questions/50415/how-do-i-filter-by-payload-type)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50415-score" class="post-score" title="current number of votes">0</div><span id="post-50415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Given my raw pcap I go to Telephony &gt; RTP &gt; show all streams.</p><p>I have 2 streams of h264 and 2 streams of mp4-latm. I have a method in my script to obtain and iterate through ssrc values. However, it iterates through a variable which contains all four ssrc values. I need a filter to parse out the mp4-latm.</p><p>rtp.p_type==h264 does not work. I still see the ssrc for mp4-latm.</p><p>I need a read filter which only reads through h264 payload type field, and NOT mp4-latm field. Help would me much appreciated, thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-type" rel="tag" title="see questions tagged &#39;type&#39;">type</span> <span class="post-tag tag-link-payload" rel="tag" title="see questions tagged &#39;payload&#39;">payload</span> <span class="post-tag tag-link-stream" rel="tag" title="see questions tagged &#39;stream&#39;">stream</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>22 Feb '16, 10:50</strong></p><img src="https://secure.gravatar.com/avatar/2a64be647ac8ec21b76a6c042bebb6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testname0110&#39;s gravatar image" /><p><span>testname0110</span><br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testname0110 has 3 accepted answers">75%</span></p></div></div><div id="comments-container-50415" class="comments-container"></div><div id="comment-tools-50415" class="comment-tools"></div><div class="clear"></div><div id="comment-50415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50417"></span>

<div id="answer-container-50417" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50417-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50417-score" class="post-score" title="current number of votes">0</div><span id="post-50417-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="testname0110 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>figured it out. You want to add the read filter to your tshark command:</p><p>"-2 -R rtp.p_type==xxx" where "xxx" is the number of your dynamic payload type.</p><p>the dynamic payload type should be readable from your wireshark pcap file and is a number like 96 or 126</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Feb '16, 14:22</strong></p><img src="https://secure.gravatar.com/avatar/2a64be647ac8ec21b76a6c042bebb6e4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="testname0110&#39;s gravatar image" /><p><span>testname0110</span><br />
<span class="score" title="15 reputation points">15</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="testname0110 has 3 accepted answers">75%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>22 Feb '16, 14:23</strong> </span></p></div></div><div id="comments-container-50417" class="comments-container"></div><div id="comment-tools-50417" class="comment-tools"></div><div class="clear"></div><div id="comment-50417-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

