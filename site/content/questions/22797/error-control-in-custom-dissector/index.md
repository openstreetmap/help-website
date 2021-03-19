+++
type = "question"
title = "Error Control in custom dissector"
description = '''Hi, i am working on a cutstom dissector plugin for wireshark and i am wondering how error control is implemented with the wireshark API. I have read some of the documentation, mainly README.developer and README.plugin but i cant find anthing there about it. To give an example of what i want to do: S...'''
date = "2013-07-10T04:22:00Z"
lastmod = "2013-07-10T23:14:00Z"
weight = 22797
keywords = [ "custom", "dissector", "wireshark" ]
aliases = [ "/questions/22797" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Error Control in custom dissector](/questions/22797/error-control-in-custom-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22797-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22797-score" class="post-score" title="current number of votes">0</div><span id="post-22797-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, i am working on a cutstom dissector plugin for wireshark and i am wondering how error control is implemented with the wireshark API. I have read some of the documentation, mainly README.developer and README.plugin but i cant find anthing there about it.</p><p>To give an example of what i want to do: Standard in wireshark if the packet being dissected isn't following the protocol for any reason it just say "Malformed Packet". I have some cases where i know it can go wrong and i would like to have different error messages for theese cases. For example if a field that is being read as as the length of the rest of the packet or similar and it doesnt add up, i would like to specify what the user are being told the reason for this is. Also if it is possible i would like it to show where it went wrong in the hex table.</p><p>Is there methods to use for this ? Best Regards Kit</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jul '13, 04:22</strong></p><img src="https://secure.gravatar.com/avatar/b93cb303b8ca7bc14188730687491169?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kitg&#39;s gravatar image" /><p><span>Kitg</span><br />
<span class="score" title="16 reputation points">16</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kitg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>10 Jul '13, 04:23</strong> </span></p></div></div><div id="comments-container-22797" class="comments-container"><span id="22803"></span><div id="comment-22803" class="comment"><div id="post-22803-score" class="comment-score"></div><div class="comment-text"><p>I found out that expert infos probably is the way to go here. Can some one show me an easy example of how this is used ?</p></div><div id="comment-22803-info" class="comment-info"><span class="comment-age">(10 Jul '13, 06:42)</span> <span class="comment-user userinfo">Kitg</span></div></div></div><div id="comment-tools-22797" class="comment-tools"></div><div class="clear"></div><div id="comment-22797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22802"></span>

<div id="answer-container-22802" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22802-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22802-score" class="post-score" title="current number of votes">2</div><span id="post-22802-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kitg has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Use Expert info, PI_PROTOCOL . Note the Export info API is undergoing changes in trunk.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>10 Jul '13, 06:41</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p><span>Anders ♦</span><br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-22802" class="comments-container"><span id="22805"></span><div id="comment-22805" class="comment"><div id="post-22805-score" class="comment-score"></div><div class="comment-text"><p>Okej thanks, if it isnt to much to ask i would appreciate a code example if you know where i can find one. Otherwhise thanks for the response.</p></div><div id="comment-22805-info" class="comment-info"><span class="comment-age">(10 Jul '13, 06:47)</span> <span class="comment-user userinfo">Kitg</span></div></div><span id="22811"></span><div id="comment-22811" class="comment"><div id="post-22811-score" class="comment-score"></div><div class="comment-text"><p>Beeing lazy I just picked a checkin of updates to use the new API. just check changed code in any file <a href="http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=50454">http://anonsvn.wireshark.org/viewvc/viewvc.cgi?view=rev&amp;revision=50454</a></p><p>See also expert.c in epan/</p></div><div id="comment-22811-info" class="comment-info"><span class="comment-age">(10 Jul '13, 07:52)</span> <span class="comment-user userinfo">Anders ♦</span></div></div><span id="22830"></span><div id="comment-22830" class="comment"><div id="post-22830-score" class="comment-score"></div><div class="comment-text"><p>Thanks alot Anders.</p></div><div id="comment-22830-info" class="comment-info"><span class="comment-age">(10 Jul '13, 23:14)</span> <span class="comment-user userinfo">Kitg</span></div></div></div><div id="comment-tools-22802" class="comment-tools"></div><div class="clear"></div><div id="comment-22802-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

