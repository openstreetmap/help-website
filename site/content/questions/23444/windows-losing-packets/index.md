+++
type = "question"
title = "windows losing packets?"
description = '''We are experiencing a strange behaviour in some TCP connection. During a tcp connection we are sending data from compiter A to computer B. (wireshark is capturing packet on computer B) wiresharking the connection we can see the data from A to B , the SEQ number are ok and the ACKs are coming from B ...'''
date = "2013-07-30T06:06:00Z"
lastmod = "2013-07-30T08:02:00Z"
weight = 23444
keywords = [ "packetloss" ]
aliases = [ "/questions/23444" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [windows losing packets?](/questions/23444/windows-losing-packets)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23444-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23444-score" class="post-score" title="current number of votes">0</div><span id="post-23444-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>We are experiencing a strange behaviour in some TCP connection. During a tcp connection we are sending data from compiter A to computer B. (wireshark is capturing packet on computer B) wiresharking the connection we can see the data from A to B , the SEQ number are ok and the ACKs are coming from B to A... after a while we can see the the computer B doesn't acknoledge the data any more, even if the data are captured by wireshark. (we are just downloading a JPG using a browser from "A" http server, it happen with different browser).. Example</p><pre><code>A send packet 100 B ACK it
A send packet 101 B ACK 100 again (I can see packet 101 in wireshark capture)
A send packet 102 B ACK 100 again or do nothing (I can see packet 102 as well)
after a while A resend packet 101 then B ack 101 and 102....</code></pre><p>that can happen several times... with several packets... and of course often the connection is terminated..</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packetloss" rel="tag" title="see questions tagged &#39;packetloss&#39;">packetloss</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Jul '13, 06:06</strong></p><img src="https://secure.gravatar.com/avatar/7c9084c5c192ac3cbc352c3769bfc924?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="OmarP&#39;s gravatar image" /><p><span>OmarP</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="OmarP has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>30 Jul '13, 08:00</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23444" class="comments-container"><span id="23447"></span><div id="comment-23447" class="comment"><div id="post-23447-score" class="comment-score"></div><div class="comment-text"><p>seems to be something wrong on hardware calculated checksum....</p></div><div id="comment-23447-info" class="comment-info"><span class="comment-age">(30 Jul '13, 07:49)</span> <span class="comment-user userinfo">OmarP</span></div></div><span id="23448"></span><div id="comment-23448" class="comment"><div id="post-23448-score" class="comment-score"></div><div class="comment-text"><p>Posting a link to a public capture showing the symptoms (if you can share the capture) would be a great help.</p><p><a href="http://cloudshark.org">Cloudshark</a>, Google Drive and Dropbox are all useful options.</p></div><div id="comment-23448-info" class="comment-info"><span class="comment-age">(30 Jul '13, 08:02)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23444" class="comment-tools"></div><div class="clear"></div><div id="comment-23444-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

