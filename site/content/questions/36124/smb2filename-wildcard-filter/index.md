+++
type = "question"
title = "smb2.filename wildcard filter"
description = '''I have a complex folder structure that gets copied via SMB2 by a custom application that has a very limited logging functionality. The transfer seems to be breaking somewhere in the middle and I suspect one of the file or folder names to be the problem. Is there a way to specify a wildcard in the fi...'''
date = "2014-09-09T13:14:00Z"
lastmod = "2014-09-09T13:43:00Z"
weight = 36124
keywords = [ "filter", "smb2", "wildcard", "filename" ]
aliases = [ "/questions/36124" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [smb2.filename wildcard filter](/questions/36124/smb2filename-wildcard-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36124-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36124-score" class="post-score" title="current number of votes">0</div><span id="post-36124-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I have a complex folder structure that gets copied via SMB2 by a custom application that has a very limited logging functionality. The transfer seems to be breaking somewhere in the middle and I suspect one of the file or folder names to be the problem.</p><p>Is there a way to specify a wildcard in the filter that would show only packets that have a value in the filename filed ?</p><p>As a workaround I added Filename as a column and set up a filter for smb.create_options == 0x00200021, which does the trick, I am just wondering what I am doing wrong when I use the following filter?</p><p>smb2.filename matches "C_\\SHARENAME\\SAMPLEFOLDER\\SUBFOLDER\\$"</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-filter" rel="tag" title="see questions tagged &#39;filter&#39;">filter</span> <span class="post-tag tag-link-smb2" rel="tag" title="see questions tagged &#39;smb2&#39;">smb2</span> <span class="post-tag tag-link-wildcard" rel="tag" title="see questions tagged &#39;wildcard&#39;">wildcard</span> <span class="post-tag tag-link-filename" rel="tag" title="see questions tagged &#39;filename&#39;">filename</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Sep '14, 13:14</strong></p><img src="https://secure.gravatar.com/avatar/bcfdf26904f3a8a9fb69c7ca0dc5e7b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="net_tech&#39;s gravatar image" /><p><span>net_tech</span><br />
<span class="score" title="116 reputation points">116</span><span title="30 badges"><span class="badge1">●</span><span class="badgecount">30</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="net_tech has 2 accepted answers">13%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Sep '14, 13:16</strong> </span></p></div></div><div id="comments-container-36124" class="comments-container"></div><div id="comment-tools-36124" class="comment-tools"></div><div class="clear"></div><div id="comment-36124-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36125"></span>

<div id="answer-container-36125" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-36125-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-36125-score" class="post-score" title="current number of votes">1</div><span id="post-36125-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="net_tech has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I think "matches" is the regex version, maybe using "contains" helps?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Sep '14, 13:19</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p><span>Jasper ♦♦</span><br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-36125" class="comments-container"><span id="36126"></span><div id="comment-36126" class="comment"><div id="post-36126-score" class="comment-score"></div><div class="comment-text"><p>both matches and contains seem to work, but once I get to the 1st slash and reapply the filter no packets are displayed</p><p>smb2.filename matches "C_"</p></div><div id="comment-36126-info" class="comment-info"><span class="comment-age">(09 Sep '14, 13:40)</span> <span class="comment-user userinfo">net_tech</span></div></div><span id="36128"></span><div id="comment-36128" class="comment"><div id="post-36128-score" class="comment-score"></div><div class="comment-text"><p>I guess it has to do with regex using some characters as special commands. You'd have to check regex syntax to see what the slashes mean.</p></div><div id="comment-36128-info" class="comment-info"><span class="comment-age">(09 Sep '14, 13:43)</span> <span class="comment-user userinfo">Jasper ♦♦</span></div></div></div><div id="comment-tools-36125" class="comment-tools"></div><div class="clear"></div><div id="comment-36125-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

