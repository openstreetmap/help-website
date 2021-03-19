+++
type = "question"
title = "How can i decode dynamic RTP to AMR-WB?"
description = '''Hi. Please let me know the way to decode dynamic RTP to AMR-WB. Sometimes Wireshark show wrong information. Actually those RTP packets are AMR-WB. But this tool just show it as RTP. Like below PT=DynamicRTP-Type-104 Definately, regarded information is written in SDP Body messages. Like below Media A...'''
date = "2016-02-24T01:45:00Z"
lastmod = "2016-02-24T06:30:00Z"
weight = 50460
keywords = [ "rtp" ]
aliases = [ "/questions/50460" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How can i decode dynamic RTP to AMR-WB?](/questions/50460/how-can-i-decode-dynamic-rtp-to-amr-wb)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-50460-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-50460-score" class="post-score" title="current number of votes">0</div><span id="post-50460-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi. Please let me know the way to decode dynamic RTP to AMR-WB. Sometimes Wireshark show wrong information.</p><p>Actually those RTP packets are AMR-WB. But this tool just show it as RTP. Like below PT=DynamicRTP-Type-104</p><p>Definately, regarded information is written in SDP Body messages. Like below Media Attribute (a): rtpmap:104 AMR-WB/16000</p><p>So. What I really want to know is... how to decode those dynamic_RTP to AMR-WB. I am eager to see AMR-WB in protocol description.</p><p>Please help me.</p><p>A-&gt; B : AMR-WB B-&gt; A : RTP but in reality both of them AMR-WB</p><p><img src="http://" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rtp" rel="tag" title="see questions tagged &#39;rtp&#39;">rtp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Feb '16, 01:45</strong></p><img src="https://secure.gravatar.com/avatar/ec996df8047ae716cf7cb8e429bcf486?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Bro&#39;s gravatar image" /><p><span>Bro</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Bro has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Feb '16, 02:37</strong> </span></p></div></div><div id="comments-container-50460" class="comments-container"><span id="50461"></span><div id="comment-50461" class="comment"><div id="post-50461-score" class="comment-score"></div><div class="comment-text"><p>Without the capture file which contains the issue it is hard to say what is wrong, as analysis of dynamic payload type normally works. Please publish the file on cloudshark (google drive, microsoft onedrive, etc.) for a login-free access and place a link to it to your question (use <code>edit</code> to do so).</p></div><div id="comment-50461-info" class="comment-info"><span class="comment-age">(24 Feb '16, 02:12)</span> <span class="comment-user userinfo">sindy</span></div></div><span id="50465"></span><div id="comment-50465" class="comment"><div id="post-50465-score" class="comment-score"></div><div class="comment-text"><p>The version of Wireshark you are using will be helpful too. You should also checkout the AMR preferences Edit-&gt;preferences-&gt;protocols-AMR.</p></div><div id="comment-50465-info" class="comment-info"><span class="comment-age">(24 Feb '16, 03:30)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="50467"></span><div id="comment-50467" class="comment"><div id="post-50467-score" class="comment-score"></div><div class="comment-text"><p>Well. Before that i used Version 1.~ At that time it looks like RTP. But after I instal Version 2.0.1. It looks like AMR not an AMR-WB. I try to put screen. but i don't really know how to put it on the post.</p></div><div id="comment-50467-info" class="comment-info"><span class="comment-age">(24 Feb '16, 06:14)</span> <span class="comment-user userinfo">Bro</span></div></div><span id="50468"></span><div id="comment-50468" class="comment"><div id="post-50468-score" class="comment-score"></div><div class="comment-text"><p>A screenshot would not help. If you cannot post the capture as I've suggested above, I'm afraid there is no way to help you.</p></div><div id="comment-50468-info" class="comment-info"><span class="comment-age">(24 Feb '16, 06:30)</span> <span class="comment-user userinfo">sindy</span></div></div></div><div id="comment-tools-50460" class="comment-tools"></div><div class="clear"></div><div id="comment-50460-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

