+++
type = "question"
title = "Wireshark merging pcap files"
description = '''I&#x27;m trying to merge 15 pcap files using wireshark. The merging is successful. I&#x27;m using appending function so that the second file is just added to the bottom of the first file. But when this is done, I get -ve value in time column. How can I change this? Below given is the last packet of first file...'''
date = "2014-03-24T07:46:00Z"
lastmod = "2014-03-25T07:38:00Z"
weight = 31113
keywords = [ "merge", "wireshark", "timestamp" ]
aliases = [ "/questions/31113" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark merging pcap files](/questions/31113/wireshark-merging-pcap-files)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31113-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31113-score" class="post-score" title="current number of votes">0</div><span id="post-31113-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to merge 15 pcap files using wireshark. The merging is successful. I'm using appending function so that the second file is just added to the bottom of the first file. But when this is done, I get -ve value in time column. How can I change this? Below given is the last packet of first file and first packet of second file with latter with a negative time. What I intend to do is, replace these 15 smaller files with this one merged files.</p><pre><code> No      time           Source           Dest.           Protocol Length  Info
4873    10.107185   192.168.10.107  224.10.10.107   UDP 526 Source port: 10711  Destination port: 20711
4874    -8.831791   192.168.11.104  224.11.11.104   UDP 526 Source port: 10431  Destination port: 20431</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-merge" rel="tag" title="see questions tagged &#39;merge&#39;">merge</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span> <span class="post-tag tag-link-timestamp" rel="tag" title="see questions tagged &#39;timestamp&#39;">timestamp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Mar '14, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/5bf5e940f9cb50a96c3ee06e808e5eb5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jichu&#39;s gravatar image" /><p><span>jichu</span><br />
<span class="score" title="11 reputation points">11</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jichu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Mar '14, 08:59</strong> </span></p></div></div><div id="comments-container-31113" class="comments-container"></div><div id="comment-tools-31113" class="comment-tools"></div><div class="clear"></div><div id="comment-31113-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="31118"></span>

<div id="answer-container-31118" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31118-score" class="post-score" title="current number of votes">1</div><span id="post-31118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm using appending function so that the second file is just added to the bottom of the first file.</p></blockquote><p>don't use <strong>append</strong> mode (omit -a) in mergecap.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '14, 08:53</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-31118" class="comments-container"><span id="31119"></span><div id="comment-31119" class="comment"><div id="post-31119-score" class="comment-score"></div><div class="comment-text"><p><span>@Kurt</span> If I dont append, will the merge function do the same? Because what I need is a big file that replaces the 15 smaller files.</p></div><div id="comment-31119-info" class="comment-info"><span class="comment-age">(24 Mar '14, 08:56)</span> <span class="comment-user userinfo">jichu</span></div></div><span id="31122"></span><div id="comment-31122" class="comment"><div id="post-31122-score" class="comment-score"></div><div class="comment-text"><p>Just try it ;-)</p></div><div id="comment-31122-info" class="comment-info"><span class="comment-age">(24 Mar '14, 09:01)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-31118" class="comment-tools"></div><div class="clear"></div><div id="comment-31118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31136"></span>

<div id="answer-container-31136" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31136-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31136-score" class="post-score" title="current number of votes">1</div><span id="post-31136-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm trying to merge 15 pcap files using wireshark.</p></blockquote><p>If those were separate captures, done in sequential order, so that the second capture was started after the first capture finished, the third capture was started after the second capture finished, etc., then simply concatenating them will work, as the packets will be in order by the time stamp (assuming the packets in the captures themselves are in order by the time stamp; some packet capture mechanisms can, sadly, deliver packets out of time order).</p><p>Otherwise, you <strong><em>MUST NOT</em></strong> concatenate them, as you will have packets out of order and thus have negative time deltas.</p><p>"Append mode" does concatenation, so you must not use it except in the circumstance I describe in my first paragraph.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '14, 20:00</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-31136" class="comments-container"><span id="31146"></span><div id="comment-31146" class="comment"><div id="post-31146-score" class="comment-score"></div><div class="comment-text"><p>@GuyHarris the capture files are in sequential order. But if I was to do a merge instead of append, would wireshark or mergcap automatically, re order it?</p></div><div id="comment-31146-info" class="comment-info"><span class="comment-age">(25 Mar '14, 03:10)</span> <span class="comment-user userinfo">jichu</span></div></div><span id="31152"></span><div id="comment-31152" class="comment"><div id="post-31152-score" class="comment-score"></div><div class="comment-text"><p>So, in your example, packet 4873 was captured before packet 4874 was captured?</p><p>If so, then, if you used append mode, either packet 4873 has an invalid time stamp or packet 4874 has an invalid time stamp (or both have invalid time stamps), meaning that whatever capture mechanism supplied the time stamps has a bug or the clocks were set wrong at the time the packet or packets were captured.</p><p>If not, then the capture files are <em>not</em> in sequential order, as you claim that packet 4873 is the last packet of the first file and packet 4874 is the first packet of the second file, so if packet 4874 wasn't captured after packet 4873 was captured, then the second file was started before you were finished with the first file.</p></div><div id="comment-31152-info" class="comment-info"><span class="comment-age">(25 Mar '14, 07:38)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-31136" class="comment-tools"></div><div class="clear"></div><div id="comment-31136-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="31116"></span>

<div id="answer-container-31116" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31116-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31116-score" class="post-score" title="current number of votes">0</div><span id="post-31116-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You can use reordercap (comes with Wireshark since 1.10) to reorder frames according to their timestamps. That should get rid of negative delta times.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Mar '14, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-31116" class="comments-container"></div><div id="comment-tools-31116" class="comment-tools"></div><div class="clear"></div><div id="comment-31116-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

