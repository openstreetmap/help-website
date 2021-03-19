+++
type = "question"
title = "Wireshark with lua"
description = '''Hello, I am trying to find a pre-built (executable) version of wireshark with lua support that runs on Red Hat 5.4. When I attempt to build a newer version from source, like 1.8.3, on my Red Hat 5.4 system I run into many dependency issues which look like they may lead to a dead end. My previous exp...'''
date = "2014-05-15T09:00:00Z"
lastmod = "2014-05-15T12:37:00Z"
weight = 32832
keywords = [ "lua", "redhat5", "wireshark" ]
aliases = [ "/questions/32832" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark with lua](/questions/32832/wireshark-with-lua)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32832-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32832-score" class="post-score" title="current number of votes">0</div><span id="post-32832-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I am trying to find a pre-built (executable) version of wireshark with lua support that runs on Red Hat 5.4. When I attempt to build a newer version from source, like 1.8.3, on my Red Hat 5.4 system I run into many dependency issues which look like they may lead to a dead end. My previous experiences with wireshark have just been a straight rpm installation. Thanks.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-redhat5" rel="tag" title="see questions tagged &#39;redhat5&#39;">redhat5</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '14, 09:00</strong></p><img src="https://secure.gravatar.com/avatar/e12b0b81c54cebc39e058773a090b311?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jimper&#39;s gravatar image" /><p><span>jimper</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jimper has no accepted answers">0%</span></p></div></div><div id="comments-container-32832" class="comments-container"></div><div id="comment-tools-32832" class="comment-tools"></div><div class="clear"></div><div id="comment-32832-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32835"></span>

<div id="answer-container-32835" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-32835-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-32835-score" class="post-score" title="current number of votes">0</div><span id="post-32835-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jimper has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The latest version you can (easily) get to run on Redhat EL 5.x is 1.6.16 (1.8 requires a Gtk+ that is newer than what RHEL 5 provides and upgrading that would be a <em>massive</em> effort).</p><p>The 2nd problem you'll run into is that (AFAIK) Redhat EL does not come with the Lua library.</p><p>Your best option is probably to:</p><ol><li>Install Lua on the system - this may involve compiling it yourself (not sure where you could get an RPM that would install cleanly though honestly I've never looked)</li><li>Download the Wireshark 1.6.16 source</li><li>Install the necessary dependencies (-devel packages)</li><li>Configure &amp; compile your own Wireshark</li></ol></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '14, 12:05</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-32835" class="comments-container"><span id="32837"></span><div id="comment-32837" class="comment"><div id="post-32837-score" class="comment-score"></div><div class="comment-text"><p>Jeff, Thank you very much for your very helpful response. I figured building wireshark 1.8.3 on Red Hat 5.4 would be a problem after attempting it and hitting roadblock after roadblock. It doesn't sound like getting lua support built into 1.6.16 is a piece of cake either, but I'll give it a shot. Thanks again. Jim</p></div><div id="comment-32837-info" class="comment-info"><span class="comment-age">(15 May '14, 12:26)</span> <span class="comment-user userinfo">jimper</span></div></div><span id="32838"></span><div id="comment-32838" class="comment"><div id="post-32838-score" class="comment-score"></div><div class="comment-text"><p>You're welcome. As this is a Q&amp;A site, if an answer answers your question, please Accept the answer by clicking on the checkbox next to the answer. See the FAQ for details.</p></div><div id="comment-32838-info" class="comment-info"><span class="comment-age">(15 May '14, 12:37)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div></div><div id="comment-tools-32835" class="comment-tools"></div><div class="clear"></div><div id="comment-32835-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

