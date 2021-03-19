+++
type = "question"
title = "RST, ACK at the beginning?"
description = '''I&#x27;m getting a strange RST, ACK at the beginning of a SOCK transfer. Client RST, ACK -&amp;gt; Server 1 minute later Client SYNC -&amp;gt; Server Client SYNC, ACK &amp;lt;- Server Client ACK -&amp;gt; Server Client SOCK -&amp;gt; Server Client SOCK &amp;lt;- Server It&#x27;s strange the RST, ACK seems to be in response to a sess...'''
date = "2013-08-27T09:54:00Z"
lastmod = "2013-08-27T10:09:00Z"
weight = 24104
keywords = [ "wireshark" ]
aliases = [ "/questions/24104" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [RST, ACK at the beginning?](/questions/24104/rst-ack-at-the-beginning)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24104-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24104-score" class="post-score" title="current number of votes">0</div><span id="post-24104-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm getting a strange RST, ACK at the beginning of a SOCK transfer.</p><p>Client RST, ACK -&gt; Server</p><p>1 minute later</p><p>Client SYNC -&gt; Server Client SYNC, ACK &lt;- Server Client ACK -&gt; Server Client SOCK -&gt; Server Client SOCK &lt;- Server</p><p>It's strange the RST, ACK seems to be in response to a session which completed 10 minutes earlier. Once, the SYNC is sent everything runs fine. I did notice my client sent six duplicate ACKs at the end of the last session which again was 10 minutes earlier.</p><p>Thanks in advance.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Aug '13, 09:54</strong></p><img src="https://secure.gravatar.com/avatar/fb1d58f8a64b7e0f82bc898c395ec99b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Setsuna&#39;s gravatar image" /><p><span>Setsuna</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Setsuna has no accepted answers">0%</span></p></div></div><div id="comments-container-24104" class="comments-container"><span id="24106"></span><div id="comment-24106" class="comment"><div id="post-24106-score" class="comment-score"></div><div class="comment-text"><p>some questions</p><ul><li>what is your client OS and version?</li><li>what is you SOCKS client?</li><li>is the source port of the RST,ACK the same as the SYN packet?</li><li>is it possible to post a sample capture file somewhere (google drive, dropbox, cloudshark)?</li></ul></div><div id="comment-24106-info" class="comment-info"><span class="comment-age">(27 Aug '13, 10:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-24104" class="comment-tools"></div><div class="clear"></div><div id="comment-24104-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

