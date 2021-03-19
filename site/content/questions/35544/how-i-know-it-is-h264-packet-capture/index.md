+++
type = "question"
title = "How I know it is H.264 packet capture?"
description = '''I use Wireshark to cature raw data from a direct IP.src video stream which has H.264 format. However when I look at the information in a package, I find out there is nothing indicated it was H.264 format a. What information would show it was H.264 format? b. I have read some information how to intep...'''
date = "2014-08-18T11:48:00Z"
lastmod = "2014-08-19T02:42:00Z"
weight = 35544
keywords = [ "h.264", "packet" ]
aliases = [ "/questions/35544" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How I know it is H.264 packet capture?](/questions/35544/how-i-know-it-is-h264-packet-capture)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35544-score" class="post-score" title="current number of votes">0</div><span id="post-35544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I use Wireshark to cature raw data from a direct IP.src video stream which has H.264 format. However when I look at the information in a package, I find out there is nothing indicated it was H.264 format</p><p>a. What information would show it was H.264 format?</p><p>b. I have read some information how to inteprete H.264 by using Edit --&gt; Preferences --&gt; Protocols --&gt; H264 ... but then I don't know what to do with the last step which fill-in <strong>H264 Dynamic Payload Types</strong></p><p>Can anyone help? My main question is how I know it was H.264 packet?</p><p>Thanks for any help</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-h.264" rel="tag" title="see questions tagged &#39;h.264&#39;">h.264</span> <span class="post-tag tag-link-packet" rel="tag" title="see questions tagged &#39;packet&#39;">packet</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Aug '14, 11:48</strong></p><img src="https://secure.gravatar.com/avatar/3963eae7ad755119fc24146476344a1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Curious52&#39;s gravatar image" /><p><span>Curious52</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Curious52 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Aug '14, 11:49</strong> </span></p></div></div><div id="comments-container-35544" class="comments-container"></div><div id="comment-tools-35544" class="comment-tools"></div><div class="clear"></div><div id="comment-35544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="35545"></span>

<div id="answer-container-35545" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-35545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-35545-score" class="post-score" title="current number of votes">1</div><span id="post-35545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It's me again. Meanwhile I was waiting for the answer I did ask for help from my coleague &amp; we work for awhile until we found the way:</p><ul><li>At first, we must get the Wiresahrk ready for capture only with the intended H.264 video stream</li><li>Secondly, start the video stream (i.e. VLC Player at the same PC with using Wireshark)</li><li>Then the Captured Packet will be shown on Wireshark screen</li><li>In one of the Packet, the Real Time Stream Protocol/Media Attribute will show: rtpmap: 98 H264/90000 (in my case)</li></ul><p><strong>Note:</strong> It only shows in those first packets! When i placed my question: at that time I was looking after ... therefore I missed this packet info.</p><p>This solve my issue, I hope that it also help someone looking the same issue as me!</p><p>Cheers!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Aug '14, 13:25</strong></p><img src="https://secure.gravatar.com/avatar/3963eae7ad755119fc24146476344a1b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Curious52&#39;s gravatar image" /><p><span>Curious52</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Curious52 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>18 Aug '14, 13:26</strong> </span></p></div></div><div id="comments-container-35545" class="comments-container"><span id="35555"></span><div id="comment-35555" class="comment"><div id="post-35555-score" class="comment-score"></div><div class="comment-text"><p>If we did a packet string search by "H264" or just "264", we should be able to locate the specific packet by no more than tens of clicks.</p></div><div id="comment-35555-info" class="comment-info"><span class="comment-age">(19 Aug '14, 02:42)</span> <span class="comment-user userinfo">SteveZhou</span></div></div></div><div id="comment-tools-35545" class="comment-tools"></div><div class="clear"></div><div id="comment-35545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

