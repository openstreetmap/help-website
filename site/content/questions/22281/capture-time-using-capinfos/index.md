+++
type = "question"
title = "Capture time using capinfos"
description = '''&#x27;capinfos &quot;filename&quot; -u&#x27; rounds off capture time and does not return decimal places in windows. On Linux, however, it returns time to two decimal places.  Can you please clarify, how capture time upto two decimal places be retrieved using capinfos/tshark in windows environment?'''
date = "2013-06-24T07:47:00Z"
lastmod = "2013-06-25T08:35:00Z"
weight = 22281
keywords = [ "capture-time", "tshark", "capinfos" ]
aliases = [ "/questions/22281" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Capture time using capinfos](/questions/22281/capture-time-using-capinfos)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22281-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22281-score" class="post-score" title="current number of votes">0</div><span id="post-22281-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>'capinfos "filename" -u' rounds off capture time and does not return decimal places in windows. On Linux, however, it returns time to two decimal places.</p><p>Can you please clarify, how capture time upto two decimal places be retrieved using capinfos/tshark in windows environment?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-capture-time" rel="tag" title="see questions tagged &#39;capture-time&#39;">capture-time</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-capinfos" rel="tag" title="see questions tagged &#39;capinfos&#39;">capinfos</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>24 Jun '13, 07:47</strong></p><img src="https://secure.gravatar.com/avatar/e007baa1950a507d2163e10837a2861d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rajat&#39;s gravatar image" /><p><span>Rajat</span><br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rajat has no accepted answers">0%</span></p></div></div><div id="comments-container-22281" class="comments-container"></div><div id="comment-tools-22281" class="comment-tools"></div><div class="clear"></div><div id="comment-22281-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="22285"></span>

<div id="answer-container-22285" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22285-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22285-score" class="post-score" title="current number of votes">1</div><span id="post-22285-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Adding the <code>-T</code> flag to get table output causes the duration to be printed with full precision on Windows.</p><p>Looking at the code, the output without the <code>-T</code> will show an integer value on all platforms. What versions did you test on Linux and Windows?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '13, 08:30</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-22285" class="comments-container"></div><div id="comment-tools-22285" class="comment-tools"></div><div class="clear"></div><div id="comment-22285-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="22287"></span>

<div id="answer-container-22287" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22287-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22287-score" class="post-score" title="current number of votes">0</div><span id="post-22287-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I would consider this a bug, as the result of the following command delivers a the duration time with decimals, even on Windows (in contrary to option -u).</p><blockquote><p><code>capinfos input.pcap -T</code><br />
</p></blockquote><p>Please file a bug/enhancement report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Jun '13, 08:38</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>24 Jun '13, 08:41</strong> </span></p></div></div><div id="comments-container-22287" class="comments-container"><span id="22289"></span><div id="comment-22289" class="comment"><div id="post-22289-score" class="comment-score"></div><div class="comment-text"><p>Possibly a bug, but the code seems to be quite explicit in non-table mode that the duration should be shown with no decimal places.</p></div><div id="comment-22289-info" class="comment-info"><span class="comment-age">(24 Jun '13, 08:59)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="22290"></span><div id="comment-22290" class="comment"><div id="post-22290-score" class="comment-score"></div><div class="comment-text"><blockquote><p>non-table mode that the duration should be shown with no decimal places.</p></blockquote><p>Then it is still a bug, as it show decimals on Linux (according to the OP statement) ;-)</p><p>ALTHOUGH: I cannot reproduce that effect on Linux, so maybe it's just a problem with the (yet unknown) version the OP tested with.</p></div><div id="comment-22290-info" class="comment-info"><span class="comment-age">(24 Jun '13, 09:20)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22298"></span><div id="comment-22298" class="comment"><div id="post-22298-score" class="comment-score"></div><div class="comment-text"><p>Yes: capinfos.c was changed in May 2009 to not print decimals for the capture duration (-u).</p></div><div id="comment-22298-info" class="comment-info"><span class="comment-age">(24 Jun '13, 14:38)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="22300"></span><div id="comment-22300" class="comment"><div id="post-22300-score" class="comment-score"></div><div class="comment-text"><p>BTW: What was the motivation for that?</p><p>If the decimals are there, one can still take the full value and remove the decimals or round the value. So, why relinquish that possibility by not printing the decimals?</p></div><div id="comment-22300-info" class="comment-info"><span class="comment-age">(24 Jun '13, 18:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="22330"></span><div id="comment-22330" class="comment"><div id="post-22330-score" class="comment-score"></div><div class="comment-text"><p>Fair question:</p><p>Digging deeper:</p><p>I've no idea why I made that explicit change to not show any decimals for the capture duration.</p><p>The code before I made the change: ... printf("Capture duration: %f seconds\n", cf_info-&gt;duration);</p><p>Did I (mistakenly) think %f format wouldn't print any decimals ? [I really don't want to believe I would have made that mistake. :) ]</p><p>In any case the current output formatting of certain vals seems inconsistent between the "Human Readable", "Machine Readable" and "Table" output modes.</p><p>I've filed a bug report ...</p><p><a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8848">https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8848</a></p></div><div id="comment-22330-info" class="comment-info"><span class="comment-age">(25 Jun '13, 08:29)</span> <span class="comment-user userinfo">Bill Meier ♦♦</span></div></div><span id="22331"></span><div id="comment-22331" class="comment not_top_scorer"><div id="post-22331-score" class="comment-score"></div><div class="comment-text"><blockquote><p>I've no idea why I made that explicit change</p></blockquote><p>maybe just a copy-paste error? ;-)</p></div><div id="comment-22331-info" class="comment-info"><span class="comment-age">(25 Jun '13, 08:35)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-22287" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-22287-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

