+++
type = "question"
title = "FC malformed packet - no source addr or dest addr. All zeros"
description = '''Have you seen this issue? How should I proceed to troubleshoot this issue?'''
date = "2013-08-28T09:35:00Z"
lastmod = "2013-08-28T10:44:00Z"
weight = 24145
keywords = [ "malformed" ]
aliases = [ "/questions/24145" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [FC malformed packet - no source addr or dest addr. All zeros](/questions/24145/fc-malformed-packet-no-source-addr-or-dest-addr-all-zeros)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24145-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24145-score" class="post-score" title="current number of votes">0</div><span id="post-24145-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>Have you seen this issue? How should I proceed to troubleshoot this issue?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-malformed" rel="tag" title="see questions tagged &#39;malformed&#39;">malformed</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Aug '13, 09:35</strong></p><img src="https://secure.gravatar.com/avatar/64a599f90c9b72b1849eea7c16e11ed8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dtootle&#39;s gravatar image" /><p><span>dtootle</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dtootle has no accepted answers">0%</span></p></div></div><div id="comments-container-24145" class="comments-container"></div><div id="comment-tools-24145" class="comment-tools"></div><div class="clear"></div><div id="comment-24145-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24147"></span>

<div id="answer-container-24147" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24147-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24147-score" class="post-score" title="current number of votes">0</div><span id="post-24147-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Is this a real FC frame, or do you just think it is a FC frame, because Wireshark show FC as protocol?</p><p>Wireshark shows frames with an ethertype of 0 as FC. See Bug 8256</p><blockquote><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8256">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8256</a></p></blockquote><p>So, this could be just a malformed ethernet frame (lots of zeros at the beginning - maybe caused by a broken NIC) and Wireshark shows it as FC.</p><p>Is it possible to post a sample capture file (Google Drive, Dropbox, etc.)?</p><blockquote><p>How should I proceed to troubleshoot this issue?</p></blockquote><p>First I suggest to figure out if it it makes sense to see a FC (over Ethernet) frame on the link where you captured the traffic.</p><ul><li>If it makes sense: You need to figure out where the frame was originated. Take a look at the rest of the frame and check if there are any 'known' byte sequences that might help.</li><li>If it makes no sense: It could be just a damaged ethernet frame and Wireshark shows it as FC (see bug above). In that case you need to find the broken NIC/switch port that generated the packet.</li></ul><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Aug '13, 10:19</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-24147" class="comments-container"><span id="24148"></span><div id="comment-24148" class="comment"><div id="post-24148-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much. I would like to upload a capture but do not have Google Drive or Dropbox - anything options?</p></div><div id="comment-24148-info" class="comment-info"><span class="comment-age">(28 Aug '13, 10:34)</span> <span class="comment-user userinfo">dtootle</span></div></div><span id="24149"></span><div id="comment-24149" class="comment"><div id="post-24149-score" class="comment-score"></div><div class="comment-text"><p>There is also <a href="http://cloudshark.org">http://cloudshark.org</a></p><p>HINT: You cannot (later) delete an uploaded file, so please just upload files without any sensitive information!</p><p>Otherwise, please use one of those (free) <a href="http://en.wikipedia.org/wiki/File_hosting_service">online file hosters</a> like <a href="https://mega.co.nz/">https://mega.co.nz/</a> (or others)</p></div><div id="comment-24149-info" class="comment-info"><span class="comment-age">(28 Aug '13, 10:44)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24147" class="comment-tools"></div><div class="clear"></div><div id="comment-24147-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

