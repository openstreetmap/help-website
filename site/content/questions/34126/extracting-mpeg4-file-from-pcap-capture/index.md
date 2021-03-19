+++
type = "question"
title = "Extracting mpeg4 file from pcap capture"
description = '''Hi, I have a multicast Mpeg4 part II video stream Having joined the stream on my PC, I can view the incoming packets in wireshark, and save the capture as a pcap file With the appropriate filters, I can then filter this capture to show me only the UDP video traffic, then decode this traffic as RTP I...'''
date = "2014-06-24T07:58:00Z"
lastmod = "2015-08-17T15:21:00Z"
weight = 34126
keywords = [ "pcap", "multicast", "mpeg4" ]
aliases = [ "/questions/34126" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting mpeg4 file from pcap capture](/questions/34126/extracting-mpeg4-file-from-pcap-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-34126-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-34126-score" class="post-score" title="current number of votes">0</div><span id="post-34126-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I have a multicast Mpeg4 part II video stream Having joined the stream on my PC, I can view the incoming packets in wireshark, and save the capture as a pcap file</p><p>With the appropriate filters, I can then filter this capture to show me only the UDP video traffic, then decode this traffic as RTP</p><p>If I then add a further filter such that the first packet is the start of an i-frame, then I can save the payload as an m4v file (vi the telephony&gt;stream_analysis menu) and play it in VLC media player</p><p>However, this will only play in some players (like VLC). In addition, if I change the extension from m4v to avi, VLC will not play the file.</p><p>My guess is that this is because VLC is taking the m4v file extension as a hint as to how to decode the file, and without it fails to play. It presumably needs to do this because the file itself is missing suitable mpeg headers describing the stream...but I'm guessing here. Can someone give any pointers as to whether I am doing anything obciously wrong, and how I might go about rewriting the mepg headers if this is indeed the problem?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span> <span class="post-tag tag-link-multicast" rel="tag" title="see questions tagged &#39;multicast&#39;">multicast</span> <span class="post-tag tag-link-mpeg4" rel="tag" title="see questions tagged &#39;mpeg4&#39;">mpeg4</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '14, 07:58</strong></p><img src="https://secure.gravatar.com/avatar/ed56b38042032c7d46130c321dbcbd7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dbrb2&#39;s gravatar image" /><p><span>dbrb2</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dbrb2 has no accepted answers">0%</span></p></div></div><div id="comments-container-34126" class="comments-container"><span id="35797"></span><div id="comment-35797" class="comment"><div id="post-35797-score" class="comment-score"></div><div class="comment-text"><p>hello dbrb2...can you help me with the sample mpeg4 pcap...thanks...</p></div><div id="comment-35797-info" class="comment-info"><span class="comment-age">(27 Aug '14, 05:01)</span> <span class="comment-user userinfo">david90210</span></div></div><span id="45175"></span><div id="comment-45175" class="comment"><div id="post-45175-score" class="comment-score"></div><div class="comment-text"><p>Hello dbrb2 and david90210,</p><p>I am facing the same issue. It will be great if you can point me to how you solved it :)</p><p>Thanks</p></div><div id="comment-45175-info" class="comment-info"><span class="comment-age">(17 Aug '15, 15:21)</span> <span class="comment-user userinfo">zeinas</span></div></div></div><div id="comment-tools-34126" class="comment-tools"></div><div class="clear"></div><div id="comment-34126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

