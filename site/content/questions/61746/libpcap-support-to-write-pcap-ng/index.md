+++
type = "question"
title = "libpcap support to write pcap ng"
description = '''I would like to know if libpcap latest version (1.8.1) support writing pcapng format ? From reading different blogs, I see it supports only reading pcapng format. However I see that wireshark supports both read/write pcapng. So, Has wireshark implemented writing in pcapng format ?. Kindly let me kno...'''
date = "2017-06-02T03:36:00Z"
lastmod = "2017-06-02T19:08:00Z"
weight = 61746
keywords = [ "pcapng", "libpcap" ]
aliases = [ "/questions/61746" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [libpcap support to write pcap ng](/questions/61746/libpcap-support-to-write-pcap-ng)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61746-score" class="post-score" title="current number of votes">0</div><span id="post-61746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I would like to know if libpcap latest version (1.8.1) support writing pcapng format ? From reading different blogs, I see it supports only reading pcapng format. However I see that wireshark supports both read/write pcapng. So, Has wireshark implemented writing in pcapng format ?.</p><p>Kindly let me know. Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcapng" rel="tag" title="see questions tagged &#39;pcapng&#39;">pcapng</span> <span class="post-tag tag-link-libpcap" rel="tag" title="see questions tagged &#39;libpcap&#39;">libpcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Jun '17, 03:36</strong></p><img src="https://secure.gravatar.com/avatar/38a15fccab6827bd3319fe93cf058e1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subhashmohan&#39;s gravatar image" /><p><span>subhashmohan</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subhashmohan has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>02 Jun '17, 03:37</strong> </span></p></div></div><div id="comments-container-61746" class="comments-container"></div><div id="comment-tools-61746" class="comment-tools"></div><div class="clear"></div><div id="comment-61746-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="61748"></span>

<div id="answer-container-61748" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61748-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61748-score" class="post-score" title="current number of votes">2</div><span id="post-61748-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Wireshark has supported reading and writing in pcap-ng for a long time. Wireshark has its own code to read and write pcap-ng files. As far as I know libpcap does not support writing pcap-ng files. Questions abou that are better asked on tcpdump mailing lists.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '17, 05:37</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-61748" class="comments-container"><span id="61749"></span><div id="comment-61749" class="comment"><div id="post-61749-score" class="comment-score"></div><div class="comment-text"><p>Thanks will check with tcpdump mailing lists..</p></div><div id="comment-61749-info" class="comment-info"><span class="comment-age">(02 Jun '17, 05:51)</span> <span class="comment-user userinfo">subhashmohan</span></div></div></div><div id="comment-tools-61748" class="comment-tools"></div><div class="clear"></div><div id="comment-61748-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="61755"></span>

<div id="answer-container-61755" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-61755-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-61755-score" class="post-score" title="current number of votes">0</div><span id="post-61755-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I would like to know if libpcap latest version (1.8.1) support writing pcapng format ?</p></blockquote><p>No.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jun '17, 19:08</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-61755" class="comments-container"></div><div id="comment-tools-61755" class="comment-tools"></div><div class="clear"></div><div id="comment-61755-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

