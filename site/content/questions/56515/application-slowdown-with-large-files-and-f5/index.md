+++
type = "question"
title = "Application slowdown with large files and F5"
description = '''Having application slowdown issues when we try to access a large list or upload a file, but only through F5. The pic attached is sorted by length, and all of the packets with length 16114 were bad checksum as well as virtually any over 1500 size. The 16114 packets all happened when the upload starts...'''
date = "2016-10-19T15:28:00Z"
lastmod = "2016-10-19T15:28:00Z"
weight = 56515
keywords = [ "checksum", "badchecksum", "f5", "slow" ]
aliases = [ "/questions/56515" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Application slowdown with large files and F5](/questions/56515/application-slowdown-with-large-files-and-f5)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-56515-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Having application slowdown issues when we try to access a large list or upload a file, but only through F5. The pic attached is sorted by length, and all of the packets with length 16114 were bad checksum as well as virtually any over 1500 size. The 16114 packets all happened when the upload starts. It happens with both 1 or 2 servers in the pool and does not happen if you bypass the F5</p></div><div id="question-tags" class="tags-container tags">checksum badchecksum f5 slow</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Oct '16, 15:28</strong></p><img src="https://secure.gravatar.com/avatar/4c3747fe2c34d5e57a7aa3dcc2da72df?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mysta&#39;s gravatar image" /><p>Mysta<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mysta has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Oct '16, 16:23</p></div></div><div id="comments-container-56515" class="comments-container"><span id="56516"></span><div id="comment-56516" class="comment"><div id="post-56516-score" class="comment-score">1</div><div class="comment-text"><p>That capture seems pretty much useless as it was most likely taken on one of the systems involved. It doesn't show what really happened on the network cable at all. See <a href="https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/">https://blog.packet-foo.com/2014/05/the-drawbacks-of-local-packet-captures/</a></p></div><div id="comment-56516-info" class="comment-info"><span class="comment-age">(19 Oct '16, 15:33)</span> Jasper ♦♦</div></div><span id="56517"></span><div id="comment-56517" class="comment"><div id="post-56517-score" class="comment-score"></div><div class="comment-text"><p>Ahhh, so that's why there's so many bad checksum then? <a href="http://i.imgur.com/9iF0emB.png">http://i.imgur.com/9iF0emB.png</a></p></div><div id="comment-56517-info" class="comment-info"><span class="comment-age">(19 Oct '16, 15:53)</span> Mysta</div></div><span id="56518"></span><div id="comment-56518" class="comment"><div id="post-56518-score" class="comment-score">1</div><div class="comment-text"><p>Ethernet checksum errors are usually caused by Wireshark interpreting trailing bytes as checksum. It can't be a bad checksum because the frame would have been discarded and not captured if it were.</p></div><div id="comment-56518-info" class="comment-info"><span class="comment-age">(19 Oct '16, 15:59)</span> Jasper ♦♦</div></div><span id="56519"></span><div id="comment-56519" class="comment"><div id="post-56519-score" class="comment-score"></div><div class="comment-text"><p>Well thanks for your help! In the past I was able to get a lot of data from the pcap but I see now that for real details you have to go with the mirrored solution. Great site you linked!</p></div><div id="comment-56519-info" class="comment-info"><span class="comment-age">(19 Oct '16, 16:02)</span> Mysta</div></div></div><div id="comment-tools-56515" class="comment-tools"></div><div class="clear"></div><div id="comment-56515-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

