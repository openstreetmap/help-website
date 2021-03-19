+++
type = "question"
title = "How to obtain sequence number of RTP while using tshark command line?"
description = '''I tried this script and I get a csv file with all content except the RTP sequence number. I&#x27;ve already used &quot;-e rtp.seq&quot;: tshark -Y &quot;udp.srcport == 2346&quot; -T fields -n -r &quot;C:&#92;not_land.pcap&quot; -E separator=, -e ip.src -e ip.dst -e ip.proto -e udp.srcport -e rtp.seq &amp;gt;&amp;gt; &quot;C:&#92;not_land.csv&quot; Is there an...'''
date = "2015-04-28T00:05:00Z"
lastmod = "2015-04-30T04:20:00Z"
weight = 41908
keywords = [ "tshark", "rtp" ]
aliases = [ "/questions/41908" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to obtain sequence number of RTP while using tshark command line?](/questions/41908/how-to-obtain-sequence-number-of-rtp-while-using-tshark-command-line)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41908-score" class="post-score" title="current number of votes">0</div><span id="post-41908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I tried this script and I get a csv file with all content except the RTP sequence number. I've already used "-e rtp.seq":</p><p>tshark -Y "udp.srcport == 2346" -T fields -n -r "C:\not_land.pcap" -E separator=, -e ip.src -e ip.dst -e ip.proto -e udp.srcport -e rtp.seq &gt;&gt; "C:\not_land.csv"</p><p>Is there any problem with this command?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Apr '15, 00:05</strong></p><img src="https://secure.gravatar.com/avatar/d10e76912ae0a0d745f3451d29395d86?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DiveDave&#39;s gravatar image" /><p><span>DiveDave</span><br />
<span class="score" title="21 reputation points">21</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DiveDave has one accepted answer">100%</span></p></div></div><div id="comments-container-41908" class="comments-container"></div><div id="comment-tools-41908" class="comment-tools"></div><div class="clear"></div><div id="comment-41908-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="41923"></span>

<div id="answer-container-41923" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-41923-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-41923-score" class="post-score" title="current number of votes">0</div><span id="post-41923-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Jaap has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Either use Wireshark to set the preference 'Try to decode RTP outside of conversations' or pass it in via the command line.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Apr '15, 09:07</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-41923" class="comments-container"><span id="41965"></span><div id="comment-41965" class="comment"><div id="post-41965-score" class="comment-score"></div><div class="comment-text"><p>Thanks for helping. I solved this problem by adding "-o rtp.heuristic_rtp:TRUE" in my command :)</p></div><div id="comment-41965-info" class="comment-info"><span class="comment-age">(30 Apr '15, 04:20)</span> <span class="comment-user userinfo">DiveDave</span></div></div></div><div id="comment-tools-41923" class="comment-tools"></div><div class="clear"></div><div id="comment-41923-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

