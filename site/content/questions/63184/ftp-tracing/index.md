+++
type = "question"
title = "FTP tracing"
description = '''Today I did a wireshark capture and seemed to capture everything EXCEPT the FTP activity. I know for a fact that the ftp transaction occurred. Why can&#x27;t I see it in my pcap file?'''
date = "2017-07-27T15:54:00Z"
lastmod = "2017-07-27T16:59:00Z"
weight = 63184
keywords = [ "ftp" ]
aliases = [ "/questions/63184" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [FTP tracing](/questions/63184/ftp-tracing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63184-score" class="post-score" title="current number of votes">0</div><span id="post-63184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Today I did a wireshark capture and seemed to capture everything EXCEPT the FTP activity. I know for a fact that the ftp transaction occurred. Why can't I see it in my pcap file?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ftp" rel="tag" title="see questions tagged &#39;ftp&#39;">ftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '17, 15:54</strong></p><img src="https://secure.gravatar.com/avatar/5e5b25e4a5d699369168947d0469cd9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="daveschmitzca&#39;s gravatar image" /><p><span>daveschmitzca</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="daveschmitzca has no accepted answers">0%</span></p></div></div><div id="comments-container-63184" class="comments-container"><span id="63185"></span><div id="comment-63185" class="comment"><div id="post-63185-score" class="comment-score"></div><div class="comment-text"><p>What are some of the packets in the "everything except" that was captured? Are there any TCP packets, such as HTTP or HTTPS? Or are they just broadcast packets?</p><p>Did you do the capture on the FTP server, the FTP client, or some other machine? If it's on the FTP server or client, on which interface did you do the capture - the interface the FTP traffic used, or some other interface, if the machine has that interface? If it's on some other machine, how was that machine connected to the network over which the FTP traffic was sent?</p></div><div id="comment-63185-info" class="comment-info"><span class="comment-age">(27 Jul '17, 16:59)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-63184" class="comment-tools"></div><div class="clear"></div><div id="comment-63184-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

