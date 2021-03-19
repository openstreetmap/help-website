+++
type = "question"
title = "Identify SYN packets without SYN/ACK"
description = '''From a PCAP Trace how to identify tcp SYN frames that have not received tcp SYN/ACK ?'''
date = "2011-09-26T21:12:00Z"
lastmod = "2011-09-28T07:30:00Z"
weight = 6576
keywords = [ "ack", "syn" ]
aliases = [ "/questions/6576" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Identify SYN packets without SYN/ACK](/questions/6576/identify-syn-packets-without-synack)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6576-score" class="post-score" title="current number of votes">0</div><span id="post-6576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>From a PCAP Trace how to identify tcp SYN frames that have not received tcp SYN/ACK ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ack" rel="tag" title="see questions tagged &#39;ack&#39;">ack</span> <span class="post-tag tag-link-syn" rel="tag" title="see questions tagged &#39;syn&#39;">syn</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>26 Sep '11, 21:12</strong></p><img src="https://secure.gravatar.com/avatar/6e44cf9d0f059be7e73b48522975364a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Norbert&#39;s gravatar image" /><p><span>Norbert</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Norbert has no accepted answers">0%</span></p></div></div><div id="comments-container-6576" class="comments-container"></div><div id="comment-tools-6576" class="comment-tools"></div><div class="clear"></div><div id="comment-6576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="6620"></span>

<div id="answer-container-6620" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6620-score" class="post-score" title="current number of votes">0</div><span id="post-6620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Here's the gist of an idea:</p><ol><li><p>Use tshark reading a file (and redirecting output to a file) with something like the following:</p><p>a. a read filter to find all the SYN frames: <code>-R tcp.flags.syn == 1</code></p><p>b. ouput fields: <code>-T fields -e ip.src -e ip.dst -e tcp.srcport -e tcp.dstport -e tcp.flags.ack</code></p></li><li><p>With some scripting (or maybe just some clever sorting) I think you should be able to identify SYNs without SYN/ACKS.</p><p>You'll probably also want to output the frame number field (<code>frame.number</code>)</p><p>I could imagine doing two passes with tshark (the first for SYNs, the second for SYN/ACKS) so as to be able to output the address/ports in the right order in each pass so that a sort of the combined output files would work.</p></li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '11, 07:26</strong></p><img src="https://secure.gravatar.com/avatar/bfb20acfe44690473b10c7963b5d4a18?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bill%20Meier&#39;s gravatar image" /><p><span>Bill Meier ♦♦</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="50 badges"><span class="bronze">●</span><span class="badgecount">50</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bill Meier has 31 accepted answers">17%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Sep '11, 07:30</strong> </span></p></div></div><div id="comments-container-6620" class="comments-container"></div><div id="comment-tools-6620" class="comment-tools"></div><div class="clear"></div><div id="comment-6620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="6621"></span>

<div id="answer-container-6621" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6621-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6621-score" class="post-score" title="current number of votes">0</div><span id="post-6621-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Another nice move might be to filter for tcp.flags.syn==1 and then go to conversation statistics. There you can sort by number of packets and those sessions with only 1 to a few packets outgoing and zero incoming are the ones not getting SYN/ACK back. Then go .csv Copy etc.</p><p>Sorry, this is not professional but I had no time to try scripting stuff ;)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '11, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/36b41326bff63eb5ad73a0436914e05c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Landi&#39;s gravatar image" /><p><span>Landi</span><br />
<span class="score" title="2269 reputation points"><span>2.3k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Landi has 28 accepted answers">28%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Sep '11, 07:31</strong> </span></p></div></div><div id="comments-container-6621" class="comments-container"></div><div id="comment-tools-6621" class="comment-tools"></div><div class="clear"></div><div id="comment-6621-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

