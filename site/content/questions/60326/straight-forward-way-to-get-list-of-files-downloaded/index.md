+++
type = "question"
title = "Straight Forward Way to get List of Files Downloaded"
description = '''Is there a straight forward way I can simply get a list of all the files that were downloaded during a Packet Capture session? e.g. Images, Videos, Files and so on? Thanks'''
date = "2017-03-25T21:31:00Z"
lastmod = "2017-03-26T06:54:00Z"
weight = 60326
keywords = [ "files", "downloaded", "images", "videos" ]
aliases = [ "/questions/60326" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Straight Forward Way to get List of Files Downloaded](/questions/60326/straight-forward-way-to-get-list-of-files-downloaded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60326-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60326-score" class="post-score" title="current number of votes">0</div><span id="post-60326-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a straight forward way I can simply get a list of all the files that were downloaded during a Packet Capture session? e.g. Images, Videos, Files and so on?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-downloaded" rel="tag" title="see questions tagged &#39;downloaded&#39;">downloaded</span> <span class="post-tag tag-link-images" rel="tag" title="see questions tagged &#39;images&#39;">images</span> <span class="post-tag tag-link-videos" rel="tag" title="see questions tagged &#39;videos&#39;">videos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '17, 21:31</strong></p><img src="https://secure.gravatar.com/avatar/29bc6afba6733309ed8acf31b4f80f2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SirSwish&#39;s gravatar image" /><p><span>SirSwish</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SirSwish has no accepted answers">0%</span></p></div></div><div id="comments-container-60326" class="comments-container"></div><div id="comment-tools-60326" class="comment-tools"></div><div class="clear"></div><div id="comment-60326-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60328"></span>

<div id="answer-container-60328" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-60328-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-60328-score" class="post-score" title="current number of votes">1</div><span id="post-60328-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SirSwish has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You didn't specify the protocol used to download files.</p><p>I guess you mean HTTP. If this is the case you can find a list of all captured requests in the "Statistics" -&gt; "HTTP" -&gt; "Requests" menu.</p><p>If you're using another protocol (e.g. FTP) please add more details to your question.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>26 Mar '17, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/11cda2a4be5391632a5b28af1927307b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Uli&#39;s gravatar image" /><p><span>Uli</span><br />
<span class="score" title="903 reputation points">903</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Uli has 16 accepted answers">29%</span></p></div></div><div id="comments-container-60328" class="comments-container"><span id="60329"></span><div id="comment-60329" class="comment"><div id="post-60329-score" class="comment-score"></div><div class="comment-text"><p>Hi,</p><p>Sorry about lack of detail, I'm kind of a novice at Wireshark. I was looking for something that could comprehensively list every file that was downloaded no matter the protocol, but at the very least HTTP, so thanks very much for the tip! ;) Just a quick clarifier if I may, does this include items that were fetched via HTTPS. If not is there an equivalent function for HTTPS?</p><p>Thanks</p></div><div id="comment-60329-info" class="comment-info"><span class="comment-age">(26 Mar '17, 05:29)</span> <span class="comment-user userinfo">SirSwish</span></div></div><span id="60330"></span><div id="comment-60330" class="comment"><div id="post-60330-score" class="comment-score"></div><div class="comment-text"><p>You also can try networkminer for such a task.</p></div><div id="comment-60330-info" class="comment-info"><span class="comment-age">(26 Mar '17, 06:17)</span> <span class="comment-user userinfo">Christian_R</span></div></div><span id="60331"></span><div id="comment-60331" class="comment"><div id="post-60331-score" class="comment-score"></div><div class="comment-text"><p>Thanks for the tip Christian. Unfortunately, the traffic is 802.11 and is encrypted. I have not been able to successfully convert the encyrpted PCAP file to a decrypted PCAP file thus far. and I wasn't able to find any WPA decryption functionality native to Network Miner.</p></div><div id="comment-60331-info" class="comment-info"><span class="comment-age">(26 Mar '17, 06:54)</span> <span class="comment-user userinfo">SirSwish</span></div></div></div><div id="comment-tools-60328" class="comment-tools"></div><div class="clear"></div><div id="comment-60328-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

