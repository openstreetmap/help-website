+++
type = "question"
title = "pcap_next_ex vs pcap_loop"
description = '''I&#x27;m writing a program which reads live captures and processes them. I&#x27;m using pcap_next_ex for capturing and it returns -1 and -2 unexpectdly. Will it be nice to use pcap_loop rather than pcap_next_ex? Which one is more efficient? Is the problem associated with read time out?'''
date = "2011-05-18T23:30:00Z"
lastmod = "2011-05-19T01:04:00Z"
weight = 4131
keywords = [ "pcap_loop", "pcap_next_ex", "pcap" ]
aliases = [ "/questions/4131" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [pcap\_next\_ex vs pcap\_loop](/questions/4131/pcap_next_ex-vs-pcap_loop)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4131-score" class="post-score" title="current number of votes">0</div><span id="post-4131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm writing a program which reads live captures and processes them. I'm using pcap_next_ex for capturing and it returns -1 and -2 unexpectdly. Will it be nice to use pcap_loop rather than pcap_next_ex? Which one is more efficient? Is the problem associated with read time out?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-pcap_loop" rel="tag" title="see questions tagged &#39;pcap_loop&#39;">pcap_loop</span> <span class="post-tag tag-link-pcap_next_ex" rel="tag" title="see questions tagged &#39;pcap_next_ex&#39;">pcap_next_ex</span> <span class="post-tag tag-link-pcap" rel="tag" title="see questions tagged &#39;pcap&#39;">pcap</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>18 May '11, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/26ff72f1b8778dc8db9e4bb518e71ffe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Fitsum&#39;s gravatar image" /><p><span>Fitsum</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Fitsum has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>19 May '11, 21:24</strong> </span></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-4131" class="comments-container"><span id="4133"></span><div id="comment-4133" class="comment"><div id="post-4133-score" class="comment-score"></div><div class="comment-text"><p>Well, this is really a <span class="__cf_email__" data-cfemail="d8acbba8bcadb5a8f5afb7aab3bdaaab98acbba8bcadb5a8f6b7aabf">[email protected]</span> question, but:</p><ol><li><p>On what operating system is this?</p></li><li><p>Are you calling pcap_breakloop() in your program?</p></li><li><p>When pcap_next_ex() returns -1, what does pcap_geterr() return?</p></li></ol></div><div id="comment-4133-info" class="comment-info"><span class="comment-age">(19 May '11, 01:04)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-4131" class="comment-tools"></div><div class="clear"></div><div id="comment-4131-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

