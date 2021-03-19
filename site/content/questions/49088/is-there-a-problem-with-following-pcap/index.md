+++
type = "question"
title = "Is there a problem with following pcap"
description = '''Hi there I have a https listener running, supporting many clients. How ever one client cannot connect. I ran a network capture and got following. Can anyone advise what problem is?  Is it something to so with cipher suites? I really appreciate any help here. Lost several days on this already.'''
date = "2016-01-11T08:08:00Z"
lastmod = "2016-01-11T08:51:00Z"
weight = 49088
keywords = [ "ssl", "tlsv1" ]
aliases = [ "/questions/49088" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is there a problem with following pcap](/questions/49088/is-there-a-problem-with-following-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-49088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-49088-score" class="post-score" title="current number of votes">0</div><span id="post-49088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi there</p><p>I have a https listener running, supporting many clients. How ever one client cannot connect. I ran a network capture and got following. Can anyone advise what problem is?</p><p><img alt="screen shot" title="wireshark screen shot"></img></p><p>Is it something to so with cipher suites? I really appreciate any help here. Lost several days on this already.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tlsv1" rel="tag" title="see questions tagged &#39;tlsv1&#39;">tlsv1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Jan '16, 08:08</strong></p><img src="https://secure.gravatar.com/avatar/1c135e598ca5780aa6d2288f6904debf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="edmondH&#39;s gravatar image" /><p><span>edmondH</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="edmondH has no accepted answers">0%</span></p></img></div></div><div id="comments-container-49088" class="comments-container"><span id="49089"></span><div id="comment-49089" class="comment"><div id="post-49089-score" class="comment-score"></div><div class="comment-text"><p>FYI: the screenshot is not visible.</p><p><strong>Furthermore</strong>, it's almost impossible to do packet analysis based on screenshots. Please upload the pcap file somewhere (google drive, dropbox, etc.) and post the link here.</p></div><div id="comment-49089-info" class="comment-info"><span class="comment-age">(11 Jan '16, 08:11)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="49090"></span><div id="comment-49090" class="comment"><div id="post-49090-score" class="comment-score"></div><div class="comment-text"><p>sorry... here is screen shot</p><p><img src="https://osqa-ask.wireshark.org/upfiles/Capture_pVPVnTm.PNG" alt="alt text" /></p></div><div id="comment-49090-info" class="comment-info"><span class="comment-age">(11 Jan '16, 08:11)</span> <span class="comment-user userinfo">edmondH</span></div></div><span id="49091"></span><div id="comment-49091" class="comment"><div id="post-49091-score" class="comment-score"></div><div class="comment-text"><p>Hi Kurt</p><p>Thanks for your help. Can u access it here?</p><p><a href="https://drive.google.com/open?id=0B4e9GWrGlxl3azFMUnRpcl9KVkk">https://drive.google.com/open?id=0B4e9GWrGlxl3azFMUnRpcl9KVkk</a></p></div><div id="comment-49091-info" class="comment-info"><span class="comment-age">(11 Jan '16, 08:26)</span> <span class="comment-user userinfo">edmondH</span></div></div><span id="49094"></span><div id="comment-49094" class="comment"><div id="post-49094-score" class="comment-score"></div><div class="comment-text"><p>It looks like the conversation breaks down after packet 39 where you attempt the TLSv1 handshake. Is your application using TLSv1 or a different version such as TLSv1.2, etc? From this first look I would guess it's due to TLS versioning or your ciphers.</p></div><div id="comment-49094-info" class="comment-info"><span class="comment-age">(11 Jan '16, 08:51)</span> <span class="comment-user userinfo">csereno</span></div></div></div><div id="comment-tools-49088" class="comment-tools"></div><div class="clear"></div><div id="comment-49088-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

