+++
type = "question"
title = "Ubuntu 17.04, Wireshark installation removed all my groups (including sudo)"
description = '''After installing Wireshark 2.2.4 from official Ubuntu (17.04) repository and allowing the package to add me to wireshark group, I found that I am no longer a member of any other group: $ grep username /etc/group username:x:1000: wireshark:x:139:username  and running any command as root (sudo) respon...'''
date = "2017-07-27T05:21:00Z"
lastmod = "2017-07-27T05:26:00Z"
weight = 63171
keywords = [ "packaging", "installation", "ubuntu" ]
aliases = [ "/questions/63171" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Ubuntu 17.04, Wireshark installation removed all my groups (including sudo)](/questions/63171/ubuntu-1704-wireshark-installation-removed-all-my-groups-including-sudo)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63171-score" class="post-score" title="current number of votes">0</div><span id="post-63171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>After installing Wireshark 2.2.4 from official Ubuntu (17.04) repository and allowing the package to add me to wireshark group, I found that I am no longer a member of any other group:</p><pre><code>$ grep username /etc/group
username:x:1000:
wireshark:x:139:username</code></pre><p>and running any command as root (sudo) responds with:</p><pre><code>username is not in the sudoers file.  This incident will be reported.</code></pre><p>While I am perfectly fine with fixing this situation, I would like to know where can I report this unusual behavior.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packaging" rel="tag" title="see questions tagged &#39;packaging&#39;">packaging</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jul '17, 05:21</strong></p><img src="https://secure.gravatar.com/avatar/5c2bcd640eb7b85e1e70d052e8e1d58d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fuszumasa&#39;s gravatar image" /><p><span>fuszumasa</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fuszumasa has no accepted answers">0%</span></p></div></div><div id="comments-container-63171" class="comments-container"></div><div id="comment-tools-63171" class="comment-tools"></div><div class="clear"></div><div id="comment-63171-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="63172"></span>

<div id="answer-container-63172" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-63172-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-63172-score" class="post-score" title="current number of votes">0</div><span id="post-63172-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="fuszumasa has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You should report that to the Ubuntu package manager responsible for the package as the Wireshark project does not produce the distribution packages.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>27 Jul '17, 05:25</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-63172" class="comments-container"><span id="63173"></span><div id="comment-63173" class="comment"><div id="post-63173-score" class="comment-score"></div><div class="comment-text"><p>That's exactly what I needed. Thanks!</p></div><div id="comment-63173-info" class="comment-info"><span class="comment-age">(27 Jul '17, 05:26)</span> <span class="comment-user userinfo">fuszumasa</span></div></div></div><div id="comment-tools-63172" class="comment-tools"></div><div class="clear"></div><div id="comment-63172-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

