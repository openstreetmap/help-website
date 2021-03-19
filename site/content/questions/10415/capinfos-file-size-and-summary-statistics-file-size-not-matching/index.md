+++
type = "question"
title = "capinfos file size and summary statistics file size not matching"
description = '''hey experts, i used tshark and applied a filter to the pcap file .and then used capinfos utility  capinfos -c -s pcapfiledirectory  and found the output(no of packets and file size) .but the file size in not matching with that of the value i found using the same pcap in wireshark GUI ,applying same ...'''
date = "2012-04-24T02:37:00Z"
lastmod = "2012-04-24T10:08:00Z"
weight = 10415
keywords = [ "capinfos", "tshark", "file", "filesize" ]
aliases = [ "/questions/10415" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [capinfos file size and summary statistics file size not matching](/questions/10415/capinfos-file-size-and-summary-statistics-file-size-not-matching)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10415-score" class="post-score" title="current number of votes">0</div><span id="post-10415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hey experts,</p><p>i used tshark and applied a filter to the pcap file .and then used capinfos utility capinfos -c -s pcapfiledirectory and found the output(no of packets and file size) .but the file size in not matching with that of the value i found using the same pcap in wireshark GUI ,applying same filter.then summary&gt;statistics .but ,the values are not matching.</p><p>please can anyone tell me what is the problem</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capinfos" rel="tag" title="see questions tagged &#39;capinfos&#39;">capinfos</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-file" rel="tag" title="see questions tagged &#39;file&#39;">file</span> <span class="post-tag tag-link-filesize" rel="tag" title="see questions tagged &#39;filesize&#39;">filesize</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Apr '12, 02:37</strong></p><img src="https://secure.gravatar.com/avatar/6cb6685f12bd537f0f2e1e86a591e940?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sangmeshp&#39;s gravatar image" /><p><span>sangmeshp</span><br />
<span class="score" title="36 reputation points">36</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sangmeshp has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Apr '12, 02:46</strong> </span></p></div></div><div id="comments-container-10415" class="comments-container"></div><div id="comment-tools-10415" class="comment-tools"></div><div class="clear"></div><div id="comment-10415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="10419"></span>

<div id="answer-container-10419" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10419-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10419-score" class="post-score" title="current number of votes">1</div><span id="post-10419-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This sounds more like an issue for the bug tracker if there is a mismatch you cannot explain. I doubt someone here will be able to understand your problem without trying to reproduce it, and that again is most likely not going to happen.</p><p>My advice: if you think you found something that is not working correctly (and you want it to), do a detailed step-by-step documentation how you did what you did, and open a bug in <a href="https://bugs.wireshark.org/bugzilla/">bugzilla</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '12, 05:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-10419" class="comments-container"></div><div id="comment-tools-10419" class="comment-tools"></div><div class="clear"></div><div id="comment-10419-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="10422"></span>

<div id="answer-container-10422" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-10422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-10422-score" class="post-score" title="current number of votes">0</div><span id="post-10422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hello,</p><p>I am not sure what you actually mean here, I had a check on this on few set of captures with -c and -s and got correct info.</p><p>Could you please share the capture if you have one handy. I am sure it will be really interesting to see and dig further by adding few debug on how pkts are counted.</p><p>As Jasper suggested, please log a defect if you can re-create this.</p><p>Regards,</p><p>-Deepak</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Apr '12, 10:08</strong></p><img src="https://secure.gravatar.com/avatar/a8aa1b50bd4e70fe64d8c9612d100eb4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Deepak&#39;s gravatar image" /><p><span>Deepak</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Deepak has one accepted answer">25%</span></p></div></div><div id="comments-container-10422" class="comments-container"></div><div id="comment-tools-10422" class="comment-tools"></div><div class="clear"></div><div id="comment-10422-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

