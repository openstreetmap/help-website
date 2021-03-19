+++
type = "question"
title = "revive/continue ring buffer"
description = '''Hi, for reconstruction of network attacks or failures I am currently working on a system that stores all incoming network-traffic on a harddrive. So far this works completely fine, also due to the ring buffer feature. But: After shutdown I would very much like to continue my existing ring buffer wit...'''
date = "2013-12-18T12:55:00Z"
lastmod = "2013-12-19T15:21:00Z"
weight = 28273
keywords = [ "continue", "tshark", "ringbuffer" ]
aliases = [ "/questions/28273" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [revive/continue ring buffer](/questions/28273/revivecontinue-ring-buffer)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28273-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28273-score" class="post-score" title="current number of votes">0</div><span id="post-28273-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>for reconstruction of network attacks or failures I am currently working on a system that stores all incoming network-traffic on a harddrive. So far this works completely fine, also due to the ring buffer feature. But: After shutdown I would very much like to continue my existing ring buffer without having to manually delete the old files. Unfortunately I did not yet find any hint on how to achieve this. Ideally I would like to pass an argument to tshark which contains the last logfile and it continues the ring buffer.</p><p>Does this feature exist? Or does anyone have any helpful suggestions for me?</p><p>Thanks in advance, straw</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-continue" rel="tag" title="see questions tagged &#39;continue&#39;">continue</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-ringbuffer" rel="tag" title="see questions tagged &#39;ringbuffer&#39;">ringbuffer</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 Dec '13, 12:55</strong></p><img src="https://secure.gravatar.com/avatar/29c0629c406e2304ba6371aefcede460?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="straw&#39;s gravatar image" /><p><span>straw</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="straw has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 Dec '13, 02:49</strong> </span></p></div></div><div id="comments-container-28273" class="comments-container"></div><div id="comment-tools-28273" class="comment-tools"></div><div class="clear"></div><div id="comment-28273-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="28277"></span>

<div id="answer-container-28277" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-28277-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-28277-score" class="post-score" title="current number of votes">2</div><span id="post-28277-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="straw has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not sure but I guess dumpcap keeps a list of files in memory and deletes the oldest when the limit is reached and a new file is created. If that is the case I'm pretty sure that this list is not written to disk when dumpcap exits, so when you start a new session it doesn't "know" the old file names anymore.</p><p>Maybe a feature request to scan the directory for files with the <strong>exact same name pattern</strong> when starting dumpcap could be added to <a href="http://bugs.wireshark.org">http://bugs.wireshark.org</a>, but it would most likely also require a new command line switch to force that behavior. Otherwise ppl will overwrite their old files by mistake because they do not expect this to happen.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '13, 14:46</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28277" class="comments-container"><span id="28284"></span><div id="comment-28284" class="comment"><div id="post-28284-score" class="comment-score"></div><div class="comment-text"><p>Hi Jasper, thanks for your reply. As far as I found out so far the list of files is indeed stored in memory which explains why it does not delete those old files of course. Thanks for the hint writing a feature request. Any other ideas on how I could solve my problem until this feature makes it to a stable version (if so)?</p></div><div id="comment-28284-info" class="comment-info"><span class="comment-age">(19 Dec '13, 02:52)</span> <span class="comment-user userinfo">straw</span></div></div><span id="28287"></span><div id="comment-28287" class="comment"><div id="post-28287-score" class="comment-score"></div><div class="comment-text"><blockquote><p>Any other ideas on how I could solve my problem until this feature makes it to a stable version (if so)?</p></blockquote><p>You could write a wrapper script that replaces dumpcap. Within the script, you should clean up the old files and then call the real dumpcap.</p><p>Regards<br />
Kurt</p></div><div id="comment-28287-info" class="comment-info"><span class="comment-age">(19 Dec '13, 04:50)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="28291"></span><div id="comment-28291" class="comment"><div id="post-28291-score" class="comment-score"></div><div class="comment-text"><p>Thanks Kurt, but I don't think I really will do this. Seems quite a lot of work to me.</p></div><div id="comment-28291-info" class="comment-info"><span class="comment-age">(19 Dec '13, 06:15)</span> <span class="comment-user userinfo">straw</span></div></div><span id="28302"></span><div id="comment-28302" class="comment"><div id="post-28302-score" class="comment-score">1</div><div class="comment-text"><p>well, then your options are</p><ul><li>do it manually</li><li>file an enhancement bug</li></ul></div><div id="comment-28302-info" class="comment-info"><span class="comment-age">(19 Dec '13, 15:21)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-28277" class="comment-tools"></div><div class="clear"></div><div id="comment-28277-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

