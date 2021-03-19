+++
type = "question"
title = "How to change wireshark binary package name in Linux?"
description = '''Current name is wireshark-1.x.x-1.i686.rpm. I want to rename the Linux binary package as wireshark-1.x.x-MySoftware-Version.i686.rpm, while -Version is -1, -2, etc. Config.nmake was changed: VERSION_EXTRA=-MySoftware-2 But it did not work. The name was not changed. Any other file I should change to ...'''
date = "2014-03-07T11:35:00Z"
lastmod = "2014-03-21T05:43:00Z"
weight = 30576
keywords = [ "package", "name", "linux" ]
aliases = [ "/questions/30576" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to change wireshark binary package name in Linux?](/questions/30576/how-to-change-wireshark-binary-package-name-in-linux)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30576-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30576-score" class="post-score" title="current number of votes">0</div><span id="post-30576-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Current name is wireshark-1.x.x-1.i686.rpm. I want to rename the Linux binary package as wireshark-1.x.x-MySoftware-Version.i686.rpm, while -Version is -1, -2, etc. Config.nmake was changed:</p><p>VERSION_EXTRA=-MySoftware-2</p><p>But it did not work. The name was not changed.</p><p>Any other file I should change to put local build information in the binary package?</p><p>Thank you.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-package" rel="tag" title="see questions tagged &#39;package&#39;">package</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-linux" rel="tag" title="see questions tagged &#39;linux&#39;">linux</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Mar '14, 11:35</strong></p><img src="https://secure.gravatar.com/avatar/5428a0ee14871ca6db736dcf6099b4fc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="huang-shi&#39;s gravatar image" /><p><span>huang-shi</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="huang-shi has no accepted answers">0%</span></p></div></div><div id="comments-container-30576" class="comments-container"><span id="30609"></span><div id="comment-30609" class="comment"><div id="post-30609-score" class="comment-score"></div><div class="comment-text"><p>some questions.</p><ul><li>what is your Linux distribution</li><li>what is your Wireshark version</li><li>how did you build/create the RPM</li></ul></div><div id="comment-30609-info" class="comment-info"><span class="comment-age">(09 Mar '14, 03:26)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-30576" class="comment-tools"></div><div class="clear"></div><div id="comment-30576-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30641"></span>

<div id="answer-container-30641" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-30641-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-30641-score" class="post-score" title="current number of votes">0</div><span id="post-30641-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You will have to amend the Release field in the Wireshark.spec file from which you build the RPM.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Mar '14, 05:40</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-30641" class="comments-container"><span id="31008"></span><div id="comment-31008" class="comment"><div id="post-31008-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot. I know I need to change some wireshark.spec files. Can you let me know which file?</p></div><div id="comment-31008-info" class="comment-info"><span class="comment-age">(20 Mar '14, 12:15)</span> <span class="comment-user userinfo">huang-shi</span></div></div><span id="31047"></span><div id="comment-31047" class="comment"><div id="post-31047-score" class="comment-score"></div><div class="comment-text"><p>packaging/rpm/SPECS/wireshark.spec.in</p></div><div id="comment-31047-info" class="comment-info"><span class="comment-age">(21 Mar '14, 05:43)</span> <span class="comment-user userinfo">Jaap ♦</span></div></div></div><div id="comment-tools-30641" class="comment-tools"></div><div class="clear"></div><div id="comment-30641-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

