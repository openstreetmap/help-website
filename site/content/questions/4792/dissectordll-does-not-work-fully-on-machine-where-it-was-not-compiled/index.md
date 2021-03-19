+++
type = "question"
title = "Dissector/dll does not work fully on machine where it was not compiled"
description = '''I wrote a Custom Dissector for one of the Protocols. I used Wireshark 1.5.2 Dev Version. The problem is that if I use the dll anywhere on my machine(whether dev version or installed 1.6 version) it works. But if I transfer it to some other machine and even if I run it with Wireshark 1.6 then the par...'''
date = "2011-06-28T11:02:00Z"
lastmod = "2011-06-30T18:20:00Z"
weight = 4792
keywords = [ "problem", "dissector", "dll" ]
aliases = [ "/questions/4792" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Dissector/dll does not work fully on machine where it was not compiled](/questions/4792/dissectordll-does-not-work-fully-on-machine-where-it-was-not-compiled)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4792-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4792-score" class="post-score" title="current number of votes">0</div><span id="post-4792-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I wrote a Custom Dissector for one of the Protocols. I used Wireshark 1.5.2 Dev Version. The problem is that if I use the dll anywhere on my machine(whether dev version or installed 1.6 version) it works. But if I transfer it to some other machine and even if I run it with Wireshark 1.6 then the part related to conversations and finding the Response time does not work. All other parts of dissector work perfectly even on the other machine.</p><p>For finding Response Time I use logic similar to DIAMETER Protocol Dissector WHEREIN i store Time when Req came in a Tree and later on when Rsp packet comes, query the tree to find req time.</p><p>Does anyone know what could be the Problem ? Does it have anything to do with WinPCAP Version ?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-dll" rel="tag" title="see questions tagged &#39;dll&#39;">dll</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Jun '11, 11:02</strong></p><img src="https://secure.gravatar.com/avatar/98b912fc4a13fff8fae6632b403d9ce6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="varun%20saxena&#39;s gravatar image" /><p><span>varun saxena</span><br />
<span class="score" title="1 reputation points">1</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="varun saxena has one accepted answer">100%</span></p></div></div><div id="comments-container-4792" class="comments-container"><span id="4877"></span><div id="comment-4877" class="comment"><div id="post-4877-score" class="comment-score"></div><div class="comment-text"><p>Which version of the Microsoft compiler are you using? Which version of the compiler were the versions of Wireshark running on the other computers compiled with? Find out from Wireshark's "Help -&gt; About" dialog. Have you tried compiling your dll against the same 1.6.0 sources using the same version as what's running on the other computers?</p><p>I don't know the answer to your question, but it has nothing to do with WinPcap.</p></div><div id="comment-4877-info" class="comment-info"><span class="comment-age">(30 Jun '11, 18:20)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-4792" class="comment-tools"></div><div class="clear"></div><div id="comment-4792-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

