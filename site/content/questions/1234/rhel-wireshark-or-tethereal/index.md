+++
type = "question"
title = "RHEL wireshark ? or tethereal ?"
description = '''Ok so im installing wireshark on RHEL 5 and I did &quot;yum install wireshark&quot; but now cant seem to find wireshark on the system -- the version that was installed was &quot;wireshark-1.0.15-1.el5_5.1&quot;. I was able to see /usr/share/wireshark but they are all html files, no executable. I did manage after some w...'''
date = "2010-12-03T13:45:00Z"
lastmod = "2010-12-03T16:13:00Z"
weight = 1234
keywords = [ "path", "executable", "tethereal", "rhel", "install" ]
aliases = [ "/questions/1234" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [RHEL wireshark ? or tethereal ?](/questions/1234/rhel-wireshark-or-tethereal)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1234-score" class="post-score" title="current number of votes">0</div><span id="post-1234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Ok so im installing wireshark on RHEL 5 and I did "yum install wireshark" but now cant seem to find wireshark on the system -- the version that was installed was "wireshark-1.0.15-1.el5_5.1". I was able to see /usr/share/wireshark but they are all html files, no executable. I did manage after some web searching to find tethereal in /usr/bin is this what RHEL is calling wireshark? If so whats up with all the html files in /usr/share/wireshark ? "which wireshark" and "locate wireshark" as well as searched for 'tshark' dont seem to return anything -- any suggestions?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-path" rel="tag" title="see questions tagged &#39;path&#39;">path</span> <span class="post-tag tag-link-executable" rel="tag" title="see questions tagged &#39;executable&#39;">executable</span> <span class="post-tag tag-link-tethereal" rel="tag" title="see questions tagged &#39;tethereal&#39;">tethereal</span> <span class="post-tag tag-link-rhel" rel="tag" title="see questions tagged &#39;rhel&#39;">rhel</span> <span class="post-tag tag-link-install" rel="tag" title="see questions tagged &#39;install&#39;">install</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Dec '10, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/1c3d6f8857bd3142696f258bec6e59a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve_77&#39;s gravatar image" /><p><span>steve_77</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve_77 has no accepted answers">0%</span></p></div></div><div id="comments-container-1234" class="comments-container"></div><div id="comment-tools-1234" class="comment-tools"></div><div class="clear"></div><div id="comment-1234-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1239"></span>

<div id="answer-container-1239" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-1239-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-1239-score" class="post-score" title="current number of votes">0</div><span id="post-1239-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>nevermind found tshark in /usr/sbin - seems you need root permissions to run it...</p><p>However what are all the files in /usr/share/wireshark ?? what is the purpose of the files if the tool can only be run in command-line mode? Has anyone tried running this on vmware or via wine?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '10, 16:13</strong></p><img src="https://secure.gravatar.com/avatar/1c3d6f8857bd3142696f258bec6e59a4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="steve_77&#39;s gravatar image" /><p><span>steve_77</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="steve_77 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Dec '10, 16:14</strong> </span></p></div></div><div id="comments-container-1239" class="comments-container"></div><div id="comment-tools-1239" class="comment-tools"></div><div class="clear"></div><div id="comment-1239-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

