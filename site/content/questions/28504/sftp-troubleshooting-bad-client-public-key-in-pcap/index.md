+++
type = "question"
title = "SFTP troubleshooting bad client public key in pcap"
description = '''Is there a way to determine a bad public key presented to an SFTP server configured for public key authentication? I am comparing two pcap files next to each other one is a success and the other I know is failure with client presenting wrong key for public key authentication attempt. They look very ...'''
date = "2013-12-31T13:24:00Z"
lastmod = "2014-01-12T15:13:00Z"
weight = 28504
keywords = [ "authentication", "public", "key", "sftp" ]
aliases = [ "/questions/28504" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [SFTP troubleshooting bad client public key in pcap](/questions/28504/sftp-troubleshooting-bad-client-public-key-in-pcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28504-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28504-score" class="post-score" title="current number of votes">0</div><span id="post-28504-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there a way to determine a bad public key presented to an SFTP server configured for public key authentication? I am comparing two pcap files next to each other one is a success and the other I know is failure with client presenting wrong key for public key authentication attempt. They look very similar except the successfull connection obviously has more encrypted packets back/forth. Is there any tell tail sign of a wrong client certificate presented like an ssl session? In the SSL session we can see an unecnrypted "Bad Cert" message. I can't find a similar one in an SSH/SFTP session captured.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-authentication" rel="tag" title="see questions tagged &#39;authentication&#39;">authentication</span> <span class="post-tag tag-link-public" rel="tag" title="see questions tagged &#39;public&#39;">public</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span> <span class="post-tag tag-link-sftp" rel="tag" title="see questions tagged &#39;sftp&#39;">sftp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '13, 13:24</strong></p><img src="https://secure.gravatar.com/avatar/8e66e6bc8d31ff8a07232309b937807d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bonds3212000&#39;s gravatar image" /><p><span>bonds3212000</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bonds3212000 has no accepted answers">0%</span></p></div></div><div id="comments-container-28504" class="comments-container"><span id="28833"></span><div id="comment-28833" class="comment"><div id="post-28833-score" class="comment-score"></div><div class="comment-text"><p>are you using 'plain' public key authentication (AuthorizedKeysFile) or certificate authentication (AuthorizedPrincipalsFile)?</p><p>BTW: What is your SSH software? OpenSSH or a commercial product?</p></div><div id="comment-28833-info" class="comment-info"><span class="comment-age">(12 Jan '14, 15:13)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28504" class="comment-tools"></div><div class="clear"></div><div id="comment-28504-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

