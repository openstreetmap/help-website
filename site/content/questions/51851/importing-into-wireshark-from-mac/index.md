+++
type = "question"
title = "Importing into Wireshark from Mac"
description = '''I&#x27;m trying to import a file to modify it in Wireshark version 2.0.1 and it won&#x27;t import. The file I&#x27;m trying to import is in the TextEdit app, what type of files can I import into Wireshark? Thanks'''
date = "2016-04-21T16:29:00Z"
lastmod = "2016-07-20T08:32:00Z"
weight = 51851
keywords = [ "macimportfile2.0.1" ]
aliases = [ "/questions/51851" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Importing into Wireshark from Mac](/questions/51851/importing-into-wireshark-from-mac)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51851-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51851-score" class="post-score" title="current number of votes">0</div><span id="post-51851-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm trying to import a file to modify it in Wireshark version 2.0.1 and it won't import. The file I'm trying to import is in the TextEdit app, what type of files can I import into Wireshark?</p><p>Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-macimportfile2.0.1" rel="tag" title="see questions tagged &#39;macimportfile2.0.1&#39;">macimportfile2.0.1</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Apr '16, 16:29</strong></p><img src="https://secure.gravatar.com/avatar/2d8854635ec01f4485008b74064c9a5b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="canigetanole&#39;s gravatar image" /><p><span>canigetanole</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="canigetanole has no accepted answers">0%</span></p></div></div><div id="comments-container-51851" class="comments-container"><span id="54190"></span><div id="comment-54190" class="comment"><div id="post-54190-score" class="comment-score"></div><div class="comment-text"><p>What is the actual file you're trying to import? And what format is it? Is it a text file in the format described by <a href="https://www.wireshark.org/docs/man-pages/text2pcap.html"><code>text2pcap</code></a> or something else? Maybe you could provide the file contents or at least a portion of it?</p></div><div id="comment-54190-info" class="comment-info"><span class="comment-age">(20 Jul '16, 08:32)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-51851" class="comment-tools"></div><div class="clear"></div><div id="comment-51851-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="51852"></span>

<div id="answer-container-51852" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-51852-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-51852-score" class="post-score" title="current number of votes">0</div><span id="post-51852-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>I'm trying to import a file to modify it in Wireshark version 2.0.1</p></blockquote><p>Then you're presumably using the GTK+ version - the Qt version doesn't currently support the packet editor.</p><blockquote><p>The file I'm trying to import is in the TextEdit app, what type of files can I import into Wireshark?</p></blockquote><p>A number of file types, including <a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format</a> (ELF) binary files, but <em>not</em> <a href="https://en.wikipedia.org/wiki/Mach-O">Mach-O</a> binary files, so you might be able to modify Linux and *BSD and Solaris binaries, but <em>not</em> OS X binaries.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Apr '16, 17:06</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-51852" class="comments-container"></div><div id="comment-tools-51852" class="comment-tools"></div><div class="clear"></div><div id="comment-51852-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

