+++
type = "question"
title = "How to see sequence of parameters for NBAP protocol?"
description = '''Hi, I have using NBAP (using IP stack over SCTP), I have some wireshark traces, but not able to find exact sequence of data I need to add to created desired packet.'''
date = "2013-09-11T01:11:00Z"
lastmod = "2013-09-11T06:41:00Z"
weight = 24551
keywords = [ "dissector", "packet" ]
aliases = [ "/questions/24551" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to see sequence of parameters for NBAP protocol?](/questions/24551/how-to-see-sequence-of-parameters-for-nbap-protocol)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-24551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-24551-score" class="post-score" title="current number of votes">0</div><span id="post-24551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I have using NBAP (using IP stack over SCTP), I have some wireshark traces, but not able to find exact sequence of data I need to add to created desired packet.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Sep '13, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/4d5a1d4ba48122bcddd239a84b8bf3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pranitkothari&#39;s gravatar image" /><p><span>pranitkothari</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pranitkothari has one accepted answer">100%</span></p></div></div><div id="comments-container-24551" class="comments-container"><span id="24558"></span><div id="comment-24558" class="comment"><div id="post-24558-score" class="comment-score"></div><div class="comment-text"><p>I don't understand your question, you have NBAP over SCTP but when looking at the trace you only see the SCTP layer + data? If so try "decode as" and chose NBAP. If that's not the problem you will have to explain in more detail what the problem is.</p></div><div id="comment-24558-info" class="comment-info"><span class="comment-age">(11 Sep '13, 04:10)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="24560"></span><div id="comment-24560" class="comment"><div id="post-24560-score" class="comment-score"></div><div class="comment-text"><p>No problem is I have NBAP packet (downloaded from wireshark site), and I want to create my own packet, but I am not able to get exact sequence of parameter I want to add. I referred 3GPP TS 25.433 but it is of very less help.</p></div><div id="comment-24560-info" class="comment-info"><span class="comment-age">(11 Sep '13, 04:13)</span> <span class="comment-user userinfo">pranitkothari</span></div></div><span id="24573"></span><div id="comment-24573" class="comment"><div id="post-24573-score" class="comment-score"></div><div class="comment-text"><p>So you ar trying to hand craf a NBAP message? Not realy a Wireshark question. That's not going to be easy ;)</p></div><div id="comment-24573-info" class="comment-info"><span class="comment-age">(11 Sep '13, 06:39)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="24574"></span><div id="comment-24574" class="comment"><div id="post-24574-score" class="comment-score"></div><div class="comment-text"><p>I have created messages like BSSAP same way, but I am not getting proper documentation for NBAP.</p></div><div id="comment-24574-info" class="comment-info"><span class="comment-age">(11 Sep '13, 06:41)</span> <span class="comment-user userinfo">pranitkothari</span></div></div></div><div id="comment-tools-24551" class="comment-tools"></div><div class="clear"></div><div id="comment-24551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

