+++
type = "question"
title = "delete saved cap"
description = '''Hi guys i can&#x27;t see any saved files in linux(ubuntu),but i can see from the &quot;open&quot; from wireshark.I want delete some files but i can&#x27;t see(not files sthealt activated on my ubuntu ¿what is the problem?I saved the files on Desktop but desktop is clean :/ Greetings!'''
date = "2014-10-28T08:48:00Z"
lastmod = "2014-11-06T06:32:00Z"
weight = 37404
keywords = [ "files", "delete", "wireshark" ]
aliases = [ "/questions/37404" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [delete saved cap](/questions/37404/delete-saved-cap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37404-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37404-score" class="post-score" title="current number of votes">0</div><span id="post-37404-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi guys i can't see any saved files in linux(ubuntu),but i can see from the "open" from wireshark.I want delete some files but i can't see(not files sthealt activated on my ubuntu ¿what is the problem?I saved the files on Desktop but desktop is clean :/</p><p>Greetings!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-files" rel="tag" title="see questions tagged &#39;files&#39;">files</span> <span class="post-tag tag-link-delete" rel="tag" title="see questions tagged &#39;delete&#39;">delete</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Oct '14, 08:48</strong></p><img src="https://secure.gravatar.com/avatar/8a2b17b0fced9139cc9abf53b8edad5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sniper&#39;s gravatar image" /><p><span>sniper</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sniper has no accepted answers">0%</span></p></div></div><div id="comments-container-37404" class="comments-container"></div><div id="comment-tools-37404" class="comment-tools"></div><div class="clear"></div><div id="comment-37404-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="37407"></span>

<div id="answer-container-37407" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37407-score" class="post-score" title="current number of votes">0</div><span id="post-37407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Sounds like you are running Wireshark with a different account, possibly as root via <strong>sudo</strong>.</p><p>If that's the case, please check the directories of <strong>that</strong> account.</p><p>If that's <strong>not</strong> the case, please post the output of the following command. Run it on the CLI in the same account you were running Wireshark.</p><blockquote><p>ls -alrt ~/Desktop</p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Oct '14, 08:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-37407" class="comments-container"><span id="37408"></span><div id="comment-37408" class="comment"><div id="post-37408-score" class="comment-score"></div><div class="comment-text"><p>Im root on wireshark.So many thanks,one ask!what is CLI? i go try " ls -alrt ~/root/Desktop "</p></div><div id="comment-37408-info" class="comment-info"><span class="comment-age">(28 Oct '14, 09:05)</span> <span class="comment-user userinfo">sniper</span></div></div><span id="37409"></span><div id="comment-37409" class="comment"><div id="post-37409-score" class="comment-score"></div><div class="comment-text"><blockquote><p>what is CLI?</p></blockquote><p>bash!</p></div><div id="comment-37409-info" class="comment-info"><span class="comment-age">(28 Oct '14, 09:07)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="37411"></span><div id="comment-37411" class="comment"><div id="post-37411-score" class="comment-score"></div><div class="comment-text"><blockquote><p>ls -alrt ~/root/Desktop</p></blockquote><p>correct would be:</p><blockquote><p>ls -alrt ~root/Desktop</p></blockquote><p>or</p><blockquote><p>ls -alrt /root/Desktop</p></blockquote><p>but you won't have access as a regular user. So:</p><blockquote><p>sudo ls -alrt /root/Desktop</p></blockquote></div><div id="comment-37411-info" class="comment-info"><span class="comment-age">(28 Oct '14, 09:09)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-37407" class="comment-tools"></div><div class="clear"></div><div id="comment-37407-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="37618"></span>

<div id="answer-container-37618" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-37618-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-37618-score" class="post-score" title="current number of votes">0</div><span id="post-37618-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Hey guys!I solved hehe i used superoot ( nautilus ) for see the files. Have fun,greetings!</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Nov '14, 06:32</strong></p><img src="https://secure.gravatar.com/avatar/8a2b17b0fced9139cc9abf53b8edad5c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sniper&#39;s gravatar image" /><p><span>sniper</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sniper has no accepted answers">0%</span></p></div></div><div id="comments-container-37618" class="comments-container"></div><div id="comment-tools-37618" class="comment-tools"></div><div class="clear"></div><div id="comment-37618-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

