+++
type = "question"
title = "How to preserve timestamps in tshark output file?"
description = '''I&#x27;m using tshark to extract specific TCP streams and write that to an output pcap file using the -w option. But, the frames in the output pcap do not have any timestamps or delta times (they&#x27;re all zero while in the original pcap there are timestamps and delta times for the frames). Is there any way...'''
date = "2014-02-10T18:35:00Z"
lastmod = "2014-02-11T15:32:00Z"
weight = 29656
keywords = [ "timestamp", "pcap", "tshark", "output" ]
aliases = [ "/questions/29656" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to preserve timestamps in tshark output file?](/questions/29656/how-to-preserve-timestamps-in-tshark-output-file)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29656-score" class="post-score" title="current number of votes">0</div><span id="post-29656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm using tshark to extract specific TCP streams and write that to an output pcap file using the -w option.</p><p>But, the frames in the output pcap do not have any timestamps or delta times (they're all zero while in the original pcap there are timestamps and delta times for the frames).</p><p>Is there any way to ensure that the original timestamps (from the original pcap file) are preserved in the output pcap?</p><p>I'm using TShark 1.10.5 (SVN Rev 54262 from /trunk-1.10) on MacOS. Here's what I'm doing:</p><blockquote><p>tshark -r test.pcap -2 -R "tcp.stream == 53" -w test_53.pcap</p></blockquote><p>Thanks!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-output" rel="tag" title="see questions tagged &#39;output&#39;">output</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Feb '14, 18:35</strong></p><img src="https://secure.gravatar.com/avatar/fe8d839d303ac5484d9d834f812726ba?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wwwalker&#39;s gravatar image" /><p><span>wwwalker</span><br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wwwalker has no accepted answers">0%</span></p></div></div><div id="comments-container-29656" class="comments-container"></div><div id="comment-tools-29656" class="comment-tools"></div><div class="clear"></div><div id="comment-29656-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="29658"></span>

<div id="answer-container-29658" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-29658-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-29658-score" class="post-score" title="current number of votes">1</div><span id="post-29658-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="wwwalker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>the frames in the output pcap do not have any timestamps or delta times (they're all zero while in the original pcap there are timestamps and delta times for the frames).</p></blockquote><p>That is what is technically known as a "bug". Please file it as a bug on <a href="http://bugs.wireshark.org">the Wireshark Bugzilla</a>; if you can attach your original pcap file for testing purposes, that would be good. (If not, please run the <code>file</code> command on it and show the results, just so we know what file type the input file is - it might, for example, be a pcap-ng file rather than a pcap file, the <code>.pcap</code> nonwithstanding).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Feb '14, 21:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-29658" class="comments-container"><span id="29721"></span><div id="comment-29721" class="comment"><div id="post-29721-score" class="comment-score"></div><div class="comment-text"><p>Thanks, here's the bug: <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9747">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=9747</a></p></div><div id="comment-29721-info" class="comment-info"><span class="comment-age">(11 Feb '14, 15:32)</span> <span class="comment-user userinfo">wwwalker</span></div></div></div><div id="comment-tools-29658" class="comment-tools"></div><div class="clear"></div><div id="comment-29658-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

