+++
type = "question"
title = "LUA dissector set pinfo.cols.info question"
description = '''Hi All,  I use pinfo struct in LUA to handle TCP reassembly which works well, but I may have misunderstood something about updating the info column.  First dissector call: on packet x-1, message 1 dissected, append to info column on packet x-1 works fine, pinfo desegment offset, desegment len, retur...'''
date = "2016-09-07T06:17:00Z"
lastmod = "2016-09-07T06:17:00Z"
weight = 55369
keywords = [ "info", "lua", "dissector", "columns", "pinfo" ]
aliases = [ "/questions/55369" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [LUA dissector set pinfo.cols.info question](/questions/55369/lua-dissector-set-pinfocolsinfo-question)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-55369-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-55369-score" class="post-score" title="current number of votes">0</div><span id="post-55369-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi All,</p><p>I use pinfo struct in LUA to handle TCP reassembly which works well, but I may have misunderstood something about updating the info column.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/tcpdissector_sLZXKuc.jpg" alt="alt text" /></p><p>First dissector call: on packet x-1, message 1 dissected, append to info column on packet x-1 works fine, pinfo desegment offset, desegment len, return</p><p>Second call: on packet x, but buffer contains only message2 (due to previous desegment offset and len) ,message 2 dissected, append info to column on packet x works, return</p><p>Third call: on packet x again, but with buffer remaining messages: 3,4,5,partial 6, message 3,4,5 dissected, append to info column on packet x again - not appending anything</p><p>What do I miss? Any help is appreciated.</p><p>Thanks in advance. Szicsu</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-info" rel="tag" title="see questions tagged &#39;info&#39;">info</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-columns" rel="tag" title="see questions tagged &#39;columns&#39;">columns</span> <span class="post-tag tag-link-pinfo" rel="tag" title="see questions tagged &#39;pinfo&#39;">pinfo</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Sep '16, 06:17</strong></p><img src="https://secure.gravatar.com/avatar/4fc2c02f1f2d595d0e12ec9bcad03c79?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="szicsu&#39;s gravatar image" /><p><span>szicsu</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="szicsu has no accepted answers">0%</span></p></img></div></div><div id="comments-container-55369" class="comments-container"></div><div id="comment-tools-55369" class="comment-tools"></div><div class="clear"></div><div id="comment-55369-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

