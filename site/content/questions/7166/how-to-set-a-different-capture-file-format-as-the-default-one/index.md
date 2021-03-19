+++
type = "question"
title = "How to set a different capture file format as the default one?"
description = '''Hello All, According to my group&#x27;s requirements ,we need K12 txt file format for saving a file always. So may i know where i can hardcode this?'''
date = "2011-10-30T21:59:00Z"
lastmod = "2011-10-31T04:41:00Z"
weight = 7166
keywords = [ "file-format", "save" ]
aliases = [ "/questions/7166" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to set a different capture file format as the default one?](/questions/7166/how-to-set-a-different-capture-file-format-as-the-default-one)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7166-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7166-score" class="post-score" title="current number of votes">0</div><span id="post-7166-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello All,</p><p>According to my group's requirements ,we need K12 txt file format for saving a file always. So may i know where i can hardcode this?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-file-format" rel="tag" title="see questions tagged &#39;file-format&#39;">file-format</span> <span class="post-tag tag-link-save" rel="tag" title="see questions tagged &#39;save&#39;">save</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>30 Oct '11, 21:59</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p><span>Terrestrial ...</span><br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div></div><div id="comments-container-7166" class="comments-container"></div><div id="comment-tools-7166" class="comment-tools"></div><div class="clear"></div><div id="comment-7166-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="7170"></span>

<div id="answer-container-7170" class="answer accepted-answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-7170-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-7170-score" class="post-score" title="current number of votes">0</div><span id="post-7170-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Terrestrial shark has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>goto <code>wireshark\win32\file_dlg_win32.c</code> make necessary modifications to <code>build_file_type_list()</code> or set appropriate filetype number to <code>FILE_SAVE_DEFAULT</code> macro.</p></div><div class="answer-controls post-controls"><div class="community-wiki">This answer is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>31 Oct '11, 01:25</strong></p><img src="https://secure.gravatar.com/avatar/968cc7ddfc48322ffbd1d7f5e3d37b85?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Terrestrial%20shark&#39;s gravatar image" /><p><span>Terrestrial ...</span><br />
<span class="score" title="96 reputation points">96</span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="28 badges"><span class="silver">●</span><span class="badgecount">28</span></span><span title="29 badges"><span class="bronze">●</span><span class="badgecount">29</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Terrestrial shark has 3 accepted answers">42%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>31 Oct '11, 02:30</strong> </span></p></div></div><div id="comments-container-7170" class="comments-container"><span id="7171"></span><div id="comment-7171" class="comment"><div id="post-7171-score" class="comment-score"></div><div class="comment-text"><p>See also <a href="http://ask.wireshark.org/questions/7057/how-does-save-as-work-in-wireshark">this</a> question, in particular my answer about adding a preference for the default save format.</p></div><div id="comment-7171-info" class="comment-info"><span class="comment-age">(31 Oct '11, 02:45)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="7172"></span><div id="comment-7172" class="comment"><div id="post-7172-score" class="comment-score"></div><div class="comment-text"><p>Do you mean to put a question in bug tracker and answer/send patch to it?</p></div><div id="comment-7172-info" class="comment-info"><span class="comment-age">(31 Oct '11, 03:23)</span> <span class="comment-user userinfo">Terrestrial ...</span></div></div><span id="7173"></span><div id="comment-7173" class="comment"><div id="post-7173-score" class="comment-score">1</div><div class="comment-text"><p>A patch would be great, but the bug tracker entry would be a start.</p></div><div id="comment-7173-info" class="comment-info"><span class="comment-age">(31 Oct '11, 04:41)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div></div><div id="comment-tools-7170" class="comment-tools"></div><div class="clear"></div><div id="comment-7170-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

