+++
type = "question"
title = "tshark crashing because of temp pcap files in /tmp"
description = '''I am trying to run tshark for an extended period of time to reassemble NFS requests that I capture using tcpdump (with pf_ring). I am streaming the pcap to standard out from tcpdump (using -w -) and into tshark (using -i -). It seems that tshark calls dumpcap to do the packet capture (even from stdi...'''
date = "2012-12-11T13:17:00Z"
lastmod = "2012-12-12T12:31:00Z"
weight = 16779
keywords = [ "performance", "temp", "streaming" ]
aliases = [ "/questions/16779" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [tshark crashing because of temp pcap files in /tmp](/questions/16779/tshark-crashing-because-of-temp-pcap-files-in-tmp)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16779-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16779-score" class="post-score" title="current number of votes">0</div><span id="post-16779-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to run tshark for an extended period of time to reassemble NFS requests that I capture using tcpdump (with pf_ring). I am streaming the pcap to standard out from tcpdump (using -w -) and into tshark (using -i -). It seems that tshark calls dumpcap to do the packet capture (even from stdin) and then dumpcap writes the packets to the /tmp directory and then tshark reads from there. The reading and writing to disk was a bottleneck for me so I specified a new location using the TMPDIR environment variable and set it to a tmpfs mount. This was successful in speeding up the tshark processing but once the tmpfs mount fills up, tshark crashes. First, I would like to confirm that this is the correct behavior. If so, I have two questions:</p><ol><li>Can we remove dumpcap from the equation if we are just reading from stdin (so that it is similar to reading from a file)?</li><li>Is there a way to tell tshark to roll the temp files (similarly to how it will roll the raw packet captures if using the -w argument) so that it just overwrites old files rather than filling up the directory until it gets an Out of Memory exception?</li></ol><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-temp" rel="tag" title="see questions tagged &#39;temp&#39;">temp</span> <span class="post-tag tag-link-streaming" rel="tag" title="see questions tagged &#39;streaming&#39;">streaming</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Dec '12, 13:17</strong></p><img src="https://secure.gravatar.com/avatar/08f0b2e3262cfb486306c28a042948f3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="notorious-pcaper&#39;s gravatar image" /><p><span>notorious-pc...</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="notorious-pcaper has no accepted answers">0%</span></p></div></div><div id="comments-container-16779" class="comments-container"></div><div id="comment-tools-16779" class="comment-tools"></div><div class="clear"></div><div id="comment-16779-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="16807"></span>

<div id="answer-container-16807" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-16807-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-16807-score" class="post-score" title="current number of votes">0</div><span id="post-16807-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>There is currently an old bug which says that tshark should not be using files when in this configuration (<a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=2743">bug 2743</a>).</p><p>To answer your questions:</p><ol><li>Not if tshark is reading from a pipe. If tshark supported live-capture from a file (as requested in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5982">bug 5982</a>) then that would be a way to avoid the pipe.</li><li>Yes, I would think (but I have not tried) that using the standard ring-buffer options would achieve this.</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Dec '12, 07:52</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-16807" class="comments-container"><span id="16823"></span><div id="comment-16823" class="comment"><div id="post-16823-score" class="comment-score"></div><div class="comment-text"><p>Using the -b option when not writing out raw packets with the -w option does not work. The -b will only affect the explicit output. If there is no -w option, then tshark will just exit immediately.</p></div><div id="comment-16823-info" class="comment-info"><span class="comment-age">(12 Dec '12, 09:25)</span> <span class="comment-user userinfo">notorious-pc...</span></div></div><span id="16825"></span><div id="comment-16825" class="comment"><div id="post-16825-score" class="comment-score"></div><div class="comment-text"><p>Ah, right, makes sense. Oh well...</p></div><div id="comment-16825-info" class="comment-info"><span class="comment-age">(12 Dec '12, 12:31)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-16807" class="comment-tools"></div><div class="clear"></div><div id="comment-16807-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

