+++
type = "question"
title = "An error while capturing with gns 3"
description = '''I was running gns3 in my laptop and was simulating 3 routers with ospf configured. I started to capture using wireshark but it was showing an error (frame 151 too long (-1 bytes)) can some one give me a suitable solution for this?'''
date = "2013-08-07T12:18:00Z"
lastmod = "2014-06-09T12:18:00Z"
weight = 23620
keywords = [ "gns3", "ospf" ]
aliases = [ "/questions/23620" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [An error while capturing with gns 3](/questions/23620/an-error-while-capturing-with-gns-3)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23620-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23620-score" class="post-score" title="current number of votes">0</div><span id="post-23620-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I was running gns3 in my laptop and was simulating 3 routers with ospf configured. I started to capture using wireshark but it was showing an error (frame 151 too long (-1 bytes)) can some one give me a suitable solution for this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-gns3" rel="tag" title="see questions tagged &#39;gns3&#39;">gns3</span> <span class="post-tag tag-link-ospf" rel="tag" title="see questions tagged &#39;ospf&#39;">ospf</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Aug '13, 12:18</strong></p><img src="https://secure.gravatar.com/avatar/3c99ce5d09233c40d515ceec98d10f48?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arjun05&#39;s gravatar image" /><p><span>arjun05</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arjun05 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>07 Aug '13, 12:53</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-23620" class="comments-container"><span id="23621"></span><div id="comment-23621" class="comment"><div id="post-23621-score" class="comment-score"></div><div class="comment-text"><p>Posting the capture somewhere others can see it, e.g. <a href="http://cloudshark.org">Cloudshark</a> will allow others to help you, otherwise we have no idea what might be up in frame 151 of <em>your</em> capture.</p></div><div id="comment-23621-info" class="comment-info"><span class="comment-age">(07 Aug '13, 12:54)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-23620" class="comment-tools"></div><div class="clear"></div><div id="comment-23620-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23638"></span>

<div id="answer-container-23638" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23638-score" class="post-score" title="current number of votes">0</div><span id="post-23638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This problem has been reported by others in the GNS3 forum.</p><blockquote><p><a href="http://forum.gns3.net/topic4796.html">http://forum.gns3.net/topic4796.html</a></p></blockquote><p>I guess, that the GNS3 simulator creates a broken pcap file structure and Wireshark simply complains about that.</p><blockquote><p>frame 151 too long (-1 bytes)</p></blockquote><p>This message is generated by dumpcap if a frame is larger than the supported length of 65535 bytes.</p><p>dumpcap.c:</p><pre><code>        if (pcap_opts-&gt;cap_pipe_rechdr.hdr.incl_len &gt; WTAP_MAX_PACKET_SIZE) {
            g_snprintf(errmsg, errmsgl, &quot;Frame %u too long (%d bytes)&quot;,
                       ld-&gt;packet_count+1, pcap_opts-&gt;cap_pipe_rechdr.hdr.incl_len);
            break;</code></pre><p>wtap.h</p><pre><code>/*
 * Maximum packet size we&#39;ll support.
 * 65535 is the largest snapshot length that libpcap supports, so we
 * use that.
 */
#define WTAP_MAX_PACKET_SIZE    65535</code></pre><p>So, this is either a bug in GNS3 or a configuration problem, like using 'super Jumbo Frames' with packet length &gt; 65535 bytes in GNS3.</p><p>I suggest to discuss this issue in the GNS3 forum, with a link to this question, as there is nothing the Wireshark 'community' can do about this problem.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Aug '13, 06:03</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>08 Aug '13, 06:06</strong> </span></p></div></div><div id="comments-container-23638" class="comments-container"><span id="33592"></span><div id="comment-33592" class="comment"><div id="post-33592-score" class="comment-score"></div><div class="comment-text"><p>GNS3 uses dynamips. The capture file was being corrupted due to a thread safety issue in dynamips. The fix will be a part of dynamips 0.2.13.</p><p>Related issue: <a href="https://github.com/GNS3/dynamips/issues/41">https://github.com/GNS3/dynamips/issues/41</a></p></div><div id="comment-33592-info" class="comment-info"><span class="comment-age">(09 Jun '14, 12:18)</span> <span class="comment-user userinfo">flaviojs</span></div></div></div><div id="comment-tools-23638" class="comment-tools"></div><div class="clear"></div><div id="comment-23638-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

